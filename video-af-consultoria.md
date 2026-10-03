# Vídeo Institucional A.F Consultoria — "Enxergue o que vem pela frente"

**Duração:** 30 segundos · 6 cenas de 5 segundos · **Formato:** 16:9 widescreen
**Conceito extraído do site:** *"Antes de construir, enxergue o que vem pela frente. Um projeto que orienta, um orçamento para planejar e uma equipe técnica para acompanhar. Do início à medição final."*
**Paleta:** Terracota, areia, cobre (`#b6722d`), cimento e luz de golden hour de Goiás/Brasil.

---

## Estrutura Narrativa (30s)

| Cena | Tempo | Foco | Técnica Eyecandy | Narração Sugerida (PT-BR) |
|---|---|---|---|---|
| **01** | 0s–5s | **O Terreno:** Estação total / topografia ao amanhecer | [Ground Level](https://eyecannndy.com/technique/ground-shot) + Tracking | *"Cada obra de sucesso começa antes da primeira pedra."* |
| **02** | 5s–10s | **O Projeto:** Prancha executiva e tablet BIM na mesa | [Macro / Probe](https://eyecannndy.com/technique/probe-lens) | *"Um projeto executivo que antecipa desafios..."* |
| **03** | 10s–15s | **O Orçamento:** Planilhas oficiais (SINAPI/SICRO) e cronograma | [Rack Focus](https://eyecannndy.com/technique/focal-shift) | *"...e um orçamento com base técnica oficial, item por item."* |
| **04** | 15s–20s | **A Obra:** Engenheiro com capacete branco e tablet em campo | [Pedestal / Crane](https://eyecannndy.com/technique/pedestal) | *"Acompanhamento rigoroso para sua obra não parar."* |
| **05** | 20s–25s | **A Medição:** Pavimentação urbana pronta, linha de meio-fio perfeita | [Tracking Shot](https://eyecannndy.com/technique/tracking-shot) | *"Medição precisa do que foi realmente executado."* |
| **06** | 25s–30s | **A Entrega & Marca:** Tomada aérea golden hour + logo A.F | [FPV Pull-back](https://eyecannndy.com/technique/fpv-drone) | *"A.F Consultoria em Engenharia. Do projeto à entrega final."* |

---

## Estratégia Anti-Gasto de Créditos no Magnific

1. **Cena Âncora Escolhida:** **Cena 06 (Visão Geral de Infraestrutura)**
   - Gerar primeiro a imagem da Cena 06:
     ```bash
     python3 magnific.py imagens --cena 6
     ```
   - Uma vez gerada e aprovada, ela ancora o estilo e as cores de todas as demais:
     ```bash
     python3 magnific.py imagens --ref saida/cena6.png
     ```
2. **Geração dos Vídeos no Kling v2.6:**
   - Todos os movimentos são de vetor único (sem rotação complexa, sem giros bruscos), garantindo taxa de acerto de 100% no Kling sem deformar construções ou maquinários:
     ```bash
     python3 magnific.py videos
     ```
