#!/usr/bin/env python3
"""Estado de revisão de um vídeo. Só uma pessoa aprova; o agente só registra.

Uso:
  python3 ferramentas/estado.py ver      video.mp4
  python3 ferramentas/estado.py aprovar  video.mp4 --por "Thiago" --ouvi --vi-quadros [--nota "..."]
  python3 ferramentas/estado.py reprovar video.mp4 --por "Thiago" --motivo "voz com sotaque"
  python3 ferramentas/estado.py publicado video.mp4 --onde "Instagram" --por "Thiago"

Estados, em ordem:
  renderizado          existe o arquivo, sem QA
  reprovado-tecnico    QA mediu algo fora do alvo
  aguardando-escuta    QA técnico passou; falta uma pessoa ouvir e ver
  reprovado            pessoa ouviu/viu e recusou
  aprovado             pessoa ouviu e viu, e aprovou ESTE arquivo (hash conferido)
  publicado            foi ao ar

Regra: o agente só roda `aprovar` quando o usuário disser explicitamente, nesta
conversa, que ouviu e aprovou este arquivo. Nunca por conta própria.
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path


def sha256(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def carregar(video):
    qa = video.with_suffix(".qa.json")
    if not qa.exists():
        return qa, None
    return qa, json.loads(qa.read_text())


def agora():
    return datetime.now().isoformat(timespec="seconds")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("acao", choices=["ver", "aprovar", "reprovar", "publicado"])
    p.add_argument("video")
    p.add_argument("--por", help="quem revisou (pessoa)")
    p.add_argument("--ouvi", action="store_true", help="a pessoa ouviu o áudio inteiro")
    p.add_argument("--vi-quadros", action="store_true", help="a pessoa viu o vídeo/folha de quadros")
    p.add_argument("--nota", default="")
    p.add_argument("--motivo", default="")
    p.add_argument("--onde", default="")
    a = p.parse_args()

    video = Path(a.video).resolve()
    if not video.is_file():
        sys.exit(f"Não encontrado: {video}")
    arq_qa, qa = carregar(video)

    if a.acao == "ver":
        if qa is None:
            print(f"{video.name}: renderizado (sem QA). Rode ferramentas/qa_video.py.")
            return
        mudou = qa.get("sha256") != sha256(video)
        print(f"{video.name}: {qa['estado']}" + ("  ATENÇÃO: arquivo mudou depois do QA; refaça o QA." if mudou else ""))
        for c in qa["checagens"]:
            if not c["ok"]:
                print(f"  falhou: {c['checagem']} (medido {c['medido']}, esperado {c['esperado']})")
        for chave in ("aprovacao", "reprovacao", "publicacao"):
            if qa.get(chave):
                print(f"  {chave}: {qa[chave]}")
        return

    if qa is None:
        sys.exit("Sem QA técnico. Rode ferramentas/qa_video.py antes.")
    if not a.por:
        sys.exit("Informe --por (a pessoa que revisou).")
    if qa.get("sha256") != sha256(video):
        sys.exit("O arquivo mudou depois do QA. Rode qa_video.py de novo antes de registrar revisão.")

    if a.acao == "aprovar":
        if qa["estado"] not in ("aguardando-escuta", "reprovado"):
            sys.exit(f"Não dá para aprovar no estado '{qa['estado']}'. QA técnico precisa passar primeiro.")
        if not (a.ouvi and a.vi_quadros):
            sys.exit("Aprovação exige --ouvi e --vi-quadros: a pessoa precisa ter ouvido e visto.")
        qa["estado"] = "aprovado"
        qa["aprovacao"] = {"por": a.por, "em": agora(), "ouviu": True, "viu": True, "nota": a.nota}
    elif a.acao == "reprovar":
        if not a.motivo:
            sys.exit("Informe --motivo.")
        qa["estado"] = "reprovado"
        qa["reprovacao"] = {"por": a.por, "em": agora(), "motivo": a.motivo}
    elif a.acao == "publicado":
        if qa["estado"] != "aprovado":
            sys.exit(f"Só vídeo aprovado é publicado (estado atual: {qa['estado']}).")
        qa["estado"] = "publicado"
        qa["publicacao"] = {"por": a.por, "em": agora(), "onde": a.onde}

    arq_qa.write_text(json.dumps(qa, ensure_ascii=False, indent=2))
    print(f"{video.name}: {qa['estado']}")


if __name__ == "__main__":
    main()
