# Fase 1 — Hipóteses do usuário: H1 "Mimo Gift Revenda" x H2 "Invitaciones web"

Coleta: 2026-09-22. Referência "agora" = epoch 1790095977. Dias ativo = (1790095977 - ad_delivery_start_time) / 86400.
Meta Ad Library via MCP, `ad_active_status=ACTIVE`, limit 30–50. "ES11" = MX, CO, AR, CL, PE, EC, GT, BO, UY, DO, US. "BR" = só Brasil (espelho em PT).
A ferramenta não retorna o texto do anúncio nem o alcance. Julguei a relevância só por page_name + link_title + moeda, de forma conservadora; o que não deu para identificar está marcado como "não identificado".
Mesmo rigor para as duas hipóteses. Tudo o que é contagem é **proxy** (nº de anúncios ativos, dias do anúncio ativo mais antigo, nº de anunciantes, estimated_total_count). Não é faturamento.

---

## 0. Como a busca se comporta (vale para ler os números)
- `search_terms` busca palavras soltas (AND sem ordem). Aspas não forçam frase: `"página personalizada"` deu 2.904, quase tudo ruído. Termos genéricos de amor em ES ("página de amor", "carta digital pareja", "sorprende a tu pareja") trazem dramas, tarô e videntes.
- Os resultados vêm do mais novo para o mais antigo. Em termos com muito volume, os 50 anúncios que aparecem cobrem só ~1–2 dias. Então "anunciantes distintos nos 50" é uma janela curta, não o total.
- Quando busco várias páginas numa chamada só (page_ids), o limite de 50 é dividido entre elas. Se uma página domina o resultado, as outras perdem os anúncios mais antigos, e aí a idade vira **limite inferior** (indicado na tabela).

---

## 1. Buscas rodadas (termo → estimated_total_count → o que aparece)

### H1 — página de amor / regalo digital (B2C e revenda)
| # | Termo | Países | est. | Leitura |
|---|---|---|---|---|
| Q1 | página de amor | MX,CO,AR,CL,PE,US | 3.633 | ruído total (DramaBox, Ai-CodeMotion, Net Short) |
| Q3 | "página personalizada" | MX,CO,AR,CL,PE,US | 2.904 | ruído (lojas, clínicas, tarô) |
| Q10 | regalos digitales vender | ES11 | 77 | packs de imprimibles (Bonito Digital, Recursoslandia, Aprende en casa). **Impulso digital** (PEN) "🌻 ¡Sorprende con Flores Amarillas!" (sazonal, 21/set). Mundo Digital (CLP) "SOLO X HOY $3.500" (não identificado) |
| Q12 | flores amarillas digitales | ES11 | 8 | Impulso digital (3), KIT Papeleria (ARS), Niiogo (PEN), floriculturas |
| Q13 | página web pareja regalo | ES11 | 41 | ruído. **Daniela Michilena** (USD) "💝 El regalo que jamás olvidará" (produto não identificado) |
| Q14 | carta digital pareja | ES11 | 88 | ruído total |
| Q15 | regalo digital fotos mensaje | ES11 | 39 | quase tudo convite ou fotografia (Tarjetas Interactivas, Invitate, Confirm the date); Rock N Roll MKT (PEN) "🌻 Promoción especial"; Jose Gutierrez (PEN) "Detalles para 21 de septiembre" |
| Q24 | vende páginas personalizadas | ES11 | 4 | Aprendamos IA con Fer (USD, não identificado), Nova Studio (PEN, não identificado), Marketero Digital |
| Q25 | regalo digital código QR pareja | ES11 | 0 | — |
| Q26 | página web novia sorpresa | ES11 | 1 | ruído |
| Q28 | regalos digitales parejas emprende | ES11 | 1 | Cursos Digitales S&A (BOB, não identificado) |
| Q29 | retrospectiva pareja regalo | ES11 | 0 | — |
| Q4 | revenda páginas personalizadas | BR | 1 | irrelevante (sublimação) |
| Q5 | retrospectiva namoro | BR | 1 | **CoupleRewind** "Reconquiste o amor dela 💖" |
| Q6 | retrospectiva | BR | 403 | ruído (buffets, eventos) |
| Q7 | vender páginas personalizadas | BR | 28 | só "páginas de vendas" (Ganhardinheiro FN, Guih Tech). Nenhuma página de amor |
| Q8 | site personalizado namorada | BR | 9 | **amoreetech** + ruído (quadros, roupa) |
| Q9 | presente digital namorado | BR | 21 | **TimelineLove**, **qartinha**, **Seu Amor** + canção IA (Alot Digital) |
| Q11 | renda extra presentes digitais | BR | 17 | nenhuma oferta de páginas (gráficos natalinos, moldes) |
| Q27 | sites personalizados renda extra | BR | 2 | ruído |
| Q30 | site do namoro presente | BR | 11.094 | ruído total |

