# Fase 3 — Scorecard

Data: 22/09/2026. São 23 ideias em concurso: as 19 sobreviventes da Fase 2 mais 4 reformulações em "versão ferramenta" (L66 a L69). A L01 entra fora de concurso, só como referência.

## 1. Método

Três avaliadores independentes deram nota de 0 a 10 a cada ideia em sete critérios, cada um com uma lente: o media buyer (dá para comprar tráfego e escalar?), o investidor cético (a evidência aguenta?) e o builder + compliance (sai em 14 dias e passa na Meta e na Hotmart?). A nota do painel é a mediana dos três em cada critério. As 8 maiores notas do painel e as hipóteses do usuário (L01 e L02) passaram por uma verificação adversarial. Nela, um verificador refez a coleta na Biblioteca de Anúncios da Meta em 22/09/2026 (anúncios ativos em MX, CO, AR, CL, PE, EC, GT, BO, UY, DO e US). Ele contou anunciantes por page_id, mediu o anúncio ativo mais antigo, buscou preços, substitutos e reclamações e rodou a calculadora de economia (`_raw/calc_economia.py`). Nas ideias verificadas, a nota final de cada critério é a média entre a mediana do painel e a nota do verificador. Nas outras, vale a mediana do painel. Os pesos são demanda 20, teto 20, criativo 15, economia 15, risco 10 (nota alta = risco baixo), build 10 e defensibilidade 10. O total é Σ(nota × peso) ÷ 10, de 0 a 100. Os avaliadores usaram três réguas de referência: teto 6 = igual ao Mimo Gift, build 0 = mais de 14 dias, e economia comparada com o líquido do Mimo no mesmo modelo (US$ 9,66 por comprador).

## 2. Ranking

| # | ID | Ideia | Demanda (20) | Teto (20) | Criativo (15) | Economia (15) | Risco (10) | Build (10) | Defens. (10) | Total | Verificado? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L02 | Invitaciones web (editor com RSVP; uso próprio + revenda) | 6,5 | 5,5 | 8,5 | 6,5 | 7 | 6,5 | 7 | **67,0** | sim |
| 2 | L67 | Gerador de kit de festa personalizado (PDF) | 6,5 | 6 | 8 | 6 | 8 | 6 | 6,5 | **66,5** | sim |
| 3 | L09 | Kit de festa temática editável no Canva | 9 | 6,5 | 7 | 5 | 6,5 | 5 | 3 | **63,5** | sim |
| 4 | L29 | Calculadora de custos e preços para quem vende em casa | 6 | 4 | 7 | 5,5 | 9 | 8 | 3,5 | **59,3** | sim |
| 5 | L66 | Gerador web de video-invitación (MP4) | 4 | 4,5 | 8 | 5,5 | 7 | 5,5 | 7 | **56,8** | sim |
| 6 | L10 | Biblioteca de papelaria criativa (+10.000 recursos) | 9,5 | 6 | 6 | 3,5 | 5 | 3,5 | 1,5 | **55,3** | sim |
| 7= | L04 | Invitaciones web de XV años | 5,5 | 3,5 | 6,5 | 4,5 | 7 | 7 | 6,5 | **55,0** | sim |
| 7= | L69 | Cardápio digital com QR e pedido por WhatsApp | 3 | 4 | 7 | 5 | 9 | 8 | 6 | **55,0** | não |
| 9 | L18 | App de stickers para vender (montador + calculadora) | 5,5 | 4,5 | 7 | 3,5 | 6,5 | 4,5 | 5,5 | **52,3** | sim |
| 10= | L27 | Receitas de sobremesas para vender, com custo | 8 | 6 | 5 | 3 | 5 | 5 | 2 | **52,0** | não |
| 10= | L68 | Editor de artes para presentes personalizados físicos | 2 | 4 | 7 | 5 | 8 | 7 | 7 | **52,0** | não |
| 12 | L06 | Mega pack de convites Canva/PPT "listos para vender" | 8 | 5 | 6 | 3 | 5 | 5 | 2 | **51,5** | não |
| 13 | L05 | Pack de video-invitaciones animadas | 5 | 5 | 7 | 5 | 5 | 5 | 3 | **51,0** | não |
| 14 | L33 | Templates Canva para empreendedoras | 4 | 5 | 5 | 4 | 7 | 6 | 2 | **46,5** | não |
| 15 | L22 | Pack sazonal "o que vender nesta data" | 5 | 4 | 6 | 4 | 5 | 5 | 3 | **46,0** | não |
| 16 | L30 | Receituário de velas, sabonetes e aromas | 5 | 4 | 4 | 5 | 5 | 4 | 3 | **43,5** | não |
| 17= | L15 | Etiquetas escolares e kit de volta às aulas | 4 | 3 | 5 | 3 | 7 | 7 | 3 | **43,0** | não |
| 17= | L16 | Agendas e planners 2027 para imprimir e vender | 5 | 3 | 5 | 3 | 6 | 6 | 3 | **43,0** | não |
| 19 | L11 | Moldes de caixinhas e cajas escenario | 5 | 3 | 5 | 2 | 6 | 7 | 2 | **41,5** | não |
| 20 | L56 | Templates para presentes físicos (quadros, ímãs) | 1 | 4 | 6 | 3 | 7 | 7 | 3 | **40,5** | não |
| 21 | L12 | Mega pack de topos de bolo | 4 | 4 | 5 | 2 | 5 | 6 | 2 | **39,5** | não |
| 22 | L32 | Kit para revendedoras de catálogo | 2 | 4 | 5 | 3 | 4 | 6 | 3 | **37,0** | não |
| 23 | L46 | Molduras editáveis para photobooth | 2 | 2 | 4 | 3 | 6 | 7 | 3 | **34,5** | não |
| fora de concurso | L01 | Mimo Gift Revenda (eliminada na Fase 2 por E2) | 1 | 2,5 | 3,5 | 4 | 3 | 8 | 6,5 | **35,8** | sim |

**Como ler**

