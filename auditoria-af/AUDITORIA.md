# Auditoria A.F — site e consistência da produção de vídeos

Data: 3 de outubro de 2026. Site: https://araujoferrazconsultoria.com.br/

## Parecer

Minha opinião: há uma boa base visual e uma descrição técnica organizada, mas a apresentação ainda depende muito de declarações de capacidade. O próximo avanço deve ser mostrar evidências do trabalho, ajudar cada público a escolher seu caminho e transformar a produção de vídeos em um processo com validação, histórico e critérios objetivos de aceite.

Não recomendo começar aumentando efeitos ou quantidade de cenas. Recomendo começar pela precisão: o que a empresa realmente faz, para quem, quais documentos entrega e quais imagens comprovam isso.

## Escopo e limites

Inspecionei as 13 páginas públicas encontradas na navegação: início, serviços, método, obra parada, sobre, contato, FAQ e as seis frentes de serviço. Testei expansão de serviço, expansão de FAQ e seleção de etapa do vídeo. Capturei 20 evidências em desktop e em viewport de 390 × 844. Os controles de etapa funcionaram após a transição; a ausência de alteração imediata não foi classificada como botão quebrado. O vídeo da home tem 16 segundos e é controlado pela experiência da página; é um ativo diferente do institucional local planejado.

Li os roteiros, prompts e scripts locais e medi os três clipes e oito WAV disponíveis com ffprobe. Não gerei mídia, não consumi créditos e não alterei o site ou os scripts. As cenas 4–6 em vídeo não estavam disponíveis nesta pasta durante a inspeção. Não avaliei um filme institucional final completo, nem ouvi toda a locução; as conclusões de sincronização abaixo são calculadas sobre os arquivos e a montagem.

Sem código do site, acesso ao servidor, Analytics, Search Console ou painel comercial, não é possível concluir sobre segurança, entregabilidade dos e-mails, conversão real, indexação, disponibilidade histórica ou Core Web Vitals. Não submeti contatos nem enviei mensagens. Verifiquei os destinos publicados, não o atendimento do número. O teste móvel foi uma emulação de viewport, não um aparelho físico. Não fiz certificação de acessibilidade ou parecer jurídico sobre atribuições e normas.

## Percurso e saúde de cada etapa

| Etapa | Superfície | Saúde observada | Evidência |
|---|---|---|---|
| 1 | Início desktop | Boa hierarquia; proposta ampla e abertura visual pouco explicativa | 01-inicio.jpg |
| 2 | Etapas de pavimentação | Funcionam; falta distinguir demonstração visual de obra real | 02-etapas.jpg |
| 3 | Serviço expandido na home | Funciona; catálogo extenso aumenta esforço de leitura | 03-servicos-home.jpg |
| 4 | Índice de serviços | Organizado; destaque em quantidade em vez de resultado | 04-servicos.jpg |
| 5 | Método | Boa explicação de entradas e saídas; cobertura parcial das frentes | 05-metodo.jpg |
| 6 | Obra parada | Melhor recorte de problema; afirmações precisam de condicionantes | 06-obra-parada.jpg |
| 7 | Sobre | Identifica sócios; falta prova verificável da experiência | 07-sobre.jpg |
| 8 | Contato | Direto e segmentado em três demandas; qualificação ainda manual | 08-contato.jpg |
| 9 | FAQ | Expansão funciona; textos longos e navegação por assunto limitada | 09-faq.jpg |
| 10 | Projeto | Catálogo legível; faltam exemplos e escopo de entrega | 10-projeto.jpg |
| 11 | Orçamento | Lista documentos; explicação de data-base precisa de precisão | 11-orcamento.jpg |
| 12 | Licitação e contrato | Boa ressalva sobre contestação; falta exemplo de pacote | 12-licitacao.jpg |
| 13 | Obra | Legível; erro confirmado de singular/plural | 13-obra.jpg |
| 14 | Convênio e recurso | Boa organização; generalizações sobre reprovação | 14-convenio.jpg |
| 15 | Regularização e planos | Catálogo organizado; atribuições e afirmações amplas pedem revisão | 15-regularizacao.jpg |
| 16 | Início móvel | Sem transbordamento horizontal na home; grande espaço sem conteúdo | 16-inicio-mobile.jpg |
| 17 | Etapas móveis | Rótulos visuais viram apenas números e cabeçalho ocupa muito espaço | 17-etapas-mobile.jpg |
| 18 | Seleção móvel de etapa | Resposta visual não foi imediata; estado durante transição registrado | 18-etapa-obra-mobile.jpg |
| 19 | Contato móvel | CTA legível e cartões empilhados | 19-contato-mobile.jpg |
| 20 | Confirmação da etapa final | Seleção concluída; texto e imagem chegaram à etapa 05 | 20-controle-obra.jpg |

