"""Testes do magnific.py com API falsa (nenhuma chamada real, nenhum crédito gasto).

Rodar: python3 -m unittest discover -s ferramentas/testes -v
"""
import shutil
import sys
import tempfile
import types
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ))
import magnific  # noqa: E402


class ApiFalsa:
    def __init__(self, cair_no_post=False, falhar_tarefa=False):
        self.posts = 0
        self.cair_no_post = cair_no_post
        self.falhar_tarefa = falhar_tarefa

    def req(self, metodo, caminho, corpo=None):
        if metodo == "POST":
            self.posts += 1
            if self.cair_no_post:
                raise magnific.SubmissaoAmbigua("conexão caiu (simulado)")
            return {"data": {"task_id": f"t{self.posts}"}}
        status = "FAILED" if self.falhar_tarefa else "COMPLETED"
        return {"data": {"status": status, "generated": ["http://falso/arquivo"]}}


def opcoes(**kw):
    base = dict(simular=False, regerar_desatualizadas=False, reenviar_ambiguas=False)
    base.update(kw)
    return types.SimpleNamespace(**base)


class TestMagnific(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.reg = magnific.Registro(self.tmp)
        self.destino = self.tmp / "cena1.png"
        self._req, self._baixar, self._esperar_sleep = magnific.req, magnific.baixar, magnific.time.sleep
        magnific.baixar = lambda url, destino: destino.write_bytes(b"x" * 2048)
        magnific.time.sleep = lambda s: None

    def tearDown(self):
        magnific.req, magnific.baixar, magnific.time.sleep = self._req, self._baixar, self._esperar_sleep
        shutil.rmtree(self.tmp)

    def rodar(self, api, corpo, explicita=False, **kw):
        magnific.req = api.req
        return magnific.processar(self.reg, "imagem-cena1", "/rota", "/rota", corpo, self.destino,
                                  explicita, opcoes(**kw))

    def test_gera_e_reaproveita_mesmo_pedido(self):
        api = ApiFalsa()
        self.assertEqual(self.rodar(api, {"prompt": "a"}), "concluida")
        self.assertEqual(self.rodar(api, {"prompt": "a"}), "em-dia")
        self.assertEqual(api.posts, 1, "não pode pagar de novo pelo mesmo pedido")

    def test_pedido_mudou_nao_gasta_sozinho(self):
        api = ApiFalsa()
        self.rodar(api, {"prompt": "a"})
        self.assertEqual(self.rodar(api, {"prompt": "b"}), "desatualizada")
        self.assertEqual(api.posts, 1)
        self.assertEqual(self.rodar(api, {"prompt": "b"}, regerar_desatualizadas=True), "concluida")
        self.assertEqual(api.posts, 2)

    def test_arquivo_sem_registro_nao_e_reaproveitado_nem_regerado(self):
        self.destino.write_bytes(b"antigo" * 500)
        api = ApiFalsa()
        self.assertEqual(self.rodar(api, {"prompt": "a"}), "desatualizada")
        self.assertEqual(api.posts, 0)

    def test_post_que_cai_nao_e_repetido(self):
        api = ApiFalsa(cair_no_post=True)
        self.assertEqual(self.rodar(api, {"prompt": "a"}), "ambigua")
        self.assertEqual(api.posts, 1)
        # rodar de novo não reenvia sem autorização explícita
        self.assertEqual(self.rodar(api, {"prompt": "a"}), "ambigua")
        self.assertEqual(api.posts, 1)
        api.cair_no_post = False
        self.assertEqual(self.rodar(api, {"prompt": "a"}, reenviar_ambiguas=True), "concluida")
        self.assertEqual(api.posts, 2)

    def test_tarefa_ja_submetida_e_retomada_sem_novo_post(self):
        h = magnific.hash_pedido("/rota", {"prompt": "a"})
        self.reg.set("imagem-cena1", hash=h, estado="submetida", task_id="t-antiga")
        api = ApiFalsa()
        self.assertEqual(self.rodar(api, {"prompt": "a"}), "concluida")
        self.assertEqual(api.posts, 0, "tinha task_id gravado: devia retomar, não pagar de novo")

    def test_registro_sobrevive_a_reabertura(self):
        api = ApiFalsa()
        self.rodar(api, {"prompt": "a"})
        self.reg = magnific.Registro(self.tmp)  # simula novo processo
        self.assertEqual(self.rodar(api, {"prompt": "a"}), "em-dia")
        self.assertEqual(api.posts, 1)

    def test_simulacao_nao_envia(self):
        api = ApiFalsa()
        self.assertEqual(self.rodar(api, {"prompt": "a"}, simular=True), "simulada")
        self.assertEqual(api.posts, 0)

    def test_tarefa_falha_fica_registrada(self):
        api = ApiFalsa(falhar_tarefa=True)
        self.assertEqual(self.rodar(api, {"prompt": "a"}), "falhou")
        self.assertEqual(self.reg.get("imagem-cena1")["estado"], "falhou")
        self.assertFalse(self.destino.exists())

    def test_cena_explicita_regera(self):
        api = ApiFalsa()
        self.rodar(api, {"prompt": "a"})
        self.assertEqual(self.rodar(api, {"prompt": "a"}, explicita=True), "concluida")
        self.assertEqual(api.posts, 2)


if __name__ == "__main__":
    unittest.main()