- **A verificação derrubou quase todas as notas.** Caíram 7 das 8 ideias verificadas em concurso; na média das 8, o total final ficou 2,6 pontos abaixo do painel. As maiores quedas, do painel ao verificador, foram L02 (72 → 62), L18 (56,5 → 48), L04 (59 → 51) e L66 (60 → 53,5). Só a L29 subiu (58,5 → 60). As 15 não verificadas mantêm só a nota do painel e provavelmente estão otimistas na mesma direção (inferência).
- **O painel quase não divergiu.** A maior diferença entre avaliadores foi de 2 pontos num critério: L02 demanda, L10 build, L04 build, L01 economia e L01 defensibilidade. A divergência real foi entre painel e verificador: L29 demanda 5 → 7, L02 defensibilidade 8 → 6, L66 defensibilidade 8 → 6 e L01 build 9 → 7.
- **Há um trade-off central.** As ideias com demanda forte (L09, L10, L06, L27) são commodity, com defensibilidade de 1,5 a 3. As ferramentas, que têm defensibilidade, têm demanda da versão ferramenta não comprovada.
- **Nenhuma ideia verificada em concurso supera o Mimo em economia.** Os cenários de front a US$ 9,90 com bumps chegam no máximo a US$ 9,56 por comprador (L66, cenário otimista), contra US$ 9,66 do Mimo. Com front no nível dos concorrentes (US$ 4,90–7,90), o líquido fica entre US$ 3,6 e 6,8.
- **Ressalvas que valem para todas:**
  - O reembolso real por nicho não foi verificado.
  - A calculadora usa taxa fixa Hotmart de US$ 1,49. O log da Fase 1 registra mudança para US$ 1,00 em 21/09/2026 (não verificado na página oficial), o que melhoraria mais os fronts baratos.
  - Em L66 a L69, a demanda da versão ferramenta não foi medida; ela é herdada das ideias-pai.

## 3. Justificativa por ideia

### 1º · L02 — Invitaciones web (editor com RSVP; uso próprio + revenda) — 67,0
Painel 72 → verificador 62. Verificada. Hipótese do usuário. Absorveu o L03 (ângulo B2C) na Fase 2.

