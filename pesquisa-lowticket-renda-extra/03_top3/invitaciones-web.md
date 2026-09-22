# L02 · Invitaciones web: editor de convite web com RSVP (uso próprio + licença para clientes)

Data: 22/09/2026. Consolida pesquisa, build, oferta, criativo e red team (notas de trabalho privadas, fora do repositório), já com as correções do red team.

**Convenções:**
- **[medido]**: Biblioteca de Anúncios da Meta (só ACTIVE, 22/09/2026) ou página com link.
- **[estimativa]**: conta aberta, feita na calculadora do usuário (`_raw/calc_economia.py`).
- **[inferência]**: leitura minha.
- **não verificado**: não confirmado.

Contagem de anúncios e dias no ar são proxies, não faturamento. Do Mimo Gift entram só quatro números: líquido por comprador ~US$ 9,4, adesão do bump principal ~1/3, reembolso < 1% e gasto > R$ 2.600/dia (dado do usuário).

## Resumo em 5 linhas

1. **O produto.** É um editor web sem login. O anfitrião monta um convite com envelope animado, música, contagem regressiva, fotos, botões "Cómo llegar" e confirmação de presença com painel. Criar e ver a prévia é grátis; publicar custa US$ 9,90 em moeda local, em A/B contra US$ 7,90. A licença para fazer convites para clientes vem num bump, o "+5 invitaciones".
2. **A evidência.** Em espanhol, a compra para o próprio evento só se sustenta com ticket alto (Invitio, 599 MXN) ou com venda assistida (Miboda, via chat). Os 6 editores baratos ou grátis em ES estão no ar há 18 dias ou menos. **Nenhum editor de ticket baixo se provou em ES** [medido; proxy].
3. **A economia [estimativa].** A US$ 9,90, o líquido por comprador fica em 8,01 / 8,79 / 9,61 (conservador / base / otimista), contra ~9,4 do Mimo. O CPA máximo para ROI 1,5 com conta de anúncio em BRL fica em 4,77 / 5,23 / 5,72. A US$ 7,90, que é a base conservadora, o cenário base cai para 7,06 de líquido e 4,20 de CPA.
4. **O teto [estimativa, confiança baixa].** Em espanhol, US$ 150–400/dia (base de 250), ou 30–80% do Mimo (> R$ 2.600/dia ≈ US$ 506). O limite é o CPA, não o tamanho do mercado: só compra quem tem evento marcado para as próximas 2–12 semanas, cerca de 1% dos usuários do Facebook no MX em cada momento.
5. **O veredito.** Vale um teste barato com critérios de corte: MVP vendável no D11 e no máximo US$ 2.000 gastos para aprender. O desfecho mais provável é um CPA estável de US$ 6–8, que paga a mídia mas não chega ao ROI 1,5. O L02 complementa o calendário do Mimo, mas não o substitui como motor de escala.


> **Nota de reconciliação com a decisão final** (`00_decisao.md`, `04_validacao.md`), que vale onde este dossiê disser o contrário:
> - no lançamento de outubro, só XV años, cumpleaños infantil e baby shower; boda ganha peso a partir de 28/12;
> - o front fica travado em US$ 9,90, sem A/B de preço até o K2; depois do K2, o teste é para cima (12,90), não para 7,90. Nessa fase, as réguas duplas 9,90/7,90 dos cortes K1–K4 valem só para a coluna de 9,90;
> - a célula de revenda fica fechada até o K2. Na Etapa 1, o ângulo de revenda é medido só como teste de gancho/lead, sem venda.

## O que o comprador recebe e o mecanismo (por que é diferente do que já existe)

**Como funciona:**
1. **Editor web sem login**, feito no Lovable reaproveitando o fluxo editor → página → Hotmart do Mimo. O MVP tem boda, XV años, cumpleaños infantil e baby shower (na decisão final, boda só ganha peso a partir de 28/12), com 3 temas por evento no lançamento e até 6 depois.
2. **Campos:** nomes, data e hora (geram a contagem regressiva), até 2 locais, até 8 fotos, música, itinerário, código de vestimenta, presentes e o WhatsApp do anfitrião.
3. **Prévia completa grátis**, com a marca d'água "VISTA PREVIA", sem link público e com `noindex`.
4. **Checkout Hotmart:** o pagamento publica o convite sem marca d'água. O comprador recebe o link próprio, o QR em PNG e uma imagem de capa para o WhatsApp.
5. **Convidado:** toca para abrir o envelope (o toque libera o áudio no celular), vê a contagem, as fotos e o "Cómo llegar" (Google Maps/Waze) e confirma presença pelo formulário ou pelo WhatsApp.
6. **Anfitrião:** no painel, vê quem confirmou (sim/não, adultos/crianças), exporta CSV, manda lembrete por `wa.me` e edita o convite quando quiser.
7. **Validade:** o link fica no ar até **90 dias depois do evento**. A pesquisa falava em 30 dias; o número que vale é o do build e da oferta.

**A licença, segundo ângulo da ideia.** O bump "+5 invitaciones" (US$ 6,90):
- dá 5 créditos (1 crédito = 1 evento), válidos por 12 meses, sem o rodapé da marca;
- **permite** cobrar dos clientes pelo serviço de montar o convite;
- **proíbe** revender créditos, acesso ou modelos. Não existe "derecho de reventa", para evitar ser tratado como PLR.

As travas contra usar um crédito para vários clientes:
- depois de publicado, o nome e o tipo de evento só mudam 3 vezes;
- a data só se move ±90 dias;
- não existe exportação de template, então não há arquivo para piratear.

