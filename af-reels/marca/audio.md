# Áudio da série A.F — voz fixa e banco de trilhas dramáticas

## Voz (FIXA — aprovada pelo usuário em 2026-10-03)

Aprovada ao assistir a V02 corrigida (`videos/obra-parada-v02/entrega/af-obra-parada-vertical-v02-audio.mp4`):
"gostei… quero que mantenha a mesma voz".

| Parâmetro | Valor |
|---|---|
| Ferramenta | **Runway `generate_speech`** (conector Runway) |
| Modelo | `eleven_v3` |
| Voz | **`Bernard`** |
| Idioma | `languageCode: "pt-br"` |
| Velocidade | `speed: 1` (nunca acelerar para caber no tempo: reescrever o texto) |
| Origem | tarefa Runway `211a73cb-3502-40b8-b92d-99e3d6acc78b` (V02) |

Grafia usada no texto falado aprovado (a legenda mantém a grafia correta):
- "A.F" → **"A A F"** (assim foi escrito na locução aprovada)
- "WhatsApp" → **"WhatsApp"** (sem grafia fonética)
- Reticências e pontuação marcam pausas ("Sua obra parou... e você…").

Regras:
- **Não trocar de voz, modelo ou ferramenta.** Se o Runway não estiver conectado nesta sessão,
  **parar e avisar** — não substituir por outra voz "parecida" (ElevenLabs Rafael, etc.).
- **Uma chamada por frase** (`f01.mp3 … f06.mp3`, uma por cena), porque `montar_reel.py` encaixa cada
  fala na sua cena. Mesmos parâmetros em todas. Se a entonação ficar desigual entre frases, avisar o usuário.
- Termos ainda não ouvidos nesta voz (BDI, SINAPI, SICRO, TCU, ETP, 14.133, nomes próprios):
  fazer **amostra curta** só com esses termos e esperar o usuário aprovar antes da locução completa.
  Registrar aqui a grafia aprovada de cada termo novo.

| Termo | Grafia aprovada para a voz Bernard | Aprovado em |
|---|---|---|
| A.F | A A F | 2026-10-03 (V02) |
| WhatsApp | WhatsApp | 2026-10-03 (V02) |

## Trilha — variações dramáticas (pedido do usuário em 2026-10-03)

O usuário quer **trilhas mais dramáticas e variadas** de um vídeo para o outro.
- Ferramenta: **Runway `generate_music`, modelo `lyria-3-clip`** (o mesmo da V02). Se indisponível,
  ElevenLabs `compose_music` com o mesmo prompt é aceitável (a trilha pode variar; a voz não).
- **Rotação:** vídeo NN usa a variação `((NN − 1) mod 6) + 1`. Pode trocar se o tema pedir outra
  (ex.: tema mais tenso → D1/D4), mas **nunca repetir a variação do vídeo anterior**.
  Registrar em `serie.json` → vídeo: `trilha: {variacao: "D3", ferramenta, tarefa, prompt}`.
- Toda variação termina **resolvida e confiante** (marca de engenharia: drama na dor, firmeza na solução).
- Sufixo obrigatório em todo prompt (colar no fim):
  `Instrumental only: no vocals, no choir, no speech, no lyrics. Leave clear midrange space for Brazilian Portuguese male narration. Cinematic and dramatic but not horror, no alarms, no jump scares. Ends resolved and confident on the final 4 seconds. Around 38 seconds.`
- Mixagem: trilha **sempre com ducking** sob a voz (`sidechaincompress`), e o QA final tem que
  passar (−16 a −14 LUFS, ≤ −1,5 dBTP). Drama alto não pode mascarar a fala nem o CTA.

### D1 — Tensão épica crescente
`Epic cinematic trailer underscore, 85 BPM. Deep low taiko and orchestral toms, sustained cello and contrabass drone in D minor, slow rising string ostinato, distant restrained brass swells. Starts sparse and tense, builds steadily in intensity, final section lifts to a major chord with warm brass and strings.`

### D2 — Cordas em suspense
`Dramatic suspense strings score, 110 BPM. Tight staccato violin and viola ostinato, pulsing cello eighth notes, soft timpani rolls, ticking high percussion. Feels urgent and focused like a countdown, tension rises every 8 bars, resolves into sustained hopeful strings with a clear tonic chord.`

### D3 — Piano dramático com orquestra
`Emotional dramatic piano score, 72 BPM. Solo grand piano plays a slow minor-key motif with reverb, joined by swelling low strings and a gentle cinematic heartbeat pulse. Melancholic and serious at first, orchestra grows behind the piano, turns to a warm major resolution with full strings.`

### D4 — Pulso grave cinematográfico
`Dark cinematic pulse, 100 BPM. Deep sub-bass heartbeat, analog synth arpeggio, metallic clock-like ticks, reversed swells and low impacts every 4 bars. Brooding and determined, builds pressure, then opens into bright layered synth pads and strings for a confident, resolved ending.`

### D5 — Orquestral heroico contido
`Heroic orchestral build, 95 BPM. Low french horns and trombones in long notes, driving string spiccato, snare rolls and big cinematic bass drum hits. Starts dramatic and weighty, rises to a triumphant but restrained climax, ends on a broad resolved brass and string chord. Corporate premium, not bombastic.`

### D6 — Minimalista de alto impacto
`Minimal high-impact cinematic score, 90 BPM. Sustained dark ambient drone, sparse deep percussive hits, rising risers and whooshes between phrases, a single repeated low piano note creating tension. Lots of space and silence, builds to a powerful final hit followed by a warm sustained major chord.`

### Referência: trilha da V02 (aprovada, menos dramática — não usar de novo como padrão)
`Instrumental advertising background bed, confident warm cinematic electronic pulse, 100 BPM. Muted piano, subtle low bass, tight soft kick, uplifting restrained strings. Immediate memorable opening pulse, gentle build toward a confident ending. Premium engineering consultancy Instagram reel. No vocals, no speech, no choir, no lyrics. Leave ample sonic space for Brazilian Portuguese narration. Not aggressive, no alarm or horror.`
