# L67 · Kit de fiesta personalizado: gerador de kit de cumpleaños com nome e idade, em PDF pronto para imprimir (a mãe faz a própria festa ou monta kits para vender)

Data: 22/09/2026. Consolida pesquisa, build, oferta, criativo e red team (notas de trabalho privadas, fora do repositório), já com as correções do red team.

**Convenções:**
- **[medido]**: Biblioteca de Anúncios da Meta (só ACTIVE, 22/09/2026) ou página com link.
- **[estimativa]**: conta aberta, feita na calculadora do usuário (`_raw/calc_economia.py`).
- **[inferência]**: leitura minha.
- **não verificado**: não confirmado.

Contagem de anúncios e dias no ar são proxies, não faturamento. Não há faturamento nem ROAS de concorrente neste documento. Do Mimo Gift entram só quatro números: líquido por comprador ~US$ 9,4, adesão do bump principal ~1/3, reembolso < 1% e gasto > R$ 2.600/dia (dado do usuário).

**Nome do produto: "[Marca]", a definir.** "Fiesta Lista", o nome provisório da pesquisa e do build, **já é uma página anunciante em BRL** ([link](https://www.facebook.com/ads/library/?id=1719759895753397)) e está descartado. A marca nova precisa ser checada na Biblioteca de Anúncios e no registro de marcas antes do D1.

## Resumo em 5 linhas

1. **O produto.** É um editor web sem login. A mãe escolhe um de 8 temas originais, digita nome e idade e vê de graça, com marca d'água, as 7 peças do kit já com o nome: convite, topo de bolo, toppers, etiquetas, banderín e cartaz. Paga para baixar o PDF pronto para imprimir (Carta e A4, com linhas de corte) e o convite em imagem para WhatsApp. O front custa US$ 9,90 em moeda local, em A/B contra US$ 7,90. Quem monta kits para vender entra por um bump de licença (US$ 6,90), não pelo gancho principal.
2. **A evidência.** A categoria-pai, o pack de kit de festa para editar no Canva, tem demanda longeva em ES. O DecoKit tem 160 anúncios ativos (102 com entrega no MX; [página no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&view_all_page_id=737352542803130&search_type=page)), e os dois mais antigos, ambos de temática, estão no ar há 136,6 e 127,1 d [medido; proxy]. **O gerador não tem prova.** Nenhum anunciante de gerador apareceu em ES em mais de 15 buscas por palavra-chave, e o líder já roda a mesma demo dentro do pack: "Solo cambió un nombre", há 39,2 d.
3. **A economia [estimativa].** A US$ 9,90, o líquido por comprador fica em 7,93 / 8,70 / 9,61 (conservador / base / otimista), contra ~9,4 do Mimo. O CPA máximo para ROI 1,5 com conta de anúncio em BRL fica em 4,72 / 5,18 / 5,72. A US$ 7,90, o cenário base cai para 6,99 de líquido e 4,16 de CPA, 26% abaixo dos ~5,60 que o Mimo tolera.
4. **O teto [estimativa, confiança baixa].** Em espanhol, US$ 100–350/dia (base de 200), ou ~20–70% do Mimo (> R$ 2.600/dia ≈ US$ 506). O limite é o público em compra: só quem tem aniversário de filho marcado para as próximas semanas, cerca de 0,2–0,4% dos usuários do Facebook no MX em cada momento.
5. **O veredito.** Vale só como teste barato com portões de corte: MVP vendável entre o D11 e o D14 e, no máximo, ~US$ 600 no braço gerador para decidir. O desfecho mais provável é um CPA de US$ 5–8 com resultado inconclusivo [estimativa]. A ideia faz mais sentido no mesmo motor do L02 do que sozinha. Complementa o Mimo, mas não o substitui como motor de escala.

## O que o comprador recebe e o mecanismo (por que é diferente do que já existe)

**Como funciona (no celular, sem login):**
1. **Tema.** A mãe escolhe entre 8 temas originais × 2 paletas, sem personagem. Os candidatos são dinosaurios, unicornio y arcoíris, safari/animalitos de la selva, espacio, fondo del mar, fútbol, mariposas y jardín e osito "mi primer añito". A escolha final não foi verificada: antes do D3, conferir quais temáticas aparecem nos títulos do DecoKit e da Deco Mundo.
2. **Dados.** Nome, idade, frase opcional ("¡Mis 5 añitos!"), data, hora e local da festa, e o e-mail para salvar o rascunho. A **foto é opcional e entra só na invitación e no cartel**, não no topo de bolo.
3. **Prévia grátis de todas as peças**, com a marca d'água "VISTA PREVIA". Dá para trocar tema, paleta e papel (Carta/A4) antes de pagar.
4. **Checkout Hotmart** em lightbox, com os bumps. Pagamento em dinheiro, como OXXO, fica pendente até ser confirmado.
5. **Página de obrigado:** "Descargar PDF" (link assinado, gerado no clique) e "Guardar invitación para WhatsApp". O link também vai por e-mail. Se a página abrir no navegador interno do Instagram, aparece o aviso para abrir no navegador.
6. **Painel "Mis kits":** baixar de novo por 12 meses, editar data, hora e local, e usar créditos.

**O que vem no PDF (front).** Os tamanhos são estimativa, a validar no teste de impressão do D6.

| Pág. | Peça | Tamanho |
|---|---|---|
| 0 | "Cómo imprimir": imprimir em "Tamaño real / 100%", quadrado de calibração de 5 cm, sugestão de papel (opalina/cartulina de 180–250 g) | — |
| 1 | Invitación, 2 por folha. Leva o QR do convite web se o comprador levar o B1 | 12,7 × 17,8 cm |
| 2 | Topo de bolo "Feliz cumple [Nombre] · [edad]" com ilustração e linha de corte, 2 por folha | ~15 cm de largura |
| 3 | 12 toppers de cupcake, alternando nome, idade e ilustrações | Ø 5 cm |
| 4 | 12 tags "¡Gracias por venir!" | Ø 6 cm |
| 5 | Etiquetas de garrafinha ou suco, 5 por folha, com o aviso "mide tu botella" | 20 × 5 cm |
| 6 | Banderín "FELIZ CUMPLE" + nome, 1 letra por bandeirinha, 2 por folha. Nomes com mais de 10 letras podem sair só com o nome ou com o apelido | — |
| 7 | Cartel "¡Bienvenidos al cumple de …!" + número gigante da idade | folha inteira |

Além do PDF, o comprador recebe o **convite em imagem vertical (PNG 1080×1920)** para WhatsApp e estados, que resolve o "no tengo impresora".

**Regras de uso do front:**
- **1 kit = 1 criança + 1 festa.** Depois do pagamento, nome, idade e tema ficam presos ao kit.
- Correções permitidas: até 3 edições pequenas no nome (erro de digitação), idade ±1 e 1 troca de tema grátis em até 48 h.
- Data, hora e local ficam livres até o dia da festa.
- Até 10 gerações de PDF por kit.
- Não existe versão em branco nem exportação editável. A arte em alta resolução nunca chega ao navegador.

**O mecanismo é "créalo gratis y míralo completo, con su nombre, antes de pagar".** É o mesmo do Mimo: o produto é a demo do anúncio. A prévia responde ao "¿es confiable?" e ao "no era lo que esperaba" [inferência].

**Onde é diferente e onde não é:**

| Alternativa | Exemplo [medido] | O que a mãe tem de fazer | Diferença real para o L67 |
|---|---|---|---|
| **Mega-pack Canva** (L09, a categoria-pai) | [DecoKit](https://www.facebook.com/ads/library/?id=3921946164603954): "¿De verdad vienen más de 10.000 diseños?"; [Activa Academy](https://www.facebook.com/ads/library/?id=1561011532248354) (MXN, 77,6 d); [Mundo Creativo Digital](https://www.facebook.com/ads/library/?id=1054639970312774) (66 ativos); Hotmart de US$ 5 a 17 | Achar o tema entre milhares de arquivos, abrir peça por peça no Canva, trocar nome e idade em cada uma | Digita uma vez e recebe todas as peças coerentes. **Mas o líder já vende esse benefício no pack:** ["✨ Solo cambió un nombre"](https://www.facebook.com/ads/library/?id=2009114323127277) (39,2 d, MX). E vende reuso, o contrário da nossa trava: ["🎉 No es para una sola fiesta"](https://www.facebook.com/ads/library/?id=918283787405166) (38,7 d, MX) |
| **Kit personalizado por designer** | [Decoraciones Infantiles](https://www.decoracionesinfantiles.com/), "desde USD 6,00"; [Elita Kits Digitales](https://www.elitakitsdigitales.com.ar/us/), 24 h úteis e 30 peças; [Munki](https://www.munki.com.ar/us/kits-personalizados/cumpleanos/), "desde $190" (moeda não verificada); [Poppy Decor](https://poppydecor.com.ar/productos/elementos-kit-de-cumpleanos-imprimible-personalizado/), ARS 8.750, com personagem de filme; [Papel Fiesta](https://www.facebook.com/ads/library/?id=1536737214484050), ARS, 127,9 d, venda por WhatsApp | Pedir, esperar horas ou dias e depender de atendimento | Mesmo resultado na hora, sem conversa e sem personagem licenciado. Em troca, esses serviços fazem "temáticas a pedido"; nós temos 8 temas |
| **"App" de festa** (EN) | [Magic Deco](https://www.facebook.com/ads/library/?id=4475514232660841): "Not Another File Bundle. It's an APP!" (1,2 d) | O material dela abre os designs no Canva ([resumo de busca](https://mundoinfantildigital.shop/products/magic-party-kit)); o mecanismo real não foi verificado | Sinal de direção fora de ES, não validação: 1,2 d no ar não prova nada |
| **Canva grátis** | [Canva: invitaciones fiesta infantil](https://www.canva.com/es_mx/crear/tarjetas/invitaciones-fiesta-infantil/) | Montar sozinha, peça por peça | Kit inteiro coerente, com nome, linhas de corte e calibração. Quem domina o Canva pode não ver valor |

**O que precisa ser verdade para o gerador vencer o pack:**
- **Velocidade sem programa de design.** O tempo não foi medido. Nenhuma promessa de minutos até o QA do D11 medir o tempo mediano do editor.
- **Prévia completa antes de pagar.**
- **Impressão certa de primeira:** tamanho real, Carta ou A4, linha de corte e quadrado de calibração. Um pack genérico não garante isso.

**Ressalvas do red team:**
- **Os títulos "menos busca, mais pronto" são sinal fraco.** "Menos tiempo buscando. Más creando." e "Encuentra. Personaliza. Crea." (Deco Mundo, ≤ 12,9 d), "Stop Searching. Start Creating." (Magic Deco, ≤ 6,3 d) e "Por fin, todo combina" (9,0 d no MX) sugerem que o mercado já nomeia a dor do excesso de escolha [inferência]. Nenhum deles tem longevidade, e o contra-sinal "Solo cambió un nombre" mostra o pack prometendo o mesmo.
- **O público é a mãe que não quer editar.** A evidência de que ele existe é indireta: ["No sos diseñadora? No importa"](https://www.facebook.com/ads/library/?id=1952196192325259) (133,1 d), ["¿Necesito Canva Pro? Para nada."](https://www.facebook.com/ads/library/?id=982322554175818) (120,2 d) e o mercado de personalização sob encomenda.
- **O convite web não é o diferencial do front.** Ele é o bump B1, com adesão base estimada em 22%, então 78% dos compradores não o recebem. O diferencial do front é a personalização instantânea, com prévia e impressão calibrada. Pôr o convite no front a um preço maior é um teste possível depois; não está modelado.
- **A ausência de gerador em ES vale só para as buscas por palavra-chave.** E é compatível tanto com espaço livre quanto com falta de demanda.

**Convergência com o L02 (invitaciones web): um motor, dois funis.**
- **Um código só.** Há um motor de temas e um registro de festa (nome, idade, data, local e tema) com duas saídas: o PDF (L67) e a página web (L02).
- **Funil infantil:** o kit é o front e o convite web é o bump B1.
- **Funil de boda, XV e baby shower:** o convite é o front e o kit "a juego" é bump (é o B3 do L02).
- **Ordem de construção:**
  - se o L02 vier primeiro, o L67 vira uma extensão de ~4–5 dias no mesmo projeto [estimativa do build];
  - se o L67 vier primeiro, o L02 herda o motor, a página do convite, o webhook e os créditos.

## Comprador: perfil, dor e objeções (com evidência)

**Perfil:**

| Segmento | Quem (provável) | Evidência [medido; proxy] |
|---|---|---|
| **1. Mãe que faz a festa do filho (principal)** | Mulher de ~25–40 anos, com filho de 1 a 8 anos [inferência pelos títulos no feminino; não verificado]. Faz a festa em casa ou em salão pequeno, em 1–4 semanas, e compra pelo celular | ["La mejor parte es ver su carita"](https://www.facebook.com/ads/library/?id=2020782765482199) (136,0 d); ["El secreto de las mamás que decoran como pros"](https://www.facebook.com/ads/library/?id=978387111269396) (134,2 d); ["La fiesta que tu hijo no va a olvidar"](https://www.facebook.com/ads/library/?id=4309605869368925) (97,1 d); Deco Mundo, ["Su fiesta. Hecha por ti."](https://www.facebook.com/ads/library/?id=1622458965940698); Magic Deco, ["Create Their Dream Party Yourself"](https://www.facebook.com/ads/library/?id=2467686010427034). Tendência de festas menores no MX, de 30–40 pessoas ([blog de inflables](https://inflablesparafiestas.com.mx/blog/tendencias-fiestas-infantiles-2026-mexico/), fonte fraca) |
| **2. Emprendedora de papelería ou decoradora (secundário)** | Mulher que vende kits ou decoração por encomenda [inferência] | DecoKit: ["Más pedidos. Menos trabajo."](https://www.facebook.com/ads/library/?id=1066028365762431) (92,0 d, MX), ["Tu negocio puede empezar con esto"](https://www.facebook.com/ads/library/?id=1477793531027394) (90,2 d), ["Tu negocio necesita un sistema"](https://www.facebook.com/ads/library/?id=2338278257322076) (95,2 d); Magic Deco, ["Say YES to More Client Orders"](https://www.facebook.com/ads/library/?id=1397155619172622); [Papel Fiesta](https://www.facebook.com/ads/library/?id=1536737214484050) (serviço, 127,9 d) |
| **3. Confeitera (toppers)** | Quem faz bolos e precisa de topper com nome [inferência] | [Emilia Creativa](https://www.facebook.com/ads/library/?id=27881754751467164), "+1.200 Cake Toppers Profesionales" (32 ativos; o mais antigo com 26,6 d); [Veronica Colombia](https://www.facebook.com/ads/library/?id=2576430022803606), "+2.500 toppers" (COP); [July Love Kits](https://www.facebook.com/ads/library/?id=1040848878786434), "750 Diseños de cake toppers" |

**Países:** MX, AR, CO, PE, CL, EC e hispanos nos EUA, pelas moedas dos anúncios (USD, MXN, ARS, CLP, COP, PEN) [inferência]. **Ressalva:** o DecoKit tem **0 anúncios ativos com entrega na AR** ([página filtrada na AR](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=AR&view_all_page_id=737352542803130&search_type=page)), e 0 no filtro AR + CO [medido hoje; o link reproduz um país, e o filtro de dois países foi feito via API em 22/09/2026]. Por isso AR e CO entram como exploratórios.

**Quanto pesa o ângulo de negócio no líder [medido; proxy]** ([DecoKit no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&view_all_page_id=737352542803130&search_type=page); o filtro UY/BO/GT/DO junta quatro países e foi feito via API em 22/09/2026):
- **Filtro UY/BO/GT/DO:** 5 de 39 títulos com ≥ 30 d (13%); entre os com ≥ 90 d, 4 de ~23.
- **Filtro MX:** 13 dos 50 anúncios mais novos (26%) e 12 de 41 com ≥ 30 d (29%). Os dois mais antigos dessa janela (92,0 e 90,2 d) são de negócio.
- **Leitura corrigida:** a longevidade máxima está na **temática** (136,6 e 127,1 d). O negócio pesa de ~1/8 a ~1/3 dos títulos, conforme o país. Proporção de títulos não é proporção de compradores.

**Dores (títulos com mais dias no ar):**

| Dor | Título observado (dias no ar) |
|---|---|
| Falta de tempo, deixar para a última hora | ["¿Otra vez dejando la fiesta al final?"](https://www.facebook.com/ads/library/?id=1375464874054271) (32,1 d); ["Deja de dejarlo para después"](https://www.facebook.com/ads/library/?id=1541424287782653) (97,1 d) |
| Custo da decoração profissional | ["Decora como una pro — sin estrés, sin gastar de más"](https://www.facebook.com/ads/library/?id=3836578819984789) (97,1 d). No MX, uma decoradora cobra MXN 2.000–10.000 ≈ US$ 116–581 ([Cronoshare](https://www.cronoshare.com.mx/cuanto-cuesta/decoracion-eventos-fiestas)) |
| Não saber desenhar ou editar | ["No necesitas ser diseñadora"](https://www.facebook.com/ads/library/?id=1624690932588700); ["¿Necesito Canva Pro? Para nada."](https://www.facebook.com/ads/library/?id=982322554175818) (120,2 d); ["No sos diseñadora? No importa"](https://www.facebook.com/ads/library/?id=1952196192325259) (133,1 d) |
| Achar o tema e fazer tudo combinar | ["¿No encontrás la temática que quiere tu hij@?"](https://www.facebook.com/ads/library/?id=1285905063665166) (127,1 d); ["Por fin, todo combina"](https://www.facebook.com/ads/library/?id=1647616600064833) |

**Desejos:**

| Desejo | Título observado |
|---|---|
| Ver a reação do filho | ["La mejor parte es ver su carita"](https://www.facebook.com/ads/library/?id=2020782765482199) |
| Ser elogiada, ter uma festa com cara de profissional | ["😳 ¿Lo hiciste tú?"](https://www.facebook.com/ads/library/?id=999401313110519); ["Haz que se vea premium"](https://www.facebook.com/ads/library/?id=2392615854878004); ["De simple a WOW"](https://www.facebook.com/ads/library/?id=2021991908441528) |
| Fazer ela mesma | ["Así armé esta fiesta desde casa"](https://www.facebook.com/ads/library/?id=1574986933976057) (97,1 d); ["Este año, haz tú la magia"](https://www.facebook.com/ads/library/?id=1107883622194662) |

**Leitura [inferência].** O gatilho emocional (a carinha do filho, o "¿lo hiciste tú?") é do mesmo tipo que o do Mimo: a reação de quem recebe. A diferença é que a compra fica presa a uma data marcada. É impulso **dentro de uma janela**, não impulso puro.

**Objeções:**

| Objeção (ES) | Evidência | Resposta no produto ou no criativo |
|---|---|---|
| "¿Tienen la temática que quiere mi hijo?" | DecoKit: 127,1 d e [136,6 d](https://www.facebook.com/ads/library/?id=2779896019055999); [Magic Deco](https://www.facebook.com/ads/library/?id=1575882503471281); [template de Bluey na Hotmart](https://pay.hotmart.com/B103082603B). É **temática, e provavelmente personagem (não verificado):** ["kit cumpleaños Bluey"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=kit%20cumplea%C3%B1os%20Bluey&search_type=keyword_unordered) trouxe 7 anúncios, nenhum com o personagem no título, e o corpo do anúncio não é visível (o link reproduz um país; a contagem somou vários países de ES + US via API em 22/09/2026) | Não usar personagem. Oferecer temas originais, 2 paletas e a foto opcional na invitación e no cartel. Na página, dizer "temas originales". **O risco residual é alto:** são 8 temas contra centenas, e a foto não pode aparecer no anúncio (é rosto de criança) |
| "¿Necesito Canva / saber diseño / computadora?" | DecoKit, "¿Necesito Canva Pro?" (120,2 d); digest de demanda ("¿se puede desde el celular?") | Demo 100% no celular, sem programa de design |
| "No tengo impresora" | Não verificado [inferência] | PDF para papelaria ou ciber; convite em PNG para WhatsApp |
| "Por ese precio me dan 10.000 diseños" | DecoKit, "¿De verdad vienen más de 10.000 diseños?"; refutação 4 da Fase 3 | "No son miles de archivos: es su fiesta". Comparar pelo esforço, não pela quantidade |
| "¿Es confiable? / Hotmart estafa / no me llegó" | [decidetucurso](https://decidetucurso.com/hotmart-opiniones/); [ajuda Hotmart](https://help.hotmart.com/es/article/360038516312/-que-hacer-si-no-puedo-acceder-a-mi-compra-) | A prévia completa **antes** de pagar prova o entregável; a entrega aparece na página de obrigado e chega por e-mail |
| "No reconozco el cargo HTM*" | [Hotmart](https://help.hotmart.com/es/article/209033847/-como-identificar-un-cargo-de-hotmart-que-aparecio-en-mi-extracto-bancario-) | Avisar no checkout e no e-mail |
| "¿Queda bien impreso? ¿Qué tamaño?" | Não verificado; provável principal fonte de reembolso de imprimível [inferência] | Carta e A4, linha de corte, página 0 e teste real de impressão antes de lançar |
| "Me cobraron varias veces" | [Trustpilot Hotmart](https://www.trustpilot.com/review/hotmart.com?page=4) | Bumps com nome e preço claros; um único upsell, sem downsell |
| Desconfiança de escassez ou nota falsa | Concorrentes usam ["¡ÚLTIMAS UNIDADES!"](https://www.facebook.com/ads/library/?id=1590800242454223), ["⭐4,5/5"](https://www.facebook.com/ads/library/?id=1580948452926596) e ["¡Pronto dejará de estar disponible!"](https://www.facebook.com/ads/library/?id=1590631305803085) | Não copiar. A prova é a demo |

**Espelho BR [medido]:**
- **Pack barato:**
  - [Festa 550](https://www.facebook.com/ads/library/?id=1043999145023859): 18 ativos, 35,7 d;
  - ["20 Mil Topos de Bolo por R$ 1,49"](https://www.facebook.com/ads/library/?id=1579502953724620): 33,5 d;
  - ["Kit Festa na Mesa a partir de R$ 3,99"](https://www.facebook.com/ads/library/?id=1766927220894230).
- **Personalizado por pessoa:**
  - [Kit Festas Personalizadas](https://www.kitfestaspersonalizadas.com/): "você coloca nome e idade, imprime";
  - [Clarim Ateliê](https://clarimatelie.netlify.app/);
  - [Elo7](https://www.elo7.com.br/lista/kit-festa-para-imprimir/): ~7.566 produtos.

  A presença desses sites em anúncios não foi medida.
- **Leitura:** o BR também se divide entre pack barato e personalização feita por gente. Não achei gerador automático anunciado (a busca BR na Biblioteca não foi feita). Há ~11 operadores em BRL vendendo pack em espanhol, contados entre os 50 anúncios mais novos da busca ["papelería para fiestas"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=papeler%C3%ADa%20para%20fiestas&search_type=keyword_unordered) (o link reproduz um país; a busca original somou 11 países via API em 22/09/2026). Se o gerador funcionar, eles copiam: a defesa é execução, não barreira técnica [inferência].

## Oferta: front por país (moeda local), bumps, upsell, garantia

**Paywall (ES):**
- "Créalo gratis y míralo completo, con su nombre, antes de pagar."
- "Descargar mi kit · pago único · sin suscripción."
- "Incluye: PDF listo para imprimir (Carta y A4) con invitación, topper de pastel, toppers, etiquetas, banderín con su nombre y cartel de bienvenida + invitación en imagen para WhatsApp."
- "Temas originales (sin personajes de marca)." É honesto e evita o reembolso de quem esperava personagem [inferência].
- "Imprímelo en casa o en cualquier papelería."
- "En tu estado de cuenta el cargo aparece como HTM* / HOTMART."

**Âncoras de preço [medido]:**

| Tipo | Exemplos | Faixa em US$ |
|---|---|---|
| Pack (muitos arquivos; a mãe edita) | Hotmart [US$ 5](https://pay.hotmart.com/K106315659W), [US$ 10](https://pay.hotmart.com/P100609472X) e [US$ 17](https://pay.hotmart.com/F103010959C?off=a1kavqsu&checkoutMode=10); [Kit Digital, CLP 3.500](https://www.facebook.com/ads/library/?id=975658698913214) ≈ US$ 3,65 | 3,65–17 |
| Personalizado por designer (com espera) | [Decoraciones Infantiles](https://www.decoracionesinfantiles.com/), "desde USD 6,00"; [Una Fiesta Bonita](https://www.unafiestabonita.com/collections/kits-imprimibles-para-fiestas), kit por tema a 10,99–23,99 (valor de snippet) | 6–23,99 |
| Decoradora contratada no MX | [Cronoshare](https://www.cronoshare.com.mx/cuanto-cuesta/decoracion-eventos-fiestas): MXN 2.000–10.000 | 116–581 |
| **Âncora BR (em PT, para o BR)** | ["Kit Festa na Mesa a partir de R$ 3,99"](https://www.facebook.com/ads/library/?id=1766927220894230) ≈ US$ 0,78; ["20 TEMAS DE FESTA POR APENAS R$ 9,90!"](https://www.facebook.com/ads/library/?id=1119474840740232) ≈ US$ 1,93. Não é âncora de preço em ES | 0,78–1,93 |

**Front: A/B de US$ 9,90 (A) contra US$ 7,90 (B).** Nenhum braço é favorito:
- a matemática favorece o 9,90, porque o 7,90 só empata em líquido por lead se converter **≥ 1,24×**;
- o 7,90 pode converter mais, mas não há evidência pública de quanto: decisão de preço a validar no teste;
- **não lançar abaixo de 7,90:** a 6,90, seria preciso converter 1,42× mais.

| País | Moeda | A | ≈ US$ | B | ≈ US$ | Líquido por comprador no base, A / B [estimativa] |
|---|---|---|---|---|---|---|
| MX | MXN | MXN 169 | 9,81 | MXN 139 | 8,07 | 8,59 / 7,10 |
| CO (exploratório) | COP | COP 29.900 | 9,60 | COP 24.900 | 7,99 | 8,42 / 7,04 |
| CL | CLP | CLP 9.490 | 9,89 | CLP 7.490 | 7,81 | 8,70 / 6,92 |
| PE | PEN | S/ 32,90 | 9,77 | S/ 26,90 | 7,99 | 8,55 / 7,03 |
| AR (exploratório) | USD (recomendado) | US$ 9,90 | 9,90 | US$ 7,90 | 7,90 | 8,70 / 6,99, antes da conversão de ARS |
| EC, DO, GT | USD | US$ 9,90 | 9,90 | US$ 7,90 | 7,90 | 8,70 / 6,99 |
| US (hispanos) | USD | US$ 12,90 | 12,90 | US$ 9,90 | 9,90 | 11,27 / 8,70 |

Câmbio de 22/09/2026: 1 USD = 17,22 MXN · 3.116 COP · 959,5 CLP · 3,366 PEN · 5,14 BRL. O líquido usa os bumps do cenário base (abaixo) e 4% de reembolso. Nos países em moeda local, os bumps entram pelo preço local.

**Notas de implementação (Hotmart):**
- **Moeda local.** Um resumo de busca indica que a Hotmart aceita preço em moeda local, com MXN e COP entre as opções ([formas de pago](https://help.hotmart.com/es/article/216440337/-que-formas-y-metodos-de-pago-puedo-elegir-para-mi-producto-), [vídeo](https://www.youtube.com/watch?v=DGQ4SNOmgfI)). **CLP, PEN e moeda local nos bumps não foram verificados.**
  - Se funcionar: uma oferta por país (código de oferta da Hotmart), escolhida pela landing.
  - Se não funcionar: ficar em USD com conversão automática, **sem imprimir preço em moeda local** no anúncio nem na landing, e mostrar "US$ 9,90 · se cobra en tu moneda".
- **AR.** A oferta fica em USD. A Hotmart aplica 9,5% na conversão de ARS para ofertas em USD ([Hotmart](https://help.hotmart.com/es/article/360015794612/-en-que-moneda-obtendre-mi-comision-); valor lido no resumo da busca). **Não verificado quem paga.** Se for o produtor, o líquido cai ~US$ 1,1. O comprador argentino pode pagar impostos locais por cima ([Hotmart](https://help.hotmart.com/es/article/15038303747981/-por-que-me-cobraron-impuestos-al-comprar-desde-argentina-)).
- **US.** Oferta separada, com ≤ 6% da verba no começo. A âncora em EN é o Etsy ([printable birthday kit](https://www.etsy.com/market/printable_birthday_kit), [birthday party bundle](https://www.etsy.com/market/birthday_party_bundle)); os preços não foram verificados.
- **Regra do A/B.** Sorteio 50/50 na landing, com a variante no parâmetro de rastreio do checkout. A decisão é por **líquido por lead** (o e-mail capturado no editor), já com os bumps.
  - Para detectar 25% de diferença numa conversão lead → compra de ~5%, são precisos ~4.900 leads, ou ~245 compras por braço (16 × 0,05 × 0,95 ÷ 0,0125²).
  - Não decidir com menos de ~150 compras por braço, salvo diferença grande.
- **Decisão pendente (usuário): travar o preço durante o teste de mecanismo?** O criativo propõe travar nas S41–S42 para isolar a variável gerador × pack.
  - Travar em **9,90** deixa o CPA-alvo em 5,18 (conta BRL).
  - Travar em **7,90** baixa o alvo para 4,16 (sem evidência pública de que o 7,90 converta ≥ 1,24× mais: decisão de preço a validar no teste).
  - O controle (pack) roda no mesmo preço do braço gerador.

**Order bumps.** Regras, iguais às do L02:
- bump barato tende a vender mais que bump caro: no briefing, o usuário relata que baixar o bump principal do Mimo de 7,90 para 4,90 aumentou a adesão;
- nome e preço claros;
- sem preço riscado e sem timer;
- cada bump é um produto digital entregável.

As adesões são **estimativas, não verificadas**.

| # | Bump (ES, como aparece no checkout) | US$ | MX / CO / CL / PE | O que entrega | Adesão cons. / base / otim. |
|---|---|---|---|---|---|
| B1 | **"Invitación digital animada a juego":** "Un link para WhatsApp con cuenta regresiva, ubicación con 'Cómo llegar' y botón para confirmar asistencia. Mismo diseño y nombre de tu kit." | 4,90 | MXN 79 · COP 14.900 · CLP 4.690 · S/ 15,90 | Página pública do convite, ativa até 30 d depois da festa, com o QR impresso na invitación. É o L02 "lite" no mesmo motor. O PNG do front canibaliza parte do valor [inferência], por isso a adesão base fica abaixo do ~1/3 do Mimo | 15 / **22** / 30% |
| B2 | **"Kits para siempre: todos los cumples de tus peques":** "Cada año, su kit nuevo con su nueva edad (y otro tema si quiere). Hasta 3 peques. Pago único." | 3,90 | MXN 69 · COP 11.900 · CLP 3.790 · S/ 12,90 | Até 3 nomes presos à conta; 1 kit por nome a cada 12 meses, com a idade atualizada. "Para siempre" = enquanto o serviço existir (dizer isso em `/es/terminos`). O DecoKit usa ["♾️ Un kit. Fiesta tras fiesta."](https://www.facebook.com/ads/library/?id=1097383766200420). **Ressalva:** a adesão é incerta, porque o pack concorrente já dá reuso sem custo extra [inferência] | 10 / **16** / 24% |
| B3 | **"Licencia Emprendedora":** "Crea hasta 10 kits en 12 meses para tus clientas y vende el kit impreso o tu servicio de personalización. Sin pie de página de la marca." | 6,90 | MXN 119 · COP 21.900 · CLP 6.590 · S/ 22,90 | 10 créditos, no máximo 3 kits novos por dia, uso comercial do **impresso**. **Não inclui revenda de arquivos, temas ou versões em branco** (evita PLR/MRR) | 2 / **4** / 6% |

- **Reconciliação dos arquivos anteriores:**
  - a licença a 9,90 da pesquisa cai para 6,90;
  - o "Kit XL / cajitas" vira o upsell;
  - o "Kit para otra fiesta" do build é absorvido pelo B2.

  O criativo, que seguia o build, só precisa trocar o nome do B2 no gancho reserva H18.
- **Ordem no checkout:** B1, B2, B3.
- **Se a taxa fixa incidir em cada bump** (regime R3, na seção Contas), o B2 a 3,90 retém só 64% do preço. Nesse caso, subir o B2 para 4,90.

**Upsell pós-compra de um clique (v1.1, fora do MVP): "Mesa dulce completa", US$ 7,90** (MXN 139 · COP 24.900 · CLP 7.490 · S/ 26,90).
- **O que é:** cajitas, envolturas de chocolate, etiquetas de agua e fondo de mesa, com o mesmo nome e o mesmo tema.
- **Copy:** "¿Completamos la mesa dulce? … Un clic, sin volver a ingresar tu tarjeta."
- **Demanda [medido]:** ["Todo puede empezar con una cajita"](https://www.facebook.com/ads/library/?id=1797800404690208) (Deco Mundo); ["+650 Plantillas de Candy Bar"](https://pay.hotmart.com/V89088274S); ["🍭 Crea Candy Bars Increíbles"](https://www.facebook.com/ads/library/?id=2845888295783849) (PEN, 23,1 d).
- **Build:** +2–3 dias, porque exige moldes com faca.
- **Adesão estimada:** 4 / 8 / 12%.
- **Com OXXO, PSE ou PagoEfectivo:** não verificado se o upsell funciona ([Hotmart, upsell](https://help.hotmart.com/pt-br/article/43101499107597/como-configurar-um-upsell-usando-o-funil-de-vendas-e-o-hotmart-pages)).
- Sem downsell encadeado.

**Garantia de 7 dias**, o mínimo da Hotmart ([garantia](https://help.hotmart.com/es/article/360034552751/-como-ajustar-el-plazo-de-garantia-del-producto-que-he-creado-)). Vendas para a UE têm mínimo de 15 dias. Por que 7 [inferência]:
- a prévia completa grátis faz o papel da garantia longa;
- o PDF impresso não é revogável, e com 30 dias quase toda compradora poderia fazer a festa e pedir o dinheiro de volta;
- o Mimo usa 7 dias e tem reembolso < 1%.

**Ressalvas:**
- **Nem todo comprador fica protegido pelos 7 dias.** Para quem compra 1 a 3 semanas antes, a janela de "usa e reembolsa" diminui. Mas os ganchos H07/H08 ("¿El cumple es este sábado?") atraem quem faz a festa **dentro** da garantia [inferência]. Medir o reembolso por gancho e cortar H07/H08 se ficarem acima da média.
- **"Si algo no se imprime bien, escríbenos y lo ajustamos" tem custo.** Regenerar o PDF custa ~0, mas o atendimento é tempo humano de um operador solo.
- **FAQ (ES):** "Tienes 7 días de garantía. Si pides el reembolso, tu enlace de descarga, tu invitación digital y tus créditos se desactivan."
- **Limite a vigiar:** chargeback de ~0,9% por região, acima do qual a Hotmart pode reter saldo (digest de políticas; confiança média).

**Controle L09 (pack Canva), para o teste de mecanismo:**
- Produto Hotmart separado, "Kit de Cumpleaños Editable en Canva": 4 dos 8 temas × as mesmas 7 peças, com as mesmas ilustrações.
- Mesmo preço do braço gerador, garantia de 7 dias e só um bump (a licença a 6,90). B1 e B2 dependem do motor.
- É um produto honesto, que entrega o que promete. Pela [licença do Canva](https://www.canva.com/help/using-canva-to-create-products-for-sale/), template com conteúdo Free e arte própria pode ser vendido como PDF ou link de template.
- O link de template é copiável (risco E4). Serve para o teste, não para escalar.

**O que não entra na oferta:**
- timer, preço riscado sem referência real e "¡ÚLTIMAS UNIDADES!";
- "⭐4,5/5", "+5000 VENDIDOS" ou "miles de mamás" sem base real, e depoimento;
- avatar de IA como "mamá clienta";
- personagem licenciado em tema, prompt, anúncio ou nome de arquivo;
- "+10.000 diseños". "Temas nuevos cada semana" só vale com a cadência real no ar;
- promessa de tempo ("en 2 minutos", "en 5 minutos") antes de o QA medir;
- na célula emprendedora: valor em dinheiro, "gana", "ingresos", "listas para vender" ou menção à situação financeira de quem vê. Copy permitida: "Kits personalizados para tus clientas, sin diseñar desde cero."

## Build: stack, telas, dias até o MVP

Uma pessoa só, no Lovable. Reaproveita o fluxo editor → página → Hotmart do Mimo Gift, em nível funcional.

**Correção do red team:** o motor do PDF **não** vem pronto. **O motor multipágina com imagens, TTF próprio e dois renderizadores é novo** e é o que decide o prazo.

**Stack:**

| Camada | Escolha | Observação |
|---|---|---|
| App | **Lovable** (stack padrão do Lovable) | Marca, domínio, pixel, produtos, dados e dashboard separados do Mimo; conferir no D1 que nenhum dado do Mimo veio junto |
| Banco e arquivos | **Supabase** (Lovable Cloud), backend próprio | Buckets: `kit-assets-preview` (público, WebP leve), `kit-assets-hires` (**privado**, PNG 300 dpi), `kit-pdfs` (privado), `party-photos` (caminho não adivinhável). Preço de teto do Supabase Pro: US$ 25/mês, 100 GB de storage e 250 GB de egress ([Supabase](https://supabase.com/pricing), via snippet). O Lovable Cloud não publica preço por GB |
| PDF | **jsPDF no servidor:** gera → Storage → `createSignedUrl` | PNG em alta, embutido uma vez por alias; fonte TTF própria (o jsPDF só aceita TTF, e as 14 fontes padrão não cobrem UTF-8: [npm](https://www.npmjs.com/package/jspdf), [Medium](https://medium.com/@berkayyyulguel/jspdf-utf-8-support-b7df7a76e593)); link assinado **curto (10 min) gerado no clique**, para o reembolso conseguir revogar. Limites de CPU e memória do Lovable para ~15 páginas com imagens: **não verificados** (spike do D2) |
| Prévia | **SVG em React**, a partir da mesma especificação do PDF, em baixa resolução e com marca d'água | Custo zero; é também o que se grava para os criativos |
| PNG do convite | Canvas 2D no navegador → salvar a imagem no aparelho | Custo zero |
| Pagamento | Hotmart: front + 3 bumps, em lightbox | Os produtos entram em análise: caminho crítico no D1 |
| Liberação | Notificação de pagamento da Hotmart (webhook): resposta de sucesso sempre, idempotência por transação, kit identificado pelo parâmetro de rastreio do checkout, bumps identificados pelo produto, fallback por e-mail | Aprovado → libera o kit; B1 → libera o convite; B2/B3 → concede créditos; reembolso ou chargeback → apaga o PDF, tira o convite público do ar, zera créditos; OXXO → pendente |
| Atribuição | UTMify (parâmetro de origem do checkout) + Meta CAPI com dataset novo | A configuração da UTMify fica com o usuário |
| E-mail | E-mail transacional | "Tu kit está listo" (link para o painel, não para o PDF), pago pendente, carrinho abandonado 1 h/24 h, recuperação de acesso |
| IA e vídeo no produto | **Nenhum no MVP** | A IA entra uma vez, para produzir as ilustrações |

**Motor de peças (a parte nova).**
- **Uma especificação, dois renderizadores.** Cada peça é uma função `layout(peça, tema, dados, papel)` que devolve elementos em **milímetros**: imagem, texto com tamanho máximo e mínimo, forma com cor da paleta e linha de corte. A mesma lista vira SVG (prévia) e jsPDF (arquivo).
- **Ajuste de texto idêntico nos dois lados.** Uma tabela de larguras de glifo por fonte (Latin-1: á é í ó ú ñ ü ¡ ¿) alimenta um `fitText()` compartilhado. Assim o nome quebra no mesmo lugar na prévia e no PDF.
- **Arte por tema:** 4–5 PNG com transparência (ilustração principal, 2–3 stickers, 1 ícone). Fundos, molduras, bandeirinhas e confete são vetor desenhado em código com a paleta. Dá **~32–40 ilustrações** no total (8 temas), não as 160–240 artes que a Fase 3 estimou. Fontes OFL/Apache do Google Fonts.
- **Papel.** Carta no MX, CO e parte da América Central; A4 na AR, PE e boa parte da América do Sul; o CL aparece nas duas listas ([convertica](https://convertica.net/es/blog/a4-vs-us-letter-printable-sizes/), [ariapsa](https://ariapsa.com/tamanos-de-papel-mas-usados-a4-vs-carta-mexico/)). A área útil comum é de 190 × 259 mm, com margem ≥ 10 mm.
- **Fora do MVP:** cajitas, wrapper de chocolate e painel gigante, porque exigem faca e variam por país. Vão para o upsell da v1.1.

**Telas:**
1. Landing `/es`: vídeo do nome aparecendo nas 7 peças, fotos de um kit impresso "Ejemplo", chips dos 8 temas, CTA "Crea tu kit gratis y míralo antes de pagar", FAQ (impressão, Carta/A4, meios de pagamento, cargo "HTM*", entrega).
2. Onboarding 1, tema: grade de 8 × 2 paletas, com miniatura ao vivo.
3. Onboarding 2, dados + e-mail.
4. Editor: formulário + prévia SVG por peça em carrossel, foto opcional, seletor Carta/A4.
5. Prévia do kit com marca d'água e a barra "Descargar mi kit", sem timer e sem preço riscado.
6. Checkout Hotmart com B1, B2 e B3 (kit e variante do A/B no parâmetro de rastreio do checkout).
7. Obrigado / descarga: link HTTPS direto, PNG, instruções e aviso para o navegador interno.
8. Painel "Mis kits".
9. Edição pós-compra dentro da trava; regenera o PDF.
10. Editor do convite web (B1).
11. Convite público (B1): envelope → nome e idade → contagem → foto → local com Google Maps/Waze → "Confirmar por WhatsApp" → rodapé "Crea el kit de tu peque". Com `noindex` e link "Reportar".
12. Convite expirado.
13. Entrega dos bumps no painel: selo do convite, saldo de créditos, selo da licença.
14. Recuperar acesso, Termos, Privacidade e `/es/licencia`.
15. Admin: painel, A/B, órfãos, carrinhos abandonados, "tirar do ar", contador de gerações por e-mail.

**Reaproveitado do Mimo (em nível funcional):** o fluxo editor → página → Hotmart (cria grátis, vê a prévia, paga, recebe). O motor de peças, o PDF multipágina, a trava de kit e os créditos são novos.

**Não levar:** marca, ofertas e dados do Mimo.

**Privacidade:**
- a foto é opcional e é apagada 30 d depois da festa;
- rascunhos sem compra são apagados em 30 d;
- a lei de dados de cada país (ex.: LFPDPPP no MX) não foi verificada.

**Cronograma (uma pessoa, D1 = 23/09/2026):**

| Dia | Entrega | Pronto quando |
|---|---|---|
| D1 | Projeto base, Knowledge com as restrições, marca e domínio. **Criar front + B1 + B2 + B3 na Hotmart** (entram em análise). Guia de estilo dos 2 primeiros temas | Projeto só em ES, sem dado do Mimo; produtos enviados |
| D2 | **Spike técnico (decide o resto):** 1 tema e 3 peças (invitación, toppers, banderín com nome longo), TTF com ñ/á/¡/¿, PNG em alta, Carta e A4, gerado no servidor do Lovable. Impressão real a 100% | PDF de 15 páginas em < 10 s e < 8 MB, com a medida certa na régua. Se falhar, plano B no navegador |
| D3 | Arte: 8 temas × 4–5 ilustrações (IA + curadoria + remoção de fundo + checklist de PI) | 32–40 arquivos aprovados. **Otimista:** o próprio build estima ~1,5 dia de curadoria |
| D4 | Onboarding + editor + renderizador SVG ao vivo + `fitText()` | Digitar o nome atualiza as peças do spike no celular em < 100 ms |
| D5 | Peças 1–7 + página 0 nos dois renderizadores; 2 paletas | Prévia = PDF, lado a lado |
| D6 | **Teste de impressão nº 1:** kit inteiro em Carta e A4, em 2 impressoras domésticas; cortar e montar | Quadrado de 5,0 cm; topo, toppers e banderín montados |
| D7 | Checkout + webhook: front, bumps, A/B; pago → PDF → link no clique; reembolso → revogação; OXXO → pendente | Compra de teste libera tudo; reembolso apaga o PDF |
| D8 | Obrigado com navegador interno, PNG, painel, créditos, trava de edição, limite de gerações, `/es/licencia` | 2º kit por crédito sem pagar; 4ª troca de nome bloqueada |
| D9 | B1: editor + página pública do convite + OG + QR na invitación + expiração | O link abre bonito no WhatsApp |
| D10 | Landing, FAQ, termos, e-mails, limpeza de rascunhos e fotos | Textos sem promessa de renda, de tempo ou "+10.000", e sem personagem |
| **D11** | **QA de ponta a ponta:** compra real com cartão em 2 países + OXXO, reembolso real, bump órfão, download no navegador interno do Instagram, do Facebook e do WhatsApp (iOS e Android), impressão nº 2 numa gráfica rápida | **MVP vendável (~03/10) pelo plano do build** |
| D12 | Kits-demo "Ejemplo" impressos e filmados; gravação de tela → fábrica de criativos. Controle L09 no Canva, como produto Hotmart separado | 10–15 variações; controle enviado |
| D13 | Soft launch (05/10), braço gerador + braço controle | Primeiras vendas liberadas sem intervenção |
| D14 | Folga | — |

**Dias até o MVP:** o build planeja o MVP vendável no D11. Com o D3 realista (~1,5 dia de arte), conte com o **D12**. O **D14 é o limite**, e o D21 é o ponto de parada (Portão 0, na última seção). A estimativa de 7–10 dias da pesquisa fica superada.

**Riscos técnicos e mitigação:**

| Risco | Mitigação |
|---|---|
| Arte incoerente ou parecida com personagem licenciado | Guia de estilo por tema; checklist de PI (prompt sem personagem, marca ou estúdio; revisão humana; busca reversa por amostragem); sem campo de "tema livre" nem geração por IA a pedido. Se o D3 atrasar, lançar com 5 temas |
| Impressão fora de escala ("Ajustar a página") e margem não imprimível | Página 0, quadrado de 5 cm em toda página, área útil comum, testes no D6 e no D11 |
| Limites do servidor do Lovable para PDF com imagens (não verificados) | Spike no D2. Plano B: gerar no navegador de quem pagou. Isso protege menos a arte, e o upload pelo 4G leva 10–30 s [estimativa] |
| Download no navegador interno do Instagram no iOS: o blob falha ([FileSaver #754](https://github.com/eligrey/FileSaver.js/issues/754), [flyn.to](https://www.flyn.to/blog/instagram-in-app-browser)) | Nunca usar blob para o PDF: link HTTPS assinado com `download`, aviso "Abrir en navegador" e link por e-mail |
| Acentos e fontes | TTF OFL embutido; testar "Sofía Ñañez ¡5 añitos!" no D2 |
| Prévia ≠ PDF | Tabela de glifos única, margem de 8%, comparação lado a lado no D5 |
| Nomes longos ("María José Valentina") | `fitText` com 2 linhas; banderín só com o nome ou com o apelido |
| Aprovação da Hotmart (prazo não verificado) | Criar os produtos no D1; se os bumps atrasarem, lançar só com o front |
| Regressão no webhook causada pelo agente do Lovable | Knowledge fixa, `get_diff` em toda mudança nesses arquivos, repetir o teste de compra do D11 |

**Corte de escopo se atrasar (nesta ordem):**
1. controle L09 (sem código; pode entrar na semana 3);
2. B1 → v1.1 (o produto perde o diferencial contra o pack, então volta com prioridade);
3. 8 temas → 5, e 2 paletas → 1;
4. 7 peças → 5 (saem a etiqueta de garrafinha e o número gigante);
5. foto opcional;
6. A/B de preço → preço único.

**Nunca cortar:**
- webhook idempotente com 200 sempre;
- reembolso → revogação;
- download por link HTTPS;
- página 0 e teste de impressão real;
- checklist de PI;
- marca d'água na prévia e arte em alta fora do navegador;
- página de licença;
- ausência de timer e de preço riscado.

**Custo marginal por venda [estimativa]: ~US$ 0,01–0,02 de infraestrutura, com pior caso de ~0,05.**
- **Premissas:** 10–20 visitantes do editor por venda (conversão editor → compra não verificada), ~1 MB de prévia por visitante, PDF de ~5 MB, até 3 gerações e 3 downloads, e o B1 com ~100 visualizações a 20% de adesão.
- **Condições:** só vale com prévia em WebP leve, limite de gerações e limpeza de rascunhos e fotos.
- **O que fica fora:** o CPU da geração no servidor não foi verificado (calibrar com a fatura do Lovable Cloud ÷ vendas do mês, depois do lançamento). **O suporte de impressão também não entra:** é tempo humano.
- **Custo fixo:** ilustrações. São ~320 imagens geradas × US$ 0,02–0,08 (preço não verificado) ≈ US$ 6–26, mais ~1,5 dia de curadoria. Cada tema novo custa ~US$ 1–3 e ~2 h.

## Criativo: 15 ganchos em espanhol, 5 formatos, 30 variações/semana

**Princípio:** o anúncio vende o nome da criança aparecendo nas 7 peças e, em seguida, a mesa impressa de verdade.
- 3 dos 5 formatos são só demonstração: gravação de tela, peças renderizadas pelo **mesmo motor do produto** (`kit-engine` no Remotion) e kit impresso real com o selo "Ejemplo". O que o vídeo mostra é o que o PDF entrega.
- 2 formatos usam uma **apresentadora virtual com o rótulo "Presentadora virtual · IA"**, que demonstra e nunca finge ser mãe nem cliente.
- **Nenhum rosto de criança**, real ou de IA. A "reação" é a revelação da mesa, a mão pondo o topo no bolo e o som "pop" a cada peça que ganha o nome.
- **O vídeo não mostra preço.** Com o A/B sorteado na landing, metade do tráfego veria um preço diferente.
- **A mesa só mostra o que o kit inclui.** Onde ainda não houver impressão, a cena leva o selo "Montaje ilustrativo" (peças reais sobre um fundo de mesa sem pessoas).

**Ângulos com evidência [medido; proxy].** Nos 50 anúncios mais novos do DecoKit no filtro UY/BO/GT/DO, 39 têm ≥ 30 d ([DecoKit no UY](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=UY&view_all_page_id=737352542803130&search_type=page); o link reproduz um país, e o filtro de quatro países foi feito via API em 22/09/2026):

| Ângulo | Anúncios com ≥ 30 d | Exemplo |
|---|---|---|
| Curiosidade | 14 | ["El secreto no era una decoradora"](https://www.facebook.com/ads/library/?id=1622827009278039) (9 anúncios, 42,9 d); ["Nadie te cuenta esto sobre las fiestas infantiles"](https://www.facebook.com/ads/library/?id=962067306718766) (118,1 d) |
| Objeção de design | 5 | ["Deja de diseñar todo desde cero"](https://www.facebook.com/ads/library/?id=1009636068162962) (116,3 d) |
| Renda | 5 | ["Empieza a vender sin saber diseñar"](https://www.facebook.com/ads/library/?id=1373901138093140) (133,1 d) |
| Emoção | 4 | ["La mejor parte es ver su carita"](https://www.facebook.com/ads/library/?id=2020782765482199) (136,0 d) |
| Tema | 3 | ["Tenemos la temática favorita de tu peque"](https://www.facebook.com/ads/library/?id=2779896019055999) (136,6 d) |
| Outros | 8 | ["No es un kit cualquiera"](https://www.facebook.com/ads/library/?id=1039503565182532) (88,0 d) |

No MX, o ângulo de negócio pesa ~2× isso (26–29%, na seção Comprador). **13 dos 15 ganchos são de uso próprio.** Os 2 de revenda vendem só a ferramenta, numa célula com ≤ 15% da verba e só com o B3 no ar. O motivo não é a longevidade, e sim o risco de política (E2) e de reembolso desse público [inferência].

**15 ganchos (0–3 s).** Regras:
- texto de tela com ≤ 8 palavras; voz com ≤ 9;
- nome fictício, selo "Ejemplo" e nenhum personagem. Nomes que coincidem com personagem (Elsa, Moana, Ariel, Mirabel) ficam fora;
- **nenhuma promessa de tempo** até o QA medir;
- "listo hoy" só vale para pagamento aprovado na hora. O end card leva sempre "Se entrega al confirmarse el pago".

| # | Ângulo | Uso | Texto de tela (ES) | Voz 0–3 s (ES) | Evidência / condição |
|---|---|---|---|---|---|
| H01 | Demo | próprio | Escribe su nombre y mira toda la fiesta | "Escribe su nombre… y mira lo que pasa." | Hipótese central; não há gerador anunciando em ES. Fora de ES, Magic Deco ["It's an APP!"](https://www.facebook.com/ads/library/?id=4475514232660841) (1,2 d) |
| H02 | Curiosidade | próprio | Nombre, edad y tema. Mira lo que sale. | "Tres datos: nombre, edad y tema. Mira." | Curiosidade é o ângulo com mais anúncios ≥ 30 d ([118,1 d](https://www.facebook.com/ads/library/?id=962067306718766)) |
| H03 | Tema favorito | próprio | ¿Le encantan los {tema}? | "¿Le encantan los dinosaurios? Mira su fiesta." | [136,6 d](https://www.facebook.com/ads/library/?id=2779896019055999). `{tema}` só entre os temas do produto, nunca personagem |
| H04 | 1º ano | próprio | Su primer añito, con su nombre en todo | "Su primer añito, con su nombre en todo." | **Sem evidência:** ["primer añito kit imprimible"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=primer%20a%C3%B1ito%20kit%20imprimible&search_type=keyword_unordered) = 0 anúncios (o link reproduz um país; a busca original somou vários países de ES + US via API em 22/09/2026). É exploração |
| H05 | Em casa | próprio | Cumple en casa: así queda la mesa | "Cumple en casa: así queda su mesa." | ["Así armé esta fiesta desde casa"](https://www.facebook.com/ads/library/?id=1574986933976057) (97,1 d), aqui em voz de marca, não em 1ª pessoa |
| H06 | Emoção | próprio | Imagina su carita al ver su nombre | "Imagina su carita cuando vea su nombre en todo." | [136,0 d](https://www.facebook.com/ads/library/?id=2020782765482199); [97,1 d](https://www.facebook.com/ads/library/?id=4309605869368925). Banderín na parede, sem criança |
| H07 | Data (mês) | próprio | ¿Cumple en {mes}? Tenlo listo hoy. | "¿Cumple en octubre? Tu kit, listo hoy." | Compra 1–3 semanas antes [inferência]. `{mes}` = mês de hoje + 10 d. **Medir o reembolso** |
| H08 | Última hora | próprio | ¿El cumple es este sábado? | "¿El cumple es este sábado? Imprímelo hoy." | ["Deja de dejarlo para después"](https://www.facebook.com/ads/library/?id=1541424287782653) (97,1 d). **Medir o reembolso** (festa dentro da garantia) |
| H09 | Objeção (tema) | próprio | Esta vez, el protagonista es {nombre} | "Esta vez, el protagonista es Mateo." | [127,1 d](https://www.facebook.com/ads/library/?id=1285905063665166). A moldura de foto no cartel mostra **um objeto** (ursinho, sapatinhos), nunca uma criança |
| H10 | Objeção (design) | próprio | Sin programas de diseño. Solo su nombre. | "Sin programas de diseño: solo su nombre." | [133,1 d](https://www.facebook.com/ads/library/?id=1952196192325259); [116,3 d](https://www.facebook.com/ads/library/?id=1009636068162962). Sem citar o Canva |
| H11 | Objeção (impressora) | próprio | ¿Sin impresora? Es un PDF. | "¿Sin impresora? Es un PDF: imprímelo donde quieras." | Não verificado [inferência]; o front inclui o PNG para WhatsApp |
| H12 | Objeção (confiança) | próprio | Míralo completo antes de pagar | "Lo ves completo, con su nombre, antes de pagar." | [decidetucurso](https://decidetucurso.com/hotmart-opiniones/); prévia grátis |
| H13 | Contraste | próprio | No son miles de archivos. Es su fiesta. | "No son miles de archivos: es su fiesta." | ["No es un kit cualquiera"](https://www.facebook.com/ads/library/?id=1039503565182532) (88,0 d). Nenhum concorrente nomeado |
| H14 | Vender (ferramenta) | vender | ¿Haces kits de cumple por encargo? | "¿Haces kits de cumple por encargo? Mira esto." | [133,1 d](https://www.facebook.com/ads/library/?id=1373901138093140); [Magic Deco](https://www.facebook.com/ads/library/?id=1397155619172622) (1,2 d). Só na célula REV, com o B3 no ar, sem valor cobrado |
| H15 | Vender (fluxo) | vender | Te pasan su nombre. Entregas su kit. | "Te pasan su nombre. Tú entregas su kit." | [Magic Deco](https://www.facebook.com/ads/library/?id=1575882503471281) (1,2 d). A licença cobre vender o impresso, não os arquivos |

**Removidos das versões anteriores:**
- "Listo en 2 minutos" e "en 5 minutos": tempo não medido;
- "Sin Canva": marca de terceiro;
- "Sube su foto y sale en el topper": a foto não vai no topper, e rosto de criança não pode aparecer no anúncio.

**Reserva para as semanas 2+:**
- H16 "¿Festejo en la escuela?";
- H17 "Sin decoradora: así se armó esta mesa";
- H18 "Un kit para cada hermanito" (só com o B2 no ar);
- H19 "Cambia el tema con un toque" (antes de pagar).

**Variantes por país [inferência]:**

| Locale | Tratamento | Escola | Papel | Nomes de exemplo | Exemplo |
|---|---|---|---|---|---|
| es-MX (também EC, GT, BO, DO, US) | tú | escuela / kínder | Carta | Mateo, Valentina, Emiliano, Regina | "Escribe su nombre y mira toda la fiesta" |
| es-AR / es-UY | vos | jardín | A4 | Thiago, Martina, Benjamín | "Escribí su nombre y mirá toda la fiesta" |
| es-CO | tú | colegio / jardín | Carta | Samuel, Salomé | "¿Cumple en {mes}? Tenlo listo hoy." |
| es-CL | tú | jardín / colegio | A4 ou Carta (não verificado) | Agustín, Emilia | "¿Le encantan los dinosaurios?" |
| es-PE | tú | nido / colegio (não verificado) | A4 | Luciana, Thiago | "Su primer añito, con su nombre en todo" |

**5 formatos.** Todos em 1080×1920, com versão 4:5 para o Feed. O end card traz a lista "Incluye" e a linha "Pastel, globos y dulces no incluidos · Se entrega al confirmarse el pago".

| # | Nome | Duração | Rosto | Estrutura | CTA na tela |
|---|---|---|---|---|---|
| F1 (C1) | "Escribe su nombre" | 12–15 s (corte de 10 s) | Não | Gancho → digita "Mateo", "5" → as 7 peças ganham o nome com "pop" → troca de tema na prévia → mesa impressa, com a mão pondo o topo no bolo → end card | "Míralo gratis antes de pagar" |
| F2 (C2) | "De la pantalla a la mesa" | 18–24 s | Não | Gancho → digita → imprime e recorta (selo "Acelerado") → monta → revela a mesa. O nome digitado tem de ser o do kit impresso filmado | "Míralo gratis antes de pagar" |
| F3 (C3) | "Pieza por pieza vs. una vez" | 12–15 s | Não | Tela dividida: plantillas genéricas (arte nossa), editadas de 1/7 a 7/7, contra "digita uma vez" e 7/7 com ✓. Sem marca de terceiro e sem números de tempo | "Las 7 piezas, con su nombre" |
| F4 (C4) | "Te lo muestro" | 20–25 s | IA rotulada | Close da apresentadora → ela vira círculo no canto superior sobre a demo → mesa → "Lo ves completo antes de pagar" | "Míralo gratis antes de pagar" |
| F5 (C5) | "Tres dudas" | 25–30 s | IA rotulada | 3 de 6 perguntas sorteadas (20 combinações): ¿Tienen personajes? ("No: temas originales…") / ¿Sin impresora? / ¿Sale del tamaño correcto? / ¿Y si me equivoco en el nombre? / ¿Cómo me llega? / ¿Lo puedo ver antes? | "Pago único, sin suscripción" |

- **Variantes:**
  - **C1K (controle L09):** mostra a edição de plantillas peça por peça, sem logo nem interface do Canva, porque o logo do Canva em publicidade é reservado a licenciados ([diretrizes do Canva](https://s3.amazonaws.com/static-cse.canva.com/pages/media-kit/Guidelines+for+Using+Canva+Trademarks.pdf)).
  - **C2R e C4R:** versões de revenda do F2 e do F4.
- **Peso da IA.** Os formatos com IA ficam em ~20% do volume, com teto de 8 por semana. Motivos:
  - a Meta aplica o rótulo "AI info" ([Meta](https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/));
  - um estudo mediu queda de 31,5% no CTR com aviso de IA ([NYU Stern](https://www.stern.nyu.edu/experience-stern/faculty-research/ai-advertising-paradox)), e outro não achou efeito ([MediaScience](https://www.marketingdive.com/news/ai-disclosure-labels-dont-hurt-ad-performance-heres-what-the-numbers-say/822711/)).

**30 variações por semana.** Os módulos:
- 15 ganchos, mais ~3 novos por semana (vindos dos comentários e dos títulos novos do DecoKit e da Magic Deco, checados por `page_ids` toda segunda);
- 5 corpos + C1K, C2R e C4R;
- 4 eventos: CUM (genérico), A1 (primer añito), CASA e ESC;
- 8 temas × 2 paletas;
- nome e idade da criança por país;
- 6 locales: MX, AR, CO, CL, PE, US;
- com ou sem apresentadora.

São ~480 anúncios distintos antes de paleta, criança e país [estimativa]. **O limite real é o gancho, não a combinação.** A troca de tema é o antídoto de fadiga mais barato: re-renderiza o anúncio sem gravar nada.

**Semana 1 (S41, 05–11/10), 30 anúncios.** Temas impressos no D12: DIN, UNI, ESP e OSO, os mesmos 4 do controle.

| Bloco | Nº | Anúncios |
|---|---|---|
| Teste de mecanismo: gerador | 5 | H03, H04, H05, H06 e H08 no C1 (DIN, OSO, UNI, ESP, DIN), MX |
| Teste de mecanismo: controle L09 | 5 | Os mesmos 5 ganchos no C1K, mesma verba e mesmo público |
| Exploração de gancho no C1 | 6 | H01, H02, H07, H09, H10, H12 |
| Pantalla → mesa (C2) | 3 | H11, H02, H05 |
| Contraste (C3) | 2 | H13, H10 |
| Apresentadora (C4) | 3 | H01, H03, H09 |
| Dúvidas (C5) | 2 | H12, H11 |
| Localização | 2 | H01 AR (voseo, A4) · H03 CL |
| Revenda (campanha própria, ≤ 15% da verba) | 2 | H14 no C2R · H15 no C4R |

Os ganchos do teste de mecanismo não dependem do mecanismo nos primeiros 3 s. O texto é idêntico nas duas células; só o corpo muda. Os 15 ganchos aparecem na semana, e o balanço é de 24 anúncios sem rosto e 6 com IA.

**Da semana 2 em diante:**

| Bloco | Nº | Regra |
|---|---|---|
| Iteração de gancho | 6 | O melhor anúncio da semana com 6 ganchos trocados |
| Iteração de corpo | 6 | Os 2 melhores ganchos × 3 corpos novos |
| Exploração | 6 | 3 ganchos novos × C1 e C2 |
| Fadiga visual | 4 | Os 2 melhores com a paleta `b` e 1 tema novo (só re-render) |
| Localização | 4 | Vencedores levados para AR, CO, CL/PE e US |
| Controle / revenda | 4 | O controle segue até o teste fechar; depois essas vagas vão para exploração. A revenda fica com 2 vagas e as devolve ao B2C se não tiver vencedor em 2 semanas |

**Pipeline:**
- **Peças:** `kit-engine` copiado do produto para o Remotion (`KitPiece`, `KitGrid`, `KitMockup`), com as mesmas fontes, conferido contra um PDF real.
- **Tela:** gravação nativa no celular, ou a rota `/demo` capturada por Playwright, que é pedido ao build (~0,5 dia; a qualidade do Playwright não foi verificada).
- **Físico:** 5 clipes por tema (`print`, `cut`, `assemble`, `reveal`, `detail`), com o logo da impressora coberto e nenhum objeto com personagem no quadro.
- **Voz e legenda:** TTS por locale; legendas com `toCaptions()` + `createTikTokStyleCaptions()` ([Remotion](https://www.remotion.dev/docs/captions/api)).
- **Apresentadora:** um rosto sintético genérico, checado por busca reversa, sem remover os metadados C2PA.
- **Música:** só da [Meta Sound Collection](https://www.facebook.com/sound/collection/terms), com licença válida só para Facebook e Instagram. Nunca gravação comercial de "Las Mañanitas".
- **Montagem:** planilha semanal da matriz → script que monta as propriedades de cada vídeo (valida as regras) → render em lote → pós-processamento com ffmpeg (trilha, loudness, capa).

**QA antes de subir (qualquer "sim" barra o anúncio):**
1. Valor de ganho, "negocio", "emprende" ou "ingresos"?
2. Escassez ou urgência de oferta?
3. Personagem ou coisa parecida, marca FIFA ou logo de terceiro?
4. Rosto de criança?
5. IA sem rótulo, ou falando como mãe ou cliente?
6. Item que o kit não inclui, sem o aviso "no incluido"?
7. Promessa de tempo ou "sin esfuerzo"?
8. "Gratis" sem "antes de pagar"?
9. Nome na tela diferente do nome do kit filmado, ou falta o selo "Ejemplo"?
10. Música sem licença?
11. Atributo pessoal?
12. Interface falsa?
13. Promessa que o produto não cumpre: foto no topper, troca livre de tema, entrega imediata em pagamento em dinheiro?
14. Gancho de revenda fora da célula REV?

**Nomenclatura (UTMify):**
- anúncio `KIT_{CEL}_{H}_{C}_{EVT}_{TEMA}{PAL}_{LOC}_{PRES}_W{AAWW}_v{n}`, ex.: `KIT_GEN_H03_C1_CUM_DINa_MX_NA_W2641_v1`;
- campanha `KIT_{CEL}_{OBJ}_{AAWW}`;
- conjunto `KIT_{CEL}_{PAISES}_{PUBLICO}`;
- CEL = GEN, CTL ou REV;
- a variante de preço vai no parâmetro de rastreio do checkout, não no nome;
- não renomear anúncio no ar.

**Regras de pausa (corrigidas pelo red team)** [estimativa; conta BRL]. O criativo usava o CPA de ROI 1,5 do cenário conservador (3,68), o que gera falsos cortes com pixel novo. A régua passa a ser o **CPA de break-even**:

| Preço no ar | CPA de break-even (BRL) | Pausar o anúncio com gasto sem venda ≥ |
|---|---|---|
| US$ 7,90 | 6,24 | US$ 12,48 |
| US$ 9,90 | 7,77 | US$ 15,54 |

- Pausar também depois de ~1.000 impressões, se o hook rate estiver no terço inferior da semana.
- No teste de mecanismo, não pausar anúncios individuais nos primeiros 7 dias: a decisão é por célula.
- O "teto de perda de US$ 221/semana" do criativo **não é teto de perda**: ignorava o gasto nos anúncios que sobrevivem. O teto de aprendizado vem dos portões da última seção.

**Teste gerador × controle.** A regra que vale é a do Portão 4, na última seção. Com 40–50 compras por braço, o teste só detecta diferença de CPA ≥ 1,48–1,55×. **Ele mostra direção, não prova.**

**Calendário:**

| Semanas | O que fazer |
|---|---|
| S41–S42 (05–18/10) | Lançamento + teste de mecanismo. O H07 se ajusta sozinho ("octubre" → "noviembre") |
| S43–S44 (19/10–01/11) | Tema "Monstruitos" (genérico). Nada parecido com Monsters Inc., Coco ou Hotel Transylvania. Demanda não verificada |
| S45–S47 | Rotina, com checklist de PI em cada tema novo |
| S48 (Black Friday, 27/11) | Não escalar nem subir teste: CPM 2–3× maior (dados dos EUA: [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics); LATAM não verificado) |
| S49–S52 | Rotina; tema de inverno para aniversários de dezembro (hipótese) |
| 28/12–10/01 | CPM barato (dados dos EUA: [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics); LATAM não verificado), mas o MX tem menos aniversários em janeiro: não escalar só pelo CPM. **Nunca "cuesta de enero"** |
| Fev–mar/2027 | Reforçar a CO, onde março foi o 1º mês em nascimentos em 2023 e 2024 ([DANE](https://www.dane.gov.co/files/operaciones/EEVV/2024/19-dic-2024/bol-EEVV-Nacimientos-2024pr.pdf)) |

## Ângulos proibidos

Valem para o vídeo, o texto, o título, a landing, a página da Hotmart e as respostas nos comentários. A Meta revisa o destino ([burla de sistemas](https://transparency.meta.com/km-kh/policies/ad-standards/deceptive-content/circumventing-systems)). Concorrente usar algo **não prova** que é permitido.

| Não pode | Exemplo proibido (ES) | Motivo | Reescrita segura (ES) |
|---|---|---|---|
| Promessa de renda ou valor por kit | "Vende cada kit en $300"; "Recupera tu inversión con un solo kit" | [Resultados irreais (Meta)](https://transparency.meta.com/en-gb/policies/ad-standards/deceptive-content/unrealistic-outcomes/); [uso responsável (Hotmart)](https://hotmart.com/en/legal/responsible-use-policy) | "¿Haces kits de cumple por encargo? Mira este editor." |
| "Negocio", "emprende", "ingresos extra", "desde casa" como renda | ["💰 ¿Y si empiezas a venderlos?"](https://www.facebook.com/ads/library/?id=2072230433424563); ["Tu negocio puede empezar con esto"](https://www.facebook.com/ads/library/?id=1477793531027394) (DecoKit) | [Fraude e golpes (Meta)](https://transparency.meta.com/policies/ad-standards/fraud-scams/fraud-scams-deceptive-practices/); eliminatória E2 | "Te pasan su nombre. Tú entregas su kit." (só na célula REV) |
| Print de ganho, notificação de venda | Extrato; "te pago $250 por el kit" | [Funcionalidade inexistente (Meta)](https://www.facebook.com/business/help/655450495896770) | Painel "Mis kits" com nomes de exemplo, sem dinheiro |
| Depoimento inventado ou em 1ª pessoa | ["Me ahorré una fortuna"](https://www.facebook.com/ads/library/?id=27008891068812716); ["⭐4,5/5"](https://www.facebook.com/ads/library/?id=1580948452926596); ["+5000 VENDIDOS"](https://www.facebook.com/ads/library/?id=3377779535705085) | [FTC (2024)](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials); art. 32 da [LFPC](https://www.profeco.gob.mx/juridico/pdf/l_lfpc_ultimo_camdip.pdf) | "Así queda una mesa armada con el kit (ejemplo)." |
| Avatar de IA como mãe ou cliente | "Lo usé para el cumple de mi hijo"; "mis clientas me encargan…" | Enganoso (digest de políticas; FTC) | "Te muestro cómo queda un kit hecho con [Marca]", com o rótulo de IA |
| Rosto parecido com famoso, influencer ou jornalista; cenário de telejornal | Avatar "inspirado" numa apresentadora | [Isca de celebridade (Meta 2024)](https://about.fb.com/news/2024/10/testing-combat-scams-restore-compromised-accounts/), [Meta 2026](https://about.fb.com/news/2026/02/meta-takes-legal-action-against-scam-advertisers/) | Rosto sintético genérico, checado por busca reversa |
| Escassez ou urgência falsa | ["¡ÚLTIMAS UNIDADES!"](https://www.facebook.com/ads/library/?id=1762121668819675) num produto digital; ["¡Pronto dejará de estar disponible!"](https://www.facebook.com/ads/library/?id=1590631305803085); cronômetro; "ANTES/HOY" sem preço anterior real | [Profeco multa ofertas falsas](https://www.infobae.com/mexico/2026/05/28/las-ofertas-falsas-saldran-caras-profeco-aplicara-multas-a-negocios-infractores-hasta-por-6-millones-de-pesos/); art. 32 da LFPC | Urgência do evento, que é real: "¿El cumple es este sábado?" |
| Personagem licenciado ou parecido | Bluey ([template na Hotmart](https://pay.hotmart.com/B103082603B)), Stitch, Disney/Pixar, Patrulla Canina, Peppa, Pokémon, Mario, Minecraft, Roblox, Spider-Man, Barbie; "temática inspirada en…"; "perrita azul" | [Copyright e marcas (Meta)](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/copyright-and-trademarks/) | "¿Le encantan los dinosaurios?"; "Esta vez, el protagonista es Mateo" |
| Marcas da Copa (tema fútbol) | "Kit Mundial", mascotes oficiais, escudo de clube ou seleção, nome de jogador | FIFA com 357 marcas no IMPI ([Milenio](https://www.milenio.com/futbol-internacional/mundial/mundial-2026-fifa-registro-cientos-de-marcas-y-productos-ante-impi), [Infobae](https://www.infobae.com/mexico/deportes/2026/05/27/esta-es-la-multa-millonaria-que-podrias-enfrentar-por-usar-marcas-y-frases-oficiales-de-la-fifa-durante-el-mundial-2026/)); [PI de terceiros (Meta)](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/third-party-infringement/) | "¿Fan del fútbol? Su fiesta, con su nombre." Bola e campo genéricos |
| Mostrar o que o kit não inclui | Mesa com cajitas, painel gigante e balões, sem aviso | "Veraz y comprobable" (LFPC); vira reembolso [inferência] | Lista "Incluye" + "Pastel, globos y dulces no incluidos" |
| Volume inflado | "+10.000 diseños"; "miles de temas" | Não comprovável; temos 8 temas | "8 temas originales"; "No son miles de archivos. Es su fiesta." |
| Tempo não medido; "sin esfuerzo" | "Listo en 2 minutos"; "fiesta lista en 5"; ["Tu fiesta WOW en menos de 60 minutos"](https://www.facebook.com/ads/library/?id=1432932032020466) | Não comprovável; num contexto de renda, é enriquecimento rápido | "Escribe su nombre y mira toda la fiesta." Minutos só depois de medir o tempo **do editor** |
| "Gratis" enganoso | "Kit gratis"; "Descárgalo gratis" | A prévia é grátis; o download é pago | "Míralo gratis antes de pagar." |
| Marcas de terceiros | Logo ou interface do Canva; "Mejor que Canva"; ["Sí, funciona con Cricut"](https://www.facebook.com/ads/library/?id=1768072504173864); logo de impressora; logo alterado de app de mensagens | [Diretrizes do Canva](https://s3.amazonaws.com/static-cse.canva.com/pages/media-kit/Guidelines+for+Using+Canva+Trademarks.pdf); [uso de marca (Meta)](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/brand-usage/); [marca WhatsApp](https://www.meta.com/brand/resources/whatsapp/whatsapp-brand/) | "Sin programas de diseño"; "invitación en imagen para compartir por mensaje" |
| Atributo pessoal | "¿No te alcanza para una decoradora?"; "¿Mamá soltera y con fiesta?"; "Cuesta de enero: ahorra en su cumple" | [Atributos pessoais (Meta)](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/) | "Imprímelo en casa o en la papelería." |
| Economia sem base | "Ahorra $2.000 en decoración" | Precisa ser comprovável (LFPC) | "Lo imprimes tú, en casa o en la papelería." |
| Menor de idade | Rosto de criança, real ou de IA; falar com a criança ("¡Pídele a mamá tu kit!") | Prudência (a regra exata da Meta não foi verificada); foto de criança é dado sensível | "Para su cumple…" (fala com o adulto); público 18+ |
| Interface falsa | "Toca aquí 👆"; play desenhado; caixa de seleção | [Funcionalidade inexistente](https://www.facebook.com/business/help/655450495896770) | A mão toca dentro do vídeo; ✓ como ícone |
| Revenda de arquivos (PLR) | "Licencia de reventa incluida"; "Derechos PLR" | [Hotmart barra PLR](https://help.hotmart.com/es/article/31594947721485/-por-que-mi-producto-no-esta-disponible-para-la-venta-); eliminatória E4 | "Licencia opcional: imprime y vende los kits impresos de tus clientas. No incluye reventa de archivos." |
| Nome ou visual de concorrente | "Fiesta Lista" ([já é página em BRL](https://www.facebook.com/ads/library/?id=1719759895753397)); "Kit Fiesta Mágica"; copiar título ou vídeo do DecoKit | [PI de terceiros (Meta)](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/third-party-infringement/) | Marca própria checada antes do D1; títulos escritos do zero |
| Música comercial | Hit infantil; gravação comercial de "Las Mañanitas" | Exige licença ([Meta](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/copyright-and-trademarks/)) | Faixa da Meta Sound Collection, com o ID no CSV |
| Esconder que é IA | Remover C2PA; recortar o rótulo | [Transparência de IA (Meta)](https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/) | Rótulo na tela + marcação no Gerenciador |

Qualquer reprovação por resultados irreais desliga a célula de revenda.

## Contas (definição de ROI explícita; AOV, líquido, reembolso, CPA de break-even, CPA para ROI 1,5)

**Definição de ROI:** faturamento líquido (depois das taxas da Hotmart e dos reembolsos) ÷ gasto em anúncios.
- **CPA de break-even** = líquido por comprador (ROI 1,0).
- **CPA para ROI 1,5** = líquido ÷ 1,5.
- **Com conta de anúncio em BRL** (o UTMify soma 12% de imposto ao gasto; é a régua provável): break-even = líquido ÷ 1,12; ROI 1,5 = líquido ÷ 1,68.

**Taxas (modelo do usuário, `_raw/calc_economia.py`):**
- **Front:** 10,95% + US$ 1,49, o que deixa ~74% a US$ 9,90 (9,90 × 0,8905 − 1,49 = 7,33).
- **Bumps:** 88% líquido.
- **Upsell:** calculado com a taxa do front; a 7,90 deixa US$ 5,55.
- **Reembolso:** aplicado sobre o líquido total. Não foi verificado se a Hotmart devolve as taxas no reembolso.

**Reembolso estimado para o nicho.**
- **Por que acima do Mimo (< 1%) [inferência]:**
  - o PDF impresso não é revogável;
  - há o risco de impressão e o "mi hijo quería X";
  - o público emprendedor reembolsa mais;
  - são três bumps.
- **Por que abaixo de um produto de renda extra [inferência]:** a prévia grátis mostra exatamente o que se compra, o ticket é baixo e não há promessa de ganho.

Premissas por segmento [estimativa]:

| Cenário | Mãe, uso próprio (~83%) | Emprendedora (~17%) | Ponderado | Usado |
|---|---|---|---|---|
| Conservador | 5% | 12% | 6,2% | **6%** |
| Base | 3% | 8% | 3,9% | **4%** |
| Otimista | 1,5% | 5% | 2,1% | **2%** |

**Ressalva do red team.** A divisão 83/17 veio de títulos de anúncio (4 de 23), não de compradores, e está subestimada para o MX (26–29%). Com a fatia do MX, o ponderado base iria a ~4,3–4,5%. O efeito no líquido a 9,90 é pequeno: 8,70 → ~8,66 [estimativa].

**Front US$ 9,90 (regime de taxas R1).** Adesões e reembolso são estimativas não verificadas. Bumps: B1 4,90 · B2 3,90 · B3 6,90.

| US$ por comprador de front | Conservador | **Base** | Otimista | Ruim (red team) | Sem bumps |
|---|---|---|---|---|---|
| Adesão B1 / B2 / B3 | 15 / 10 / 2% | 22 / 16 / 4% | 30 / 24 / 6% | 10 / 6 / 2% | — |
| Reembolso | 6% | 4% | 2% | 7% | 4% |
| **AOV bruto** | 11,16 | **11,88** | 12,72 | 10,76 | 9,90 |
| Líquido do front | 7,33 | 7,33 | 7,33 | 7,33 | 7,33 |
| Líquido dos bumps (88%) | 1,11 | 1,74 | 2,48 | 0,76 | 0 |
| **Líquido por comprador** | **7,93** | **8,70** | **9,61** | **7,52** | **7,03** |
| CPA de break-even, sem imposto / BRL | 7,93 / 7,08 | **8,70 / 7,77** | 9,61 / 8,58 | 7,52 / 6,71 | 7,03 / 6,28 |
| CPA para ROI 1,5, sem imposto | 5,29 | **5,80** | 6,41 | 5,01 | 4,69 |
| **CPA para ROI 1,5, BRL** | **4,72** | **5,18** | **5,72** | **4,48** | **4,18** |
| *Upsell (v1.1): adesão* | *4%* | *8%* | *12%* | — | — |
| *Líquido com upsell* | *8,14* | *9,13* | *10,26* | — | — |
| *CPA ROI 1,5 com upsell, sem imposto / BRL* | *5,43 / 4,84* | *6,08 / 5,43* | *6,84 / 6,11* | — | — |

**Conta do cenário base:**
- Bumps bruto: 4,90 × 0,22 + 3,90 × 0,16 + 6,90 × 0,04 = 1,078 + 0,624 + 0,276 = **1,978**.
- AOV bruto: 9,90 + 1,978 = **11,88**.
- Líquido: front 7,33 + bumps 1,978 × 0,88 = 1,74, soma **9,07**.
- Depois do reembolso: 9,07 × 0,96 = **8,70**.
- CPAs: 8,70 ÷ 1,5 = **5,80**; ÷ 1,68 = **5,18**; break-even em BRL 8,70 ÷ 1,12 = **7,77**.

**Front US$ 7,90 (mesmas adesões):**

| | Conservador | **Base** | Otimista | Ruim | Sem bumps |
|---|---|---|---|---|---|
| AOV bruto | 9,16 | **9,88** | 10,72 | 8,76 | 7,90 |
| Líquido por comprador | 6,26 | **6,99** | 7,87 | 5,86 | 5,32 |
| CPA de break-even, BRL | 5,59 | **6,24** | 7,03 | 5,23 | 4,75 |
| CPA para ROI 1,5, sem imposto / BRL | 4,17 / 3,72 | **4,66 / 4,16** | 5,24 / 4,68 | 3,91 / 3,49 | 3,55 / 3,17 |

**Sensibilidade ao preço do front (cenário base):**

| Front | Líquido do front (% do preço) | Líquido por comprador | CPA ROI 1,5, sem imposto / BRL | Conversão para empatar com o 9,90 |
|---|---|---|---|---|
| 5,90 | 3,76 (64%) | 5,28 | 3,52 / 3,15 | 1,65× |
| 6,90 | 4,65 (67%) | 6,14 | 4,09 / 3,65 | 1,42× |
| 7,90 | 5,54 (70%) | 6,99 | 4,66 / 4,16 | 1,24× |
| 9,90 | 7,33 (74%) | 8,70 | 5,80 / 5,18 | 1,00× |
| 12,90 (US) | 10,00 (78%) | 11,27 | 7,51 / 6,71 | 0,77× |

A taxa fixa pune o ticket baixo: de 9,90 para 7,90, o preço cai 20% e o líquido do front cai 24%.

**Sensibilidade ao B1 [estimativa, recalculada na `_raw/calc_economia.py`].** Com o B1 a 10% e as demais adesões no base, o líquido cai para 6,50 a 7,90 (CPA ROI 1,5 em BRL de 3,87) e para 8,21 a 9,90 (4,89). O red team citou 6,12 a 7,90, número que não fecha com os bumps da oferta.

**A taxa da Hotmart pode ter mudado em 21/09/2026 (não verificado).** Pelo digest de políticas, a taxa do Player (US$ 1,49) teria sido absorvida numa taxa fixa de US$ 1,00 ([Hotmart](https://help.hotmart.com/es/article/208298448/-cuales-son-las-tarifas-cobradas-por-hotmart-)). Não se sabe se a microtransação mudou nem se cada bump paga taxa fixa própria.

| Regime (cenário base) | Front / cada bump | Líquido por comprador a 9,90 | CPA ROI 1,5, sem imposto / BRL | Líquido a 7,90 |
|---|---|---|---|---|
| R1: modelo do usuário | 10,95% + 1,49 / 88% | 8,70 | 5,80 / 5,18 | 6,99 |
| R2: fim do Player, microtransação a 9,9% + 0,10 | 9,9% + 0,10 / igual | 10,14 | 6,76 / 6,03 | 8,41 |
| R3: US$ 1,00 fixo em toda transação, inclusive em cada bump | 9,9% + 1,00 / igual | 8,91 | 5,94 / 5,30 | 7,18 |

- **No R3, cada bump retém menos:** 3,90 → 2,51 (64%), 4,90 → 3,41 (70%), 6,90 → 5,22 (76%).
- **Como confirmar:** abrir o detalhe da primeira venda real (front + bump).
  - Se for R3, subir o B2 para 4,90.
  - Se for R2, refazer o A/B de preço, porque o 7,90 ganha força.
  - Até lá, as contas usam o R1.

**Controle L09 (pack Canva, só com a licença a 6,90 e 4% de adesão, 4% de reembolso):**
- A 9,90: (7,33 + 6,90 × 0,04 × 0,88) × 0,96 = **US$ 7,27 por comprador**. O gerador base (8,70) rende 1,20× isso.
- A 7,90: **US$ 5,56**. O gerador base (6,99) rende 1,26× isso.
- Para o mesmo ROI, o gerador pode ter um CPA 20–26% maior que o do controle.

**Contra o Mimo** (~9,4 de líquido; CPA para ROI 1,5 de ~6,27 sem imposto e ~5,60 em BRL):
- O L67 base a 9,90 fica em **93%** do Mimo (conservador 84%, otimista 102%). Só o upsell (v1.1) leva o base a ~97%.
- A 7,90, o CPA precisa ficar **~26% abaixo** do que o Mimo tolera (4,16 contra 5,60). A pesquisa dizia ~14%, com 4 bumps otimistas; está corrigido.
- **Não há folga para pagar CPA maior que o do Mimo.**

## Teto (gasto diário sustentável, premissas, faixa de confiança, comparação com o Mimo Gift)

**Conta de baixo para cima [estimativa].** Multiplica quatro premissas não verificadas, então serve como **ordem de grandeza**, não como previsão.

| Etapa | Valor | Base |
|---|---|---|
| Crianças de 1 a 8 anos no MX | ~14,5 M | 1.672.227 nascimentos em 2024 ([INEGI](https://www.inegi.org.mx/app/saladeprensa/noticia/10237)), com coortes anteriores maiores; soma não verificada |
| × % com festa decorada | 30% → 4,35 M festas/ano ≈ 11.900/dia | Chute |
| × % que compra decoração digital paga | 2 / 4 / 7% → 238 / 477 / 834 por dia no MX | Chute |
| × 1,95 (resto da LATAM em ES = 0,8× o MX; hispanos nos EUA = 0,15×) | 465 / 930 / 1.627 por dia | Mesma conta do L02 |
| × 1,17 (emprendedora e confeitera) | **544 / 1.088 / 1.903 compradores pagos/dia** | Proxy de títulos |
| × participação nossa de 3 / 6 / 12% × CPA de ROI 1,5 (5,29 / 5,80 / 6,41) | **~US$ 86 / 378 / 1.464 por dia** | Faixa de 17×: mostra só que o tamanho bruto não é o limite |

**Por que o teto fica abaixo da conta:**
1. **O público em compra é estreito.** São 11.900 festas/dia × ~14 dias de antecedência × ~1,2 decisor ≈ 200 mil pessoas, ~0,2% dos 93,5 M de usuários do Facebook no MX ([DataReportal](https://datareportal.com/reports/digital-2026-mexico)); com janela de 4 semanas, ~0,4% [estimativa]. O L02 fica em ~1,1% [estimativa], e o Mimo fala com qualquer pessoa num relacionamento, em qualquer dia [inferência]. O pack "10.000 diseños" vende "por si acaso" a um público mais largo; o gerador pede um filho, um nome e uma festa [inferência].
2. **Abre mão da alavanca mais longeva do nicho, a temática:** 8 temas contra centenas e nenhum personagem. A perda de conversão não foi medida.
3. **O leilão está denso.** O DecoKit tem 102 anúncios ativos no MX ([página no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&view_all_page_id=737352542803130&search_type=page)), em lotes de 9 a 12, e há ~11 operadores em BRL em ["papelería para fiestas"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=papeler%C3%ADa%20para%20fiestas&search_type=keyword_unordered) [medido; o link reproduz um país, e a busca original somou 11 países via API em 22/09/2026].
4. **O gerador não tem validação em ES.** É o maior desconto de confiança.
5. **Não há vantagem de lance:** o líquido base (8,70) é menor que o do Mimo (~9,4).

**Estimativa final, só espanhol, régua em BRL (CPA 5,18 a 9,90):**

| Faixa | Gasto/dia | Compradores/dia (gasto ÷ 5,18) | Participação implícita (base 1.088/dia) | Confiança |
|---|---|---|---|---|
| Piso | **US$ 100** | ~19 | ~1,8% | **Baixa.** Só sobe para média depois de um teste com CPA ≤ 5,18 e o gerador não perdendo para o controle |
| **Base** | **US$ 200** | ~39 | ~3,6% | **Baixa** |
| Topo | **US$ 350** | ~68 | ~6,2% | **Baixa** |
| Nível do Mimo | ≥ US$ 506 | ≥ 98 | ≥ 9% | **Muito baixa** sem PT-BR e sem o L02 no mesmo motor |

- **A 7,90** (CPA-alvo de 4,16), os mesmos US$ 200/dia exigem ~48 compradores/dia.
- **Margem sobre a mídia a ROI 1,5:** US$ 200/dia deixam ~US$ 100/dia, antes de ferramentas e impostos. O Mimo, a US$ 506/dia, deixaria ~US$ 253/dia [estimativa].
- **Laço viral** (rodapé do convite B1) [estimativa]: 22% × ~100 visualizações × 1% de clique × 3–5% de compra ≈ 0,007–0,011 venda extra por venda. É desprezível; não contar com ele.

**Distribuição da base de US$ 200/dia [estimativa]:**

| País | % | US$/dia | Observação |
|---|---|---|---|
| MX | 45% | 90 | Carta; OXXO; mais nascimentos em ago–out ([INEGI via El Informador](https://www.informador.mx/mexico/Este-es-el-mes-en-el-que-nacen-mas-bebes-en-Mexico-cada-ano-20250926-0076.html)) |
| AR | 12% | 24 | **Exploratório:** o líder tem 0 ativos na AR. A4; USD + conversão de 9,5% |
| CO | 12% | 24 | **Exploratório:** 0 ativos do líder no filtro AR + CO; CO isolada não verificada. Carta; PSE/Efecty |
| PE | 10% | 20 | A4; PagoEfectivo; [Diseños premiun](https://www.facebook.com/ads/library/?id=2845888295783849) (PEN, 23,1 d) |
| CL | 10% | 20 | Maior renda; pack a CLP 3.500 no mercado |
| EC, GT, DO | 5% | 10 | USD; sem dados de público |
| US (hispanos) | 6% | 12 | Front de 12,90; CPM alto |

AR e CO começam com um conjunto de teste (US$ 20–40/dia) e só recebem a fatia da base se passarem na régua. Até lá, essa verba fica no MX.

**Sazonalidade: demanda basicamente perene** [medido + estimativa]. No MX, o mês com mais nascimentos é setembro (9,4%) e o com menos, fevereiro (7,3%) ([El Informador, com dados do INEGI](https://www.informador.mx/mexico/Este-es-el-mes-en-el-que-nacen-mas-bebes-en-Mexico-cada-ano-20250926-0076.html); [Notigram](https://notigram.com/mexico/nacional/septiembre-el-mes-de-los-nacimientos-en-mexico-segun-el-inegi-20250926-1563636)), contra média de 8,33%: amplitude de +13% / −12%. O CPM sobe no Q4 (novembro +41% e Black Friday 2–3× nos EUA; [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics); LATAM não verificado). **O efeito líquido não foi medido.** A pesquisa dizia que a sazonalidade "favorece o Q4"; está corrigido. Os anúncios de mãe e tema do DecoKit atravessam mai–set ([136,6 d](https://www.facebook.com/ads/library/?id=1964080760865418)).

| Período | Fator sobre a base [estimativa] | Motivo |
|---|---|---|
| Out até 20/nov | ~1,1× | Aniversários de set–out; lançar e validar aqui |
| Semana da Black Friday | ~0,6× | CPM 2–3× maior (dados dos EUA: [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics); LATAM não verificado) |
| Dezembro | ~0,8× | Nascimentos acima da média, mas o Natal compete e o CPM fica alto |
| 26/dez a jan | ~1,0× | CPM 40–60% menor até ~15/01 (dados dos EUA: [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics); LATAM não verificado), mas janeiro tem menos nascimentos |
| Fevereiro | ~0,9× | Mês com menos nascimentos no MX |
| Mar–jul | ~1,0× | Base perene; Día del Niño no MX em 30/abr (não verificado para kit) |
| Ago–set | ~1,1× | Nascimentos acima da média |

**Outros idiomas (medições de 22/09/2026):**

| Idioma | Evidência (ACTIVE) | Acréscimo [estimativa] | Confiança |
|---|---|---|---|
| PT-BR | ["kit festa personalizado"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=kit%20festa%20personalizado&search_type=keyword_unordered) = 859, quase tudo físico ou local; ["kit festa digital editável"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=kit%20festa%20digital%20edit%C3%A1vel&search_type=keyword_unordered) = 22, com [Canva para Negócios](https://www.facebook.com/ads/library/?id=2093728848165766) (82,1 d) e [Letícia](https://www.facebook.com/ads/library/?id=849007734605966) (93,4 d); ["mesversário"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=mesvers%C3%A1rio&search_type=keyword_unordered) = 1.167, quase tudo físico ([Dolce](https://www.facebook.com/ads/library/?id=1397846729169307)). O mesversário repete todo mês e combina com o B2 [inferência; demanda digital não verificada]. Contra: âncora de R$ 3,99–9,90 | +US$ 50–150/dia | Baixa |
| EN | ["birthday party printable"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=birthday%20party%20printable&search_type=keyword_unordered) = 26 (US, GB, CA e AU; o link reproduz os US, e a soma foi feita via API em 22/09/2026); só [Magic Deco](https://www.facebook.com/ads/library/?id=2467686010427034) e [DECO MAGIC](https://www.facebook.com/ads/library/?id=952159290624190), com ~5 d; o resto é Etsy orgânico | +US$ 0–75/dia | Baixa |
| FR | ["kit anniversaire à imprimer"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=FR&q=kit%20anniversaire%20%C3%A0%20imprimer&search_type=keyword_unordered) = 4 (FR, BE, CA e CH; o link reproduz a FR, e a soma foi feita via API em 22/09/2026); [Idées de Fêtes, "Kit anniversaire pirate à son prénom"](https://www.facebook.com/ads/library/?id=985996551191139) (~0,9 d); [DECO MAGIC KIT](https://www.facebook.com/ads/library/?id=1377762184340736) (4,6 d). Garantia mínima de 15 dias na UE | +US$ 0–50/dia | Muito baixa |

**Total com todos os idiomas: US$ 150–600/dia, confiança baixa.**

**Com o L02 no mesmo motor:** L02 base (US$ 250/dia) + L67 base (US$ 200/dia), menos 15–25% de sobreposição de público, dá **~US$ 350–400/dia somados** (topo de ~600–750) [estimativa]. **Só somando os dois, e com PT-BR, o motor compartilhado chega perto do Mimo** [inferência].

**Comparação com o Mimo Gift:**

| | Mimo Gift | L67 (estimativa) |
|---|---|---|
| Gasto/dia | > R$ 2.600 ≈ US$ 506+ (dado do usuário) | ES: US$ 100–350 (base 200); com PT/EN/FR: 150–600 |
| Líquido por comprador | ~US$ 9,4 | 7,93–9,61 a 9,90 (base 8,70); 6,99 a 7,90 |
| CPA para ROI 1,5, sem imposto / BRL | ~6,27 / ~5,60 | 5,80 / 5,18 (base, 9,90) |
| Reembolso | < 1% | 2–6% (base 4%) |
| Gatilho | Impulso emocional, qualquer dia | Impulso dentro de uma janela: festa nas próximas semanas |
| Público em compra | Amplo [inferência] | ~0,2–0,4% do Facebook MX em cada momento |
| Concorrência | Não medida aqui | DecoKit (160 ativos; 102 no MX), rede Magic Deco/Deco Mundo, ~11 operadores BRL, Canva grátis |
| Vantagem própria | — | Demanda-mãe perene e a mais longeva medida em ES; motor compartilhado com o L02 |

**Veredito: o teto do L67 é MENOR que o do Mimo, ~20–70% dele em espanhol (base ~40%).** O que faria o L67 passar o Mimo, em ordem de probabilidade:
1. o gerador vencer o controle com CPA ≤ US$ 4,3 escalando (ROI ≥ 2,0);
2. B1 + B2 somando ≥ 50% de adesão (AOV ≥ 12,7);
3. PT-BR com mesversário dentro da régua;
4. a célula emprendedora escalar sem que o reembolso passe de 6%.

## Concorrentes diretos (links)

Medição na Biblioteca de Anúncios, só ACTIVE, em 22/09/2026. O ID de cada página leva à Biblioteca sem filtro de país; os filtros de um país se reproduzem trocando `country` no link, e os de vários países (UY/BO/GT/DO, AR + CO) foram feitos via API em 22/09/2026. "Mais antigo" é o anúncio ativo mais antigo visível. Em páginas com mais de 50 ativos, é limite inferior. A moeda é a da conta de anúncio, não a do país de entrega.

| Página / produto | Moeda | Ativos | Mais antigo (d) | Preço | Ângulo / nota |
|---|---|---|---|---|---|
| **DecoKit Shop** ([737352542803130](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=737352542803130&search_type=page)), +10.000 designs Canva | USD | **160**; **102 no MX**; 55 em UY/BO/GT/DO; **0 na AR** | **136,6** (limite inferior) | Não verificado | Os 2 mais antigos são de temática ([136,6 d](https://www.facebook.com/ads/library/?id=1964080760865418), [127,1 d](https://www.facebook.com/ads/library/?id=1285905063665166)). Negócio: 13% (UY/BO/GT/DO) a 26–29% (MX). **Já roda a demo do gerador e o reuso:** ["Solo cambió un nombre"](https://www.facebook.com/ads/library/?id=2009114323127277) (39,2 d), ["No es para una sola fiesta"](https://www.facebook.com/ads/library/?id=918283787405166) (38,7 d). Criativos em lotes de 9 a 12 a cada poucos dias |
| **Mundo Creativo Digital** ([1068130303039496](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=1068130303039496&search_type=page)) | USD | 66 | 37,4 (limite inferior) | ARS 17.990 na [loja](https://mundocreativo.blog/products/kit-de-papeleria) (câmbio não verificado) | Título único "+10,000 recursos listos para editar en Canva" ([link](https://www.facebook.com/ads/library/?id=1054639970312774)) |
| **Magic Deco** ([967135516493190](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=967135516493190&search_type=page)), EN | USD | 61 | 6,3 (limite inferior) | Não verificado | [It's an APP!](https://www.facebook.com/ads/library/?id=4475514232660841) (1,2 d, abre no Canva), ["Stop Searching"](https://www.facebook.com/ads/library/?id=2490781461398016), ["Do You Have This Theme? = YES"](https://www.facebook.com/ads/library/?id=1575882503471281), ["More Client Orders"](https://www.facebook.com/ads/library/?id=1397155619172622) |
| **Pequeños Con Amor** ([699624056575259](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=699624056575259&search_type=page)) | USD | 41 | 7,2 | Não identificado | Só escassez ([link](https://www.facebook.com/ads/library/?id=1590631305803085)) |
| **Emilia Creativa** ([104514041971206](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=104514041971206&search_type=page)), toppers | USD | 32 | 26,6 | Não verificado | "+1.200 Cake Toppers" em ES e EN ([link](https://www.facebook.com/ads/library/?id=27881754751467164)). A comparação com os "2" da Fase 1 misturava métodos (busca × página): **"em crescimento" não está provado** |
| **Deco Mundo** ([746385791884775](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=746385791884775&search_type=page)) | USD | 21 | 12,9 | Não verificado ([loja](https://mundodeco.shop/en/products/kit-fiesta)) | "Tu fiesta WOW en menos de 60 minutos" (15 de 21, [link](https://www.facebook.com/ads/library/?id=1432932032020466)); ["Encuentra. Personaliza. Crea."](https://www.facebook.com/ads/library/?id=1025291930534954) |
| **Kit Fiesta Mágica** ([1291271347405076](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=1291271347405076&search_type=page)) | BRL | 12 | 0,5 | Não verificado | "¡ÚLTIMAS UNIDADES!" num produto digital ([link](https://www.facebook.com/ads/library/?id=1590800242454223)) |
| **Party Magic Studio** ([1288364524353091](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=1288364524353091&search_type=page)) | USD | 12 | 1,2 | Não verificado | "LO QUIERO", "⭐4,5/5" não verificável ([link](https://www.facebook.com/ads/library/?id=1074398312015285)) |
| **Activa Academy** ([881747588346031](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=881747588346031&search_type=page)) | MXN | 7 | 77,6 | Não verificado | "Mega Kit de Fiesta: +10,000 Diseños" ([link](https://www.facebook.com/ads/library/?id=1561011532248354)) |
| **Mega pack para la Fiesta de tus Sueños** ([1317853361405992](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=1317853361405992&search_type=page)) | USD | 4 | 1,5 | Não verificado | "Tu fiesta con efecto WOW, sin diseñadora" ([link](https://www.facebook.com/ads/library/?id=1798090501643105)) |
| **cienacres.imprimibles** ([461588617027210](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=461588617027210&search_type=page)) | USD | 4 | 469,5 | Não verificado | Loja de imprimíveis, sem título; produto exato não verificado ([link](https://www.facebook.com/ads/library/?id=1620243371983362)) |
| **Papel Fiesta** | ARS | — | 127,9 | Não verificado | Serviço sob encomenda, "Temáticas a pedido", venda por WhatsApp ([link](https://www.facebook.com/ads/library/?id=1536737214484050)) |
| **Fabulandia** | ARS | — | 165,6 | Não identificado | "+5000 VENDIDOS"; produto não identificado ([link](https://www.facebook.com/ads/library/?id=3377779535705085)) |
| Toppers | COP / USD / PEN | — | — | Não verificado | [Veronica Colombia](https://www.facebook.com/ads/library/?id=2576430022803606) (COP); [July Love Kits](https://www.facebook.com/ads/library/?id=1040848878786434) (11,8 d); [Diseños premiun](https://www.facebook.com/ads/library/?id=2845888295783849) (candy bar, PEN, 23,1 d) |
| Operadores BRL vendendo em ES | BRL | ~11 páginas em "papelería para fiestas" | — | Não verificado | [Fiesta Digital](https://www.facebook.com/ads/library/?id=1650933539877510) "+10.000 Diseños"; [Bruno Lero](https://www.facebook.com/ads/library/?id=933352599458140); [Papelaria Criativa](https://www.facebook.com/ads/library/?id=1090019076727230); [Fiesta Lista](https://www.facebook.com/ads/library/?id=1719759895753397) |
| Outros ES | ARS / USD | — | — | Não verificado | [Mundo Info Digital](https://www.facebook.com/ads/library/?id=28480742124914672) "Cumple Resuelto + 3 bonos"; [Aura creativa digital](https://www.facebook.com/ads/library/?id=1733607235436468) "Empezá a vender deco para cumpleaños" |

**Personalizado por designer (fora da Meta):** [Decoraciones Infantiles](https://www.decoracionesinfantiles.com/) (desde USD 6,00, nome e idade); [Elita Kits Digitales](https://www.elitakitsdigitales.com.ar/us/) (24 h úteis, 30 peças); [Munki](https://www.munki.com.ar/us/kits-personalizados/cumpleanos/); [Poppy Decor](https://poppydecor.com.ar/productos/elementos-kit-de-cumpleanos-imprimible-personalizado/) (ARS 8.750, personagem de filme); [Una Fiesta Bonita](https://www.unafiestabonita.com/collections/kits-imprimibles-para-fiestas) (US$ 10,99–23,99 por tema). É o concorrente real do gerador: mesmo resultado, com espera e atendimento humano.

**Hotmart:** [Spa Party US$ 5](https://pay.hotmart.com/K106315659W); [Fiesta Creativa US$ 10](https://pay.hotmart.com/P100609472X); [editáveis no Canva US$ 17](https://pay.hotmart.com/F103010959C?off=a1kavqsu&checkoutMode=10); [+2.000 temas, "247" em moeda não verificada](https://pay.hotmart.com/S103755914P); [Kit Completo de Fiesta Infantil](https://pay.hotmart.com/M105464353P) (preço não verificado); [Candy Bar](https://pay.hotmart.com/V89088274S); [Bluey (risco de PI)](https://pay.hotmart.com/B103082603B).

**Possível rede de um só operador [inferência, não verificado].** A Deco Mundo e a Magic Deco usam títulos idênticos, e as lojas se chamam "DIGITAL STORE 1" ([mundodeco.shop](https://mundodeco.shop/en/products/kit-fiesta)), "DIGITAL STORE 2" ([mundoinfantildigital.shop](https://mundoinfantildigital.shop/products/magic-party-kit)) e "Online Store DK" ([magicpartykit.com](https://magicpartykit.com/products/magic-party-kit-8-bonuses)). "DK" pode ser DecoKit. Se for uma rede só, "vários vendedores" é, em parte, um operador com várias páginas. A mesma rede já testa o posicionamento "app" em EN e FR.

**Buscas em ES sem gerador:** ["kit de fiesta"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=kit%20de%20fiesta&search_type=keyword_unordered) (1.014), ["papelería para fiestas"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=papeler%C3%ADa%20para%20fiestas&search_type=keyword_unordered) (234), ["kit de cumpleaños digital"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=kit%20de%20cumplea%C3%B1os%20digital&search_type=keyword_unordered) (87), ["toppers imprimibles"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=toppers%20imprimibles&search_type=keyword_unordered) (21), ["candy bar imprimible"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=candy%20bar%20imprimible&search_type=keyword_unordered) (12), ["kit de cumpleaños personalizado"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=kit%20de%20cumplea%C3%B1os%20personalizado&search_type=keyword_unordered) (106), ["kit de fiesta personalizado imprimible"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=kit%20de%20fiesta%20personalizado%20imprimible&search_type=keyword_unordered) (4), ["escribe el nombre invitación cumpleaños"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=escribe%20el%20nombre%20invitaci%C3%B3n%20cumplea%C3%B1os&search_type=keyword_unordered) (1), ["invitación cumpleaños inteligencia artificial"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=invitaci%C3%B3n%20cumplea%C3%B1os%20inteligencia%20artificial&search_type=keyword_unordered) (2). Os totais somam vários países de ES (até 11) e foram feitos via API em 22/09/2026; cada link reproduz só o MX. As buscas por frase ("con el nombre de tu hijo", "personalizado con nombre y edad", "cambia el nombre y la edad") só trazem ruído. **A ausência de gerador vale para essas palavras, não para o mercado inteiro.**

## O melhor argumento de por que vai falhar (e o que mataria a ideia)

**O argumento: o L67 herda a demanda de um produto cujo valor é o oposto do dele.**
- **O líder vende volume e reuso, e já se apropriou da demo.** O DecoKit tem 102 anúncios ativos só no MX, com "No es para una sola fiesta" (38,7 d), e já roda "Solo cambió un nombre" (39,2 d).
- **O L67 faz o contrário e cobra mais.** Para proteger a arte, trava 1 kit = 1 criança + 1 festa. E cobra US$ 7,90–9,90, no topo da faixa dos packs (US$ 3,65–10, com centenas ou milhares de designs).
- **Tira as duas alavancas mais longevas do nicho:**
  - **a temática:** os dois anúncios mais antigos do líder são de tema, e o L67 tem 8 temas e nenhum personagem;
  - **a compradora de volume:** no MX, ~1/4 dos anúncios do líder e os dois mais antigos da janela são de negócio. Esse público compra volume, não um kit com um único nome [inferência].
- **Sobra um público estreito, sem segmentação possível.** É a mãe com festa nas próximas semanas: ~0,2–0,4% do Facebook no MX, disputada num leilão em que o líder solta lotes de 9 a 12 anúncios. E o sinal do líder nem chega à AR (0 ativos), que receberia 12% da verba.
- **A conta não perdoa.** A 7,90, o CPA para ROI 1,5 em BRL é de US$ 4,16, 26% abaixo do que o Mimo tolera, com pixel novo e sem nenhum anunciante provando que um gerador vende em ES. Com o B1 a 10%, cai para 3,87.
- **O teste não consegue decidir.** Com 40–50 compras por braço, só aparece diferença de CPA ≥ 1,48–1,55×. Enxergar 20% exige ~230 compras por braço (2 × (1,96 ÷ ln 1,2)²).
- **O desfecho mais provável não é fracasso claro, é um meio-termo caro:** CPA entre US$ 5 e 8 [estimativa], resultado inconclusivo, e semanas de um operador solo que poderiam ir para a escala do Mimo.

**Os 5 maiores riscos e o sinal precoce de cada um:**

| # | Risco | Evidência | Sinal precoce (métrica, limiar, quando) |
|---|---|---|---|
| 1 | **Mercado:** o gerador não tem demanda própria, só a herdada do pack | Zero gerador em ES em 15+ buscas; o líder já vende "Solo cambió un nombre" e reuso; os ganchos mais longevos são de temática; a Magic Deco "APP" tem 1,2 d e abre no Canva | Visitante → compra abaixo do mínimo do Portão 1 depois de 1.000 visitantes; ≥ 25% das respostas de "¿Qué tema buscabas?" (campo no editor) pedindo personagem, nas primeiras 500 sessões; controle com CPA ≤ 1/1,5 do CPA do gerador (≥ 40 compras por braço) |
| 2 | **Economia e reembolso:** a margem depende de bumps não medidos | A 7,90 sem bumps, 5,32 de líquido; o PDF impresso não é revogável; H07/H08 puxam compras dentro da garantia; o regime de taxa pós-21/09 não foi verificado | Líquido real e adesão ao B1 nas primeiras 100 vendas; linha de taxa fixa na 1ª venda com bump; motivo de cada reembolso; reembolso > 7% ou chargeback > 0,5% |
| 3 | **Criativo e CPM:** a demo é mais fraca que a do Mimo [inferência] e disputa um leilão denso | Sem rosto de criança nem personagem; a mesa exige kits impressos de verdade; rótulo "AI info" nos formatos com rosto; o líder já tem a mesma demo | Hook rate, CTR de link e CPM contra os do Mimo nas mesmas praças, depois de ~10.000 impressões por criativo. Se o CPM sair mais alto, o multiplicador exigido sobe na mesma proporção |
| 4 | **Produto e build:** PDF no servidor, impressão e suporte de um operador solo | O motor de PDF multipágina com imagens é novo; o banderín sozinho soma ~10 páginas; o D3 é otimista; o suporte de impressão é tempo humano | Spike do D2 com PDF > 10 s ou > 8 MB, ou erro de memória; quadrado ≠ 5,0 cm no D6; tickets de impressão por 100 compradores; MVP depois do D14 |
| 5 | **Cópia** | A rede DecoKit/Deco Mundo/Magic Deco (inferência) já testa "app" em EN e FR; ~11 operadores BRL; tudo o que funcionar fica visível na mesma Biblioteca | Anúncios em ES dessas páginas com "app", "escribe su nombre" ou "con su nombre"; o "It's an APP!" passando de 30 d; nosso CPA subindo > 20% por semana, 2 semanas seguidas, sem fadiga de frequência |

Fora do top 5, com risco baixo: conta e política. O DecoKit roda "Emprende con decoración" há ~81 d no MX sem sinal de bloqueio [proxy; [página no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&view_all_page_id=737352542803130&search_type=page)]. Os riscos residuais são o rótulo de IA, a foto de criança na página pública do convite (lei de dados por país não verificada) e a célula de revenda escorregar para "gana".

**O que mataria a ideia.** Réguas [estimativa, cenário base, conta BRL]:

| Front | Líquido por comprador | CPA de break-even | CPA para ROI 1,25 | CPA para ROI 1,5 |
|---|---|---|---|---|
| US$ 7,90 | 6,99 | **6,24** | 4,99 | **4,16** |
| US$ 9,90 | 8,70 | **7,77** | 6,21 | **5,18** |
| Mimo (~9,4) | 9,4 | 8,39 | 6,71 | 5,60 |

**Portão 0: build, antes de gastar em mídia.**
- **Parar** se o spike do D2 falhar e o plano B (PDF no navegador) também falhar no navegador interno do Instagram no iOS.
- Sem compra de teste liberada ponta a ponta até o **D14**, cortar escopo pela lista do build.
- Sem ela até o **D21**, parar e devolver a atenção ao Mimo.

**Portão 1: funil, nos primeiros ~US$ 150 por braço e ≥ 10.000 impressões.** A régua é relativa ao Mimo, porque o usuário tem os números dele.
- **Eficiência** = CTR de link × taxa clique → compra (equivale a 1/CPA com o mesmo CPM).
- **Multiplicador exigido** = CPA do Mimo ÷ CPA-alvo do L67. Com o Mimo em ROI 1,5 (CPA 5,60):

  | Meta | Front 7,90 | Front 9,90 |
  |---|---|---|
  | Break-even | 0,90× o Mimo | 0,72× o Mimo |
  | ROI 1,5 | 1,35× o Mimo | 1,08× o Mimo |

  Se o Mimo roda acima de ROI 1,5, o CPA dele é menor e o multiplicador exigido sobe.
- **Corte:** eficiência abaixo do multiplicador de break-even, corrigida pela diferença de CPM.
- **Editor:** a taxa mínima visitante → compra é o CPC real ÷ o CPA de break-even. Com CPC de US$ 0,20 [estimativa], isso dá 3,2% a 7,90 e 2,6% a 9,90. Ficar abaixo depois de ≥ 1.000 visitantes é corte.

**Portão 2: produto, pelo CPA combinado do braço gerador, com bumps** (95% de confiança de que o CPA está acima do break-even, Poisson):

| Front | Depois de US$ 250 | Depois de US$ 400 |
|---|---|---|
| 7,90 | Matar se ≤ 29 compras (CPA ≥ 8,62) | Matar se ≤ 50 (CPA ≥ 8,00) |
| 9,90 | Matar se ≤ 22 compras (CPA ≥ 11,36) | Matar se ≤ 39 (CPA ≥ 10,26) |

- **Zona cinzenta** (CPA entre o break-even e esses limites): uma rodada extra com 15 ganchos novos, até US$ 600. Se o CPA combinado seguir acima do break-even, matar.
- **Para continuar:** CPA ≤ o de ROI 1,25 (4,99 a 7,90; 6,21 a 9,90), com ≥ 60 compras.
- **Para escalar:** CPA ≤ o de ROI 1,5, com +20–30% de verba a cada 48–72 h.
- **Por país:** testar a US$ 20–40/dia por conjunto e parar o país com CPA acima do break-even (6,24 / 7,77) depois de US$ 150. As regras da oferta ("continuar ≤ 7,0 / parar > 8,7") ignoravam os 12% da conta BRL; estão corrigidas.

**Portão 3: economia real, nas primeiras 100 vendas de front.**
- **Líquido real por comprador:** matar ou reprecificar se ficar abaixo do cenário ruim, < US$ 5,86 a 7,90 ou < 7,52 a 9,90. Nesse ponto, o CPA exigido cai para ≤ 3,49 ou ≤ 4,48 (BRL), abaixo do plausível.
- **B1 com adesão < 10%:** o "diferencial" não pega. Levar o convite para o front a preço maior, ou matar.
- **Reembolso > 7% ou chargeback > 0,5%:** parar e revisar. O limite da Hotmart é ~0,9% (digest de políticas; confiança média).
- **Tickets de impressão > 10 por 100 compradores** depois de corrigir a página 0: o custo marginal deixa de ser zero para um operador solo.

**Portão 4: mecanismo, gerador × controle L09** (substitui as regras de 20–25% da oferta e do criativo, que a amostra não consegue ver).
- **Matar o gerador** se o CPA do controle for ≤ 1/1,5 do CPA do gerador, com ≥ 40 compras por braço. É a única diferença detectável nesse tamanho de amostra. Como o gerador tem 1,20–1,26× mais líquido, esse caso deixa o ROI do controle ~1,2–1,25× maior.
- **Diferença menor que 1,5×:** o resultado é inconclusivo. O gerador não ganha o direito de escalar por comparação e precisa passar sozinho no Portão 2. Não gastar ~US$ 1.400 por braço para detectar 20%.
- **Personagem:** se ≥ 25% das respostas de "¿Qué tema buscabas?" pedirem personagem licenciado, a objeção é estrutural. Rever os temas ou matar [limiar proposto].

**Posição final sobre o ângulo duplo:**
- **Uso próprio (a mãe que faz a festa) é o produto e o anúncio.**
- **Quem monta kits para vender entra pelo bump B3** e por uma célula de revenda pequena: ≤ 15% da verba, só com demonstração, sem valor cobrado e só com o B3 no ar. A célula é desligada na primeira reprovação por resultados irreais.
- **A evidência não sustenta subir a revenda para o gancho principal.** O público pesa 1/8 a 1/3 dos títulos do líder, mas compra volume (o que a trava não dá), reembolsa mais [inferência] e é o único ponto que arrisca a conta.
