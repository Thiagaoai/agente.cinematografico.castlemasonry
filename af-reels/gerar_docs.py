#!/usr/bin/env python3
"""Gera cronograma-outubro.md e roteiros.md a partir de serie.json (fonte única da verdade).

Uso: python3 gerar_docs.py
Rode de novo sempre que mudar status/data em serie.json.
"""
import json
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).parent
serie = json.loads((RAIZ / "serie.json").read_text())
marca = serie["marca"]
DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
STATUS = {"roteiro": "⬜ roteiro pronto", "em-producao": "🟨 em produção", "pronto": "✅ pronto para postar",
          "postado": "📣 postado"}


def d(s):
    x = date.fromisoformat(s)
    return f"{DIAS[x.weekday()]} {x.strftime('%d/%m')}"


vids = serie["videos"]

# ---------- cronograma ----------
c = ["# Cronograma — A.F Consultoria · Reels de outubro/novembro de 2026", "",
     "Ritmo: **3 vídeos por semana (segunda, quarta e sexta)**. O vídeo 1 foi produzido e é postado hoje (sábado).",
     "Cada vídeo é produzido no dia anterior à publicação (coluna *Produzir até*).", "",
     "> Conta honesta: começando em 03/10, **13 vídeos cabem em outubro** (o 1 de hoje + 12 de segunda a sexta até 30/10). "
     "Os vídeos 14 e 15 caem em 02/11 e 04/11. Para fechar os 15 ainda em outubro seria preciso postar 5 na última semana "
     "ou usar sábados — me avise se preferir.", "",
     "| # | Publicar | Produzir até | Tema | Pilar do site | Status |", "|---|---|---|---|---|---|"]
for v in vids:
    c.append(f"| {v['id']:02d} | {d(v['publicar'])} | {d(v['produzir_ate'])} | {v['titulo']} | {v['pilar']} | {STATUS[v['status']]} |")
c += ["", "## Semana a semana", ""]
semanas = {}
for v in vids:
    x = date.fromisoformat(v["publicar"])
    semanas.setdefault(x.isocalendar()[1], []).append(v)
for i, (_, lista) in enumerate(sorted(semanas.items()), 1):
    c.append(f"- **Semana {i}:** " + " · ".join(f"{d(v['publicar'])} → #{v['id']:02d} {v['titulo']}" for v in lista))
c += ["", "## Como pedir o próximo", "",
      "Diga apenas **“próximo vídeo”** (ou “faz o vídeo 4”). A skill `proximo-video-af` lê o `serie.json`, "
      "pega o primeiro que não está pronto e produz tudo.", ""]
(RAIZ / "cronograma-outubro.md").write_text("\n".join(c))

# ---------- roteiros ----------
r = [f"# Roteiros — {marca['nome']}", "",
     f"Formato: vertical {serie['formato']['proporcao']} ({serie['formato']['resolucao']}), {serie['formato']['duracao_alvo_s']} s, "
     f"{serie['formato']['cenas']} cenas. Voz: {serie['formato']['voz']}.", "",
     "## Regras de conteúdo", ""] + [f"- {x}" for x in serie["regras_de_conteudo"]] + [""]
for v in vids:
    r += [f"## {v['id']:02d} · {v['titulo']}", "",
          f"**Publicar:** {d(v['publicar'])} · **Pilar:** {v['pilar']} · **Status:** {STATUS[v['status']]}", "",
          "| Cena | Imagem | Narração |", "|---|---|---|"]
    for i, (cena, fala) in enumerate(zip(v["cenas"], v["narracao"]), 1):
        r.append(f"| {i} | {cena} | {fala} |")
    r += ["", f"**Legenda do post:** {v['legenda']}", ""]
(RAIZ / "roteiros.md").write_text("\n".join(r))
print("ok: cronograma-outubro.md e roteiros.md atualizados")