## O que manter

- Paleta areia/cobre, tipografia e layout seguem um padrão reconhecível.
- A mensagem central conecta planejamento, orçamento e acompanhamento.
- A página Método explica o material de entrada e a entrega, incluindo arquivos editáveis.
- Há separação explícita entre assinatura direta, coordenação e conferência.
- Obra parada tem problema, procedimento, entregáveis e chamada de contato específicos.
- Navegação principal e páginas de serviço abriram na inspeção, sem página de erro observada.
- Há link para pular ao conteúdo, títulos estruturados e descrição de imagens no conteúdo inspecionado.
- A home apresenta description, canonical e metadados de compartilhamento. Não seria correto dizer que o SEO básico está ausente.
- O contato já usa mensagens diferentes para orçamento, projeto e obra parada.

## Achados do site

P1 = corrigir primeiro; P2 = próximo ciclo; P3 = refinamento. “Observado” significa presença/ausência no material inspecionado. “Risco” não é falha comprovada em todos os cenários.

| ID | Prioridade e natureza | Evidência / problema | Melhoria e critério de aceite |
|---|---|---|---|
| S01 | P1 · observado | Não encontrei casos documentados, depoimentos atribuídos ou exemplos de entregas nas 13 páginas. A promessa depende principalmente de texto. | Publicar casos autorizados com problema, escopo real da A.F, peças entregues e resultado verificável; usar exemplos demonstrativos identificados quando não houver autorização. |
| S02 | P1 · observado | Sobre identifica sócios, mas o conteúdo inspecionado não apresenta registro profissional, formação e portfólio associado a cada responsável. | Acrescentar credenciais verificáveis e papéis claros. Isso melhora confiança; não é uma conclusão sobre habilitação real. |
| S03 | P1 · risco de interpretação | O vídeo de pavimentação parece uma visualização digital, mas o bloco não informa claramente se é conceito, simulação, projeto próprio ou obra executada. | Identificar a natureza do material junto à imagem e declarar o papel da empresa. Não usar visualização como prova de execução. |
| S04 | P1 · observado | O título “Execução” na home descreve acompanhamento e medição. Pode sugerir que a A.F executa fisicamente a construção. | Usar “Acompanhamento e medição”, se esse for o escopo real, e manter a mesma denominação nos vídeos e propostas. |
| S05 | P1 · risco editorial | “Orçamento que passa na análise” pode soar como garantia de aprovação, enquanto Licitação reconhece que itens podem ser contestados. | Padronizar uma promessa defensável: orçamento rastreável e preparado para análise, com suporte a diligências conforme contrato. |
| S06 | P1 · observado | Não encontrei prazo de primeira resposta ou horário de atendimento no contato. | Informar uma expectativa que a equipe consiga cumprir e distinguir resposta inicial de envio da proposta. |
| S07 | P2 · observado | Contato encaminha para WhatsApp e e-mail; não há coleta estruturada no site de localidade, estágio da obra, tipo de contratante e urgência. | Criar briefing curto opcional ou checklist na mensagem inicial. Aceite: demanda chega com os dados mínimos sem bloquear quem só tem uma descrição. |
| S08 | P2 · observado | Atendimento público e privado aparece nas respostas, mas a entrada principal não diferencia prefeitura, empresa e proprietário. | Oferecer três caminhos com problemas e exemplos próprios; medir se melhora a qualidade das demandas antes de expandir. |
| S09 | P2 · opinião | 168 especialidades e nove softwares aparecem como prova de capacidade; volume não demonstra experiência nem capacidade de atendimento simultâneo. | Dar prioridade a especialidades centrais, casos e entregáveis; manter catálogo completo como consulta. |
| S10 | P2 · observado | Páginas de serviço são principalmente listas de especialidades. Falta mostrar um pacote concreto de contratação. | Em cada frente: quando contratar, entradas, etapas, documentos, formatos, condicionantes e exemplo. |
| S11 | P2 · observado | Método detalha orçamento, medição e projeto; as outras três frentes não têm percurso equivalente nessa página. | Completar método para licitação/contrato, convênio/recurso e regularização/planos. |
| S12 | P2 · observado | CTA específico de contratação não aparece no topo das seis páginas de serviço; o contato principal vem no rodapé. | Colocar CTA contextual próximo à explicação inicial e após os entregáveis, com mensagem da frente selecionada. |
| S13 | P2 · observado | A abertura móvel preserva uma grande área vazia entre a instrução de rolagem e o vídeo. O cabeçalho fixo ocupa aproximadamente um quinto da tela. | Reduzir altura e espaçamento no celular e compactar navegação; o visitante deve chegar ao conteúdo útil com menos rolagem. |
| S14 | P2 · observado | No celular os botões das etapas exibem só 01–05, embora o nome completo exista para acessibilidade. | Mostrar nome da etapa selecionada e tornar a navegação compreensível sem memorizar números. |
| S15 | P2 · risco de acessibilidade | Botões de etapa têm 32 × 44 px no DOM móvel. São estreitos para toque confortável. Isso sozinho não comprova violação de norma. | Aumentar área de toque, espaçamento e visibilidade de foco; testar com teclado e aparelho real. |
| S16 | P2 · observado | Os botões de etapa não expõem aria-pressed ou aria-selected no DOM consultado. O destaque depende de aparência. | Comunicar etapa atual com estado semântico apropriado, sem usar aria-selected fora de um padrão compatível. |
| S17 | P2 · risco de acessibilidade | A experiência do vídeo depende de movimento/rolagem; não há controles nativos visíveis. Funcionamento com movimento reduzido e leitor de tela não foi validado. | Oferecer versão estática ou acesso equivalente às etapas, respeitar preferência de movimento reduzido e testar teclado/foco. |
| S18 | P2 · opinião visual | Microtextos, navegação e rótulos têm tamanho reduzido e cobre sobre areia pode ser difícil para baixa visão. Contraste não foi medido. | Medir contraste e testar zoom; ampliar informações úteis antes de ampliar títulos decorativos. |
| S19 | P2 · observado | Na página Contato o bloco de e-mails/endereço/Instagram é repetido no rodapé. | Simplificar a duplicação nessa página e usar o espaço para instruções de início e expectativa de resposta. |
| S20 | P2 · observado | FAQ tem 26 perguntas em uma página longa. Não há índice de assuntos na interface inspecionada. | Adicionar âncoras por categoria; busca só se o uso justificar. Abrir resposta por link compartilhável. |
| S21 | P3 · erro confirmado | Página Obra mostra “9 especialidades em 1 grupos”. | Corrigir para “1 grupo” e revisar singular/plural dos contadores. |
| S22 | P1 · consistência editorial | Método solicita “data-base pretendida”, enquanto Orçamento afirma usar a que vale no dia da entrega. | Explicar como a data-base é definida no escopo, em quais situações muda e quando atualização é serviço adicional. Não concluo aqui qual regra deve reger cada contrato. |
| S23 | P1 · revisão técnica pendente | Regularização descreve atribuições de topografia/georreferenciamento/SPT em termos gerais; Obra parada e Convênio também fazem generalizações sobre causas e desfechos. | Submeter essas frases aos responsáveis técnicos, com fonte, contexto e condicionantes. A auditoria não valida nem invalida juridicamente essas afirmações. |
| S24 | P2 · observado | Não encontrei link de privacidade na navegação/rodapé inspecionados. | Publicar informação clara sobre dados enviados por contato e serviços terceiros, alinhada à operação real. Não é diagnóstico de conformidade legal. |
| S25 | P2 · verificação pendente | Cliques não revelam conversão real; não inspecionei Analytics/CRM. | Medir CTA por página, demanda qualificada, proposta e contrato. Não usar clique no WhatsApp como sinônimo de venda. |

