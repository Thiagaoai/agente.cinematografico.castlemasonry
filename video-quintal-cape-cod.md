# Vídeo — Quintal Cape Cod: pátio, piscina, putting green, lareira e fire pit

**Formato:** 16:9 · **Duração:** ~35 s · 7 cenas de 5 s · **Ferramenta:** Magnific
**Arco:** chegada pela casa → um dia inteiro no quintal (manhã → tarde → pôr do sol → noite) → revelação aérea final com tudo aceso.

## Bíblia visual (colar no começo de TODO prompt para manter a mesma casa)
> Casa clássica de Cape Cod de dois andares, paredes e telhado de telha de cedro (cedar shingle) envelhecida em cinza prateado, acabamentos brancos, janelas de guilhotina com venezianas brancas, chaminé de pedra. Quintal com pátio de bluestone, piscina retangular com borda de granito, putting green de grama sintética, lareira externa de pedra natural e fire pit redondo de granito. Hortênsias azuis, capim costeiro, pinheiros ao fundo.

**Dica de consistência:** gere primeiro a imagem da **Cena 7 (visão aérea geral)**, escolha a melhor e use-a como imagem de referência (style/structure reference) em todas as outras cenas. Assim a casa e a disposição do quintal não mudam entre os planos.

## Mapa de cenas + técnicas (eyecannndy.com)