- **Demanda 6,5** — ~10 operadores de kit ES; longevo só o Kit Digital (template, 118,8 d). Editores web ES: 5, todos ≤18 d.
- **Teto 5,5** — Eventos perenes e ângulo duplo, mas a compra exige evento próximo e o B2C concorre com freemium (Convitia, InvitaWeb).
- **Criativo 8,5** — Convite abrindo no celular com música, contagem e RSVP vende sozinho; Mega Plantillas roda 10 variações "Mira como funciona".
- **Economia 6,5** — Concorrentes a US$ 3,7–6. Front 9,90 + bumps: US$ 8,21 líquido, contra 9,66 do Mimo; a US$ 6,90, US$ 5,47.
- **Risco 7** — Uso próprio é risco baixo; o mercado lidera com "listas para VENDER" e "Sistema de Ingresos". Liderar com uso próprio.
- **Build 6,5** — Reusa o editor e a página do Mimo, mas RSVP, painel multiconvite e modelos por evento levam até 14 dias.
- **Defensibilidade 7** — Editor hospedado supera PDF, mas já existem 5 editores ES, marca branca (Ariapsa, veamoslasfotos) e kits Hotmart com "RSVP".
- **Divergências:** é a maior queda do scorecard (−10 do painel ao verificador). A defensibilidade caiu de 8 para 6 porque o painel partiu da premissa "nenhum editor em ES", que hoje é falsa. No painel, a demanda foi de 6 (investidor cético) a 8 (builder).
- **Links:** [Kit Digital, 118,8 d](https://www.facebook.com/ads/library/?id=1376630554316244) · [Mega Plantillas, 49,5 d](https://www.facebook.com/ads/library/?id=1708910720392963) · [Invitoo, 1,8 d](https://www.facebook.com/ads/library/?id=1723104108989856) · [Event Builder Studio, 2,2 d](https://www.facebook.com/ads/library/?id=1056284580730092) · [Hotmart US$ 14,99](https://pay.hotmart.com/K102179105D) · [Ariapsa](https://ariapsa.com/eventos/)

### 2º · L67 — Gerador de kit de festa personalizado (PDF) — 66,5
Painel 68 → verificador 65. Verificada. Reformulação da Fase 2: versão ferramenta de L09 + L12; a demanda própria não foi medida.

- **Demanda 6,5** — Categoria-pai forte: DecoKit com 160 ativos, 12–15 anunciantes ES. Mas a versão gerador tem zero anunciantes em ES.
- **Teto 6** — Festa infantil é perene e multipaís (Magic Deco, 61 ativos em EN); sem personagens, o alcance encolhe. Igual ao Mimo.
- **Criativo 8** — Nome digitado aparecendo no convite, no topo e nas etiquetas é demo de tela. DecoKit roda 20+ títulos.
- **Economia 6** — Front 9,90 + bumps: US$ 9,29 líquido; a 7,90, US$ 7,60. O mercado ancora em US$ 5–10 por pack gigante.
- **Risco 8** — Uso próprio, sem promessa; DecoKit roda "¿Y si empiezas a venderlos?" há 30+ d. Risco real: personagens (PI).
- **Build 6** — Reusa editor e checkout do Mimo, mas PDF multipeça com linhas de corte e 160–240 artes originais ≈ 14 dias.
- **Defensibilidade 6,5** — Motor sob medida supera pack, mas Canva grátis já personaliza nome e idade; Magic Deco testa "It's an APP!".
- **Divergências:** nenhuma relevante; o verificador tirou 1 ponto em demanda e 1 em defensibilidade. O alerta dele é que o produto abre mão dos dois gatilhos do nicho: a temática ou o personagem favorito da criança e o volume ("+10.000 diseños").
- **Links:** [DecoKit, 136,6 d](https://www.facebook.com/ads/library/?id=1964080760865418) · ["¿No encontrás la temática…?", 127,1 d](https://www.facebook.com/ads/library/?id=1285905063665166) · [Magic Deco "It's an APP!"](https://www.facebook.com/ads/library/?id=4475514232660841) · [Hotmart com template de Bluey](https://pay.hotmart.com/B103082603B) · [Canva grátis](https://www.canva.com/es_mx/crear/tarjetas/invitaciones-fiesta-infantil/)

### 3º · L09 — Kit de festa temática editável no Canva — 63,5
Painel 64 → verificador 63. Verificada.

- **Demanda 9** — 15+ anunciantes ES e ~7 BRL; DecoKit com 160 ativos, o mais antigo com 191,0 d. Longevidade concentrada num só.
- **Teto 6,5** — Perene, roda em ES e EN, mas o Canva grátis é substituto direto; sem prova de gasto acima do Mimo.
- **Criativo 7** — "Crea toda la fiesta en Canva" é demo de tela; temáticas rendem dezenas de ganchos. Festa pronta pede mockup/IA.
- **Economia 5** — Mercado em US$ 3,6–10; front 6,90 dá US$ 5,5–6,8 líquido, contra 9,66 do Mimo; CPA máximo US$ 3,7–4,5.
- **Risco 6,5** — Os anúncios mais longevos da DecoKit (191 e 169 d) são de uso próprio; o risco é PI de personagens.
- **Build 5** — 20–30 temáticas originais no Canva ≈ 14 dias, sem reuso do motor do Mimo.
- **Defensibilidade 3** — Pack clonável; o "+10.000 diseños" em 6 vendedores sugere o mesmo PLR (inferência). A Hotmart reprova produto repetido.
- **Divergências:** nenhuma relevante (o risco foi 6 no painel e 7 no verificador). Ressalva: a DecoKit está parada em 160 ativos e sem criativo novo há 6,6 d.
- **Links:** [DecoKit, 191,0 d](https://www.facebook.com/ads/library/?id=2197772724365280) · ["¿Y si empiezas a venderlos?"](https://www.facebook.com/ads/library/?id=2072230433424563) · [KIT PREMIUM Fiesta Creativa, US$ 10](https://pay.hotmart.com/P100609472X) · [Canva, modelos grátis de fiesta infantil](https://www.canva.com/es_mx/plantillas/s/fiesta-infantil/)

### 4º · L29 — Calculadora de custos e preços para quem vende em casa — 59,3
Painel 58,5 → verificador 60. Verificada. Única verificada que subiu.

- **Demanda 6** — Verificador achou ~13 anunciantes ES (Fase 1: 5); Chef Anna 119,2 d (produto não verificado), Plantilla S/10 92 d.
- **Teto 4** — Só quem já vende (confeitaria, comida, crochê); compra nasce de dor, não de impulso. Público menor que o Mimo.
- **Criativo 7** — Gravação de tela de ingrediente → preço; concorrentes já usam 8+ ganchos de dor. O "aha" numérico é pouco visual.
- **Economia 5,5** — Âncora S/ 10–19 (US$ 3–6). Front 6,90 + bumps: US$ 6,16 líquido (64% do Mimo). Upsell possível (GastroKit US$ 57).
- **Risco 9** — Ferramenta sem promessa de renda; só evitar ganchos "gana más", que concorrentes já usam.
- **Build 8** — Web app no Lovable em poucos dias; não depende do editor do Mimo.
- **Defensibilidade 3,5** — Calculadoras grátis (Supleo, CalculadoraPrecios.com, Excel de blogs) e 10+ clones na Hotmart ES e BR; clonável em um dia.
- **Divergências:** a demanda passou de 5 (painel) para 7 (verificador), a maior revisão para cima do scorecard. Nenhuma página tem 20+ variações e a maioria entrou há menos de 7 d.
- **Links:** [Chef Anna, 119,2 d](https://www.facebook.com/ads/library/?id=1276480471319495) · [Plantilla Gastronómica S/10](https://www.facebook.com/ads/library/?id=1047240127991578) · [Cuentas Claras, 41,1 d](https://www.facebook.com/ads/library/?id=1696683294754899) · [GastroKit US$ 57](https://latinastogether.com/products/gastrokit) · [Supleo (grátis)](https://www.supleo.app/calcular-costo/reposteria)

### 5º · L66 — Gerador web de video-invitación (MP4) — 56,8
Painel 60 → verificador 53,5. Verificada. Reformulação da Fase 2: versão ferramenta do L05.

- **Demanda 4** — Em vídeo, só 1–2 anunciantes ES (Someri 8,5 d; Web Online 21,4 d). Nenhuma ferramenta geradora de MP4 anunciando.
- **Teto 4,5** — Depende de um evento; CapCut e Canva têm modelos grátis de XV em vídeo; a revenda é subnicho.
- **Criativo 8** — "Digito os nomes e sai o MP4" é demo nativa em Remotion; sem personagens, o tema infantil perde força.
- **Economia 5,5** — Concorrentes a ~US$ 6. Front 9,90 conservador: US$ 8,27 líquido; a 7,90, US$ 6,59. Custo de render não verificado.
- **Risco 7** — Ferramenta demonstrável; concorrentes usam "listas para VENDER" e "Emprende". Evitar personagens.
- **Build 5,5** — Render por usuário (fila, cota, armazenamento) é infra nova e cada modelo animado é código; provavelmente passa de 10 dias.
- **Defensibilidade 7** — O pipeline de render é difícil de copiar, mas CapCut, Canva, VEED e apps grátis entregam o mesmo MP4.
- **Divergências:** a defensibilidade caiu de 8 (painel) para 6 (verificador). A demanda B2C forte (Corazón de Fiesta, 70 anúncios, 82,4 d) é de serviço, não de ferramenta.
- **Links:** [Someri, 8,5 d](https://www.facebook.com/ads/library/?id=1950759622550013) · [Corazón de Fiesta, 82,4 d](https://www.facebook.com/ads/library/?id=1672846363944431) · [CapCut, modelos de XV](https://www.capcut.com/es-es/explore/15th-birthday-invitation) · [Hotmart, 190 video invitaciones](https://hotmart.com/es/marketplace/productos/pack-de-190-video-invitaciones-digitales-para-cumpleanos/N84722082H)

### 6º · L10 — Biblioteca de papelaria criativa (+10.000 recursos) — 55,3
Painel 58 → verificador 52,5. Verificada.

- **Demanda 9,5** — Maior cluster: 25+ anunciantes, Mundo Creativo Digital 66 e DecoKit 160 ativos. Os longevos (90+ d) têm 1–4 anúncios.
- **Teto 6** — Público perene e multipaís, mas o ticket de US$ 3–7 limita o gasto diário; nada indica verba acima do Mimo.
- **Criativo 6** — A edição no Canva se demonstra, mas a peça montada pede mockup; o gancho "+10.000 recursos" é genérico.
- **Economia 3,5** — Front 4,90: US$ 4,98 líquido; 6,90: US$ 6,66 (52–69% do Mimo). CPA máximo de US$ 3,3–4,4.
- **Risco 5** — Cara de PLR (3 listagens "hagsxd-papeleria-creativa" na Hotmart), páginas BR de 1–3,5 d, ângulo de revenda e personagens.
- **Build 3,5** — Igualar os "10.000 recursos" sem PLR exige semanas de conteúdo; nada se reaproveita do Mimo.
- **Defensibilidade 1,5** — Título clonado palavra por palavra ("Papeleria Digital"); mesmo pack no Gumroad (US$ 10) e Etsy (abaixo de € 1).
- **Divergências:** no painel, o build foi de 3 a 5. A demanda é alta, mas por uma commodity já clonada.
- **Links:** [Mundo Creativo Digital, 66 ativos](https://www.facebook.com/ads/library/?id=1054639970312774) · [clone "Papeleria Digital"](https://www.facebook.com/ads/library/?id=1082357534162439) · [Papelería Creativa BR, 101,9 d](https://www.facebook.com/ads/library/?id=1517888309821966) · [Hotmart, listagem clonada](https://hotmart.com/es/marketplace/productos/hagsxd-papeleria-creativa-osm6z/R102572444D) · [Gumroad US$ 10](https://borgatacorp16.gumroad.com/l/hzwfq)

### 7º (empate) · L04 — Invitaciones web de XV años — 55,0
Painel 59 → verificador 51. Verificada.

- **Demanda 5,5** — Nenhum kit de revenda exclusivo de XV; 228 anúncios de XV, quase todos serviço B2C (My Invite, 116,3 d).
- **Teto 3,5** — Um evento só; o revendedor prefere pacote multievento ("+1200 invitaciones", "Boda y XV" a US$ 5).
- **Criativo 6,5** — A demo do convite de XV (padrinos, música, RSVP) vende, mas os ângulos ficam presos a um evento.
- **Economia 4,5** — Âncoras de US$ 5 (Hotmart) e MXN 119 (~US$ 6,9): US$ 4,7–6,3 líquido, contra 9,66 do Mimo.
- **Risco 7** — Mesmo perfil baixo do L02; evitar "Ganhe até R$ 200 por convite" e ganchos de "ingresos".
- **Build 7** — Subconjunto do L02 sobre o motor do Mimo, mas RSVP e gestão de vários clientes são novos (~14 dias).
- **Defensibilidade 6,5** — Ferramenta hospedada, mas 4+ SaaS de convite com RSVP já anunciam; o recorte XV se copia fácil.
- **Divergências:** no painel, o build foi de 7 a 9 (o builder o viu como subconjunto do L02). A nota caiu 8 pontos do painel ao verificador. Cabe como pacote de modelos do L02, não como produto separado.
- **Links:** [My Invite, 116,3 d](https://www.facebook.com/ads/library/?id=1894344334607556) · [Marqstudio, serviço B2C](https://www.facebook.com/ads/library/?id=4601506146759840) · [Aprendizaje Total, 136,4 d](https://www.facebook.com/ads/library/?id=1546723633540219) · [Hotmart "Boda y Quinceaños" US$ 5](https://pay.hotmart.com/T102280557H)

### 7º (empate) · L69 — Cardápio digital com QR e pedido por WhatsApp — 55,0
Painel 55. **Não verificada.** Reformulação da Fase 2 (versão ferramenta); a demanda própria não foi medida.

- **Demanda 3** — 12 anunciantes, quase todos SaaS ou agência, todos com menos de 5 d; nenhum kit low ticket visto.
- **Teto 4** — Quem vende comida em casa é muita gente, mas concorre com SaaS grátis ("Tu menú QR, gratis").
- **Criativo 7** — Cardápio no celular e pedido chegando no WhatsApp é demo clara, com ângulos por tipo de comida.
- **Economia 5** — Referência US$ 6,99 (LX Diseño Web); SaaS grátis limita o preço; hospedagem contínua cria expectativa de serviço.
- **Risco 9** — Ferramenta para quem já vende, sem promessa de renda.
- **Build 8** — Quase o motor do Mimo: editor → página com link e QR + pedido formatado no WhatsApp.
- **Defensibilidade 6** — O link hospedado cria dependência, mas há SaaS grátis equivalentes.
- **Divergências:** nenhuma. Como as verificadas caíram em média 2,6 pontos, esta nota provavelmente está otimista (inferência).
- **Links:** [anúncio de menu QR](https://www.facebook.com/ads/library/?id=2161817697787903) · [Hotmart Menu App QR](https://hotmart.com/es/marketplace/productos/menu-app-qr-para-restaurantes/D64832885T) · [Hotmart Carta Virtual](https://hotmart.com/es/marketplace/productos/carta-virtual/V68221977S)

### 9º · L18 — App de stickers para vender (montador de folha + calculadora) — 52,3
Painel 56,5 → verificador 48. Verificada.

- **Demanda 5,5** — 3–5 anunciantes relevantes; só um longevo ("Stickers para vender", 74,7 d, 12 ativos). Busca de 367 inflada por gráficas.
- **Teto 4,5** — Público de quem revende stickers, concentrado em AR/UY (voseo, ARS); mais estreito que o de casais do Mimo.
- **Criativo 7** — "Mirá cómo funciona la app", "No cobres a ojo" e "Dejá de desperdiciar papel" já são demos de tela.
- **Economia 3,5** — Âncora de US$ 3,90 (Hotmart) e ARS 2–4 mil; front 5,90 + bumps: US$ 4,95 líquido (51% do Mimo).
- **Risco 6,5** — A ferramenta é de baixo risco, mas "empezá a vender" e a pressão por personagens (Stitch, Bluey) pesam.
- **Build 4,5** — Biblioteca de milhares de stickers por IA com curadoria, mais montador com marcas de corte ≈ 14 dias.
- **Defensibilidade 5,5** — Montador e calculadora valem mais que PDF, mas se replicam em dias; biblioteca copiável; Canva e Flaticon grátis.
- **Divergências:** a nota caiu 8,5 pontos do painel ao verificador, a segunda maior queda. O comprador precisa de impressora e papel adesivo, o que pode gerar reembolso por frustração (não verificado).
- **Links:** ["+8000 stickers", 74,7 d](https://www.facebook.com/ads/library/?id=1003636949331535) · ["Mirá cómo funciona la app"](https://www.facebook.com/ads/library/?id=2197892240793228) · [Tu Solucion Digital, 32,3 d](https://www.facebook.com/ads/library/?id=2469373846902705) · [Super Pack US$ 3,90](https://pay.hotmart.com/M102998773E)

### 10º (empate) · L27 — Receitas de sobremesas para vender, com custo — 52,0
Painel 52. **Não verificada.**

- **Demanda 8** — 20 anunciantes, Chef Eli com 32 variações, "recetas para vender" = 3.042; anúncios de Natal ativos há 287–366 d.
- **Teto 6** — Público enorme e perene (mais o Natal), mas o mercado é ultradenso; não há razão para superar o Mimo.
- **Criativo 5** — Não há ferramenta para demonstrar; depende de imagem de comida (IA ou banco) e de folhear o ebook.
- **Economia 3** — US$ 1,4–9; o modelo "primero recibes y luego pagas" ancora o preço baixo; reembolso de renda extra maior.
- **Risco 5** — Meta médio (o nicho abusa de "gana $X"); Hotmart médio (receita genérica = baixo valor).
- **Build 5** — O ebook sai rápido, mas receitas com custo por porção precisam ser testadas e fotografadas.
- **Defensibilidade 2** — PDF clonável em um dia, no mercado mais denso da fase.
- **Divergências:** nenhuma relevante. O media buyer lembrou que, fora os de Natal, o anúncio mais antigo tem só 7,5 d.
- **Links:** [anúncio 1](https://www.facebook.com/ads/library/?id=1418570293571960) · [anúncio 2](https://www.facebook.com/ads/library/?id=2132493034287794) · [Hotmart "100 recetas de postres rentables"](https://hotmart.com/es/marketplace/productos/100-recetas-de-postres-rentables-para-emprender-desde-casa/T103881974V)

### 10º (empate) · L68 — Editor de artes para presentes personalizados físicos — 52,0
Painel 52. **Não verificada.** Reformulação da Fase 2 (versão ferramenta do L56); a demanda própria não foi medida.

- **Demanda 2** — Templates em ES não verificados; o mapa estelar só aparece como produto físico (busca = 4; Kindred 275 d).
- **Teto 4** — Quem imprime ou sublima presentes: público menor que o do Mimo e não medido em ES.
- **Criativo 7** — DNA do Mimo: nomes e data viram arte ou mapa estelar na tela, mais mockup físico.
- **Economia 5** — A única referência é um pack de US$ 3,90; o preço de uma ferramenta não foi verificado.
- **Risco 8** — Ferramenta de presente sem promessa de renda; licença comercial clara.
- **Build 7** — Reusa o editor do Mimo, mais exportação em alta resolução, mapa estelar e calculadora; viável em 14 dias.
- **Defensibilidade 7** — Um editor sob medida com exportação para impressão supera templates.
- **Divergências:** nenhuma relevante. A nota vem quase toda de build e risco; é a pior demanda entre as 13 primeiras.
- **Links:** [mapa estelar, anúncio](https://www.facebook.com/ads/library/?id=1091840433262853) · [Hotmart, templates de presente](https://pay.hotmart.com/M104164269T)

### 12º · L06 — Mega pack de convites Canva/PPT "listos para vender" — 51,5
Painel 51,5. **Não verificada** (a verificação do L02 mediu o mesmo mercado).

- **Demanda 8** — 12 anunciantes, Kit Digital com 118,8 d e 17 variações, 12+ produtos na Hotmart; rede 6U$D em 4+ páginas.
- **Teto 5** — Muitos eventos e países, mas a guerra de preço entre US$ 3 e 6 limita o gasto rentável.
- **Criativo 6** — A rolagem de templates e o "Mira como funciona" funcionam, mas são iguais aos dos 12 concorrentes.
- **Economia 3** — A US$ 4,90 + bumps, ~US$ 4,53 líquido: metade do Mimo; a taxa fixa come a margem.
- **Risco 5** — E2 forte no mercado ("Emprende desde casa") e cara de PLR; a Hotmart barra produto repetido.
- **Build 5** — 150–300 peças originais em Canva; trabalho de design, sem reuso do Mimo.
- **Defensibilidade 2** — Pack clonável em um dia; a rede 6U$D já o replica em 4+ páginas.
- **Divergências:** nenhuma. A Fase 2 sugeriu trocar o pack pelo editor do L02, mas a verificação do L02 mostra que a demanda comprovada é justamente deste formato.
- **Links:** [Kit Digital, 118,8 d](https://www.facebook.com/ads/library/?id=1376630554316244) · [Mega Plantillas](https://www.facebook.com/ads/library/?id=1708910720392963) · [Hotmart, mega pack](https://hotmart.com/es/marketplace/productos/mega-pack-de-invitaciones-digitales/N86477437U)

### 13º · L05 — Pack de video-invitaciones animadas — 51,0
Painel 51. **Não verificada** (a verificação do L66 mediu o mesmo mercado).

- **Demanda 5** — 5 anunciantes, até 8 variações; o mais antigo tem 21,4 d em ES e 38,3 d no BR.
- **Teto 5** — Vários eventos e ângulo duplo, mas o vídeo-convite é subnicho do convite (MX, PE, CO).
- **Criativo 7** — O vídeo animado se demonstra sozinho e vira template em Remotion; há ângulos por evento.
- **Economia 5** — Someri a MXN 99–119 (~US$ 5,5–6,6); front de ~US$ 6 dá ~US$ 5–6 líquido.
- **Risco 5** — O mercado usa "listas para VENDER" (E2) e personagens Disney/Pixar (PI).
- **Build 5** — ~50 vídeos editáveis em Canva ou CapCut em 14 dias; reusa a fábrica de vídeo, não o Mimo.
- **Defensibilidade 3** — Template clonável; já há 2 packs na Hotmart.
- **Divergências:** nenhuma. A verificação do L66 achou demanda paga por vídeo ainda mais fina e modelos grátis de XV no CapCut.
- **Links:** [Someri](https://www.facebook.com/ads/library/?id=1950759622550013) · ["CONVITES CINEMATOGRÁFICOS" BR, 38,3 d](https://www.facebook.com/ads/library/?id=1412094170985815) · [Hotmart, 190 video invitaciones](https://hotmart.com/es/marketplace/productos/pack-de-190-video-invitaciones-digitales-para-cumpleanos/N84722082H)

### 14º · L33 — Templates Canva para empreendedoras — 46,5
Painel 46,5. **Não verificada.**

- **Demanda 4** — 6 anunciantes, o mais antigo com 4,2 d; ~15 produtos na Hotmart; sem longevidade.
- **Teto 5** — Pequenos negócios são público amplo, mas saturado ("plantillas editables" = 1.635).
- **Criativo 5** — A rolagem de templates é genérica e difícil de destacar.
- **Economia 4** — US$ 5–11 observado; ~US$ 5–6 líquido com bumps.
- **Risco 7** — Anúncio de ferramenta sem renda; não vender direito de revenda (MRR, como a InstaPremium).
- **Build 6** — Centenas de templates Canva em 1–2 semanas, sem reuso do Mimo.
- **Defensibilidade 2** — Pack Canva clonável; ~15 parecidos na Hotmart.
- **Divergências:** nenhuma.
- **Links:** [Hotmart 1](https://pay.hotmart.com/K103856475B) · [Hotmart 2](https://pay.hotmart.com/K102983255Y)

### 15º · L22 — Pack sazonal "o que vender nesta data" — 46,0
Painel 46. **Não verificada.**

- **Demanda 5** — 7 anunciantes, o mais antigo com 8,7 d (PP Studio); "vender en navidad" = 934 anúncios (proxy).
- **Teto 4** — Recorrente por data, mas cada janela é curta e o kit precisa ser refeito.
- **Criativo 6** — Os designs por data se mostram na tela, com ângulo novo a cada data ("quien se adelanta, vende").
- **Economia 4** — US$ 6 (Kit Muestra de Fin de Año): ~US$ 5–5,9 líquido com bumps.
- **Risco 5** — "O que vender" fica colado em renda: E2 moderada.
- **Build 5** — O kit por data sai rápido, mas é trabalho recorrente a cada data.
- **Defensibilidade 3** — Designs e moldes clonáveis em um dia.
- **Divergências:** nenhuma. A ideia se sobrepõe a L16 e L10.
- **Links:** [PP Studio](https://www.facebook.com/ads/library/?id=1050530871372346) · [Hotmart](https://pay.hotmart.com/B105630358A)

### 16º · L30 — Receituário de velas, sabonetes e aromas — 43,5
Painel 43,5. **Não verificada.**

- **Demanda 5** — 6 anunciantes de velas e 4 de aromas; os mais antigos têm 3,8 e 0,9 d. Nicho dominado por cursos.
- **Teto 4** — Artesanato de velas e aromas é perene, mas estreito e disputado por cursos.
- **Criativo 4** — Produto físico sem demo de tela; os concorrentes usam pessoa real; a IA rende pouco aqui.
- **Economia 5** — Hotmart a US$ 5,99–15 permite front maior, mas é provável reembolso quando a fórmula falha.
- **Risco 5** — Gancho "se vende caro" (E2); sabonete com soda exige fórmula testada (segurança).
- **Build 4** — Fórmulas seguras exigem teste físico; não saem de IA em 14 dias.
- **Defensibilidade 3** — Ebook clonável; 11 produtos na Hotmart.
- **Divergências:** nenhuma.
- **Links:** [anúncio de velas](https://www.facebook.com/ads/library/?id=948666801622176) · [Hotmart, megaebook](https://hotmart.com/es/marketplace/productos/hagsxd-megaebook-velas-y-jabones-artesanales-aroma-y-glow-kscxu/V100266138S)

### 17º (empate) · L15 — Etiquetas escolares e kit de volta às aulas — 43,0
Painel 43. **Não verificada.**

- **Demanda 4** — 5 anunciantes; o mais antigo confirmado tem 12,4 d (há um de 82,4 d com oferta incerta); busca = 49.
- **Teto 3** — Sazonal (volta às aulas), com calendário escolar diferente por país.
- **Criativo 5** — O nome da criança nas etiquetas é boa demo, mas há poucos ângulos fora da temporada.
- **Economia 3** — MXN 89 (~US$ 4,8): ~US$ 5 líquido com bumps; pouco espaço para bumps.
- **Risco 7** — Uso próprio pela mãe, sem promessa de renda.
- **Build 7** — Kit ou editor simples com nome; poucos dias, reusando parte do Mimo.
- **Defensibilidade 3** — Templates clonáveis em um dia.
- **Divergências:** nenhuma.
- **Links:** [Diseña Creativo](https://www.facebook.com/ads/library/?id=2229308641185714) · [anúncio 2](https://www.facebook.com/ads/library/?id=1270026136202268)

### 17º (empate) · L16 — Agendas e planners 2027 para imprimir e vender — 43,0
Painel 43. **Não verificada.**

- **Demanda 5** — 10 anunciantes (Inu studio com 12 variações), mas o mais antigo tem 6,2 d: é pico sazonal, sem longevidade.
- **Teto 3** — Janela de setembro a janeiro; sem gasto no resto do ano.
- **Criativo 5** — Capas e datas se mostram na tela; a agenda física pede mockup.
- **Economia 3** — US$ 3,90 (Hotmart) e CLP 3.500; um front de US$ 3,90 dá ~US$ 1,98 líquido na calculadora.
- **Risco 6** — "Elegí, imprimí, vendé" não cita valor; a licença é para imprimir, não para revender os arquivos.
- **Build 6** — Agenda com datas automáticas em PPT ou Canva: 1–2 semanas, e a janela desta temporada já abriu.
- **Defensibilidade 3** — Arquivo editável clonável, renovado todo ano.
- **Divergências:** nenhuma.
- **Links:** [anúncio](https://www.facebook.com/ads/library/?id=2232346370955983) · [Hotmart](https://pay.hotmart.com/N96421608B)

### 19º · L11 — Moldes de caixinhas e cajas escenario — 41,5
Painel 41,5. **Não verificada.**

- **Demanda 5** — 6 anunciantes, o mais antigo confirmado com 25 d; Mi Masterclass com 19 variações.
- **Teto 3** — Nicho estreito; o ticket de US$ 2 indica produto de bump, não de front.
- **Criativo 5** — "Transforma tus cosméticos en Regalos Premium" é visual, mas exige mostrar a caixa física montada.
- **Economia 2** — US$ 2–2,7 morre na taxa fixa: a US$ 2,70, ~US$ 0,91 líquido. Só serve como bump.
- **Risco 6** — Anúncio sem renda passa; moldes compilados de terceiros trazem risco de PLR na Hotmart.
- **Build 7** — ~40 facas em PDF ou Canva, ou um gerador paramétrico no Lovable, em dias.
- **Defensibilidade 2** — Moldes em PDF clonáveis em um dia.
- **Divergências:** nenhuma. A Fase 2 sugeriu usá-la como bump do L10 ou do L09.
- **Links:** [anúncio](https://www.facebook.com/ads/library/?id=1087199917345042) · [anúncio 2](https://www.facebook.com/ads/library/?id=1109426881423561)

### 20º · L56 — Templates para presentes físicos (quadros, ímãs) — 40,5
Painel 40,5. **Não verificada.**

- **Demanda 1** — Anunciantes e longevidade não verificados; só 2–3 produtos na Hotmart.
- **Teto 4** — Quem vende personalizado físico, com datas como as do Mimo; demanda em ES não medida.
- **Criativo 6** — Edição no Canva e mockups de quadros e ímãs; ângulos por data e destinatário.
- **Economia 3** — US$ 3,90 (Pack 30 Plantillas Cuadros en Pareja): ~US$ 2 líquido de front.
- **Risco 7** — Não precisa prometer ganho; a licença é só de uso comercial.
- **Build 7** — 30 templates Canva em poucos dias.
- **Defensibilidade 3** — Templates clonáveis.
- **Divergências:** nenhuma. A versão ferramenta desta ideia é o L68.
- **Links:** [Hotmart 1](https://pay.hotmart.com/M104164269T) · [Hotmart 2](https://pay.hotmart.com/N103896032H)

### 21º · L12 — Mega pack de topos de bolo — 39,5
Painel 39,5. **Não verificada.**

- **Demanda 4** — Digital em ES: só Emilia Creativa (2 anúncios, 11,5 d) e Activa Academy (33,1 d); forte só no BR.
- **Teto 4** — "toppers para pastel" = 55 em ES, contra "topo de bolo" = 1.307 no BR.
- **Criativo 5** — O topo no bolo é visual, mas perde apelo sem personagens.
- **Economia 2** — Referência BR de R$ 1,49–3,99 (isca); preço em ES não verificado.
- **Risco 5** — A oferta observada é PLR de personagens licenciados (E4 + PI).
- **Build 6** — Pack original com IA em 14 dias; sem reuso do Mimo.
- **Defensibilidade 2** — PNG ou PDF clonável; o BR vende 20 mil topos por R$ 1,49.
- **Divergências:** nenhuma. A versão ferramenta está dentro do L67.
- **Links:** [anúncio BR](https://www.facebook.com/ads/library/?id=1579502953724620) · [anúncio 2](https://www.facebook.com/ads/library/?id=2155772475373199)

### 22º · L32 — Kit para revendedoras de catálogo (Natura, Ésika, Yanbal) — 37,0
Painel 37. **Não verificada.**

- **Demanda 2** — 3 anunciantes; Sello Propio foi lançado há 0,3 d; "plantillas para revendedoras" = 2.
- **Teto 4** — Muitas revendedoras (número não medido), mas sem poder citar as marcas o gancho encolhe.
- **Criativo 5** — A arte com o nome da revendedora se demonstra, mas sem logos perde o gancho.
- **Economia 3** — Preço não verificado; kits parecidos custam US$ 3–6.
- **Risco 4** — Citar as marcas é personificação na Meta; o público é em parte de multinível.
- **Build 6** — Centenas de artes editáveis com IA ou Canva em 1–2 semanas.
- **Defensibilidade 3** — Templates clonáveis.
- **Divergências:** nenhuma.
- **Links:** [anúncio](https://www.facebook.com/ads/library/?id=2156814638591939) · [anúncio 2](https://www.facebook.com/ads/library/?id=1107576018528128)

### 23º · L46 — Molduras editáveis para photobooth — 34,5
Painel 34,5. **Não verificada.**

- **Demanda 2** — 2 anunciantes (BRL), o mais antigo com 7,8 d; "marcos para photobooth" em ES = 7.
- **Teto 2** — Nicho B2B minúsculo (operadores de cabine de fotos).
- **Criativo 4** — A moldura na foto se demonstra, mas há poucos ângulos (XV, boda, bautizo).
- **Economia 3** — Preço não verificado; o B2B poderia pagar mais, mas não há evidência.
- **Risco 6** — O mercado usa "Cabine Lucrativa" (E2); um ângulo de produto passa.
- **Build 7** — Pack ou editor de molduras em PNG transparente; simples.
- **Defensibilidade 3** — Pack clonável; só um editor subiria a nota.
- **Divergências:** nenhuma.
- **Links:** [anúncio](https://www.facebook.com/ads/library/?id=4627474187578843) · [anúncio 2](https://www.facebook.com/ads/library/?id=1710483000052810)

### Fora de concurso · L01 — Mimo Gift Revenda — 35,8
Painel 39 → verificador 32,5. Verificada. Hipótese do usuário, eliminada na Fase 2 por E2 e pontuada só como referência.

- **Demanda 1** — 0 anunciantes de revenda em 28 buscas Meta (18 da Fase 1, 10 novas) e 6 web; nada na Hotmart.
- **Teto 2,5** — Nicho de revendedores; o cliente final tem 7+ opções em ES grátis ou de US$ 5.
- **Criativo 3,5** — A demo vende o presente, não a licença; o único gancho de negócio é promessa de ganho.
- **Economia 4** — Licença a US$ 14,90 daria US$ 12,9–13,7 líquido (hipotético); não há preço de mercado; reembolso de renda extra.
- **Risco 3** — E2: "gana vendiendo páginas" esbarra em "resultados irreais" na Meta e em promessa de ganho na Hotmart.
- **Build 8** — O motor do Mimo serve quase direto, mas painel multicliente e marca branca levam até 14 dias.
- **Defensibilidade 6,5** — Ferramenta hospedada, não PDF, mas há 10+ SaaS parecidos (QLovy, GiftsQR, TLANEX, iloveyou.gift).
- **Divergências:** no painel, a economia foi de 3 a 5 e a defensibilidade de 5 a 7. O build caiu de 9 (painel) para 7 (verificador).
- **Links:** [QLovy (grátis)](https://qlovy.com/es/blog/regalo-digital-gratis) · [GiftsQR (grátis)](https://giftsqr.com/es-ES/love) · [TLANEX](https://www.tlanex.com/) · [iloveyou.gift, US$ 5](https://iloveyou.gift/) · [anúncio visto nas buscas de revenda](https://www.facebook.com/ads/library/?id=1068030272817915)

## 4. Hipóteses do usuário

### H2 — L02 Invitaciones web: 1º lugar, 67,0 (painel 72, verificador 62)

Ganhou, mas só meio ponto à frente do L67 e com a maior queda de todo o scorecard. O veredito, sem dó:

- **O mercado comprova template barato, não editor web.** A oferta longeva em ES é o Kit Digital: um template Canva de CLP 3.500 (~US$ 3,7), com 118,8 d. Os 5 editores web em ES que o verificador achou têm todos 18 d ou menos. Ninguém provou ainda que o formato ferramenta escala em espanhol.
- **A premissa da Fase 1 caiu.** "Nenhum editor self-service em ES" é falso hoje. O diferencial "editor com RSVP" já existe em marca branca (Ariapsa, veamoslasfotos) e em kits da Hotmart que imitam RSVP no Canva.
- **O ângulo B2C (uso próprio, herdado do L03) apanha do grátis.** A Convitia passou a liderar com "Crie seu convite grátis", e InvitaWeb e Compartiremos são freemium. Quem compra para o próprio evento compra uma vez, com prazo e sem o impulso emocional do Mimo.
- **O ângulo de revenda concentra o volume, mas é o que puxa para E2.** Os títulos dominantes são "listas para VENDER" e "Sistema de Ingresos".
- **A economia é pior que a do Mimo.** No cenário conservador, o líquido é de US$ 8,21 por comprador, 85% do Mimo. Se o preço cair ao nível dos concorrentes (US$ 6,90), vai a US$ 5,47.
- **O build encosta no limite da régua.** Até 14 dias, que é o teto aceito.
- **Por que ainda fica em 1º:** é a ideia que mais reaproveita o ativo que o usuário já tem, porque a saída é a mesma do Mimo: um editor que gera uma página web. Também tem demo de tela que vende sozinha, ângulo duplo e risco controlável.

É uma aposta, não uma certeza. A pergunta que o deep dive precisa responder é se alguém paga US$ 9,90 por um editor quando o kit custa US$ 3,7.

### H1 — L01 Mimo Gift Revenda: fora de concurso, 35,8 (painel 39, verificador 32,5)

Em concurso, ficaria em 23º de 24, à frente só do L46 (34,5). **Veredito: morta.**

Não há comprador visível: 0 anunciantes de revenda em 28 buscas na Meta (ES e BR), nenhum programa de marca branca na web e nenhum produto na Hotmart. Sem um revendedor para imitar, o único anúncio possível é "gana vendiendo páginas de amor", que é E2 e bate nas regras da Meta e da Hotmart.

**Canibalização com o Mimo Gift**

- **O público comprador é o mesmo?** Quem compra a licença é outra pessoa (quem busca renda extra). Mas o cliente dela é exatamente o cliente do Mimo: quem quer presentear o parceiro, a parceira ou a mãe. Cada venda do revendedor sai do mercado que o Mimo já atende.
- **A criatividade é a mesma?** Sim. A demo que venderia a licença é a mesma página de amor abrindo no celular que vende o Mimo; só a legenda muda para "vende esto", que é justamente o gancho E2. Se os revendedores anunciarem essa demo para o mesmo público, disputam o mesmo leilão que o Mimo (inferência).
- **O revendedor vira concorrente de preço?** Sim. O cliente final acha a página grátis ou por US$ 5 (QLovy, GiftsQR, TLANEX, iloveyou.gift), e o Mimo cobra US$ 8–9. O revendedor só tem margem com quem não pesquisa, então tende a derrubar o preço. Os dois desenhos de produto perdem:
  - Sem marca branca, o cliente do revendedor descobre o Mimo e compra direto.
  - Com marca branca, o Mimo passa a disputar o próprio público com páginas iguais e mais baratas (inferência).
- **A sazonalidade é dupla.** Os picos de venda do presente viram vales de venda da licença.
- **O que dá para aproveitar.** A Fase 2 sugeriu pôr modelos de página-presente (amor, aniversário, dia das mães) como mais um tipo de evento no editor do L02. Isso carrega a mesma canibalização. O mais seguro é testar o L02 sem esse modelo e só incluí-lo depois de medir.

## 5. Top 3 para deep dive

1. **L02 — Invitaciones web (67,0):** maior nota final, reusa o motor do Mimo e tem ângulo duplo. Precisa provar que alguém paga US$ 9,90 por um editor num mercado ancorado em kits de US$ 3,7–6.
2. **L67 — Gerador de kit de festa personalizado (66,5):** a categoria-pai tem uma das demandas mais fortes do scorecard (DecoKit, 160 ativos, até 191 d), num formato que foge da commodity. Testar o gerador sem personagens contra o pack L09, que entra como controle.
3. **L29 — Calculadora de custos e preços (59,3):** melhor risco (9) e build (8) do top 5, e a demanda foi revisada para cima pelo verificador (~13 anunciantes, 119,2 d). Precisa vencer a âncora de US$ 3–6 e o substituto grátis.

**Por que não o L09 (3º pela nota, 63,5):** é quase idêntico ao L67. Tem a mesma persona (a mãe que faz a festa infantil), a mesma evidência (DecoKit) e o mesmo entregável final; muda só o formato, pack Canva ou gerador. Dois deep dives separados duplicariam o trabalho. Por isso, o deep dive do L67 cobre o L09 como formato de controle, e a vaga foi para a próxima ideia distinta, o L29 (59,3).

**Outros descartes:** o L66 (56,8) também não entraria, porque é a versão vídeo do cluster convite, já coberto pelo L02. O top 3 é robusto: as próximas ideias distintas ficam uns 4 pontos atrás do L29. São o L10 (55,3), commodity com defensibilidade 1,5, e o L69 (55,0), que não foi verificado, tem demanda 3 e tende a cair se for verificado.

**Nota de sobreposição:** L02 e L67 dividem parte do público (festa infantil) e do motor (editor do Mimo). O deep dive deve avaliar se funcionam melhor como um produto só, com convite web e kit impresso juntos.