## Achados da produção local de vídeos

| ID | Prioridade e natureza | Evidência / problema | Melhoria |
|---|---|---|---|
| V01 | P1 · confirmado por cálculo | montar_af.py resulta em 31,25 s: 31,25 s de cenas já considerando a última lenta, menos 2,5 s de transições, mais 2,5 s de retenção. Briefing anuncia 30 s. | Definir duração final como requisito e calcular cortes/transições a partir dela; confirmar com ffprobe após exportação. |
| V02 | P1 · confirmado sobre ativos atuais | f03 entra em 9,4 s e dura 4,608 s: termina em 14,008 s. f04 entra em 13,9 s. Há sobreposição de aproximadamente 108 ms. | Medir cada voz e montar uma timeline sem colisão involuntária; reservar margem de respiração. Conferir auditivamente, pois duração inclui possíveis pausas. |
| V03 | P1 · observado no código | O script reutiliza cenaN.png/mp4 apenas por existência. Não verifica mudança no prompt, imagem mestre, modelo ou briefing. | Usar identificação do projeto e assinatura dos parâmetros; invalidar somente etapas afetadas. |
| V04 | P1 · observado no código | Task IDs ficam só em memória. Uma interrupção ou timeout não deixa estado persistido para retomar. | Salvar ID e estado antes de esperar; retomar consulta da tarefa existente, evitando nova geração paga. |
| V05 | P1 · risco no código | req repete requisições após falha de conexão, inclusive POST. Se o provedor aceitou a criação antes da desconexão, uma repetição pode criar outra tarefa. | Usar idempotência se a API suportar; caso contrário, tratar criação ambígua e reconciliar o estado antes de repetir. Não validei o suporte atual da API. |
| V06 | P1 · observado no código | referencia_fixas existe em cenas.json, mas magnific.py não lê esse campo. A referência depende de --ref. | Resolver a imagem mestre pela configuração e registrar qual referência foi de fato enviada. |
| V07 | P1 · inconsistência confirmada | Cena 6 pede pull-back e subida, contrariando a regra local de movimento único; também não usa a trava estrutural exigida nas regras. | Escolher um movimento principal e aplicar uma trava específica aos elementos da cena. Não prometer que isso elimina toda deformação. |
| V08 | P1 · promessa incorreta | prompt-sistema.md e o roteiro falam em 100% de consistência/acerto. Referência de estilo não fixa geometria, identidade e continuidade. | Substituir garantia por critérios de avaliação e validação visual quadro a quadro dos pontos críticos. |
| V09 | P1 · observado | A “bíblia” descreve atmosfera, materiais e paleta, mas não fixa mapa da obra, medidas, personagens, roupas ou posição de objetos. | Criar ficha de continuidade espacial e de identidade, com imagens aprovadas e elementos imutáveis por tomada. |
| V10 | P2 · observado | Pedido de planilhas oficiais é representado por tela gerada, enquanto estilo e negativo pedem ausência de texto. Pode resultar em planilha sem conteúdo legível ou pseudotexto. | Compor tabelas e documentos verificáveis na edição, com dados demonstrativos claramente identificados. |
| V11 | P2 · observado | Cena “Medição” mostra avenida pronta. A imagem demonstra resultado visual, mas não evidencia o procedimento de medir. | Mostrar coleta de medida, conferência de quantitativo e boletim, respeitando o escopo real da empresa. |
| V12 | P2 · observado | Cena final local usa texto desenhado em vez do símbolo/logo oficial exibido no site. | Usar arquivos oficiais de marca e padronizar nome, área de proteção, contraste e encerramento em todos os formatos. |
| V13 | P2 · observado | Exportação local é somente 16:9; não há legendas nem especificação de versão vertical. | Definir canal no briefing; entregar 16:9 e 9:16 quando contratados, com enquadramento próprio, legendas revisadas e áreas seguras. |
| V14 | P1 · observado | Falta pré-validação de duração, áudio, referência, resolução e arquivos complementares; montagem checa só presença dos clipes. | Fazer preflight completo antes de renderizar ou gastar créditos; falhar com mensagem que indique o item e a solução. |
| V15 | P2 · observado | Clipes atuais são 1928 × 1072 a 24 fps; montagem escala e recorta para 1920 × 1080. | Verificar enquadramento depois do crop e registrar especificação de entrega. Não é automaticamente um defeito visual. |
| V16 | P2 · observado | Compressão/ganho aparecem na geração da voz e novamente na montagem. Há loudnorm final, mas não relatório de áudio. | Consolidar tratamento e medir loudness/pico da exportação; ouvir em celular, fone e caixa para validar inteligibilidade. |
| V17 | P1 · observado | Não há orçamento máximo, custo registrado por cena, aceite persistido ou limite de tentativas. | Criar limite por projeto e etapa; aprovar imagem antes de animar; registrar motivo de rejeição e custo de retrabalho. |
| V18 | P2 · observado | Voz, prompts, roteiro e tempos vivem em arquivos separados; existem oito WAV, enquanto a montagem usa seis. | Usar um manifesto único com versão ativa das falas, cenas, aprovações e exportações. Arquivo extra não prova erro, mas exige identificação. |
| V19 | P2 · opinião | O institucional tenta percorrer seis assuntos em 30 s; abordagem ampla pode produzir imagens bonitas com pouco diferencial concreto. | Cada filme deve ter um público, um problema, uma evidência e uma ação. Criar filmes específicos para orçamento, retomada e projeto. |
| V20 | P1 · observado | Não encontrei vínculo claro de licença/origem da trilha e aprovação dos ativos dentro da configuração. | Registrar origem, permissão de uso e aprovação junto ao ativo; verificar antes de entrega comercial. Isso não afirma que a trilha atual esteja sem licença. |