### H2 — invitaciones web
| # | Termo | Países | est. | Leitura |
|---|---|---|---|---|
| Q2 | invitaciones digitales | MX,CO,AR,CL,PE,US | 1.169 | ~20 microempresas B2C (Corazón de Fiesta, Invi Digi, Subligraf, Pearl Atelier, Calixta Card, Limasystem, Miboda.love…) + kits (Mega Plantillas USD; Ana Rosa BRL) |
| Q16 | invitaciones digitales para vender | ES11 | 86 | **kits de revenda**: Mega Plantillas, Web Online, Kit Digital, Creativa Pack Studio, Bruno Lero (BRL), Ana Rosa (BRL), Papelería Creativa (BRL), rede "6U$D" (Asesoría digital, Digitalizaciónonline, Laprofesióndelfuturo, Impulsodigital360, Emprende con IA), Diseñando Eventos |
| Q17 | invitación web | ES11 | 653 | serviço B2C: Limasystem (7 nos 50), Invita Kairós "$99", DLC.Invitaciones, She Said Web, My Invite, Arte Invita "Aparta con $199", Atentamente, vivaboda, Calixta Card |
| Q18 | aprende a hacer invitaciones digitales | ES11 | 1.035 | ruído total; nenhum curso de invitación visível |
| Q19 | invitación confirmación de asistencia | ES11 | 463 | **~32 anunciantes distintos em ~1,3 dia**, quase todos serviço B2C (andoinvitando, Fecha Link, Invita Kairós, Limasystem, Auras "desde $499 MXN", Marqstudio, Arte Invita, Valery Digital, My Invite, Dayfold.mx, Bloomka, Jose Jwtm "desde $5", Paola CM "DESDE $250", Bunti, Invitae…) |
| Q22 | invitación digital XV años | ES11 | 225 | serviço B2C + **Event Builder Studio** (USD) "Crea invitaciones digitales para tus clientes" (ferramenta B2B p/ revendedor) + Invitio "Pago único" |
| Q23 | invitación digital baby shower | ES11 | 139 | serviço B2C (InvitArte, Invidi, Invítalo.cl, Craedis, Ayayita "Invitación Web Interactiva de Winnie Pooh", Angie video invitaciones, Video invitaciones Reina) |
| Q31 | invitaciones digitales para tus clientes plataforma | ES11 | 1 | ruído |
| Q32 | emprende invitaciones interactivas | ES11 | 9 | **Someri** (MXN) "$119.20 … Ideal Para Emprendedores … Vende Invitaciones por WhatsApp … Invitaciones de Video"; Invictationes Digitales (BRL) "💸 Emprende desde casa vendiendo invitaciones digitales"; Genios Online e Morador marketer (COP) "CURSO EMPRENDE CON INVITACIONES DIGITALES"; Emprende.con.Gloria "+1,000 alumnos"; Aprende más (PEN) "+120 plantillas editables para tu boda" |
| Q20 | convite digital renda extra | BR | 11 | formula_do_convite_digital, KitsFesta, phil_wokoski (curso renda extra) |
| Q21 | convite interativo vender | BR | 8 | **Convitia** "Fature até R$250 por Convite Digital!", **O Poder das Mulheres no Digital** "CONVITES CINEMATOGRÁFICOS" |

