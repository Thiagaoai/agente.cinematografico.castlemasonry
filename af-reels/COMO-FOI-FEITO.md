# Como o vídeo 01 foi feito — passo a passo

Vídeo entregue: `entregas/af.consultoria.vsclaude.mp4` · vertical 1080×1920 · 37 s · 30 fps · −14,2 LUFS.

## 1. Leitura do site
Li a home, `/obra-parada/` e `/faq/` de araujoferrazconsultoria.com.br e extraí: serviços, dores do cliente, método em 5 etapas, frases do próprio site, WhatsApp, cores (`#b6722d`, `#f4ece3`, `#241a12`) e fontes (Archivo, Plex Mono).
O site não traz números de clientes nem depoimentos. Por isso **nenhum roteiro afirma resultado, prazo ou preço**.

## 2. Marca
Baixei o logo oficial em SVG direto do site e gerei o PNG branco (a versão cobre foi feita para fundo claro e some no escuro). Converti a fonte Archivo para uso nas legendas e no cartão final.

## 3. Série de 15 roteiros
Cada pilar do site virou um vídeo: obra parada, método, orçamento/SINAPI/BDI, glosa, medição, prefeitura pequena, convênio, Lei 14.133, projeto executivo, BIM, infraestrutura, saneamento, "manda o que você tem", quem assina, Brasil inteiro. Tudo em `serie.json` (fonte única); `roteiros.md` e `cronograma-outubro.md` são gerados dele.

## 4. Imagens (Magnific · Seedream 5 Pro, 9:16, 2K)
1. Gerei **a cena âncora** (obra de concreto abandonada em Goiás) em 2 variações e escolhi a mais coerente.
2. As outras 5 cenas usaram a âncora como referência (estilo ou imagem), para manter luz, cor e local.
3. Revisei uma folha de contato: sem texto, sem rosto deformado, estrutura coerente.

## 5. Animação (Magnific · Kling 3.0, 1080p, 5 s, sem som)
Um **único movimento de câmera** por cena, com a trava "estruturas permanecem sólidas, sem deformar". Extraí 4 quadros de cada clipe e conferi: nada derreteu.

## 6. Voz e música (ElevenLabs)
- Locução: voz **Rafael – Deep & Professional** (pt-BR), uma frase por cena. A última frase foi regravada com grafia fonética ("Á éfe", "uatsápi") para evitar pronúncia em inglês.
- Trilha: instrumental de 38 s, começa tensa e termina resolvida.

## 7. Montagem (`montar_reel.py`)
- Cenas com transição suave; onde a fala é maior que 5 s, a cena fica um pouco mais lenta.
- Legendas curtas, **logo em marca d'água** no topo, cartão final com CTA ("Falar sobre minha obra", WhatsApp e site).
- A trilha abaixa quando a voz fala (ducking) e o áudio fecha em −14 LUFS.

## 8. Controle de qualidade
Verifiquei formato, loudness e quadros-chave; corrigi marca d'água fraca e a legenda "A. F". **Não consigo ouvir o áudio**: ouça a locução antes de postar.

## Custo
Magnific: **3.950 créditos** (saldo foi de 216.810 para 212.860). ElevenLabs: poucas centenas de caracteres e uma trilha de 38 s, dentro do plano.

## Próximos vídeos
Peça "próximo vídeo". A skill `proximo-video-af` (em `.claude/skills/`) repete este fluxo para o vídeo seguinte do cronograma.