## Processo que eu implantaria

1. **Briefing fechado:** público, objetivo, canal, duração, serviço, promessa permitida, CTA, material real disponível, orçamento de geração e prazo.
2. **Fonte factual da marca:** um arquivo com nome oficial, logo, contatos, paleta, tipografia, serviços confirmados e afirmações que exigem revisão técnica.
3. **Roteiro orientado à evidência:** cada frase associada à imagem que a demonstra; marcar imagens reais, visualizações e cenas conceituais.
4. **Storyboard e continuidade:** definir espaço, personagem, figurino, horário, instrumentos e posições; aprovar composição antes de animação.
5. **Imagem mestre aprovada:** usar referência de identidade/geometria quando o recurso escolhido permitir; referência de estilo serve principalmente à aparência.
6. **Geração rastreável:** projeto isolado, ID de tarefa persistido, parâmetros e custo registrados, limite de tentativas e retomada segura.
7. **Montagem pela voz medida:** calcular entradas e cortes depois de conhecer a locução; adicionar legenda, marca oficial, música e CTA com tempo de leitura.
8. **Controle de qualidade:** continuidade, mãos/rostos, linhas de arquitetura, texto, atribuição técnica, inteligibilidade, duração, resolução, pico de áudio e áreas seguras.
9. **Aceite registrado:** roteiro aprovado, imagens aprovadas e versão final identificada; mudanças posteriores geram nova versão.
10. **Entrega e aprendizado:** filme, thumbnail, legenda, especificações, origem dos ativos e histórico; medir o que trouxe demanda qualificada e o que exigiu retrabalho.