Buscas feitas por outros agentes e usadas só como referência cruzada (não refiz): "invitación digital interactiva" 129; "invitación interactiva" 200; "vender invitaciones digitales" 88; "invitaciones interactivas para vender" 18; "video invitación" 1.955; "plantillas de invitaciones" 262; "convite interativo" BR 598; "retrospectiva namorados" BR 2 (arquivos fase1_brasil_espelho.md, fase1_meta_servicos.md, fase1_hotmart_es.md).

---

## 2. Anunciantes medidos por page_id

### H1 — páginas de amor (todos B2C: vendem a página pronta ao comprador final; nenhum vende o modelo de revenda)
| Página (page_id) | Mercado | Ads ativos | Dias do mais antigo | Títulos | Snapshot |
|---|---|---|---|---|---|
| CoupleRewind (567707623099366) | BR | 10 | 149,8 | "Reconquiste o amor dela 💖", "Reconquiste o coração dele 💙" | https://www.facebook.com/ads/library/?id=936194465917663 ; https://www.facebook.com/ads/library/?id=1625590875588295 |
| TimelineLove (594839090389230) | BR | 4 | 85,8 | "Como criar o site do seu namoro", "Esse é o presente mais criativo que você vai dar para seu amor", "Fuja do óbvio e dê um presente que vai emocionar de verdade" | https://www.facebook.com/ads/library/?id=995698710027385 ; https://www.facebook.com/ads/library/?id=1502835541109511 |
| qartinha (609373092256963) | BR | 2 | 173,6 | (sem título) | https://www.facebook.com/ads/library/?id=945751598008146 |
| Seu Amor (861232237067175) | BR | 3 | 338,5 | "Homenagens para o seu Amor" | https://www.facebook.com/ads/library/?id=800102429668832 |
| amoreetech (611790298694873) | BR | 2 | 457,1 | (sem título) | https://www.facebook.com/ads/library/?id=1323842319191326 |
| lovecupido_ofc (1176480235546962) * | BR | 1 visto | 101,6 | retrospectiva de namorados | https://www.facebook.com/ads/library/?id=888647297597053 |
| Presentim (1103529692842159) * | BR | 1 visto | 144,5 | retrospectiva de namorados | https://www.facebook.com/ads/library/?id=946262721505177 |
| Daniela Michilena (688632704343010) | ES (USD) | 14 | 46,2 | "💝 El regalo que jamás olvidará", "🥹 Un regalo que no olvidará" — **produto não identificado** (pode ser canção, página ou livro) | https://www.facebook.com/ads/library/?id=1730980927837398 ; https://www.facebook.com/ads/library/?id=914427708152061 |
| Impulso digital (1396249443561994) | PE | 5 | 11,2 | "🌻 ¡Sorprende con Flores Amarillas!" (sazonal, 21/set) | https://www.facebook.com/ads/library/?id=1433593615534414 |
| Aprendamos IA con Fer (112210798037496) | ES (USD) | 9 | 61,1 | títulos genéricos; apareceu em "vende páginas personalizadas". **Não identificado** | https://www.facebook.com/ads/library/?id=1278996131960184 |
| Nova Studio (1128150357058785) | PE | 2 | 64,9 | sem título. **Não identificado** | https://www.facebook.com/ads/library/?id=3204560966402674 |
\* medido por outro agente (fase1_brasil_espelho.md).

**Revenda de páginas de amor (o modelo exato da H1):** 0 anunciantes encontrados em 12 buscas ES e 6 buscas BR voltadas para isso. A busca por palavra solta tem limites, então isso não prova que não existe. Mas não houve nenhum sinal positivo, nem no Brasil, que é onde a categoria B2C está mais madura (7 anunciantes com 85–457 dias).