| # | Hora | Cena | Técnica Eyecandy |
|---|------|------|------|
| 1 | Manhã | Chegada: drone passa sobre o telhado de cedro e revela o quintal | [FPV Drone](https://eyecannndy.com/technique/fpv-drone) |
| 2 | Manhã | Pátio de bluestone, câmera rente ao chão | [Ground Level](https://eyecannndy.com/technique/ground-shot) + [Parallax](https://eyecannndy.com/technique/parallax) |
| 3 | Meio-dia | Piscina vista de cima | [Overhead](https://eyecannndy.com/technique/overhead) + [Pedestal](https://eyecannndy.com/technique/pedestal) |
| 4 | Tarde | Putting green: bola rolando até o buraco | [Ground Level](https://eyecannndy.com/technique/ground-shot) + [Focal shift](https://eyecannndy.com/technique/focal-shift) |
| 5 | Pôr do sol | Lareira externa de pedra sendo acesa | [Arc](https://eyecannndy.com/technique/arc-movement) + [Haze](https://eyecannndy.com/technique/haze) |
| 6 | Noite | Fire pit com família, faíscas | [Speed Ramp](https://eyecannndy.com/technique/speed-ramping) + [Arc](https://eyecannndy.com/technique/arc-movement) |
| 7 | Noite | Final: drone recua e mostra o quintal inteiro iluminado | [FPV Drone](https://eyecannndy.com/technique/fpv-drone) (pull-back) |

**Transições sugeridas:** 3→4 [Match Cut](https://eyecannndy.com/technique/match-cut) (círculo do ralo/escada da piscina → círculo do buraco do golfe); 5→6 Match Cut de fogo para fogo.

---

## Cena 1 — Chegada (FPV Drone)
```json
{
  "prompt_completo": "Drone FPV voa rasante sobre o telhado de telha de cedro prateado de uma casa clássica de Cape Cod e mergulha revelando o quintal: pátio de bluestone, piscina azul-turquesa, putting green, lareira de pedra e fire pit de granito. Lente 14mm, luz suave da manhã com névoa costeira se dissipando, 4K, sensação de chegada e descoberta.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária imobiliária",
    "estilo_visual": "Cinematográfico dinâmico e luminoso",
    "sujeito_principal": "Casa estilo Cape Cod e quintal completo revelado por cima do telhado"
  },
  "composicao": {
    "posicionamento": "Telhado ocupa o primeiro plano e sai do quadro, quintal surge no centro",
    "angulo": "Aéreo em plongée com mergulho",
    "enquadramento": "Plano aberto"
  },
  "ambiente": {
    "cenario": "Quintal residencial costeiro em Cape Cod",
    "superficie": "Telhado de cedro, depois bluestone, gramado e água",
    "elementos_visuais": "Chaminé de pedra, piscina, putting green com bandeira, pinheiros, névoa",
    "atmosfera_espacial": "Ampla e reveladora"
  },
  "iluminacao": {
    "tipo": "Sol da manhã",
    "qualidade": "Suave e difusa pela névoa",
    "direcao": "Lateral baixa (leste)",
    "efeito": "Brilho prateado nas telhas, água cintilando"
  },
  "especificacoes_tecnicas": {
    "lente": "14mm",
    "angulo_de_camera": "FPV drone dive over roofline",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto: textura das telhas de cedro nítida"
  },
  "atmosfera": {
    "mood": "Empolgante e fresco",
    "emocao": "Curiosidade e encantamento",
    "conceito": "Bem-vindo ao quintal dos sonhos"
  },
  "palavras_chave": ["FPV drone", "reveal", "cedar shingle", "Cape Cod", "névoa matinal", "ultra wide", "imobiliário"],
  "parametros_ia": { "qualidade": "ultra_high", "estilo": "cinematic_photography", "modo": "advertising_hero", "aspect_ratio": "16:9" }
}
```
**Motion:** `FPV drone flies low over the cedar shingle roof, crests the ridge and dives down revealing the backyard with patio, pool, putting green, fireplace and fire pit, morning mist clearing`

---

## Cena 2 — Pátio (Ground Level + Parallax)
```json
{
  "prompt_completo": "Câmera a 40 cm do chão desliza sobre um pátio de bluestone com juntas precisas em direção à casa Cape Cod de telhas de cedro, hortênsias azuis desfocadas no primeiro plano criando paralaxe. Lente 35mm, sol da manhã rasante realçando a textura da pedra, móveis de teca ao fundo. 4K, sensação de calma, qualidade e convite.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária",
    "estilo_visual": "Cinematográfico naturalista",
    "sujeito_principal": "Pátio de bluestone diante da casa"
  },
  "composicao": {
    "posicionamento": "Pedras no terço inferior conduzindo o olhar até a casa",
    "angulo": "Ground level",
    "enquadramento": "Plano médio-aberto"
  },
  "ambiente": {
    "cenario": "Pátio junto aos fundos da casa",
    "superficie": "Bluestone com juntas de areia polimérica",
    "elementos_visuais": "Hortênsias em primeiro plano, mesa e cadeiras de teca, vasos",
    "atmosfera_espacial": "Profunda, em camadas"
  },
  "iluminacao": {
    "tipo": "Sol da manhã",
    "qualidade": "Rasante e quente",
    "direcao": "Lateral",
    "efeito": "Relevo da pedra realçado, sombras longas"
  },
  "especificacoes_tecnicas": {
    "lente": "35mm",
    "angulo_de_camera": "Low tracking shot com paralaxe",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto: veios e juntas da pedra"
  },
  "atmosfera": {
    "mood": "Sereno e sofisticado",
    "emocao": "Desejo",
    "conceito": "Cada pedra assentada com intenção"
  },
  "palavras_chave": ["ground level", "parallax", "bluestone", "tracking", "hortênsias", "luz rasante"],
  "parametros_ia": { "qualidade": "ultra_high", "estilo": "cinematic_photography", "modo": "lifestyle", "aspect_ratio": "16:9" }
}
```
**Motion:** `low ground-level tracking shot gliding forward over the bluestone patio toward the house, hydrangeas in the foreground passing by creating parallax`

---

## Cena 3 — Piscina (Overhead + Pedestal)
```json
{
  "prompt_completo": "Vista de cima, perfeitamente perpendicular, de uma piscina retangular azul-turquesa com borda de granito e deck de bluestone, espreguiçadeiras brancas alinhadas e sombras gráficas de guarda-sóis. Câmera sobe devagar com lente 24mm sob sol de meio-dia, cáusticas de luz dançando no fundo da piscina. 4K, composição geométrica, sensação de frescor e verão perfeito.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária arquitetônica",
    "estilo_visual": "Minimalista gráfico e vibrante",
    "sujeito_principal": "Piscina com deck de pedra vista de cima"
  },
  "composicao": {
    "posicionamento": "Piscina centralizada, simetria total",
    "angulo": "Overhead (birds-eye)",
    "enquadramento": "Plano aberto"
  },
  "ambiente": {
    "cenario": "Área da piscina no quintal",
    "superficie": "Água turquesa, borda de granito, deck de bluestone",
    "elementos_visuais": "Espreguiçadeiras, guarda-sóis, toalhas listradas",
    "atmosfera_espacial": "Organizada e arejada"
  },
  "iluminacao": {
    "tipo": "Sol de meio-dia",
    "qualidade": "Dura",
    "direcao": "Zenital",
    "efeito": "Cáusticas na água, sombras gráficas e cores saturadas"
  },
  "especificacoes_tecnicas": {
    "lente": "24mm",
    "angulo_de_camera": "Overhead pedestal rise",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto: reflexos e cáusticas nítidos"
  },
  "atmosfera": {
    "mood": "Refrescante e luxuoso",
    "emocao": "Vontade de mergulhar",
    "conceito": "O verão perfeito de Cape Cod"
  },
  "palavras_chave": ["overhead", "birds-eye", "piscina", "cáusticas", "simetria", "pool deck", "verão"],
  "parametros_ia": { "qualidade": "ultra_high", "estilo": "commercial", "modo": "advertising_hero", "aspect_ratio": "16:9" }
}
```
**Motion:** `top-down overhead shot slowly rising (pedestal up), water rippling with light caustics, umbrella fabric moving in the breeze`

---

## Cena 4 — Putting green (Ground Level + Focal shift)
```json
{
  "prompt_completo": "Câmera no nível da grama de um putting green impecável, bola de golfe branca rolando em direção ao buraco com bandeira, enquanto a casa Cape Cod de cedro aparece desfocada ao fundo. Lente 100mm, luz dourada de fim de tarde, foco passa da bola para o buraco no momento exato. 4K, sensação de lazer, precisão e conquista.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária lifestyle",
    "estilo_visual": "Cinematográfico quente com foco seletivo",
    "sujeito_principal": "Bola de golfe rolando até o buraco no putting green"
  },
  "composicao": {
    "posicionamento": "Bola no terço esquerdo, buraco e bandeira no terço direito",
    "angulo": "Ground level",
    "enquadramento": "Close-up/detalhe"
  },
  "ambiente": {
    "cenario": "Putting green no quintal, ao lado da piscina",
    "superficie": "Grama sintética de green, borda de pedra",
    "elementos_visuais": "Bandeira vermelha, taco desfocado, casa ao fundo",
    "atmosfera_espacial": "Íntima, com profundidade comprimida"
  },
  "iluminacao": {
    "tipo": "Sol de fim de tarde",
    "qualidade": "Quente e suave",
    "direcao": "Contraluz",
    "efeito": "Grama com brilho nas pontas, bokeh dourado"
  },
  "especificacoes_tecnicas": {
    "lente": "100mm",
    "angulo_de_camera": "Ground-level rack focus",
    "resolucao": "4K",
    "nivel_detalhamento": "Ultra: textura da grama e covinhas da bola"
  },
  "atmosfera": {
    "mood": "Descontraído e satisfatório",
    "emocao": "Prazer da jogada perfeita",
    "conceito": "Lazer sem sair de casa"
  },
  "palavras_chave": ["putting green", "ground level", "rack focus", "bokeh", "golden hour", "lazer", "precisão"],
  "parametros_ia": { "qualidade": "ultra_high", "estilo": "cinematic_photography", "modo": "lifestyle", "aspect_ratio": "16:9" }
}
```
**Motion:** `ground-level shot, golf ball rolls across the putting green and drops into the cup, rack focus from the ball to the hole, flag fluttering gently`

---

## Cena 5 — Lareira externa (Arc + Haze)
```json
{
  "prompt_completo": "Lareira externa de pedra natural com chaminé alta sob uma pérgula, primeiras chamas ganhando força enquanto o céu de Cape Cod fica rosa e lilás. Câmera em arco lento com lente 50mm, leve névoa e fumaça suave criando halo dourado, poltronas com mantas em primeiro plano. 4K, sensação de aconchego e transição do dia para a noite.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária lifestyle",
    "estilo_visual": "Cinematográfico quente e etéreo",
    "sujeito_principal": "Lareira externa de pedra natural acesa"
  },
  "composicao": {
    "posicionamento": "Lareira no terço direito, poltronas no terço esquerdo",
    "angulo": "Eye-level",
    "enquadramento": "Plano médio"
  },
  "ambiente": {
    "cenario": "Sala de estar externa com pérgula ao lado do pátio",
    "superficie": "Piso de bluestone",
    "elementos_visuais": "Chaminé de pedra, lenha empilhada, mantas, lanternas",
    "atmosfera_espacial": "Acolhedora e protegida"
  },
  "iluminacao": {
    "tipo": "Fogo + pôr do sol",
    "qualidade": "Suave e enevoada",
    "direcao": "Fogo frontal, céu em contraluz",
    "efeito": "Halo dourado, névoa luminosa, contraste quente e rosa"
  },
  "especificacoes_tecnicas": {
    "lente": "50mm",
    "angulo_de_camera": "Slow arc shot",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto: textura da pedra, chamas definidas"
  },
  "atmosfera": {
    "mood": "Aconchegante e nostálgico",
    "emocao": "Calma",
    "conceito": "O quintal que funciona em todas as estações"
  },
  "palavras_chave": ["lareira externa", "arc shot", "haze", "pôr do sol", "pedra natural", "aconchego", "outdoor living"],
  "parametros_ia": { "qualidade": "ultra_high", "estilo": "cinematic_photography", "modo": "lifestyle", "aspect_ratio": "16:9" }
}
```
**Motion:** `slow arc around the stone outdoor fireplace as flames grow, soft haze and smoke catching golden light, sunset sky shifting colors`

---

## Cena 6 — Fire pit (Speed Ramp + Arc)
```json
{
  "prompt_completo": "Fire pit redondo de granito aceso à noite no pátio, família e amigos rindo com mantas e marshmallows, faíscas subindo ao céu azul-escuro. Câmera em arco com lente 35mm e speed ramp: as faíscas desaceleram em câmera lenta e voltam ao normal. Luzinhas penduradas, piscina iluminada ao fundo, 4K, grão sutil, sensação de memória e calor humano.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária lifestyle",
    "estilo_visual": "Cinematográfico quente e íntimo",
    "sujeito_principal": "Fire pit de granito com pessoas ao redor"
  },
  "composicao": {
    "posicionamento": "Fogo no centro, pessoas em semicírculo",
    "angulo": "Eye-level levemente alto",
    "enquadramento": "Plano médio"
  },
  "ambiente": {
    "cenario": "Pátio à noite com piscina iluminada ao fundo",
    "superficie": "Bluestone com reflexos do fogo",
    "elementos_visuais": "Cadeiras Adirondack, mantas, marshmallows, luzinhas",
    "atmosfera_espacial": "Aconchegante e protegida"
  },
  "iluminacao": {
    "tipo": "Fogo + crepúsculo azul + piscina iluminada",
    "qualidade": "Quente e tremeluzente",
    "direcao": "Central",
    "efeito": "Contraste laranja e azul-turquesa"
  },
  "especificacoes_tecnicas": {
    "lente": "35mm",
    "angulo_de_camera": "Arc shot com speed ramp",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto, com grão de filme sutil"
  },
  "atmosfera": {
    "mood": "Caloroso e festivo",
    "emocao": "Pertencimento",
    "conceito": "Onde as memórias acontecem"
  },
  "palavras_chave": ["fire pit", "speed ramp", "slow motion", "faíscas", "lifestyle", "laranja e azul", "família"],
  "parametros_ia": { "qualidade": "ultra_high", "estilo": "cinematic_photography", "modo": "lifestyle", "aspect_ratio": "16:9" }
}
```
**Motion:** `slow arc around the fire pit, speed ramp with sparks rising in slow motion then returning to normal speed, people laughing, flames flickering`

---

## Cena 7 — Final aéreo (gere esta primeiro como referência)
```json
{
  "prompt_completo": "Vista aérea noturna de uma casa clássica de Cape Cod com telhas de cedro e janelas acesas, quintal completo iluminado: piscina turquesa brilhando, pátio de bluestone, putting green, lareira e fire pit acesos, luzinhas penduradas. Drone recua e sobe lentamente com lente 24mm, céu azul-profundo com últimas luzes no horizonte. 4K, espaço no céu para o logo, sensação de sonho realizado.",
  "configuracao_basica": {
    "tipo_fotografia": "Publicitária imobiliária",
    "estilo_visual": "Cinematográfico noturno, blue hour",
    "sujeito_principal": "Casa Cape Cod e quintal completo iluminado à noite"
  },
  "composicao": {
    "posicionamento": "Quintal no terço inferior, céu livre no terço superior para texto",
    "angulo": "Aéreo em plongée",
    "enquadramento": "Plano aberto (wide)"
  },
  "ambiente": {
    "cenario": "Propriedade costeira com pinheiros ao redor",
    "superficie": "Bluestone, água, grama de green",
    "elementos_visuais": "Piscina iluminada, fogo, luzinhas, janelas acesas",
    "atmosfera_espacial": "Ampla, acolhedora, isolada"
  },
  "iluminacao": {
    "tipo": "Blue hour + luzes práticas",
    "qualidade": "Suave com pontos quentes",
    "direcao": "Luzes internas e do fogo contra o céu azul",
    "efeito": "Quintal brilhando como uma joia na escuridão"
  },
  "especificacoes_tecnicas": {
    "lente": "24mm",
    "angulo_de_camera": "Drone pull-back and rise",
    "resolucao": "4K",
    "nivel_detalhamento": "Alto: todas as áreas do quintal legíveis"
  },
  "atmosfera": {
    "mood": "Grandioso e acolhedor",
    "emocao": "Orgulho e desejo",
    "conceito": "O quintal completo, do dia à noite"
  },
  "palavras_chave": ["aerial", "blue hour", "pull-back", "Cape Cod", "outdoor living", "end card", "luxo"],
  "parametros_ia": { "qualidade": "ultra_high", "estilo": "cinematic_photography", "modo": "advertising_hero", "aspect_ratio": "16:9" }
}
```
**Motion:** `drone slowly pulls back and rises revealing the whole illuminated backyard at night, flames flickering, pool glowing, string lights twinkling`

**Texto final na edição:** `CASTLE MASONRY` / `Built to last. Worth the reveal.` / `Cape Cod & Martha's Vineyard · (774) 487-0592`