Critérios propostos de entrega: duração dentro da tolerância contratada (para este institucional, alvo de 30 s com tolerância de um quadro a 24 fps), zero sobreposição de falas não planejada, zero erro de nome/contato, nenhuma cena rejeitada incluída, nenhuma declaração de execução real sem evidência, legendas revisadas quando previstas e marca legível no celular. A exigência de revisão técnica aplica-se às afirmações do serviço, não à aprovação estética de cada efeito.

## Direção recomendada para os vídeos da A.F

O filme principal deveria explicar como a A.F transforma informação dispersa em decisão e documentação confiável. Exemplos reais de prancha, quantitativo, planilha e boletim comunicam o diferencial com mais precisão que uma sucessão de avenidas perfeitas.

Separaria três linhas: institucional para apresentar equipe e método; vídeos por problema para orçamento/obra parada/projeto; e provas de trabalho com casos e documentos autorizados. Manteria a mesma assinatura visual e voz, variando o conteúdo conforme o público.

Exemplo de argumento para orçamento, sujeito à revisão da responsável técnica: “Você tem o projeto. Agora precisa saber o que contratar. A A.F organiza quantitativos, composições e cronograma, com a referência definida para sua obra. Você recebe a planilha e os arquivos editáveis. Envie o projeto para dimensionarmos o escopo.” Mostrar os documentos citados; não tentar criar números legíveis por geração de imagem.