### H2 — kits/ferramentas para vender convites (modelo de revenda)
| Página (page_id) | Moeda | Ads ativos | Dias do mais antigo | Títulos | Snapshot |
|---|---|---|---|---|---|
| Kit Digital (433531919848589) | CLP | 16 | 118,8 | "Solo a $3500💜" (~US$3,7, estimativa), "Obtén el tuyo ahora💜", "Revisa nuestro material exclusivo" — conteúdo não verificado | https://www.facebook.com/ads/library/?id=1376630554316244 ; https://www.facebook.com/ads/library/?id=975658698913214 |
| Mega Plantillas Digitales (1154408571089804) | USD | 10 | 49,5 | "Mira como funciona📱" (9), "Ver invitaciones digitales ✨" | https://www.facebook.com/ads/library/?id=1708910720392963 ; https://www.facebook.com/ads/library/?id=3711236485701842 |
| Web Online (1105601812626238) | PEN | 9 | 21,4 | "CURSO PASO A PASO +1200 INVITACIONES listas para VENDER" (E1 parcial) | https://www.facebook.com/ads/library/?id=2313998366006369 |
| Someri (104137866122244) | MXN | 3 | 8,5 | "$119.20 … Incluye Bodas y XV Años … Ideal Para Emprendedores … Vende Invitaciones por WhatsApp … Invitaciones de Video"; "EMPIEZA HOY POR SOLO $99 … ANTES $249" | https://www.facebook.com/ads/library/?id=1950759622550013 ; https://www.facebook.com/ads/library/?id=1392068805735135 |
| Creativa Pack Studio (1173011945891969) | USD | 1 | 4,4 | "Invitaciones premium listas para vender 💍" | https://www.facebook.com/ads/library/?id=1450835596895541 |
| Invictationes Digitales (1250088564854288) | BRL (BR vendendo em ES) | 3 | 13,5 | "💸 Emprende desde casa vendiendo invitaciones digitales" | https://www.facebook.com/ads/library/?id=1591072372564444 |
| Event Builder Studio (655700850956283) | USD | 1 | 2,2 | "Crea invitaciones digitales para tus clientes" (ferramenta B2B para revendedor) | https://www.facebook.com/ads/library/?id=1056284580730092 |
| Aprende más (1147621821772902) | PEN | ~33 (loja com várias ofertas; 8 do pack boda) | 97,3 (pack boda) | "+120 plantillas editables para tu boda" | https://www.facebook.com/ads/library/?id=1828872404777423 |
| Diseñando Eventos - Cursos Online (104933269211198) | USD | ~49 (est. do lote) | ≥16,9 (limite inferior) | papelaria de festa (Halloween, Día de Muertos, "Más de 100 Diseños para Crear y Vender"). Não é convite web | https://www.facebook.com/ads/library/?id=4503277299952753 |
| Genios Online (103961612783471) * | COP | 4 | 77,2 | "EMPRENDE CON INVITACIONES DIGITALES" (curso, E1) | https://www.facebook.com/ads/library/?id=2004948203720677 |
| Morador marketer (103001559484790) * | COP | ~14 | 77,3 | "CURSO EMPRENDE CON INVITACIONES DIGITALES" | https://www.facebook.com/ads/library/?id=1529789795491834 |
| Educacion nexus (1138492386003949) * | COP | 24 | 59,9 (convite) | "Invitaciones Interactivas que Sorprenden 🎉" | https://www.facebook.com/ads/library/?id=1015627584605774 |
| Rede "6U$D": Asesoría digital (1104144052790356), Digitalizaciónonline (1294794033723838), Laprofesióndelfuturo (1286388787896891), Impulsodigital360 (1344499118746066), Emprende con IA (1351772444677949) | USD/PYG | 4 / 4 / 7 / 6 / 2 nos 50 | ≤5 (vistos) | "SOLO POR 6U$D", "Accede al MEGAPACK mas completo por solo 6U$D" — megapack não identificado; **E4 suspeita** (várias páginas com a mesma oferta, típico de PLR) | https://www.facebook.com/ads/library/?id=1053810084318032 ; https://www.facebook.com/ads/library/?id=2433925800352136 |
\* medido por outro agente (fase1_meta_servicos.md).

