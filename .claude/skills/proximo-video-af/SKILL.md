---
name: proximo-video-af
description: Produz o próximo vídeo vertical (Reels/Shorts, 9:16) da série A.F Consultoria e Assessoria em Engenharia, de ponta a ponta — imagens, animação, locução brasileira, trilha, legendas, logo em marca d'água e CTA — com portões de aprovação (amostra de voz, QA medido, escuta humana). Use quando o usuário disser "próximo vídeo", "faz o vídeo 4", "vídeo da semana", "gera o próximo reel da A.F" ou algo equivalente. Lê af-reels/serie.json para saber qual é o próximo.
---

# Próximo vídeo da série A.F

**Leia `CLAUDE.md` (raiz) antes de começar.** Ele manda em caso de conflito com este roteiro.
Um vídeo por pedido. Tudo vive em `af-reels/`. Português, resumo executivo, sem JSON no chat.

Portões (não pular nenhum): **P1 ambiente → P2 roteiro com fatos → P3 âncora aprovada →
P4 voz fixa (amostra só p/ termos novos) → P5 QA técnico → P6 escuta humana**.

## 0. Descobrir qual vídeo fazer
1. Leia `af-reels/serie.json`. Se o usuário citou um número, use-o; senão pegue o primeiro vídeo
   cujo `status` **não** seja `aprovado`, `publicado` ou `postado`.
   - `pronto` é status antigo e significa só "renderizado" — **não** é aprovado.
   - Se o primeiro da fila estiver `aguardando-escuta`, pergunte: "O vídeo NN está esperando sua
     escuta. Você aprovou? Ou sigo para o próximo?". Não decida sozinho.
2. Se o vídeo estiver `em-producao` e existir `videos/vNN/`, **retome** do que falta: leia
   `videos/vNN/tarefas.json` e não regere o que já existe e está aprovado.
3. Anuncie em uma linha: "Vídeo NN — <título>, previsto para <data>".

## 1. P1 — Ambiente e custo (antes de gastar)
- `python3 ferramentas/preflight.py`. Se falhar, pare e diga o que falta.
- Ferramentas: **Magnific MCP** (`mcp__claude_ai_Magnific__*`: `images_generate`, `video_generate`,
  `creations_wait`, `simulate_cost`, `account_balance`) e **ElevenLabs MCP** (`mcp__elevenlabs__text_to_speech`,
  `compose_music`). Carregue com ToolSearch. Se alguma não estiver conectada, **pare e diga qual**.
- `account_balance` antes; anote o número. Custo de referência do vídeo 01: 3.950 créditos
  (imagem seedream-5-pro 9:16 2k ≈ 100; clipe kling-30 1080p 5 s ≈ 450). Se faltar crédito, avise.
- **Toda criação devolvida pelo MCP:** anote imediatamente em `videos/vNN/tarefas.json`
  (`{"cena3-video": {"id": "...", "estado": "submetida", "em": "..."}}`). Se uma chamada cair sem
  resposta, **não reenvie**: liste as criações recentes (`creations_list`) e confira antes.

## 2. P2 — Roteiro com fatos verificados
- Pegue em `serie.json` as `cenas` e a `narracao`.
- **Confira cada afirmação da narração, legenda e cartão contra `af-reels/marca/fatos.md`.**
  Se algo não estiver lá, pergunte ao usuário antes de produzir. Nada de números, depoimentos,
  preços, prazos ou garantias.
- Prompts em inglês técnico, 4 camadas (`prompt-sistema.md`):
  - **Sujeito e materiais reais** (concreto aparente, tijolo cerâmico sem reboco, vergalhão
    enferrujado, terra vermelha do cerrado de Goiás, asfalto novo).
  - **Lente e enquadramento** (35mm f/5.6, 85mm f/2.8, macro 100mm, horizonte nivelado).
  - **Luz física** (late afternoon 3500K raking sun, golden hour, blue hour).
  - **Película** (`natural color science, fine Kodak Vision3 film grain`). Evite "ultra 4K, photorealistic".
  - Sempre: `No text, no logos, no signage.` Pessoas: `face not visible`, `seen from behind`.
