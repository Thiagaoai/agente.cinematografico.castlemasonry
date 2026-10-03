# Regras do Agente Cinematográfico

Fonte única de regras: **`CLAUDE.md`** na raiz do projeto. Leia antes de agir.
Este arquivo resume só a técnica de prompt (detalhes em `prompt-sistema.md`).

1. **Sem JSON na resposta ao usuário**: aplicar nos arquivos e responder em português executivo.

2. **Prompts para Mystic (imagem)** — em inglês, com ótica e materiais reais (`24mm f/4`, `35mm`,
   `blue hour`, `raking morning sunlight`, materiais físicos). Evitar "ultra 4K, photorealistic";
   usar "architectural photography, natural color science, fine film grain".

3. **Prompts para Kling (vídeo)** — **um único vetor de movimento** (`Slow dolly forward`,
   `Pedestal up`, `Gentle tracking shot`); terminar com
   `Structures, masonry, and ground remain rigid, solid and locked. Only [wind/water/fire] moves subtly.`

4. **Cena âncora** — gerar e aprovar uma cena mestre primeiro e usá-la como `style_reference`.
   Isso reduz variação entre cenas; não garante consistência: revisar cada cena contra a âncora.

5. **Entrega** — `ferramentas/qa_video.py` no arquivo final, olhar a folha de quadros, e chamar de
   "prévia aguardando escuta" até o usuário aprovar.