### H2 — convite web B2C / SaaS (a demanda do cliente final que o revendedor atende)
| Página (page_id) | Moeda | Ads ativos | Dias do mais antigo | Títulos | Snapshot |
|---|---|---|---|---|---|
| Invitaciones Digitales My Invite (104026075741755) | MXN | 16 | 116,3 | "Invitaciones digitales web para bodas con confirmación de asistencia automática", "Invitación Digital para XV" | https://www.facebook.com/ads/library/?id=1894344334607556 |
| Invitio (106968579101299) | MXN | 12 | 112,5 | "Por sólo 599 MXN \| Pago único ✨", "La app que usan miles de eventos en México🔥", "Pruébala Gratis 🔥" | https://www.facebook.com/ads/library/?id=1701673927750048 |
| Miboda.love (303780449964646) | MXN | 16 * (4 vistos aqui, truncado) | 108,9 * (48,3 visto aqui) | "Mucho más que una invitación digital.", "¿Te casas en noviembre o diciembre?" | https://www.facebook.com/ads/library/?id=1741895243716839 |
| Tarjetas Interactivas (553991364473786) * | ARS | 10 | 126,5 | — | (fase1_meta_servicos.md) |
| Corazón de Fiesta (954937514371674) | MXN | ≥43 (lote truncado) | ≥64,4 (limite inferior) | "Envíame Whats" (serviço por WhatsApp) | https://www.facebook.com/ads/library/?id=1627536802135201 |
| Invi Digi (1029623536892040) | MXN | ≥5 | ≥54,5 (limite inferior) | "Invitaciones para todo tipo de eventos" | https://www.facebook.com/ads/library/?id=1230300875866315 |
| Limasystem (896661073520377) | PEN | 10 | 10,4 | "Invitación web + sistema RSVP desde S/125.90", "Tu invitación de boda desde S/ 95.90" | https://www.facebook.com/ads/library/?id=1066163912961541 |
| Confirm the date (800013626539565) | USD | ≥2 (vistos na busca; página não medida) | ≥26,0 | "Tus invitados confirman. Tú disfrutas.", "Solicita tu demo personalizado gratis" | https://www.facebook.com/ads/library/?id=1748439102723979 |
\* medido por outro agente.

### Espelho BR H2
| Página (page_id) | Ads ativos | Dias do mais antigo | Títulos | Snapshot |
|---|---|---|---|---|
| Convitia - Convite Digital Interativo (628646776989656) | 33 | 76,9 | B2C: "Crie seu convite de casamento grátis", "Veja seu convite antes de pagar", "Seu convite pode começar com 1 prompt ✨", "Crie sua lista de presentes com taxa zero — receba pelo PIX". Revenda: "Fature até R$250 por Convite Digital!" (4), "Ganhe até R$200 por convite de 15 anos", "150+ Modelos Profissionais para Lucrar Hoje Mesmo!" (2), "Pare de começar cada convite do zero", "Aprenda a criar convites cinematográficos 🎬" | https://www.facebook.com/ads/library/?id=1042494484973953 ; https://www.facebook.com/ads/library/?id=2146534716078562 ; https://www.facebook.com/ads/library/?id=926250710492880 |
| O Poder das Mulheres no Digital (171452656057863) | 7 | 38,3 | "CONVITES CINEMATOGRÁFICOS" (provável curso ou kit de convite em vídeo; não verificado) | https://www.facebook.com/ads/library/?id=1412094170985815 |
| formula_do_convite_digital (816819528173895) | 2 | 391,4 | (sem título) | https://www.facebook.com/ads/library/?id=1943227963129540 |
| KitsFesta (1029675093572020) | 3 | 127,3 | "👉 comente "EU QUERO" que te envio" | https://www.facebook.com/ads/library/?id=2184472379063317 |
| Canva Para Noivas (663864766819174) * | 35 | 88,9 | "Convites digitais interativos por R$47", "Sua papelaria inteira por R$67" | https://www.facebook.com/ads/library/?id=1313617404312022 |

---