## Plano por impacto

| Ciclo sugerido | Trabalho | Evidência de conclusão |
|---|---|---|
| Primeiro ciclo | Corrigir duração/sobreposição; retomar tarefas sem duplicação; separar versões; rever promessas; corrigir “1 grupos” | Exportação validada, histórico de tarefa e texto consistente |
| Segundo ciclo | Marca oficial; ficha de continuidade; exemplos de entregas; credenciais; CTA por serviço; compactar mobile | Storyboard aprovado e páginas com demonstração do trabalho |
| Terceiro ciclo | Casos autorizados; vídeos por demanda; briefing estruturado; acompanhamento comercial | Demanda identificada por origem e serviço, sem depender apenas de clique |

Essa ordem é uma recomendação, não uma estimativa de prazo contratual. O código do site e os materiais reais determinarão o esforço.

## Métricas de consistência

- Taxa de aprovação na primeira versão, separando imagem, animação e filme final.
- Custo de geração por segundo final aprovado, incluindo tentativas descartadas.
- Número de defeitos de continuidade e de conteúdo por filme.
- Tempo entre briefing validado e entrega; percentual de entregas no prazo.
- Revisões por falta de briefing versus revisões por erro de produção.
- Taxa de contatos qualificados por página/vídeo e conversão de proposta em contrato.

Não fixaria metas comerciais sem medir uma linha de base. Requisitos técnicos da entrega, como duração, marca e ausência de colisão de voz, podem ser fixados desde já.

## Evidências

As capturas numeradas estão na mesma pasta. Abra EVIDENCIAS.html para ver cada tela na ordem com observações. Os arquivos 10–15 também têm snapshots de texto. O relatório distingue defeitos observados, riscos e opiniões; não apresenta como confirmados os itens que precisam de servidor, dados comerciais, revisão técnica ou teste em dispositivo físico.