- Realismo da série: nunca rosto nem mãos em close; nunca texto legível dentro da imagem;
  terço superior livre (marca d'água) e faixa 69–80% da altura limpa (legenda); local Brasil (Goiás/cerrado).

## 3. P3 — Imagens (Magnific, `images_generate`)
- `mode: seedream-5-pro`, `aspectRatio: 9:16`, `resolution: 2k`.
- **Âncora = cena 1**, `count: 2`. Baixe as duas, junte lado a lado (`magick ... +append`),
  **abra com Read e olhe**. Mostre ao usuário e peça a escolha (ou escolha com justificativa visual
  explícita se ele delegou). Se nenhuma servir, regere só a âncora.
- Cenas 2–6: `references: [{type:"style", identifier:<âncora>}]` quando a composição muda;
  `{type:"image", ...}` quando é o **mesmo objeto**. Dispare em paralelo, `creations_wait`,
  baixe (`curl -L`) para `videos/vNN/imagens/cenaN.png`.
- **Revisão:** folha de contato 3×2, **abra com Read**. Critérios: sem texto, sem rosto/mão
  deformada, estrutura coerente com a âncora, mesma luz. Regere **apenas** a que falhar.
  Diga o que viu e o que não dá para avaliar em imagem parada.

## 4. Animação (Magnific, `video_generate`)
- `slug: kling-30`, `duration: 5`, `aspectRatio: 9:16`, `resolution: 1080p`,
  `withSoundEffects: false`, `keyframes.start = {type:"image", url:<identifier da imagem>}`.
- Prompt (**um único vetor de movimento**):
  `Slow, smooth, steady <push-in | lateral slide to the right | pedestal up | aerial pull-back with subtle rise>, one single continuous camera movement. Only <grass swaying, dust drifting, fence fluttering>. <Estruturas> remain completely solid, rigid and stable. No warping, no morphing, no text. Photorealistic documentary footage.`
- `negativePrompt`: `text, watermark, logo, CGI, 3D render, cartoon, distorted architecture, warping walls, melting concrete, morphing objects, fast chaotic camera movement, flicker, glitch` (+ `people` quando não houver).
- Pessoa em cena: `stands completely still ... no walking, no turning, face never visible`.
- Baixe para `videos/vNN/clipes/cenaN.mp4`; confira com `ffprobe` que são 1080×1920.
- **Revisão:** 4 quadros por clipe (`ffmpeg -ss 0.1/1.6/3.2/4.9`), junte, **abra com Read**.
  Geometria estável, nada derretendo, enquadramento como pedido. Regere só o clipe ruim.
  Registre: "vi 4 quadros por clipe; movimento contínuo entre eles não foi visto".

## 5. P4 — Voz FIXA: Bernard (Runway) — ver `af-reels/marca/audio.md`
- **Sempre a mesma voz aprovada pelo usuário:** Runway `generate_speech`, `model: "eleven_v3"`,
  `voice: "Bernard"`, `languageCode: "pt-br"`, `speed: 1`. Não trocar. Se o Runway não estiver
  conectado, **pare e avise** — não substitua por ElevenLabs/Rafael ou outra voz.
- Texto falado com a grafia aprovada da tabela de `audio.md` ("A.F" → "A A F"; "WhatsApp" igual).
  Legenda continua com a grafia correta (`narracao`). Registre o texto falado em `narracao_tts`.
- **Termos ainda não ouvidos nesta voz** (siglas, números, nomes): gere antes uma **amostra curta**
  só com eles, entregue e **pare** até o usuário aprovar; registre a grafia aprovada em `audio.md`.
  Você não consegue ouvir: não opine sobre naturalidade.
- Uma chamada por frase, salve como `videos/vNN/voz/f01.mp3 … f06.mp3` na ordem das cenas.
  Anote cada id de tarefa em `videos/vNN/tarefas.json`.

## 6. Trilha DRAMÁTICA, variando a cada vídeo (obrigatória) — ver `af-reels/marca/audio.md`
- Escolha a variação pela rotação (`((NN − 1) mod 6) + 1` → D1…D6), **nunca a mesma do vídeo
  anterior**; pode ajustar ao tema. Use o prompt da variação + o **sufixo obrigatório** de `audio.md`.
- Ferramenta: Runway `generate_music`, `model: "lyria-3-clip"` (como na V02); se indisponível,
  ElevenLabs `compose_music` (`force_instrumental: true`, `music_length_ms: 38000`) com o mesmo prompt.
- Salve como `videos/vNN/trilha.mp3` e registre em `serie.json` → vídeo:
  `trilha: {variacao, ferramenta, tarefa, prompt}`.
- A mixagem tem ducking; drama não pode encobrir a fala nem o CTA — confira no QA e na escuta.

## 7. P5 — Montagem e QA medido
```bash
cd af-reels && python3 montar_reel.py NN
python3 ../ferramentas/qa_video.py videos/vNN/final.mp4 --duracao 33 --tolerancia 3
```
- `montar_reel.py` gera `final.mp4` (1080×1920, 30 fps, duração = soma das falas + respiros,
  alvo da série 30–36 s), com xfade, legendas, marca d'água, cartão de CTA e voz sobre trilha com ducking.
- O QA mede duração, streams, **LUFS (−16 a −14) e true peak (≤ −1,5 dBTP)**, decodifica tudo e
  gera `final.quadros.jpg`. Se reprovar no áudio: `python3 ../ferramentas/corrigir_audio.py
  videos/vNN/final.mp4 videos/vNN/final-audio.mp4` e rode o QA no novo arquivo.
- **Abra a folha de quadros com Read** e confira: legenda legível e no lugar certo (nunca
  sobre o logo/contato do cartão), marca d'água, cartão com WhatsApp e site corretos, "Cenas ilustrativas".

## 8. P6 — Entrega como prévia e registro
1. Copie o arquivo que passou no QA para `entregas/af.consultoria.vsclaude-vNN.mp4` e rode o QA
   nele também (o estado fica ao lado do arquivo).
2. Em `serie.json`: `status: "aguardando-escuta"`, `entrega`, `creditos_magnific` (diferença real
   de `account_balance`). **Nunca** `pronto` ou `aprovado` aqui.
3. `python3 gerar_docs.py` para atualizar `cronograma-outubro.md` e `roteiros.md`.
4. Responda com o bloco do CLAUDE.md (Produzido / Verificado / Pendente / Hipótese / Próximo passo),
   incluindo: caminho do MP4, **legenda do post** (`legenda`), dia/horário sugerido, créditos
   gastos e saldo, e o pedido: "Ouça e assista no celular. Se aprovar, me diga."
5. Quando o usuário disser que ouviu e aprovou: `python3 ferramentas/estado.py aprovar <mp4>
   --por "<nome>" --ouvi --vi-quadros` e `status: "aprovado"` em `serie.json`.
   Se reprovar: `estado.py reprovar ... --motivo "..."`, corrija só o que falhou.

## Regras de ouro
- Não invente fatos (`fatos.md`). Na dúvida, pergunte.
- Não poste nada nem envie e-mail: a skill só produz o arquivo.
- Gere o mínimo; nunca refaça tudo por causa de uma cena ruim; nunca reenvie geração ambígua.
- Marca: cores `#b6722d`, `#f4ece3`, `#241a12`, fonte Archivo, logo oficial de `marca/`.