**O mecanismo é "créala gratis y mírala completa antes de pagar".** Os concorrentes que duram vendem assim: a Convitia usa "Personalize seu convite antes de pagar" ([link](https://www.facebook.com/ads/library/?id=38777800845168590)), e a Invitio usa "Pruébala Gratis", há 112,5 d ([link](https://www.facebook.com/ads/library/?id=1296962249316221)). A prévia elimina o reembolso por "no me gustó" [inferência]. E o reembolso tira o convite do ar, o que desestimula quem usa e depois pede o dinheiro de volta.

**Onde é diferente e onde não é:**

| Alternativa | O que é | Diferença real para o L02 |
|---|---|---|
| Pack de template (Kit Digital ≈ US$ 3,65; Mega Plantillas) | Arquivo Canva/PPT para editar | Não precisa editar arquivo, e o RSVP tem painel. **O RSVP não é exclusivo:** há kits na Hotmart que anunciam "RSVP online" e plataformas marca branca com RSVP ([Ariapsa](https://ariapsa.com/eventos/), [veamoslasfotos](https://www.veamoslasfotos.com/post/invitaciones-digitales-premium-rsvp-muro-interactivo)) |
| Designer por WhatsApp: MXN 89 ([Ayudita](https://www.facebook.com/ads/library/?id=1802415467419849)), 119 ([Eventika](https://www.facebook.com/ads/library/?id=1073107372315166)), 250 ([Paola CM](https://www.facebook.com/ads/library/?id=1406208784815107)), 349 ([Lirio](https://www.facebook.com/ads/library/?id=1634274361447618)), 399 ([Marqstudio](https://www.facebook.com/ads/library/?id=4601506146759840)) | Convite pronto, feito por outra pessoa | Instantâneo e feito pelo próprio comprador. **Não é o mais barato:** a MXN 169, custa ~2× o serviço mais barato e ~1/2 dos serviços de faixa média |
| [Invitio](https://www.facebook.com/ads/library/?id=1701673927750048): "599 MXN, pago único" (≈ US$ 34,8) | Editor self-service, grátis para criar | Mesmo mecanismo por ~28% do preço. Mas a Invitio também anuncia "invitación + álbum digital + herramientas de organización" ([link](https://www.facebook.com/ads/library/?id=1945161146164057)), enquanto o nosso álbum é upsell da v1.1 |
| Grátis: [InvitaWeb](https://www.facebook.com/ads/library/?id=1392058722514761), [Compartiremos](https://www.facebook.com/ads/library/?id=2468620510329134), Canva | Criar e publicar sem pagar | Cobramos pelo que eles dão de graça. **Nada prova que o nosso diferencial justifique a cobrança** |

**Defensibilidade baixa.** O fosso é preço, criativo e idioma, somados ao checkout da Hotmart com meios de pagamento locais e bumps. A tecnologia não protege.

## Comprador: perfil, dor e objeções (com evidência)

**Perfil principal (uso próprio).** As idades são inferência a partir dos títulos dos anúncios.

| Perfil | Idade provável | Evidência |
|---|---|---|
| Mãe ou pai organizando XV ou festa infantil | 30–50 | "La invitación perfecta para **sus** XV", 97,4 d ([Miboda](https://www.facebook.com/ads/library/?id=2025356271678520)); "Invitación Digital para XV", 116,3 d ([My Invite](https://www.facebook.com/ads/library/?id=1894344334607556)) |
| Noiva | 24–35 | "¿Te casas en noviembre o diciembre?" ([Miboda](https://www.facebook.com/ads/library/?id=1624182579230484)); no BR, "É barato mas tem cara de CARO!" ([Canva Para Noivas](https://www.facebook.com/ads/library/?id=1419000880084087)) |
| Quem organiza baby shower | 22–45 | [Makai](https://www.facebook.com/ads/library/?id=1053673747551264) (idade não medida) |

Países, pela densidade de anúncios de "invitaciones digitales" [medido]: MX 849, AR 298, US 288, CL 275, PE 216, CO 194 ([busca no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=invitaciones%20digitales&search_type=keyword_unordered); para os outros países, troque `country=` por AR, US, CL, PE ou CO).

**Dores:**
- **Não saber quem vem.** É o benefício mais longevo nos anúncios: "Control total de tus invitados", 108,9 d ([Miboda](https://www.facebook.com/ads/library/?id=847134201787134)); "Controla a tus invitados sin estrés", 91,8 d ([Miboda](https://www.facebook.com/ads/library/?id=1182022227473852)); "confirmación de asistencia automática", 116,1 d ([My Invite](https://www.facebook.com/ads/library/?id=1652832892617377)).
- **O designer custa e demora:** MXN 89–399 e depende de conversa por WhatsApp.
- **A imagem do Canva é estática.**
- **Medo de parecer genérico.**

**Desejos:**
- ter tudo num link só ([andoinvitando](https://www.facebook.com/ads/library/?id=4009996945961577));
- o efeito de surpresa;
- resolver rápido.

**Objeções:**

| Objeção (ES) | Evidência | Resposta |
|---|---|---|
| "¿Y si no me gusta?" | Padrão freemium dos concorrentes | A prévia completa grátis |
| "Hay gratis" | InvitaWeb, Compartiremos, Canva | Mostrar o que o grátis não faz: painel de confirmados, sem marca, "Cómo llegar". **Nada prova que isso baste** |
| "Los abuelos no abren links" / "es informal" | [teinvito.digital](https://teinvito.digital/invitaciones-digitales/invitacion-digital-vs-invitacion-impresa/), [bodas.net](https://comunidad.bodas.net/debates/invitacion-en-papel-o-digital--t868022) | Bump "Versión para imprimir + QR" |
| "¿Hotmart es confiable? / cargo HTM* / no me llegó" | Digest de demanda; [descritor Hotmart](https://help.hotmart.com/es/article/209033847/-como-identificar-un-cargo-de-hotmart-que-aparecio-en-mi-extracto-bancario-) | A entrega aparece na página de obrigado e chega por e-mail; o paywall avisa "el cargo aparece como HTM* / HOTMART" |
| "Me cobraron varias veces" | [Trustpilot Hotmart](https://www.trustpilot.com/review/hotmart.com?page=4) | Bumps com nome e preço claros; um único upsell, sem downsell |
| "¿Y si cambia la fecha?" | [inferência] | Edição livre depois de publicar (data ±90 d) |

**Público secundário (licença).** Mulher de 25–50 anos que faz convites para outras pessoas ([Web Online](https://www.facebook.com/ads/library/?id=2313998366006369), [Someri](https://www.facebook.com/ads/library/?id=1950759622550013)). As objeções são "el único que gana es el que vende el curso" e "¿de dónde saco clientes?". Premissa [estimativa], herdada da Fase 3, que usou 5–8% de reembolso para este público: é o que mais reembolsa.

**Espelho BR [medido, page_ids, 22/09/2026]:**
- [Convitia](https://www.facebook.com/ads/library/?id=1042494484973953): 33 ativos, o mais antigo com 76,9 d, 16 deles com 30 d ou mais. As três medições dividiram os anúncios por ângulo de formas diferentes (16/16/1 e 11/13/9), então a divisão não sustenta conclusão. Os 4 anúncios mais novos são todos de uso próprio, com "grátis" e "antes de pagar".
- [Canva Para Noivas](https://www.facebook.com/ads/library/?id=1313617404312022): 34 ativos, 88,9 d, 100% uso próprio, R$ 47 ([link](https://www.facebook.com/ads/library/?id=1639444601193289)).

## Oferta: front por país (moeda local), bumps, upsell, garantia

**Paywall (ES):**
- "Créala gratis y mírala completa antes de pagar."
- "Publicar mi invitación · pago único · sin suscripción."
- "Incluye: link sin marca de agua, código QR, imagen para WhatsApp y lista de confirmaciones."
- "Tu invitación queda activa hasta 90 días después de tu evento."
- "En tu estado de cuenta el cargo aparece como HTM* / HOTMART."

**Front: A/B de US$ 9,90 (controle) contra US$ 7,90.** O preço de 9,90 é **hipótese a testar**, não conclusão:
- A justificativa pública é o mercado: MXN 169 fica entre o designer por WhatsApp (MXN 89–399) e a Invitio (599 MXN), e a taxa fixa deixa 74% do preço com o vendedor a 9,90 (ver Contas). O resto é decisão de preço a validar no teste. **A decisão final (`00_decisao.md`, `04_validacao.md`) trava o front em 9,90, sem A/B, até o K2**; depois dele, o A/B é só para cima (9,90 × 12,90).
- **Não lançar a 5,90**, como o build propôs. A taxa fixa deixa só 64% do preço com o vendedor, e o 5,90 precisaria converter 1,65× mais que o 9,90 para empatar em líquido.

| País | Moeda | A (controle) | ≈ US$ | B (teste) | ≈ US$ | Líquido por comprador no base, A / B [estimativa] |
|---|---|---|---|---|---|---|
| MX | MXN | MXN 169 | 9,81 | MXN 139 | 8,07 | 8,68 / 7,18 |
| CO | COP | COP 29.900 | 9,60 | COP 24.900 | 7,99 | 8,50 / 7,11 |
| CL | CLP | CLP 9.490 | 9,89 | CLP 7.490 | 7,81 | 8,78 / 6,99 |
| PE | PEN | S/ 32,90 | 9,77 | S/ 26,90 | 7,99 | 8,63 / 7,09 |
| AR | USD (recomendado) | US$ 9,90 | 9,90 | US$ 7,90 | 7,90 | 8,79 / 7,06, antes da conversão de ARS |
| EC, DO, GT | USD | US$ 9,90 | 9,90 | US$ 7,90 | 7,90 | 8,79 / 7,06 |
| US (hispanos) | USD | US$ 12,90 | 12,90 | US$ 14,90 | 14,90 | 11,38 / 13,10 |

Câmbio de 22/09/2026: 1 USD = 17,22 MXN · 3.116 COP · 959,5 CLP · 3,366 PEN · 5,14 BRL.

**Notas de implementação (Hotmart):**
- **Preço redondo em moeda local só se a Hotmart permitir ofertas em MXN/COP/CLP/PEN**, no principal e nos bumps (não verificado). Se não permitir:
  - ficar em USD com conversão automática;
  - **não imprimir preço em moeda local** no anúncio nem na landing;
  - no paywall, mostrar "US$ 9,90 · se cobra en tu moneda".

  Confira a primeira venda real de cada país antes de assumir a margem.
- **AR:** a Hotmart cobra 9,5% na conversão de ARS para ofertas em USD ([Hotmart](https://help.hotmart.com/es/article/360015794612/-en-que-moneda-obtendre-mi-comision-); valor lido no resumo da busca). **Não verificado quem paga.** Se for o produtor, o líquido cai ~US$ 1,1 por comprador.
- **US:** oferta separada, com ≤ 6% da verba no começo. O ticket é maior porque o CPM é mais alto [inferência].
- **Como decidir o A/B:** por **líquido por lead**, já contando os bumps (o lead é o e-mail capturado no editor).
  - O 7,90 só vence se converter ≥ 1,25× o 9,90.
  - Para medir uma diferença de 25% são precisas ~250 compras por braço [estimativa]. Não decidir antes de ~150 por braço, salvo diferença grande.
  - Se o 9,90 vencer, testar 12,90 (MXN 219), que ainda empata perdendo até 23% da conversão.

**Order bumps.** Regras: nome e preço claros, sem preço riscado, sem timer, cada bump como produto digital próprio. As adesões são **estimativas não verificadas**.

| # | Bump (ES) | US$ | MX / CO / CL / PE | Entrega | Adesão cons. / base / otim. |
|---|---|---|---|---|---|
| B1 | "Tu invitación para siempre": no se desactiva después del evento | 3,90 | MXN 69 · COP 11.900 · CLP 3.790 · S/ 12,90 | Remove a data de expiração. É o espelho do bump principal do Mimo (~1/3 de adesão lá), mas vale menos aqui: o convite perde a função depois da festa | 15 / 22 / 30% |
| B2 | "Versión para imprimir + QR" | 4,90 | MXN 79 · COP 14.900 · CLP 4.690 · S/ 15,90 | PDF A5/carta com QR que abre o convite. Responde à objeção dos avós | 8 / 12 / 16% |
| B3 | "Kit de fiesta a juego" (só infantil e baby shower) | 4,90 | igual ao B2 | PDF de 4 peças: cartaz, toppers, etiquetas e cartão de agradecimento. É o L67 lite, sem personagens licenciados | 3 / 5 / 8% do total. Os 8–15% entre os eventos infantis são **chute**: o [DecoKit](https://www.facebook.com/ads/library/?id=2197772724365280) (160 ativos) é proxy de outro produto |
| B4 | "+5 invitaciones": para tus próximos eventos o para hacerlas para otras personas | 6,90 | MXN 119 · COP 21.900 · CLP 6.590 · S/ 22,90 | 5 créditos por 12 meses, sem rodapé; licença de uso para clientes | 2 / 4 / 6% |

- **B3:** só entra se a Hotmart permitir bumps diferentes por oferta (não verificado). Se não permitir, vira oferta na página de obrigado. É o primeiro corte do build.
- **Se a Hotmart cobrar taxa fixa por bump** (regime R3 da seção Contas), o B1 a 3,90 fica com só 64% do preço. Nesse caso, suba o B1 para 4,90 ou junte B1 e B2 num "Pack Recuerdo" a 5,90.

**Upsell de um clique, v1.1 (fora do MVP):** "Álbum QR de tu evento", US$ 7,90 (MXN 139).
- **O que é:** os convidados sobem fotos pelo QR, e o anfitrião baixa todas.
- **Demanda [medido]:** [Momento](https://www.facebook.com/ads/library/?id=2079058782961672), 10 ativos, 111,0 d; [Cartita Digital](https://www.facebook.com/ads/library/?id=992715157187735), 27 ativos.
- **Sem downsell encadeado.**
- **Adesão estimada:** 4 / 7 / 10%.
- **Build:** +1–2 dias (estimativa).
- **Com OXXO ou pagamento em dinheiro:** não verificado se o upsell funciona.

**Garantia de 7 dias**, o mínimo da Hotmart; vendas para a Europa têm mínimo de 15 dias (não verificado). Por que 7:
- a prévia grátis já cumpre o papel de uma garantia longa;
- com 7 dias, quase todo pedido de reembolso acontece **antes** do evento, e o reembolso tira o convite do ar;
- o Mimo usa 7 dias e tem reembolso < 1%.

Texto para o FAQ (ES): "Tienes 7 días de garantía. Si pides el reembolso, tu invitación y la lista de confirmaciones se desactivan."

**O que não entra na oferta:**
- timer, "últimas unidades" ou preço "de/por" sem referência real;
- depoimento inventado ou "miles de clientes";
- valor em dinheiro, "gana" ou "ingresos" na parte da licença;
- tema de casal ou presente, que canibaliza o Mimo.

## Build: stack, telas, dias até o MVP

**Stack:**

| Camada | Escolha |
|---|---|
| App | App novo no **Lovable** (stack padrão do Lovable): reaproveita, em nível funcional, o fluxo editor → página → Hotmart. Marca, domínio, pixel, produtos Hotmart e dashboard UTMify separados do Mimo |
| Banco, arquivos e funções | **Banco, arquivos e funções próprios, obrigatório** (não compartilhar com o produto que é fonte de caixa: o experimento tem ~300 visualizações por convite). No D1, conferir que o projeto novo não herda dados de outro produto |
| Fotos | Comprimidas no navegador (~1280 px, ≤ 250 KB), até 8 por convite. Rascunhos não pagos apagados em 30 d |
| Pagamento | Hotmart: principal + bumps, checkout em lightbox, slug no parâmetro de rastreio do checkout |
| Liberação | Webhook da Hotmart próprio, idempotente por transação. "Pago" publica; reembolso ou chargeback tiram do ar; OXXO fica pendente; os bumps são associados à compra principal |
| Atribuição | UTMify (parâmetro de rastreio padrão) + Meta CAPI com dataset novo |
| Música | Embed do YouTube, com lista curada de ~30 músicas por evento e a busca como fallback. Chave Google própria. **Não é "música livre de royalties"**, como a pesquisa dizia. O mini-player fica visível: esconder pode ferir os termos do YouTube (não verificado) |
| Mapa | Cartão com endereço e botões "Cómo llegar" (Google Maps/Waze), sem mapa embutido |
| Vídeo e IA | Nenhum no MVP (custo zero por uso) |

**Telas:**
1. Landing em espanhol: demo do convite abrindo no celular, chips de evento, CTA "Crea tu invitación gratis y mírala antes de pagar" e FAQ de objeções.
2. Landing para negócios, a célula de revenda: **fora do lançamento** (ver a última seção).
3. Onboarding 1: tipo de evento e tema, com prévia ao vivo num mockup de celular.
4. Onboarding 2: nomes, data e hora com fuso, local e e-mail para salvar o rascunho.
5. Editor por passos: capa e fotos → mensagem → música → locais → detalhes → configuração da confirmação.
6. Prévia em rascunho com marca d'água e a barra "Publicar mi invitación", sem timer.
7. Checkout Hotmart em lightbox, com os bumps.
8. Obrigado / publicado: link, "Compartir por WhatsApp", "Copiar link", QR para baixar e o aviso sobre a capa em cache no WhatsApp.
9. Convite público (link próprio do convite): envelope → capa → "Faltan X días" → galeria → locais → detalhes → "¿Nos acompañas?" → rodapé "¿Te gustó? Crea la tuya".
10. Painel "Mis invitaciones": convites, créditos restantes, editar e criar outro com um crédito.
11. Confirmações: totais, lista, CSV e "Recordar por WhatsApp".
12. Entrega dos bumps: selo "Para siempre", download dos PDFs, saldo de créditos e termos.
13. Convite expirado, com CTA para o "Para siempre" e o rodapé viral.
14. Recuperar acesso, Termos, Privacidade e Licença.
15. Admin: acompanhamento de vendas, do teste de preço e de pendências de liberação, e "tirar do ar" em caso de denúncia.

**Cronograma (uma pessoa, D1 = 23/09/2026):**

| Dia | Entrega |
|---|---|
| D1 | Projeto novo, Knowledge com restrições, limpeza do que não vai. **Criar os produtos e bumps na Hotmart**, que entram em análise: é o caminho crítico |
| D2 | Schema: tabelas de confirmações e de créditos e campos de evento, com RLS. 4 eventos × 3 temas; domínio, pixel, UTMify, chave do YouTube |
| D3–D4 | Onboarding, editor, contagem com fuso, datas em ES. Pronto quando um convite completo sai em < 5 min no celular |
| D5 | Convite público com OG tags (prévia com foto no WhatsApp) |
| D6 | Confirmação com rate limit e campo-isca contra robôs; tela de confirmados; CSV |
| D7 | Checkout, webhook, bumps, reembolso → offline, OXXO pendente, A/B de preço |
| D8 | Painel, créditos, travas de edição, página de licença |
| D9 | PDFs: imprimível com QR e kit infantil |
| D10 | Landing, FAQ, termos, e-mails, limpeza de rascunhos |
| **D11** | **QA de ponta a ponta:** compra real em 2 países e OXXO; reembolso real; navegador interno do WhatsApp e do Instagram no iOS e no Android. **MVP vendável (~03/10)** |
| D12–D14 | Convites-demo "Ejemplo", gravação de tela e criativos; soft launch no D13; folga |

A pesquisa estimou 6–9 dias; o plano detalhado do build pede 11 até o MVP vendável e 14 com lançamento. Se o MVP não ficar vendável até 20/10, não lançar no Q4 (gate K0).

**Ordem de corte se atrasar:**
1. kit imprimível;
2. licença, painel com vários convites e travas;
3. seções extras viram um campo "Detalles";
4. só a lista curada de música;
5. 2 eventos em vez de 4;
6. preço único.

**Nunca cortar:**
- webhook idempotente;
- botão de checkout bloqueado se a oferta não estiver configurada;
- reembolso → offline;
- rate limit na confirmação;
- teste no navegador interno do WhatsApp;
- limpeza de rascunhos;
- página de licença.

**Custo marginal por venda [estimativa]:** ~US$ 0,01–0,04, com pior caso de ~0,20 (300 visualizações × ~1 MB, a US$ 0,03–0,09 por GB). Isso só vale com fotos comprimidas e rascunhos apagados. O Lovable Cloud não publica preço por GB. Para calibrar, divida a fatura do Cloud pelas vendas do mês, depois do primeiro mês no ar.

**Riscos técnicos que barram o lançamento:**
- a música não tocar no iPhone dentro do WhatsApp ou do Instagram (autoplay bloqueado);
- músicas com embed desativado;
- demora na aprovação da Hotmart (sem bump até aprovar);
- associar os bumps que chegam sem o parâmetro de rastreio do checkout;
- regressão no webhook causada pelo agente do Lovable.

## Criativo: 15 ganchos em espanhol, 5 formatos, 30 variações/semana

**Princípio:** o anúncio vende o convite funcionando no celular: o envelope abre, a música toca, a contagem corre, o convidado confirma e a lista enche.
- 3 dos 5 formatos são só demonstração, sem rosto.
- 2 usam uma **apresentadora virtual com o rótulo "Presentadora virtual · IA"**, que demonstra a tela e nunca finge ser cliente.
- **Nenhum criativo mostra preço** até o A/B fechar.

**Ângulos com 30 d ou mais no ar em ES [medido; proxy]:**
- evento específico XV: 10 anúncios;
- controle de convidados / RSVP: 7;
- demo "cómo funciona": 4. A Mega Plantillas conta como sinal fraco: só 1 dos 10 anúncios passa de 30 d;
- "Pruébala gratis": 1;
- "Pago único": 1.

Nenhum título de uso próprio longevo em ES fala em renda. "Mais que um convite" e infantil animado têm 1 anúncio cada.

**15 ganchos (0–3 s).** Regras:
- texto de tela com até 8 palavras;
- todo convite é demo com o selo "Ejemplo";
- a mão toca **dentro** do vídeo; nunca "toca aquí";
- nenhum valor em dinheiro.

| # | Ângulo | Texto de tela | Voz (0–3 s) | Evidência / regra |
|---|---|---|---|---|
| H01 | Demo | Mira qué pasa al abrir el sobre | "Mira lo que ven tus invitados al abrirla." | "Descubre cómo funciona", 85,7 d ([Miboda](https://www.facebook.com/ads/library/?id=2231113667734525)); "Mira como funciona", 49,5 d ([Mega Plantillas](https://www.facebook.com/ads/library/?id=1708910720392963); sinal fraco) |
| H02 | Curiosidade | Esto no es un video. Es la invitación. | "Esto no es un video: es la invitación." | Sem prova; teste [inferência] |
| H03 | Data (boda) | ¿Boda en {mes1} o {mes2}? | "¿Boda en {mes1}? Tu invitación, lista hoy." | "¿Te casas en noviembre o diciembre?" ([Miboda](https://www.facebook.com/ads/library/?id=1624182579230484)). `{mes1}` = hoje + 56 d; `{mes2}` = hoje + 84 d (envio 8–12 semanas antes, [Celebra con Nosotros](https://www.celebraconnosotros.com/blog/cuando-enviar-las-invitaciones)) |
| H04 | Evento (XV) | La invitación de sus XV, lista hoy | "Para sus XV: fotos, música y cuenta regresiva." | 97,4 d ([Miboda](https://www.facebook.com/ads/library/?id=2025356271678520)); 116,3 d ([My Invite](https://www.facebook.com/ads/library/?id=1894344334607556)). Sempre "sus", nunca "tus XV" |
| H05 | Infantil | Su nombre, su foto, su cuenta regresiva | "Su nombre, su foto y los días que faltan." | "Sorprende a todos con una invitación digital animada", 49,6 d ([Mayra Romero](https://www.facebook.com/ads/library/?id=4558598844386502)). Sem rosto de criança |
| H06 | Baby shower | ¿Organizas un baby shower? | "¿Organizas un baby shower? Mira esta invitación." | [Makai](https://www.facebook.com/ads/library/?id=1053673747551264). Nunca "¿Estás embarazada?" |
| H07 | Prazo | Faltan {n} días. ¿Y la invitación? | "Faltan {n} días… ¿y la invitación?" | XV: envio 4–6 semanas antes [inferência]. A contagem é do evento, nunca de oferta, e nunca aparece perto de preço |
| H08 | Dor (RSVP) | Deja de preguntar quién va a venir | "Deja de preguntar uno por uno quién viene." | "Controla a tus invitados sin estrés", 91,8 d ([Miboda](https://www.facebook.com/ads/library/?id=1182022227473852)); "Control total de tus invitados", 108,9 d ([Miboda](https://www.facebook.com/ads/library/?id=847134201787134)) |
| H09 | Demo (painel) | Así se llena la lista de confirmados | "Así se llena la lista de confirmados." | 116,1 d ([My Invite](https://www.facebook.com/ads/library/?id=1652832892617377)); "herramientas de organización", 40,9 d ([Invitio](https://www.facebook.com/ads/library/?id=2641207056335277)) |
| H10 | Objeção de risco | Créala gratis. Paga solo para publicarla. | "Créala gratis. Pagas solo si la publicas." | "Pruébala Gratis", 112,5 d ([Invitio](https://www.facebook.com/ads/library/?id=1296962249316221)). Variante H10b: "Pago único. Sin suscripción." ([Invitio](https://www.facebook.com/ads/library/?id=1701673927750048), 101,8 d) |
| H11 | Objeção (papel) | ¿Y quien no abre links? | "¿Y quien no abre links? También va impresa." | [teinvito.digital](https://teinvito.digital/invitaciones-digitales/invitacion-digital-vs-invitacion-impresa/). **Só com o bump de impressão no ar**, com o texto pequeno "opcional" |
| H12 | Objeção (design) | Sin diseñador y sin saber diseñar | "Sin diseñador y sin saber diseñar." | "Fácil de editar pelo celular", 66,9 d ([Canva Para Noivas](https://www.facebook.com/ads/library/?id=1891500572231481)) |
| H13 | Contraste | Una imagen no confirma asistencia. Esta sí. | "Una imagen no confirma asistencia. Esta sí." | "Mucho más que una invitación digital.", 48,3 d ([Miboda](https://www.facebook.com/ads/library/?id=1741895243716839)) |
| H14 | Licença | ¿Haces invitaciones para otras personas? | "¿Haces invitaciones para otras personas? Mira esto." | [Event Builder](https://www.facebook.com/ads/library/?id=1056284580730092), 2,2 d. **Sem longevidade:** só na célula de revenda |
| H15 | Licença (fluxo) | Te la piden por mensaje. Así la entregas. | "Te la piden por mensaje. Así la entregas." | **Sem evidência de longevidade.** Mostra o fluxo de entrega, nunca o valor cobrado. Só na célula de revenda |

**Variantes por país [inferência]:**

| Locale | Tratamento | Boda | XV | Exemplo |
|---|---|---|---|---|
| MX, CO, PE, EC, GT, DO, US | tú | boda | XV años (CO/PE: "quince") | "Créala gratis. Pagas solo si la publicas." |
| AR, UY | vos | casamiento | sus 15 | "Creala gratis. Pagás solo si la publicás." O voseo já aparece em anúncio: "Diseñá tu invitación gratis" ([InvitaWeb](https://www.facebook.com/ads/library/?id=1392058722514761)) |
| CL | tú | matrimonio | sus 15 | "¿Matrimonio en {mes1} o {mes2}?" |

**5 formatos.** Todos em 9:16 (1080×1920, 30 fps), com versão 4:5 dentro do mesmo anúncio. O áudio da gravação de tela vai sempre mudo, trocado por trilha licenciada.

| # | Nome | Duração | Rosto | Estrutura | End card / CTA |
|---|---|---|---|---|---|
| F1 | "El sobre" | 13–15 s (corte de 10 s) | Não | Gancho → envelope abre e a música entra → contagem, fotos e local → "Confirmar asistencia" → a linha "Familia Pérez · 4" entra no painel | "Créala gratis y mírala antes de pagar" · "Más información" |
| F2 | "Hecha en el celular" | 18–22 s | Não | Gancho → os 4 passos do editor, acelerados 2× com selo → prévia com marca d'água → "Publicar" → link e QR → 1 confirmação chegando | "Arma la tuya gratis". **Sem promessa de tempo** até medir o tempo mediano no QA |
| F3 | "Imagen vs. invitación viva" | 12–15 s | Não | Tela dividida: imagem estática (arte nossa) × link vivo; os itens 🎵 ⏳ 📍 📋 aparecem com ícone e sem caixa de seleção | "Todo en un solo link". Nunca citar Canva |
| F4 | "Presentadora virtual" | 20–25 s | IA rotulada | Close com o gancho → a apresentadora vira um círculo no canto superior enquanto a tela roda → close final "La haces gratis y la ves completa" | Fala "te muestro", "con [Marca]". Nunca "yo la usé" nem "mi hija" |
| F5 | "Tres dudas" | 25–30 s | IA rotulada | 3 de 6 perguntas: ¿y si no me gusta? / ¿y si cambia la fecha? / ¿descargan algo? / ¿cómo me llega? / ¿quién no abre links? / ¿cómo sé quién viene? | "Pago único, sin suscripción". Serve para público frio e remarketing |

Os formatos com IA ficam em no máximo 1/3 do volume (teto de 10 por semana). Três motivos:
- a Meta põe o rótulo "AI info" ([Meta](https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/));
- um estudo mediu queda de 31,5% no CTR com aviso de IA ([NYU](https://www.stern.nyu.edu/experience-stern/faculty-research/ai-advertising-paradox)); outro não achou efeito ([MediaScience](https://www.marketingdive.com/news/ai-disclosure-labels-dont-hurt-ad-performance-heres-what-the-numbers-say/822711/));
- a demonstração pura é o que roda há mais tempo em ES.

**30 variações por semana.** Os módulos:
- 15 ganchos, mais ~3 novos por semana;
- 5 corpos;
- 4 eventos;
- 3–6 temas;
- locales MX, AR, CL, CO/PE e US;
- com ou sem apresentadora.

São ~198 combinações de gancho × corpo × evento antes de tema e país; cada semana testa ~15%. Em relação ao Mimo, **há mais combinações de gancho, mas cada uma alcança um público menor** (cada evento só compra perto da data).

| Semana 1 (S41, 05–11/10), bloco | Nº | Exemplos |
|---|---|---|
| Exploração de gancho no corpo mais barato (F1) | 12 | H01 (2×), H02–H10 e H13 no F1, distribuídos entre XV, boda, infantil e baby shower |
| Corpo editor (F2) | 4 | H12, H10, H05, H08 |
| Contraste (F3) | 2 | H13, H02 |
| Apresentadora (F4) | 4 | H04, H03, H08, H06 |
| Dúvidas (F5) | 2 | H10, H11 (se o bump de impressão não estiver no ar, trocar por H12) |
| Localização | 3 | H01 AR (casamiento, voseo), H04 CO (quince), H03 CL (matrimonio) |
| Revenda (H14, H15) | 3 | **Condicional:** com a célula de revenda fechada, que é a recomendação, as 3 vagas vão para exploração B2C no F2 |

- **Da semana 2 em diante:** 6 de iteração de gancho (o melhor anúncio com 6 ganchos novos) · 6 de iteração de corpo (os 2 melhores ganchos × 3 corpos novos) · 6 de exploração · 4 de troca de tema contra fadiga · 4 de localização · 4 de revenda (ou B2C, se a célula estiver fechada).
- **Pipeline:**
  - gravar a tela do produto num celular real, com dados fictícios, 5 clipes por evento × tema;
  - voz por TTS (es-MX e es-AR) e legenda queimada;
  - apresentadora gerada uma vez, checada por busca reversa, sem remover os metadados C2PA;
  - trilha da Meta Sound Collection (termos oficiais não lidos, não verificado), com o ID de cada faixa no CSV;
  - render no Remotion a partir de `matrix/W{AAWW}.csv` (arquivo a criar), com ffmpeg para concatenar, fazer ducking e loudness. Os comandos estão nas notas de trabalho privadas, fora do repositório.
- **QA de 10 perguntas antes de subir.** Qualquer "sim" barra o anúncio:
  1. Algum valor de ganho?
  2. Escassez falsa?
  3. IA sem rótulo ou falando como cliente?
  4. Personagem ou marca de terceiro?
  5. Música sem licença?
  6. Convite sem o selo "Ejemplo" ou com rosto real de criança?
  7. Interface falsa?
  8. Frase sobre atributo pessoal?
  9. Promessa que o produto não cumpre?
  10. Tema de casal?
- **Nomenclatura para ler no UTMify:**
  - campanha `INV_{CELULA}_{OBJ}_{AAWW}`;
  - conjunto `INV_{CELULA}_{PAISES}_{PUBLICO}`;
  - anúncio `INV_{H}_{C}_{EVT}_{TEMA}_{LOC}_{PRES}_W{AAWW}_v{n}`, ex.: `INV_H08_C1_XV_T3_MX_NA_W2641_v1`;
  - parâmetros de URL padrão do UTMify;
  - não renomear anúncio no ar;
  - a variante de preço vai no parâmetro de rastreio do checkout, não no nome.
- **Regras de decisão (corrigidas para a conta BRL):**
  - Pausar o anúncio com gasto ≥ 2× o CPA-alvo sem venda: **US$ 10,46** a 9,90 (2 × 5,23) ou **8,40** a 7,90 (2 × 4,20). O criativo usava 10,54 / 8,52, calculados sobre um líquido que não bate com a tabela da oferta.
  - Teto de perda da rodada de 30 anúncios: ~US$ 314 / 252.
  - Pausar também depois de ~1.000 impressões se o hook rate estiver no terço inferior da semana.
  - Vencedor provisório: 3 ou mais vendas com CPA ≤ CPA-alvo. É sinal de direção, não prova.

**Calendário [estimativa]:**

| Período | O que fazer |
|---|---|
| S41–S47 (05/10–22/11) | O H03 se ajusta sozinho ("noviembre o diciembre" → "enero o febrero"). O peso fica em **XV (envio 4–6 semanas antes [inferência]) e infantil, que são perenes**. Os convites das bodas de novembro já saíram em ago–set [inferência] |
| S48 (Black Friday, 27/11) | Não escalar nem subir teste: CPM 2–3× maior (dados dos EUA; LATAM não verificado; [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [Clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics)) |
| S49–S52 | Rotina. Sem ângulo de posada (domina o grátis [inferência]). Deixar os renders prontos antes de 24/12 |
| 28/12–28/02/2027 | Escalar: CPM mais barato (40–60% menor até ~15/01, dados dos EUA; LATAM não verificado; [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [Clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics)) e compra de convites para bodas de fev–mai (MX) e mar–abr (AR). **Nunca usar "cuesta de enero"** |

## Ângulos proibidos

Valem para o vídeo, o texto, o título, a landing e a página da Hotmart. A Meta revisa o destino ([burla de sistemas](https://transparency.meta.com/km-kh/policies/ad-standards/deceptive-content/circumventing-systems)).

| Não pode | Exemplo proibido (ES) | Motivo | Reescrita segura (ES) |
|---|---|---|---|
| Promessa de renda ou valor por convite | "Gana $500 por invitación"; no BR, "Fature até R$250", 76,8 d ([Convitia](https://www.facebook.com/ads/library/?id=2146534716078562)) | [Resultados irreais (Meta)](https://transparency.meta.com/en-gb/policies/ad-standards/deceptive-content/unrealistic-outcomes/); [uso responsável (Hotmart)](https://hotmart.com/en/legal/responsible-use-policy). Ficar no ar não prova que é permitido | "Entrega invitaciones web con confirmación, desde el celular." |
| "Emprende desde casa", "ingresos", "negocio", "listas para vender" | "💸 Emprende desde casa…" ([link](https://www.facebook.com/ads/library/?id=1591072372564444)); "+1200 INVITACIONES listas para VENDER" ([Web Online](https://www.facebook.com/ads/library/?id=2313998366006369)) | [Fraude e golpes (Meta)](https://transparency.meta.com/policies/ad-standards/fraud-scams/fraud-scams-deceptive-practices/); eliminatória E2 do projeto | "¿Haces invitaciones para otras personas? Mira este editor." |
| Print de ganho, notificação de venda | "¡Otra venta! 🔔" | [Funcionalidade inexistente (Meta)](https://www.facebook.com/business/help/655450495896770) | Painel do produto com "Datos de ejemplo": convidados, não dinheiro |
| Depoimento inventado | "María compró y le encantó ⭐⭐⭐⭐⭐" | [Regra da FTC (2024)](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials); art. 32 da [LFPC](https://www.profeco.gob.mx/juridico/pdf/l_lfpc_ultimo_camdip.pdf) | "Tus invitados confirman y te dejan un mensaje" (mensagem neutra, "Confirmo 3") |
| Avatar de IA como cliente | "Yo la usé para los XV de mi hija" | Enganoso (digest de políticas; FTC) | "Te muestro cómo se ve una invitación de XV hecha con [Marca]", com rótulo de IA |
| Rosto parecido com famoso; cenário de telejornal | Avatar "inspirado" numa atriz | [Isca de celebridade (Meta 2024)](https://about.fb.com/news/2024/10/testing-combat-scams-restore-compromised-accounts/), [Meta 2026](https://about.fb.com/news/2026/02/meta-takes-legal-action-against-scam-advertisers/) | Rosto sintético genérico, checado por busca reversa |
| Prova social sem base | "Miles de familias ya la usan" (a Invitio usa, [link](https://www.facebook.com/ads/library/?id=3091096807946970); não verificado) | Precisa ser comprovável (art. 32 da LFPC) | "Con confirmación de asistencia y lista de invitados." |
| Escassez ou urgência falsa | "Solo hoy", cronômetro, "ANTES $249 HOY $99" sem preço anterior real | [Profeco multa ofertas falsas](https://www.infobae.com/mexico/2026/05/28/las-ofertas-falsas-saldran-caras-profeco-aplicara-multas-a-negocios-infractores-hasta-por-6-millones-de-pesos/) | "Créala hoy y mírala antes de pagar." A contagem do evento pode aparecer, longe do preço |
| Personagem licenciado (Disney, Bluey, Stitch, Winnie Pooh, anime) | "Invitación… de Winnie Pooh" ([link](https://www.facebook.com/ads/library/?id=1425801376141613)) | [Copyright e marcas (Meta)](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/copyright-and-trademarks/) | Temas originais: Safari, Espacio, Dinosaurios, Osito y nubes, Floral |
| Música comercial ou áudio vazando da gravação | Hit do momento; o embed do YouTube tocando dentro da gravação | Anúncio com música exige licença (mesma política) | Faixa licenciada, com o ID registrado |
| "Sin esfuerzo", "en 1 minuto" sem medição | "Se hace sola" | Enriquecimento rápido; tempo não "comprobable" | "Desde tu celular, paso a paso." |
| Marcas de terceiros | "Mejor que Canva"; logos de Maps, Waze ou WhatsApp alterados | [PI de terceiros (Meta)](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/third-party-infringement/); [marca WhatsApp](https://www.meta.com/brand/resources/whatsapp/whatsapp-brand/) | "Sin programas de diseño"; ícone genérico de pino de mapa |
| Atributo pessoal | "¿No te alcanza?", "¿Estás embarazada?", "cuesta de enero" | [Atributos pessoais (Meta)](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/) | "¿Organizas un baby shower?" |
| Interface falsa | "Toca aquí 👆", play desenhado, caixa de seleção | [Funcionalidade inexistente](https://www.facebook.com/business/help/655450495896770) | A mão toca dentro do vídeo; itens com ícone |
| Falar com menor ou mostrar menor real | "¿Cumples 15? Pide tu invitación" | Prudência (regra exata da Meta não verificada) | "La invitación de **sus** XV"; público 18+ |
| Revenda como PLR / "derechos de reventa" | "Revende este pack y quédate con el 100%" | [Hotmart barra PLR](https://help.hotmart.com/es/article/31594947721485/-por-que-mi-producto-no-esta-disponible-para-la-venta-); eliminatória E4 | "Paquete para varios eventos. No incluye reventa del editor." |
| Esconder que é IA | Remover C2PA, recortar o rótulo | [Transparência de IA (Meta)](https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/) | Rótulo na tela + marcação no Gerenciador |
| Tema de casal ou presente (regra do projeto) | "Sorprende a tu pareja" | Canibaliza o Mimo | Só celebrações com convidados |

## Contas (definição de ROI explícita; AOV, líquido, reembolso, CPA de break-even, CPA para ROI 1,5)

**Definição de ROI:** faturamento líquido (depois das taxas da Hotmart e dos reembolsos) ÷ gasto em anúncios.
- CPA de break-even = líquido por comprador (ROI 1,0).
- CPA para ROI 1,5 = líquido ÷ 1,5.
- **Com conta de anúncio em BRL** (o UTMify soma 12% de imposto ao gasto; é a régua provável): break-even = líquido ÷ 1,12 e ROI 1,5 = líquido ÷ 1,68.

**Taxas (modelo do usuário):**
- **Front:** 10,95% + US$ 1,49, o que deixa ~74% a US$ 9,90.
- **Bumps:** 88% líquido.
- **Reembolso:** aplicado sobre o líquido total.
- **Upsell:** calculado com a taxa do front; a 7,90 deixa US$ 5,55.

**Reembolso estimado para o nicho:**
- **Por que acima do Mimo (< 1%):** compra planejada, evento que pode ser cancelado, comparação posterior com o grátis e vários bumps.
- **Por que abaixo da renda extra:** a prévia grátis e o fato de o reembolso desativar o convite.

| Cenário | Uso próprio (~80%) | Licença (~20%) | Usado |
|---|---|---|---|
| Conservador | 4% | 10% | **5%** |
| Base | 2% | 7% | **3%** |
| Otimista | 1% | 4% | **1,5%** |
| Cético (red team) | — | — | 5%, com adesão aos bumps de 8 / 6 / 2 / 1% |

**Front US$ 9,90 (regime de taxas R1).** Adesões e reembolso são estimativas, não verificadas.

| US$ por comprador de front | Conservador | **Base** | Otimista | Cético | Sem bumps |
|---|---|---|---|---|---|
| Adesão B1 / B2 / B3 / B4 | 15 / 8 / 3 / 2% | 22 / 12 / 5 / 4% | 30 / 16 / 8 / 6% | 8 / 6 / 2 / 1% | — |
| Reembolso | 5% | 3% | 1,5% | 5% | 5% |
| **AOV bruto** | 11,16 | **11,87** | 12,66 | 10,67 | 9,90 |
| Líquido do front | 7,33 | 7,33 | 7,33 | 7,33 | 7,33 |
| Líquido dos bumps | 1,11 | 1,73 | 2,42 | 0,68 | 0 |
| **Líquido por comprador** | **8,01** | **8,79** | **9,61** | **7,61** | **6,96** |
| CPA de break-even, sem imposto / BRL | 8,01 / 7,15 | **8,79 / 7,85** | 9,61 / 8,58 | 7,61 / 6,79 | 6,96 / 6,21 |
| CPA para ROI 1,5, sem imposto | 5,34 | **5,86** | 6,41 | 5,07 | 4,64 |
| **CPA para ROI 1,5, BRL** | **4,77** | **5,23** | **5,72** | **4,53** | **4,14** |
| *Com upsell (v1.1): líquido* | *8,22* | *9,17* | *10,16* | — | — |

Conta do cenário base:
- Bumps: 3,90 × 0,22 + 4,90 × 0,12 + 4,90 × 0,05 + 6,90 × 0,04 = 1,967. AOV: 9,90 + 1,967 = 11,87.
- Líquido: 9,90 × 0,8905 − 1,49 = 7,33; mais 1,967 × 0,88 = 1,73; soma 9,06.
- Depois do reembolso: 9,06 × 0,97 = **8,79**.

**Front US$ 7,90, a base conservadora (mesmas adesões):**

| | Conservador | **Base** | Otimista | Cético | Sem bumps |
|---|---|---|---|---|---|
| AOV bruto | 9,16 | **9,87** | 10,66 | 8,67 | 7,90 |
| Líquido por comprador | 6,32 | **7,06** | 7,85 | 5,91 | 5,27 |
| CPA de break-even, BRL | 5,64 | **6,30** | 7,01 | 5,28 | 4,71 |
| CPA para ROI 1,5, sem imposto / BRL | 4,21 / 3,76 | **4,71 / 4,20** | 5,23 / 4,67 | 3,94 / 3,52 | 3,51 / 3,14 |

**Sensibilidade ao preço do front (cenário base):**

| Front | Líquido do front (% do preço) | Líquido por comprador | CPA ROI 1,5, BRL | Conversão para empatar com o 9,90 |
|---|---|---|---|---|
| 5,90 | 3,76 (64%) | 5,33 | 3,17 | 1,65× |
| 6,90 | 4,65 (67%) | 6,19 | 3,68 | 1,42× |
| 7,90 | 5,54 (70%) | 7,06 | 4,20 | 1,25× |
| 9,90 | 7,33 (74%) | 8,79 | 5,23 | 1,00× |
| 12,90 | 10,00 (78%) | 11,38 | 6,77 | 0,77× |

**A taxa da Hotmart pode ter mudado em 21/09/2026 (não verificado).** Pelos snippets, a taxa do Player passa a fazer parte da taxa fixa por transação ([Hotmart](https://help.hotmart.com/es/article/208298448/-cuales-son-las-tarifas-cobradas-por-hotmart-), [Tactus](https://tactus.com.br/taxas-da-hotmart-para-produtor/), [EngagED](https://engaged.com.br/blog/taxa-hotmart-quanto-custa-vender/)). Há quatro regimes plausíveis:

| Regime | Front / cada bump | Líquido por comprador (base, 9,90) | CPA ROI 1,5, sem imposto / BRL |
|---|---|---|---|
| R1: modelo do usuário | 10,95% + 1,49 / 88% | 8,79 | 5,86 / 5,23 |
| R2: fim do Player, microtransação a 9,9% + 0,10 | 9,9% + 0,10 / igual | 10,23 | 6,82 / 6,09 |
| R3: taxa fixa de US$ 1,00 em toda transação, inclusive em cada bump | 9,9% + 1,00 / 9,9% + 1,00 | 8,98 | 5,99 / 5,35 |
| R4 (red team): os ~26% vêm de imposto e conversão, **e** a taxa fixa sobe para 1,00 | front cai ~US$ 0,80 | ~8,0 | ~5,3 / ~4,77 |

**Não afirmar que a mudança é neutra ou favorável** antes de abrir o detalhe da primeira venda real (front + bump). Confirmar na primeira venda de teste se cada bump vem como transação separada; se vier, o R3 ou o R4 são plausíveis.

**Comparação com o Mimo:** ~9,4 de líquido; CPA para ROI 1,5 de ~6,27 sem imposto e ~5,60 em BRL. O L02 base, a 9,90, fica em 94% disso (conservador 85%, otimista 102%). **Não há folga para pagar CPA maior que o do Mimo.**

## Teto (gasto diário sustentável, premissas, faixa de confiança, comparação com o Mimo Gift)

**Conta de baixo para cima, só no MX.** As entradas são quase todas chutes sem fonte; só os dois números do INEGI são medidos.

| Evento | Eventos/ano no MX | % que compra convite digital pago (cons. / base / otim.) |
|---|---|---|
| Boda | 486.645 [medido, [INEGI 2024](https://www.inegi.org.mx/app/saladeprensa/noticia/10240)] | 10 / 20 / 30% [chute] |
| Baby shower | 1.672.227 nascimentos [medido, [INEGI](https://www.inegi.org.mx/app/saladeprensa/noticia/10237)] × 35% com chá = 585 mil [chute] | 3 / 5 / 10% |
| XV años | ~1,15 M meninas de 15 anos (não verificado) × 35% = 403 mil | 10 / 15 / 25% |
| Cumpleaños infantil | ~18 M crianças × 25% = 4,5 M | 1 / 2 / 4% |
| **Total** | **~5,97 M/ano ≈ 16.400/dia** | **415 / 759 / 1.329 convites pagos/dia** |

Para passar do MX para toda a LATAM em espanhol + US, multipliquei por ~1,95 [estimativa]. Com uma participação de 3 / 6 / 12% do mercado pago, o gasto sai entre **US$ ~130 e ~1.990/dia**. É uma faixa de 15×: o número serve só para mostrar que **o tamanho do mercado não é o limite**. O limite é o CPA.

**Por que o teto fica bem abaixo da conta:**
1. **O cenário base supõe liderança de mercado.** Hoje os maiores em ES têm 12–27 anúncios ativos (Invitio 12, My Invite 16, Miboda 16, Cartita 27) [proxy].
2. **Público estreito.** 16.400 eventos/dia × ~42 dias de antecedência × ~1,5 organizador por evento dá ~1,0 M de pessoas, ~1,1% dos 93,5 M de usuários do Facebook no MX ([DataReportal](https://datareportal.com/reports/digital-2026-mexico); a fração é [estimativa]). O Mimo fala com qualquer pessoa num relacionamento, em qualquer dia [inferência].
3. **Concorrência com o grátis e com serviços baratos:** 849 anúncios de "invitaciones digitales" só no MX [medido, [busca](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=invitaciones%20digitales&search_type=keyword_unordered)].
4. **Sem vantagem de lance:** o líquido base (8,79) é menor que o do Mimo (~9,4).

**Estimativa final, só espanhol, com a régua BRL (CPA 5,23 a 9,90).** O mercado pago base é de ~1.480 convites/dia (759 × 1,95).

| Faixa | Gasto/dia | Compradores/dia (gasto ÷ 5,23) | Participação implícita | Confiança |
|---|---|---|---|---|
| Piso | **US$ 150** | ~29 | ~2,0% | **Baixa**. Só sobe para média depois de um teste com CPA ≤ 5,23 |
| **Base** | **US$ 250** | ~48 | ~3,2% | **Baixa** |
| Topo | **US$ 400** | ~76 | ~5,2% | **Baixa** |
| Nível do Mimo | ≥ US$ 506 | ≥ 97 | ≥ 6,5% | **Muito baixa** sem PT-BR e sem laço viral comprovado |

- **A 7,90** (CPA-alvo 4,20), os mesmos US$ 250/dia exigem ~60 compradores/dia.
- **Margem sobre a mídia a ROI 1,5:** US$ 0,50 por dólar gasto, sem imposto (ROI 1,5 devolve 1,5 de líquido por dólar, então sobram 0,5; na régua BRL, 1,68 − 1,12 = 0,56 por dólar de anúncio). US$ 250/dia deixam ~US$ 125/dia; o Mimo, a US$ 506/dia, deixaria ~US$ 253/dia [estimativa, antes de impostos e ferramentas].
- **Laço viral** (rodapé "Crea la tuya"): 150 visualizações × 1% de clique × 3–5% de compra dão ~0,05–0,08 venda extra por venda. Isso reduz o CPA efetivo em ~5–7% [estimativa]. Medir com `utm_source=viral`.

**Distribuição da base de US$ 250/dia [estimativa]:**

| País | % da verba | US$/dia | Observação |
|---|---|---|---|
| MX | 45% | 112 | Maior densidade de concorrentes longevos |
| AR | 12% | 30 | Cobrança em USD; conversão ARS de 9,5% (não verificado quem paga); bodas de out–abr |
| CO | 12% | 30 | PSE/Efecty |
| PE | 10% | 25 | PagoEfectivo |
| CL | 10% | 25 | Maior renda; Kit Digital (CLP) longevo |
| EC, GT, DO | 5% | 13 | USD; sem dados de público |
| US (hispanos) | 6% | 15 | Front de 12,90; CPM alto |

**Sazonalidade.** Os fatores são estimativa; as curvas do Google Trends não foram verificadas.
- **~82% dos eventos são perenes:** infantil e XV somam 4,9 de 5,97 M/ano.
- **Casamento é sazonal.** MX: fev–mai e set–nov ([bodas.com.mx](https://www.bodas.com.mx/articulos/meses-favoritos-para-casarse-en-mexico--c9837)). AR: out–abr, pico em novembro ([CEMBA](https://cemba.com.ar/2025/10/13/comenzo-la-temporada-alta-de-casamientos/)).
- **Out até meados de nov (~1,2×):** vale para XV de nov–dez e bodas de fim de dezembro. Os lotes novos de anúncios da Invitio e da My Invite são renovação de criativo, não prova de gasto: a My Invite já publicou em lote há ~116 d.
- **Black Friday:** ~0,6×.
- **Dezembro:** ~0,7×.
- **26/dez a fev:** ~1,3×.
- **Mar–set:** 1,0×.

**Outros idiomas [estimativa]:**
- **PT-BR:** +US$ 50–200/dia (Convitia e Canva Para Noivas provam demanda paga; [Conviteria](https://conviteria.com.br/) é grátis até 30 convidados).
- **EN:** +0–100.
- **FR:** +0–50.

**Total com todos os idiomas: US$ 200–750/dia, confiança baixa.**

**Comparação com o Mimo Gift:**

| | Mimo Gift | L02 (estimativa) |
|---|---|---|
| Gasto/dia | > R$ 2.600 ≈ US$ 506+ (dado do usuário) | ES: US$ 150–400 (base 250); com PT/EN/FR: 200–750 |
| Líquido por comprador | ~US$ 9,4 | 8,01–9,61 a 9,90 (base 8,79); 7,06 a 7,90 |
| CPA para ROI 1,5, sem imposto / BRL | ~6,27 / ~5,60 | 5,86 / 5,23 (base a 9,90) |
| Gatilho | Impulso emocional, qualquer dia | Necessidade com prazo (evento em 2–12 semanas) |
| Público em compra | Amplo [inferência] | ~1% do Facebook MX em cada momento |
| Vantagens próprias | — | Laço viral (100–300 convidados por convite); calendário complementar |

**Veredito: o teto do L02 é menor, cerca de 30–80% do Mimo em espanhol.** O que faria o L02 passar o Mimo, em ordem de probabilidade:
1. CPA ≤ US$ 4,5 no MX escalando;
2. laço viral medido ≥ 0,1 venda extra por venda;
3. PT-BR dentro da régua;
4. adesão ao B1 perto de 1/3.

## Concorrentes diretos (links)

Medição por page_ids na Biblioteca de Anúncios, só ACTIVE, em 22/09/2026. Dias = idade do anúncio ativo mais antigo.

| Página | Tipo | Moeda | Ativos | Dias | Preço | Nota |
|---|---|---|---|---|---|---|
| [Invitio](https://www.facebook.com/ads/library/?id=1296962249316221) | Editor self-service | MXN | 12 | 112,5 | "599 MXN, pago único" ([link](https://www.facebook.com/ads/library/?id=1701673927750048)); grátis para criar | Único editor com 100+ d; vende convite + álbum + organização ([link](https://www.facebook.com/ads/library/?id=1945161146164057)). Preço premium de US$ 29,99–36 ([boda](https://invitio.events/en-US/boda), [cumple](https://invitio.events/en-US/cumpleanos)) não verificado |
| [My Invite](https://www.facebook.com/ads/library/?id=1894344334607556) | B2C, RSVP | MXN | 16 | 116,3 | não verificado | Modelo (serviço × ferramenta) desconhecido; publica em lotes |
| [Miboda.love](https://www.facebook.com/ads/library/?id=847134201787134) | B2C | MXN | 16 | 108,9 | não verificado | "Chatear con nosotros" ([link](https://www.facebook.com/ads/library/?id=38798735123072991)): venda assistida [inferência] |
| [Tarjetas Interactivas](https://www.facebook.com/ads/library/?id=1290146059969674) | ? | ARS | 8 | 126,5 | não verificado | Sem título; ângulo desconhecido |
| [Cartita Digital](https://www.facebook.com/ads/library/?id=992715157187735) | Convite + álbum | USD | 27 | 12,2 | não verificado | — |
| [Invitoo](https://www.facebook.com/ads/library/?id=1723104108989856) | Editor | USD | 2 | 1,8 | não verificado | — |
| [Event Builder Studio](https://www.facebook.com/ads/library/?id=1056284580730092) | Editor para quem faz convites para clientes | USD | 1 | 2,2 | não verificado | Único editor para revendedor em ES |
| [Con7igo](https://www.facebook.com/ads/library/?id=1078075381248787) | Editor | — | 1 | 2,6 | não verificado | Dado da Fase 3 (page_id não achado) |
| [InvitaWeb](https://www.facebook.com/ads/library/?id=1392058722514761) | Editor freemium | ARS | 1 | 7,6 | grátis | "Diseñá tu invitación gratis" |
| [Invita-Me.app](https://www.facebook.com/ads/library/?id=1598288708636661) | Editor | — | 3 | 8,6 | não verificado | "Tu invitación lista en 10 minutos… Confirman sin que los persigas" ([link](https://www.facebook.com/ads/library/?id=2104801660111309)) |
| [Compartiremos](https://www.facebook.com/ads/library/?id=2468620510329134) | Editor freemium | — | 3 | 17,9 | "Pruébalo gratis" | Dado da Fase 3 |
| [Dayfold.mx](https://www.facebook.com/ads/library/?id=1627187178748676) | B2C | MXN | 4 | 0,8 | não verificado | — |
| [Kit Digital](https://www.facebook.com/ads/library/?id=1376630554316244) | Template | CLP | 17 | 118,8 | "Solo a $3500" CLP ≈ US$ 3,65 ([link](https://www.facebook.com/ads/library/?id=975658698913214)) | Única longevidade do lado da revenda; o título não fala em revender |
| [Mega Plantillas](https://www.facebook.com/ads/library/?id=1708910720392963) | Template + demo | USD | 10 | 49,5 | não verificado | Só 1 anúncio com mais de 30 d |
| [Web Online](https://www.facebook.com/ads/library/?id=2313998366006369) | Revenda | PEN | 8 | 21,4 | não verificado | "listas para VENDER" (E2) |
| [Someri](https://www.facebook.com/ads/library/?id=1950759622550013) | Revenda | MXN | 3 | 8,5 | MXN 99–119 ≈ US$ 5,75–6,92 | Preço "ANTES/HOY" ([link](https://www.facebook.com/ads/library/?id=1392068805735135)) |
| Serviços MX | Designer por WhatsApp | MXN | — | — | [89](https://www.facebook.com/ads/library/?id=1802415467419849) · [119](https://www.facebook.com/ads/library/?id=1073107372315166) · [250](https://www.facebook.com/ads/library/?id=1406208784815107) · [349](https://www.facebook.com/ads/library/?id=1634274361447618) · [399](https://www.facebook.com/ads/library/?id=4601506146759840) | "invitación digital para XV", MX: 180 ativos ([busca](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=invitaci%C3%B3n%20digital%20para%20XV&search_type=keyword_unordered)), quase todos serviços locais; [Convite.events, pase QR](https://www.facebook.com/ads/library/?id=1731668288385176) |
| [Allegra](https://www.facebook.com/ads/library/?id=938228905499063) · [Luxe Invite](https://www.facebook.com/ads/library/?id=1567459587847561) | Serviço com pases, álbum QR e impresso | — | — | — | não verificado | Validam os bumps B2 e o upsell |
| Hotmart ES | Kits | USD | — | — | US$ 5 ([T102280557H](https://pay.hotmart.com/T102280557H)) a 14,99 ([K102179105D](https://pay.hotmart.com/K102179105D)) | Há kits na Hotmart que anunciam "RSVP online" (Fase 3) |
| BR [Convitia](https://www.facebook.com/ads/library/?id=1042494484973953) | Editor freemium, dois ângulos | BRL | 33 | 76,9 | freemium | Revenda com "Fature até R$250" (proibido para nós) |
| BR [Canva Para Noivas](https://www.facebook.com/ads/library/?id=1313617404312022) | Template B2C | BRL | 34 | 88,9 | R$ 47 / 67 | — |
| BR [Conviteria](https://conviteria.com.br/) | Editor | BRL | — | — | grátis até 30 convidados; R$ 20 acima | — |

## O melhor argumento de por que vai falhar (e o que mataria a ideia)

**O argumento.** O L02 só fecha a conta se comprar cada cliente a um CPA igual ou menor que o do Mimo. Mas o público é muito mais estreito, os substitutos são grátis ou mais baratos, e nenhum editor self-service de ticket baixo se sustentou em espanhol.

- **Margem.** A US$ 9,90, o CPA-alvo em BRL é 5,23, contra ~5,60 do Mimo. O 9,90 é decisão de preço a validar no teste (a decisão final trava o front em 9,90, sem A/B, até o K2). A 7,90, o alvo cai para **4,20**, 25% abaixo do que o Mimo tolera. Com adesão cética aos bumps (o "Para siempre" perde a função depois da festa), o 9,90 cai para **4,53**.
- **Público.** Só ~1,1% do Facebook MX está comprando convite em cada momento. O CPA de teste esperado é de US$ 5–9 [inferência]. O ponto médio, 7,0, dá ROI de 1,12 em BRL.
- **Quem dura não vende o nosso formato.** A Invitio cobra 599 MXN e empacota álbum. A Miboda vende por chat. Os 6 editores baratos ou grátis têm 18 dias ou menos no ar.
- **Preço espremido dos dois lados.** O designer a MXN 89–119 é mais barato que os nossos MXN 169 e entrega pronto. O grátis cobre quem não quer pagar nada.
- **Calendário.** O lançamento (05–11/10) pega o CPM subindo para o pico de novembro (+41% nos EUA; LATAM não verificado; [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [Clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics)). E já é tarde para as bodas de nov–dez.
- **Desfecho mais provável:** não é zero venda. É um CPA estável de US$ 6–8, que paga a mídia mas não passa na régua de 1,5. Mesmo com sucesso, são semanas de build e operação para, no máximo, 30–80% de um Mimo.

**Os 5 maiores riscos e o sinal precoce de cada um:**

| # | Risco | Sinal objetivo |
|---|---|---|
| 1 | Mercado: compra planejada, público estreito, substitutos grátis ou baratos | Taxa de prévia → pagamento < 50% da do Mimo depois de 500 prévias; mediana entre lead e compra > 72 h; > 30% dos comentários são "¿es gratis?" ou "¿cuánto cuesta?" |
| 2 | Economia: líquido real abaixo do estimado (preço, adesão ao B1, taxa pós-21/09, reembolso) | Taxa fixa por bump na primeira venda (R3/R4); B1 < 15% depois de 100 compradores; líquido medido < 7,60 (a 9,90) ou < 6,00 (a 7,90); reembolso > 4% |
| 3 | Criativo e CPM: demo saturada (849 anúncios só no MX, [busca](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=invitaciones%20digitales&search_type=keyword_unordered)), pixel novo, Q4 caro | CPM > 1,3× o do Mimo nos mesmos países; CTR de link mediano < 70% do Mimo depois de 30 anúncios |
| 4 | Produto: música e RSVP falham dentro do WhatsApp/Instagram; prazo de 14 d no limite; campo "presentes/datos bancarios" vira isca de golpe | Música que não toca no QA do D11; MVP não vendável até o D14 (06/10); < 50% dos convites com ≥ 1 confirmação em 7 d; qualquer denúncia de golpe |
| 5 | Conta e política, com contágio para o Mimo: a célula de revenda encosta em "oportunidade econômica" | Qualquer reprovação por resultados irreais; pedido de verificação de anunciante; Hotmart sem aprovar produto e bumps até o D7. **BM, conta de anúncio e cartão separados do Mimo.** Abrir conta nova depois de um bloqueio é burla de sistemas |

**O que mataria a ideia.** Todas as réguas estão em conta BRL. Depois de 100 compradores, recalcule com o líquido medido: alvo = líquido ÷ 1,68; break-even = líquido ÷ 1,12.

| Gate | Quando | Critério | Ação |
|---|---|---|---|
| K0 | D11–D14 | Música não toca no iPhone dentro do WhatsApp ou do Instagram, compra ou reembolso reais falham, ou o MVP não fica vendável até 20/10 | Não lançar. Depois de 20/10, adiar para 26/12 |
| K1 | Contínuo | Gasto ≥ US$ 10,46 (a 9,90) / 8,40 (a 7,90) sem venda | Pausar o anúncio |
| **K2** | ≥ US$ 400 na célula B2C, ≥ 20 anúncios com ≥ 1.000 impressões | CPA do front > **7,85** (9,90) / **6,30** (7,90), ou < 25 compras | **Matar** o formato atual. A US$ 400 e CPA 7,85 são ~51 compras; com margem de erro de ±28%, 7,85 × 0,72 = 5,65 ainda fica acima de 5,23 |
| K3 | 100 compradores | Líquido < 7,60 (9,90) / < 6,00 (7,90) sem bater o novo alvo; reembolso > 6%; chargeback > 0,5% (o limite da Hotmart é ~0,9%) | Matar ou parar |
| K4 | US$ 1.500 acumulados ou 15/11, o que vier primeiro | Nenhum conjunto sustenta 7 dias seguidos a ≥ US$ 50/dia com CPA ≤ 5,23 / ≤ 4,20 | **Estacionar**: não é motor de escala. Só segue rodando pequeno com CPA ≤ 6,28 / 5,04 (ROI 1,25) |
| K5 | 15/11 | Não passou no K2 | Pausar até 26/12; fazer um único reteste até 20/01 com US$ 400. Falhou de novo: morte. **Teto total de aprendizado: US$ 2.000** |
| K6 | Junto com o K2 | CTR × conversão < CPM ÷ (1.000 × CPA-alvo). Ex.: com CPM de US$ 3, mínimo de 0,057% a 9,90 | Diagnóstico: CTR bom com conversão ruim → oferta; o contrário → criativo |
| K7 | 500 prévias | Prévia → pagamento < 50% da taxa do Mimo | Um único teste de "publica grátis limitado"; se não mover, entra no K2 |
| K8 | 100 convites publicados | < 50% com ≥ 1 confirmação em 7 d | O RSVP não é o motivo da compra; reforça o corte |
| K9 | Contínuo | Uma reprovação por resultados irreais, ou 0 vendas depois de US$ 100 na célula de revenda | Desligar a célula para sempre |

**Regras de teste por país (corrigidas):**
- US$ 20–40/dia por conjunto, até ~30 compras ou US$ 250 gastos;
- **continuar** com CPA ≤ 6,28 (ROI 1,25 em BRL);
- **escalar** +20–30% a cada 48–72 h com CPA ≤ 5,23;
- **parar o país** com CPA > 7,85 depois de US$ 150.

As regras da oferta ("continuar ≤ 7,0 / parar > 8,8") ignoravam os 12% da conta BRL e deixavam perder dinheiro.

**Posição final sobre a licença, o segundo ângulo:**
- O produto mantém a licença: bump B4 "+5 invitaciones" e página de licença.
- A **célula de anúncios de revenda e a landing para negócios ficam fora do lançamento.** Três motivos:
  - a longevidade na revenda é só de template barato;
  - o único editor para revendedor em ES tem 2,2 d no ar;
  - é o público que mais reembolsa (premissa [estimativa]), e é o único ponto que arrisca a conta ligada ao Mimo.
- Ela só abre se o B2C passar no K2, com ≤ 20% da verba, só com demonstração e sujeita ao K9.
- O build, a oferta e o criativo previam essa célula desde o início. Esta é a correção do red team.
