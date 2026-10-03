# Vídeo Castle Masonry — "Worth the reveal"

**Formato:** 16:9 (landscape) · **Duração:** ~30 s · 6 cenas de 5 s
**Ferramenta:** Magnific (gerar o quadro inicial em imagem → animar em vídeo → upscale final)

## Conceito
Base no que o site diz de si mesmo:
- Tagline: *"Built to last. Worth the reveal."*
- Filosofia: *"We build the part nobody sees, first."* (base e drenagem certas no solo arenoso do Cape)
- Materiais: granito envelhecido, bluestone, paralelepípedo de granito de demolição, assentamento manual
- Território: Cape Cod e Martha's Vineyard, com casas de telha de cedro (cedar shingle) nas **paredes** e **telhado**

**Arco narrativo:** o que ninguém vê (base) → as mãos do artesão → a revelação do pátio pronto → a vida acontecendo nele → marca.

## Técnicas de referência (eyecannndy.com)
Cada cena usa uma técnica catalogada no Eyecandy — abra o link para ver exemplos antes de gerar.

| # | Cena | Técnica Eyecandy | Por que serve |
|---|------|------|------|
| 1 | Câmera atravessa o pátio pronto e mergulha nas camadas da base | [Pass Through](https://eyecannndy.com/technique/pass-through) + [Probe](https://eyecannndy.com/technique/probe-lens) | Mostra literalmente "the part nobody sees" — gancho dos 2 primeiros segundos |
| 2 | Mãos assentando bluestone | [Probe](https://eyecannndy.com/technique/probe-lens) + [Focal shift](https://eyecannndy.com/technique/focal-shift) | Macro tátil; foco passa do martelo para a junta perfeita |
| 2→3 | Transição | [Match Cut](https://eyecannndy.com/technique/match-cut) | Textura da pedra na mão = textura da pedra no muro |
| 3 | Muro de granito ao entardecer | [Pedestal](https://eyecannndy.com/technique/pedestal) + [Parallax](https://eyecannndy.com/technique/parallax) | Câmera sobe com capim em primeiro plano → profundidade |
| 4 | **A revelação:** quintal de terra vira pátio pronto | [Set Transition](https://eyecannndy.com/technique/set-transition) + [Arc](https://eyecannndy.com/technique/arc-movement) | O antes/depois É o "Worth the reveal" |
| 5 | Fire pit à noite, família | [Arc](https://eyecannndy.com/technique/arc-movement) + [Speed Ramp](https://eyecannndy.com/technique/speed-ramping) | Faíscas em câmera lenta, depois volta ao normal |
| 6 | Pátio ao amanhecer + logo | [Overhead](https://eyecannndy.com/technique/overhead) + [Haze](https://eyecannndy.com/technique/haze) | Vista de cima mostra o padrão de assentamento; névoa dá calma para o fechamento |

Alternativas se sobrar orçamento: [FPV Drone](https://eyecannndy.com/technique/fpv-drone) voando rasante pelo caminho de pedra até o pátio; [Ground Level](https://eyecannndy.com/technique/ground-shot) para a cena 1 se o Pass Through não sair bem.

> **Dica:** o site tem 119 fotos reais de obras (`castlemasonryma.com/work/...`). Usar uma delas como imagem inicial no Magnific (image-to-video) deixa o vídeo fiel ao trabalho deles — o próprio site diz "no stock, no renders".

---

## Cena 1 — A base que ninguém vê
```json
{
  "prompt_completo": "Lente probe desce rente a um pátio de bluestone em Cape Cod e atravessa a junta entre as pedras, mergulhando em um corte perfeito das camadas ocultas: areia nivelada, brita compactada e manta de drenagem. Luz dourada rasante da manhã revela cada textura granular, poeira fina suspensa. Tons terrosos, profundidade de campo rasa, 4K, clima de precisão silenciosa e fundação honesta.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária documental",
    "estilo_visual": "Cinematográfico naturalista, tons terrosos",
    "sujeito_principal": "Camadas de base compactada (brita e areia) de um pátio em construção"
  },
  "composicao": {
    "posicionamento": "Camadas em corte ocupando o terço inferior, linha de nível cruzando o quadro",
    "angulo": "Eye-level rente ao chão",
    "enquadramento": "Plano detalhe"
  },
  "ambiente": {
    "cenario": "Quintal residencial em Cape Cod durante a obra, gramado e pinheiros desfocados ao fundo",
    "superficie": "Brita compactada e areia nivelada com régua",
    "elementos_visuais": "Linhas de nível em barbante, estacas de madeira, placa compactadora desfocada",
    "atmosfera_espacial": "Íntima, focada no chão"
  },
  "iluminacao": {
    "tipo": "Sol da manhã",
    "qualidade": "Dura e rasante",
    "direcao": "Lateral baixa",
    "efeito": "Microtextura dos agregados realçada, sombras longas"
  },
  "especificacoes_tecnicas": {
    "lente": "35mm",
    "angulo_de_camera": "Low-angle slider shot",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto: grãos de areia e arestas da brita visíveis"
  },
  "atmosfera": {
    "mood": "Silencioso e meticuloso",
    "emocao": "Confiança",
    "conceito": "O que sustenta tudo é o que ninguém vê"
  },
  "palavras_chave": ["fundação", "textura", "luz rasante", "slider", "artesanal", "tons terrosos", "processo"],
  "parametros_ia": {
    "qualidade": "ultra_high",
    "estilo": "documentary",
    "modo": "advertising_hero",
    "aspect_ratio": "16:9"
  }
}
```
**Motion:** `probe lens pass-through shot: camera glides low over the stone patio, dives through the joint between stones and descends into a cross-section of compacted gravel and sand layers, dust drifting, no people`

---

## Cena 2 — As mãos
```json
{
  "prompt_completo": "Mãos calejadas de pedreiro com luvas gastas assentando uma placa de bluestone sobre areia, batendo levemente com martelo de borracha. Close com lente 100mm, push-in lento, luz suave de céu nublado de Cape Cod realçando o azul-acinzentado da pedra e as juntas precisas. Fundo em bokeh verde, 4K, sensação de ofício paciente e orgulho no detalhe.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária",
    "estilo_visual": "Cinematográfico íntimo, cores frias e naturais",
    "sujeito_principal": "Mãos de artesão assentando placa de bluestone"
  },
  "composicao": {
    "posicionamento": "Mãos e pedra no centro, ligeiramente à direita",
    "angulo": "Plongée suave (45°)",
    "enquadramento": "Close-up"
  },
  "ambiente": {
    "cenario": "Pátio em construção em quintal costeiro",
    "superficie": "Areia nivelada e placas de bluestone já assentadas",
    "elementos_visuais": "Martelo de borracha, nível de bolha, juntas alinhadas",
    "atmosfera_espacial": "Próxima e tátil"
  },
  "iluminacao": {
    "tipo": "Céu nublado costeiro",
    "qualidade": "Suave e difusa",
    "direcao": "Superior",
    "efeito": "Cores fiéis da pedra, sem sombras duras"
  },
  "especificacoes_tecnicas": {
    "lente": "100mm macro",
    "angulo_de_camera": "Slow push-in close-up",
    "resolucao": "4K",
    "nivel_detalhamento": "Ultra: veios da pedra, textura das luvas"
  },
  "atmosfera": {
    "mood": "Paciente e preciso",
    "emocao": "Respeito pelo ofício",
    "conceito": "Assentado à mão, peça por peça"
  },
  "palavras_chave": ["bluestone", "artesão", "close-up", "push-in", "tátil", "luz difusa", "precisão"],
  "parametros_ia": {
    "qualidade": "ultra_high",
    "estilo": "cinematic_photography",
    "modo": "advertising_hero",
    "aspect_ratio": "16:9"
  }
}
```
**Motion:** `macro probe shot, slow push-in, hands tap the stone with a rubber mallet, rack focus from the mallet to the tight stone joint`

**Transição 2→3 (Match Cut):** termine a cena 2 num close da superfície da pedra e comece a cena 3 no mesmo enquadramento de textura do muro — o corte "casa" as duas pedras.

---

## Cena 3 — O muro
```json
{
  "prompt_completo": "Muro de arrimo de granito envelhecido curvando por um jardim em desnível, degraus de pedra subindo até um gramado verde. Tilt-up lento com lente 24mm partindo das juntas da base até revelar o jardim sob luz dourada do fim de tarde, hortênsias azuis e capim costeiro balançando. 4K, sensação de solidez atemporal e pertencimento à paisagem.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária arquitetônica",
    "estilo_visual": "Cinematográfico quente, golden hour",
    "sujeito_principal": "Muro de arrimo e degraus de granito envelhecido"
  },
  "composicao": {
    "posicionamento": "Muro em diagonal da esquerda inferior para a direita superior",
    "angulo": "Contra-plongée evoluindo para eye-level",
    "enquadramento": "Plano médio-aberto"
  },
  "ambiente": {
    "cenario": "Jardim residencial em desnível em Cape Cod",
    "superficie": "Degraus de granito e gramado",
    "elementos_visuais": "Hortênsias azuis, capim costeiro, pinheiros ao fundo",
    "atmosfera_espacial": "Ampla, com camadas de profundidade"
  },
  "iluminacao": {
    "tipo": "Sol de fim de tarde",
    "qualidade": "Quente e direcional",
    "direcao": "Contraluz lateral",
    "efeito": "Bordas douradas nas pedras, textura em relevo"
  },
  "especificacoes_tecnicas": {
    "lente": "24mm",
    "angulo_de_camera": "Tilt-up reveal",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto: textura do granito, folhagem nítida"
  },
  "atmosfera": {
    "mood": "Sólido e acolhedor",
    "emocao": "Segurança",
    "conceito": "Feito para durar gerações"
  },
  "palavras_chave": ["granito", "muro de arrimo", "golden hour", "tilt-up", "paisagismo", "hortênsias", "solidez"],
  "parametros_ia": {
    "qualidade": "ultra_high",
    "estilo": "cinematic_photography",
    "modo": "advertising_hero",
    "aspect_ratio": "16:9"
  }
}
```
**Motion:** `pedestal shot rising from a close-up of the stone joints to reveal the garden, coastal grass in the foreground creating parallax, hydrangeas swaying in the breeze`

---

## Cena 4 — A revelação (cena-chave)
```json
{
  "prompt_completo": "Quintal de terra batida diante de uma casa clássica de Cape Cod com paredes e telhado de cedro envelhecido se transforma, pedra por pedra, num pátio de bluestone com caminho de paralelepípedos de granito, hortênsias e gramado impecável. Câmera em arco lento com lente 24mm na golden hour, luz quente rasante desenhando cada junta. 4K, sensação de revelação, orgulho e lar completo.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária",
    "estilo_visual": "Cinematográfico épico e quente",
    "sujeito_principal": "Pátio de bluestone com caminho de cobblestone em casa de Cape Cod"
  },
  "composicao": {
    "posicionamento": "Pátio no terço inferior, casa no terço superior",
    "angulo": "Aéreo em plongée, subindo",
    "enquadramento": "Plano aberto"
  },
  "ambiente": {
    "cenario": "Quintal de casa clássica de Cape Cod com revestimento de telha de cedro nas paredes e telhado",
    "superficie": "Bluestone e paralelepípedo de granito reciclado",
    "elementos_visuais": "Hortênsias, gramado, móveis de jardim, pinheiros e vislumbre de mar ao fundo",
    "atmosfera_espacial": "Ampla e convidativa"
  },
  "iluminacao": {
    "tipo": "Golden hour",
    "qualidade": "Quente e suave",
    "direcao": "Lateral baixa",
    "efeito": "Juntas e texturas desenhadas por sombras longas, brilho dourado"
  },
  "especificacoes_tecnicas": {
    "lente": "24mm",
    "angulo_de_camera": "Drone pull-back and rise reveal",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto: padrão de assentamento legível do alto"
  },
  "atmosfera": {
    "mood": "Grandioso e acolhedor",
    "emocao": "Orgulho e realização",
    "conceito": "Worth the reveal"
  },
  "palavras_chave": ["reveal", "drone", "Cape Cod", "bluestone", "cobblestone", "cedar shingle", "golden hour", "hardscape"],
  "parametros_ia": {
    "qualidade": "ultra_high",
    "estilo": "cinematic_photography",
    "modo": "advertising_hero",
    "aspect_ratio": "16:9"
  }
}
```
**Motion:** `set transition: bare dirt yard transforms stone by stone into the finished patio while the camera arcs slowly around it, warm golden light, gentle breeze`

> **Como fazer o Set Transition no Magnific:** gere duas imagens com o mesmo enquadramento — (A) quintal de terra, (B) pátio pronto — e use A como primeiro quadro e B como último quadro (start/end frame). Se o Magnific não aceitar quadro final, use a foto real de um "depois" do site como imagem B e faça a transição na edição com morph.

---

## Cena 5 — A vida no pátio
```json
{
  "prompt_completo": "Fire pit de pedra natural aceso em pátio de pedra à noite, família rindo envolta em mantas, faíscas subindo ao céu azul-escuro de Cape Cod. Órbita lenta com lente 50mm, luz quente do fogo contrastando com luzinhas penduradas e o azul do crepúsculo. 4K, granulação sutil, sensação de memória sendo criada e calor humano.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária lifestyle",
    "estilo_visual": "Cinematográfico quente e íntimo",
    "sujeito_principal": "Fire pit de pedra com família ao redor"
  },
  "composicao": {
    "posicionamento": "Fogo no centro, pessoas em semicírculo",
    "angulo": "Eye-level",
    "enquadramento": "Plano médio"
  },
  "ambiente": {
    "cenario": "Pátio de pedra no quintal ao anoitecer",
    "superficie": "Pavers de pedra com reflexos do fogo",
    "elementos_visuais": "Mantas, cadeiras Adirondack, luzinhas penduradas, faíscas",
    "atmosfera_espacial": "Aconchegante e protegida"
  },
  "iluminacao": {
    "tipo": "Fogo + crepúsculo azul",
    "qualidade": "Quente e tremeluzente",
    "direcao": "Central (fogo) com preenchimento frio do céu",
    "efeito": "Contraste laranja e azul, rostos iluminados"
  },
  "especificacoes_tecnicas": {
    "lente": "50mm",
    "angulo_de_camera": "Slow orbit shot",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto, com grão de filme sutil"
  },
  "atmosfera": {
    "mood": "Caloroso e nostálgico",
    "emocao": "Pertencimento",
    "conceito": "O espaço onde as memórias acontecem"
  },
  "palavras_chave": ["fire pit", "lifestyle", "crepúsculo", "órbita", "laranja e azul", "família", "aconchego"],
  "parametros_ia": {
    "qualidade": "ultra_high",
    "estilo": "cinematic_photography",
    "modo": "lifestyle",
    "aspect_ratio": "16:9"
  }
}
```
**Motion:** `slow arc around the fire pit, speed ramp: sparks rising in slow motion then returning to normal speed, flickering flames, people laughing naturally`

---

## Cena 6 — Encerramento / marca
```json
{
  "prompt_completo": "Pátio de bluestone vazio ao amanhecer, orvalho nas pedras e névoa costeira leve passando entre pinheiros, cadeiras Adirondack voltadas para o horizonte. Câmera estática com lente 35mm e amplo espaço negativo no céu para o logotipo. Luz rosada e suave, paleta calma, 4K, sensação de permanência serena: built to last.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária",
    "estilo_visual": "Minimalista cinematográfico",
    "sujeito_principal": "Pátio de bluestone vazio ao amanhecer"
  },
  "composicao": {
    "posicionamento": "Pátio no terço inferior, céu livre nos dois terços superiores para texto",
    "angulo": "Eye-level",
    "enquadramento": "Plano aberto"
  },
  "ambiente": {
    "cenario": "Quintal costeiro de Cape Cod com pinheiros e horizonte",
    "superficie": "Bluestone molhado de orvalho",
    "elementos_visuais": "Névoa leve, duas cadeiras Adirondack, gramado",
    "atmosfera_espacial": "Aberta e silenciosa"
  },
  "iluminacao": {
    "tipo": "Amanhecer",
    "qualidade": "Suave e difusa",
    "direcao": "Contraluz baixa no horizonte",
    "efeito": "Brilho rosado no orvalho, névoa luminosa"
  },
  "especificacoes_tecnicas": {
    "lente": "35mm",
    "angulo_de_camera": "Static locked-off shot",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto, com céu limpo para tipografia"
  },
  "atmosfera": {
    "mood": "Sereno e duradouro",
    "emocao": "Paz",
    "conceito": "Built to last"
  },
  "palavras_chave": ["amanhecer", "espaço negativo", "névoa", "minimalista", "permanência", "bluestone", "end card"],
  "parametros_ia": {
    "qualidade": "ultra_high",
    "estilo": "commercial",
    "modo": "advertising_hero",
    "aspect_ratio": "16:9"
  }
}
```
**Motion:** `slow pedestal rise into a birds-eye overhead view of the stone patio, soft hazy morning mist drifting across, light gradually warming`

**Texto na edição:** `CASTLE MASONRY` / `Built to last. Worth the reveal.` / `Cape Cod & Martha's Vineyard · (774) 487-0592`