## 3. Preços observados
**Minha cota de WebSearch acabou na 1ª chamada** (200/200 buscas usadas na sessão). Os preços da Hotmart abaixo são dos snippets de busca que outros agentes coletaram. Não abri nenhum checkout (WebFetch bloqueado).
- Kits Hotmart de invitaciones (fase1_meta_servicos.md):
  - "Negocio de Invitaciones Digitales: PACK BODA Y QUINCEAÑOS", US$5: https://pay.hotmart.com/T102280557H
  - "Tarjetas de Invitacion Digital y Shaker", US$5: https://pay.hotmart.com/M102400480I
  - "Invitaciones Digitales desde Cero", US$10: https://pay.hotmart.com/V103706751K
  - "Invitaciones Digitales Interactivas para Eventos", US$14,99: https://pay.hotmart.com/K102179105D
  - "Invitaciones de boda (Personalizado)", US$60 (serviço): https://pay.hotmart.com/H94034940L
- Produtos Hotmart ES de invitaciones com preço não verificado: https://hotmart.com/es/marketplace/productos/invitaciones-digitales-tipo-sitio-web/O101247541J ; https://hotmart.com/es/marketplace/productos/curso-para-emprender-con-invitaciones-digitales-interactivas/L83087551J (curso) ; https://hotmart.com/es/marketplace/productos/negocio-de-invitaciones-infantiles-de-principiante-a-experto/I86554392L ; https://hotmart.com/es/marketplace/productos/guia-completa-como-vender-invitaciones-digitales-desde-casa/H102322061B ; mais 8 em fase1_hotmart_es.md T1.
- Kits na Meta (preço no título do anúncio): Someri MXN $99–119,20 (~US$5,5–6,6, estimativa com ~18 MXN/USD); Kit Digital CLP 3.500 (~US$3,7, estimativa); rede "6U$D" US$6.
- Preço que o cliente final paga pelo convite web (é o preço que o revendedor cobraria; títulos de anúncio):
  - México: Invita Kairós "$99" MXN; Arte Invita "Aparta con $199"; Paola CM "desde $250" MXN; Auras "desde $499" MXN; Invitio "599 MXN pago único"
  - Peru: Limasystem S/95,90–125,90; TarjetaViva "Desde S/100" *
  - Outros: Jose Jwtm "desde $5" USD; Rodrigo Pericon Bs 50 (~US$7) *
  - Brasil: R$37–99,90 (convitedigitalinterativo.com.br, Personalize Conviteria, UniConvite *)
- Página de amor B2C em ES: iloveyou.gift "desde $5"; QLovy (grátis 24h + pagamento único); MiYo Gift; Gifft.me (fase1_meta_servicos.md, WebSearch de outro agente). Preço BR (CoupleRewind, TimelineLove etc.): não verificado.
- Revenda de páginas de amor: **não encontrei nenhuma oferta**, então não há preço de referência.
- SaaS de convite com painel para revendedor (white-label): só apareceu Event Builder Studio, e o preço não foi verificado. A busca "plataforma invitaciones digitales" no WebSearch **não foi feita** (cota esgotada).

---

## 4. Sub-ideias registradas
1. **Kit de revenda de invitación web de XV años** (editor + 20–30 modelos XV + script de WhatsApp). O XV aparece em Limasystem, My Invite (XV), DLC, Calixta Card, Convitia BR ("Ganhe até R$200 por convite de 15 anos"). Q22 = 225.
2. **Editor self-service de invitación web B2C** (a pessoa monta o próprio convite por US$5–9). É o DNA do Mimo trocando o destinatário (festa em vez de parceiro). Contraparte B2C da H2. Em ES só aparecem serviço por encomenda e SaaS a 599 MXN ou mais; não vi editor low ticket em ES (o outro agente chegou à mesma conclusão).
3. **Pack de video-invitaciones / "convites cinematográficos" para revenda**: Someri "Invitaciones de Video", Angie video invitaciones, Video invitaciones Reina, O Poder das Mulheres (BR, 38,3 d), Convitia "Aprenda a criar convites cinematográficos". Riscos: E2 e propriedade intelectual (personagens).
4. **Página-presente sazonal "Flores Amarillas" (21/set)**: Impulso digital e Rock N Roll MKT (PEN) no pico sazonal. É um ângulo de data para a H1 B2C, não um produto que se sustenta sozinho.
5. **Ângulo "reconquista"** da página de amor (CoupleRewind BR, 10 ads, 149,8 d: "Reconquiste o amor dela"). Serve de ângulo para Mimo ou H1, não é produto novo.
6. **Papelaria de boda editável + convite interativo** (Canva Para Noivas BR 35/88,9 d; Aprende más PE "+120 plantillas editables para tu boda" 97,3 d). Já está no arquivo de outro agente.

