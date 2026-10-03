# agente.video.clastle — vídeos da Castle Masonry

Pasta de trabalho para criar vídeos de **castlemasonryma.com** (Magnific: imagem + Kling), locução e montagem.
Janela do VS Code **verde** = projeto Castle (terminal com fundo e borda verdes, texto claro legível).

Estrutura herdada de `af.consultoria.vscode.agente.video`, sem o conteúdo da A.F.

## Regras e ferramentas
- **[CLAUDE.md](CLAUDE.md)** — fonte única de regras.
- `python3 ferramentas/preflight.py` — checa o ambiente antes de gastar crédito.
- `python3 ferramentas/qa_video.py video.mp4 --duracao 30` — mede o vídeo e gera folha de quadros.
- `python3 ferramentas/corrigir_audio.py entrada.mp4 saida.mp4` — corrige loudness/pico.
- `python3 ferramentas/estado.py ver|aprovar|reprovar|publicado video.mp4` — só pessoa aprova.
- `python3 magnific.py imagens --projeto cenas-cape-cod.json --simular` — mostra o que seria pago.
- Fatos permitidos: `castle/marca/fatos.md`.

## Começar um vídeo
Abrir esta pasta no VS Code, abrir o Claude Code e pedir "próximo vídeo da Castle"
(agente `agente.video.clastle`, skill `proximo-video-clastle`).

## Configuração (uma vez por computador)
`cp .env.example .env` e colocar a `MAGNIFIC_API_KEY`; `brew install ffmpeg`; `pip install -r requirements.txt`.
