---
name: proximo-video-clastle
description: Produz um vídeo da Castle Masonry (castlemasonryma.com) de ponta a ponta — briefing, cenas, imagens e animação no Magnific, voz e trilha, montagem e QA medido — com portões de aprovação. Use quando o usuário disser "próximo vídeo da Castle", "faz o vídeo da Castle", "gera o reel da Clastle" ou algo equivalente.
---

# Próximo vídeo da Castle Masonry

**Leia `CLAUDE.md` (raiz) antes de começar.** Ele manda em caso de conflito. Um vídeo por pedido,
em `castle/videos/vNN/`. Português no chat, inglês nos prompts e na locução, sem JSON no chat.

Portões: **P1 ambiente/custo → P2 briefing com fatos → P3 âncora aprovada → P4 voz aprovada →
P5 QA técnico → P6 revisão humana**.

## 0. Definir o vídeo
Se o usuário não disse, pergunte (uma vez, junto): formato (16:9 site/YouTube ou 9:16 Reels),
duração (~30 s), tema/serviço, e se há fotos reais do site para usar como imagem inicial.
Briefings prontos: `video-castle-masonry.md` ("Worth the reveal", 16:9, 6 cenas) e
`video-quintal-cape-cod.md`. Crie `castle/videos/vNN/` e `tarefas.json`.

## 1. P1 — Ambiente e custo
- `python3 ferramentas/preflight.py`; se falhar, pare e diga o que falta.
- Magnific MCP (`images_generate`, `video_generate`, `creations_wait`, `simulate_cost`,
  `account_balance`): carregue com ToolSearch. Se não estiver conectado, pare e diga.
- `account_balance` antes; anote. Todo id devolvido vai para `tarefas.json` na hora.
  Chamada sem resposta: **não reenvie**, confira em `creations_list`.

## 2. P2 — Roteiro com fatos
- Cada afirmação de fala, legenda e cartão precisa estar em `castle/marca/fatos.md`.
  Faltou: pergunte ao usuário. Sem números, depoimentos, preços, prazos.
- Prompts em inglês técnico: sujeito/material real (bluestone, aged granite, reclaimed granite
  cobble, cedar shingle em parede **e** telhado), lente (35mm, 85mm, macro 100mm), luz física
  (golden hour, raking morning sun), película (`natural color science, fine film grain`).
  Sempre `No text, no logos, no signage.` Rosto: `face not visible` / de costas.

## 3. P3 — Imagens
- `seedream-5-pro` (ou o modelo que o usuário escolher), proporção do vídeo, `2k`.
- **Âncora = cena 1**, `count: 2`; baixe, junte lado a lado, **abra com Read e olhe**, mostre ao
  usuário e peça a escolha. Cenas 2–N: `references` de estilo = âncora.
- Folha de contato, **abra com Read**: sem texto, sem rosto/mão deformada, pedra coerente, mesma luz.
  Regere **só** a que falhar. Diga o que viu e o que imagem parada não mostra.

## 4. Animação (Kling via `video_generate`)
- `kling-30`, `duration: 5`, proporção do vídeo, `1080p`, `withSoundEffects: false`, quadro inicial = imagem aprovada.
- **Um único vetor de movimento**, e feche com: `Stone, masonry and ground remain rigid, solid and locked. Only <grass / smoke / sparks> moves subtly. No warping, no morphing, no text.`
- `negativePrompt`: `text, watermark, logo, CGI, 3D render, cartoon, warping stone, melting masonry, morphing objects, fast chaotic camera movement, flicker, glitch`.
- Revisão: 4 quadros por clipe (`ffmpeg -ss 0.1/1.6/3.2/4.9`), **abra com Read**. Regere só o ruim.

## 5. P4 — Voz e trilha
Voz ainda não definida (ver CLAUDE.md §5): amostra curta em inglês → aprovação → registrar em
`castle/marca/audio.md`. Uma chamada por frase, salvar em `voz/`. Trilha instrumental com ducking.

## 6. P5 — Montagem e QA
Montagem com ffmpeg (`montar.py` do vídeo; modelo de lógica em `montar_trailer.py` quando existir).
Depois: `python3 ferramentas/qa_video.py castle/videos/vNN/final.mp4 --duracao N --tolerancia 3`,
abra a `.quadros.jpg` com Read e confira legenda, logo, contato e a marca "Cenas ilustrativas".

## 7. P6 — Entrega
Entregue como **"prévia — aguardando sua revisão"** com o bloco Produzido/Verificado/Pendente/
Hipótese/Próximo passo, créditos gastos (diferença real de saldo) e caminho do MP4.
Só após o usuário dizer que assistiu e aprovou: `python3 ferramentas/estado.py aprovar <mp4> --por "<nome>" --ouvi --vi-quadros`.

## Regras de ouro
Não invente fatos. Não poste nem envie nada: só produz o arquivo. Gere o mínimo, nunca reenvie geração ambígua.