---

## 5. Leitura (inferência, não medição)
- **H1 (revenda de páginas de amor):** a categoria B2C dura muito no BR (7 anunciantes com 85–457 dias, mas poucos anúncios por página: 2–10). Em ES a categoria quase não aparece na Meta por busca de palavra. Para o *modelo de revenda* não achei **nenhum** anunciante, nem em ES nem em BR. Então não há prova de que alguém compre "licença para vender páginas de amor". O anúncio teria que vender a promessa ("gana vendiendo páginas") → E2 forte. A demanda final existe (o próprio Mimo é a prova), mas não se vê o "revendedor" como comprador.
- **H2 (invitaciones web):**
  - A demanda final é grande e comprovada: dezenas de microempresas em ES anunciando convite web com RSVP, ~32 anunciantes distintos em ~1,3 dia só num termo, com preço final de US$5 a US$30.
  - O público que compraria um kit de revenda já age como revendedor: são essas microempresas.
  - Os kits de revenda existem e duram: Kit Digital 118,8 d, Mega Plantillas 49,5 d, Genios/Morador 77 d. Em BR, Convitia (33 ads/76,9 d) roda os dois ângulos, B2C e renda extra.
  - Os kits vistos são quase todos templates Canva ou PowerPoint, e não uma ferramenta que gera uma página web interativa. O "motor" com RSVP, contagem e música como kit low ticket em ES só aparece em Event Builder Studio (1 ad, 2,2 d) e em produtos Hotmart com preço não verificado.
  - Riscos: E2 moderado (ângulos "listas para VENDER" / "Fature até R$250"); E4 leve (rede 6U$D, packs de revenda); E3 se o revendedor precisar de suporte; E5 moderado (editor + hospedagem de páginas dos clientes do revendedor + RSVP).

---

## 6. Falhas e limitações
- **WebSearch esgotado**: "this session has used its web search budget (200 of 200)" já na primeira chamada. Buscas não feitas: `vender páginas personalizadas para parejas negocio regalo digital WhatsApp`, `site:hotmart.com página personalizada pareja regalo digital`, `plataforma invitaciones digitales` (SaaS/white-label), preços de Convitia/Invitio/Event Builder Studio, `site:pay.hotmart.com` para H1. Preços vieram só dos arquivos de outros agentes (citados).
- WebFetch/curl bloqueados (não tentei, conforme instrução).
- A busca por palavra solta dá ruído nos termos de amor em ES. Não consegui isolar concorrentes ES da página de amor pela Meta. Isso **não prova que não existem**.
- Consultas com várias páginas ficaram truncadas em 50 (Corazón de Fiesta, Miboda.love, Invi Digi, Diseñando Eventos): nº de ads e idade = limite inferior; para Miboda usei a medição de outro agente (16/108,9 d).
- Produto não identificado (sem texto do anúncio): Daniela Michilena, Kit Digital, rede 6U$D, Aprendamos IA con Fer, Nova Studio, Mundo Digital, qartinha, amoreetech, O Poder das Mulheres no Digital.
- Anúncio antigo com poucas variações (Seu Amor 338 d / 3 ads; amoreetech 457 d / 2 ads; formula_do_convite_digital 391 d / 2 ads) pode ser anúncio esquecido com gasto baixo → proxy fraco.
- Câmbio usado só para ordem de grandeza (estimativa): ~18 MXN, ~3,7 PEN, ~950 CLP por USD.
