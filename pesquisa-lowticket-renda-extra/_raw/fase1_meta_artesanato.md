# Fase 1: Meta Ads Library (ES), artesanato, receitas, fornecedores, templates e moldes

Data da coleta: 2026-09-22. Referência de "agora": epoch 1790095977. Dias ativo = (1790095977 - ad_delivery_start_time)/86400.
Ferramenta: `mcp__Meta_Ads__ads_library_search`, ad_active_status=ACTIVE, limit 50, países MX, CO, AR, CL, PE, EC, GT, BO, UY, DO, US (todos juntos em cada busca por palavra-chave).
Complemento: WebSearch (hotmart.com / pay.hotmart.com). WebFetch/curl não foram tentados (bloqueados pela rede, conforme instrução).

## 0. Leituras de método (importante para interpretar os números)

1. **Rotação diária de criativos.** Quase todos os anunciantes low-ticket desse território recriam os anúncios em lotes a cada 1 ou 2 dias. Exemplos: Entre Mujeres tem 153 ativos, todos criados no mesmo lote (~8h antes da coleta), e 230 no histórico total. 1500 Moldes de Costura tem lotes em 1789430554, 1789605851, 1789690453, 1789796120 e 1790052808. Por isso o "dias do anúncio mais antigo" **subestima** a longevidade da oferta nesses anunciantes. O proxy mais útil aqui é **nº de anúncios ativos + nº de páginas distintas vendendo a mesma oferta**. Quando aparece um anúncio com 30+ dias, isso é exceção e vale como sinal forte.
2. **Modelo "Primero recibes y luego pagas".** O modelo aparece em massa nos recetarios e moldes: Sofia Zantini, Chef Eli, Caixa Academy, Mundo Fácil, Universo Digital, Recetas desde Casa, Saber Mas, Aprende Fácil, Tus Moldes, Bendiciones diarias, Club recursos digitales, Myrlo Educa, Academia Online. É venda por WhatsApp com cobrança **depois** da entrega, ou seja, digital "contra entrega". Nesse modelo há atendimento humano por venda (suspeita de E3). No Hotmart o modelo não existe, porque o pagamento é antecipado. Quem copiar a oferta precisa converter com checkout normal.
3. **Operações BR vendendo em espanhol.** Várias páginas com moeda BRL anunciam em ES: Sueli Almeida ("Converse conosco"), Giulia Moretti, Ajudando Laurinha, Mini Postres Virales, Chef Sofía Martínez, e sobretudo o cluster "Papelería Creativa" (João Carlos, Leticia Souza, Bella Collins, CreaFiesta, Charlotte Smith, Sofía Valenzuela, Bruno Lero, artcreativa.sbs, Método CVP, Papelaria Creeativaa). É exatamente o padrão "oferta validada no BR traduzida para ES" (DNA 6).
4. Sem o corpo do anúncio, o produto de algumas páginas **não é identificável** só pelo título: Bonito Digital, Aula Mágica, Richard Delgado, Impulsa Tu Negocio, Carojo, De fiesta, Espacio Creativo e Cursos Virtual Pro. Marquei como "incerto".
5. Preços em moeda local foram convertidos por **estimativa** (aprox.): 1 USD ≈ 3,7 PEN, 18,5 MXN, 4.000 COP, 930 CLP, 7,7 GTQ, 6,9 BOB.

## 1. Queries rodadas (palavra-chave, 11 países, ACTIVE)

| # | search_terms | estimated_total_count | observação |
|---|---|---|---|
| Q1 | postres para vender | 1.120 | ~20 páginas de recetario digital; muito "primero recibes" |
| Q2 | recetas para vender | 3.042 | inclui cursos, saúde e pastelarias físicas |
| Q3 | gelatinas para vender | 104 | Sofia Zantini (9), Sueli Almeida (14+), PostreVida "S/5" |
| Q4 | paletas para vender | 180 | Impulso Creativo, Hi Pop, El Club del Helado, Paletas Gourmet, Universo Literario "CLP 2.500" |
| Q5 | velas artesanales | 1.691 | mistura lojas físicas de velas e cursos (E1) |
| Q6 | jabones artesanales | 1.236 | idem; Ajudando Laurinha (BRL), Ana Moraes "2.178 reseñas" |
| Q7 | amigurumi patrones | 353 | Tejidos y Crochet, Aula Mágica, Mundo Virt, Creando Amigurumis |
| Q8 | resina epoxica | 1.433 | quase tudo físico/insumos/talleres presenciais; Mentoría Global "Oficios Pro" (bundle de cursos) |
| Q9 | moldes de piñatas | 17 | baixo; Conexión Emprendedora (75,6d), De fiesta (97,9d, incerto) |
| Q10 | arreglos con globos | 452 | quase tudo serviço físico de decoração |
| Q11 | lista de proveedores | 10.418 | match amplo e ruidoso, pouco relevante |
| Q12 | proveedores China | 1.508 | cursos/webinars de importação (Dany Travel 30+ ads, Método TIV 8) → E1 |
| Q13 | directorio de proveedores | 116 | Cenzi (extensiones), Reactor Químico, EmprendeSeguro |
| Q14 | proveedores mayoristas para emprender | 85 | atacadistas físicos, irrelevante |
| Q15 | plantillas Canva editables | 775 | ISA (empaques), Inu studio (imprimibles), Kit Anfitrión 5 Estrellas |
| Q16 | calculadora de precios emprendedores | 35 | Latinas Together (GastroKit), Herramientas PRO, Serendipity |
| Q17 | moldes de costura | 873 | **forte**: Entre Mujeres 153 ativos, 1500 Moldes 113 ativos, Alma Costurera 47 |
| Q18 | imprimibles para vender | 159 | Bonito Digital 27, Sello Propio (Natura), Agendas 2027 |
| Q19 | plantillas para redes sociales emprendedoras | 3 | quase nada |
| Q20 | desayunos sorpresa emprender | 34 | Decoración Con Globos (56,2d, curso), Cajitas de Amor (catálogo) |
| Q21 | recetario | 7.249 | inclui fitness/saúde; ruído |
| Q22 | patrones crochet pdf | 202 | Hoshihana (+6.000), Giulia Moretti, Tejidos y Crochet, DecorCraft |
| Q23 | moldes de cajas para imprimir | 48 | Moldes Cajas Decorativas, Carojo (325,6d), Veronica Ventas/MX |
| Q24 | moldes goma eva | 62 | **5 páginas com a mesma oferta "+2000 moldes"** |
| Q25 | plantillas para revendedoras | 2 | só Sello Propio |
| Q26 | kit imprimible cumpleaños editable | 3 | só cienacres.imprimibles (469,5d) |
| Q27 | bisutería miyuki patrones | 4 | baixo |
| Q28 | etiquetas escolares editables | 49 | cluster "papelería creativa"; Espacio Creativo (82,4d) |
| Q29 | papelería creativa kit plantillas | 54 | **~25 páginas distintas**, muitas BRL |
| Q30 | diseños para sublimar | 187 | ~10 páginas de pack digital + lojas físicas de sublimação |

## 2. Medição por anunciante (page_ids, ACTIVE, limit 50)

| Página | page_id | Oferta (título) | Ativos | Dias do mais antigo | Link exemplo |
|---|---|---|---|---|---|
| cienacres.imprimibles | 461588617027210 | kits imprimibles (sem título) | 4 | **469,5** | https://www.facebook.com/ads/library/?id=1620243371983362 |
| Carojo Aprende y Emprende | 152908757899058 | "4.9/5.0" (produto incerto; veio em moldes de cajas) | 9 | **325,6** (outros 163,9 / 153,7 / 137,9) | https://www.facebook.com/ads/library/?id=1498175651393089 |
| Papelería Creativa (BRL) | 1070020366204559 | "La promo termina pronto… y aún no descargaste tu kit." | 1+ (visto na busca) | **101,9** | https://www.facebook.com/ads/library/?id=1517888309821966 |
| De fiesta | 1193895630474335 | sem título (incerto, pode ser loja física) | 5 | **97,9** | https://www.facebook.com/ads/library/?id=2001841610449530 |
| DecoKit Shop | 737352542803130 | "Tu negocio puede empezar con esto" | 2 (vistos na busca) | **90,2** | https://www.facebook.com/ads/library/?id=1477793531027394 |
| Espacio Creativo | 510930015432339 | "Chatea con Nosotros" (WhatsApp; veio em etiquetas escolares) | 14 | **82,4** (vários 65–72d) | https://www.facebook.com/ads/library/?id=1651569109650285 |
| Conexión Emprendedora | 514896881696720 | "ACCESO INMEDIATO" (veio em moldes de piñatas) | 3 | **75,6** | https://www.facebook.com/ads/library/?id=27459940186981397 |
| Impulsa Tu Negocio | 1172504619283595 | sem título (veio em calculadora de precios; incerto) | 10 | **72,2** | https://www.facebook.com/ads/library/?id=1533541694900092 |
| Decoración Con Globos | 163208480219527 | "CURSO VIRTUAL" / "5 PROGRAMAS VIRTUALES POR $15.000" COP | 5 | 56,2 | https://www.facebook.com/ads/library/?id=1382299087338977 |
| Mundo Creativo Digital | 1068130303039496 | "+10,000 recursos listos para editar en Canva" | 8+ (busca) | 37,4 | https://www.facebook.com/ads/library/?id=2291254541708920 |
| Envinil.com | 221014007754159 | "Más de 2,000 diseños para vinil por solo $197 MXN + Bonus" | 2 (busca) | 28,8 | https://www.facebook.com/ads/library/?id=1741139417615425 |
| Alma Costurera | 1269214432943794 | "Descárgalos ahora" (moldes) | 47 | 26,3 | https://www.facebook.com/ads/library/?id=1088854613831124 |
| Veronica Ventas / Veronica MX | 1276073018925773 / 1267079633165871 | "Moldes de fiesta listos para imprimir" (2 páginas) | 3 + 2 (busca) | 25,0 | https://www.facebook.com/ads/library/?id=1634761194885820 |
| Moldes Cajas Decorativas | 413447005190625 | "+300 Moldes de Cajitas Decorativas" | 5 (busca) | 23,2 | https://www.facebook.com/ads/library/?id=1097880062567915 |
| Serendipity J&P | 2286687988232447 | "Calculadora de Precios para Emprendedores" | 3 (busca) | 12,9 | https://www.facebook.com/ads/library/?id=1606182844545250 |
| Diseña Creativo | 1162766426927858 | "¡Consigue tus plantillas por solo $89 MXN!" | 6 (busca) | 12,4 | https://www.facebook.com/ads/library/?id=1270026136202268 |
| Bonito Digital | 1253683197834637 | sem título (veio em imprimibles para vender) | 27 | 9,2 | https://www.facebook.com/ads/library/?id=1745429946694639 |
| 1500 Moldes de Costura | 841929342339578 | "DESCARGAR" (+ link api.whatsapp.com) | **113** (50+ limite) | ≥7,5 (limite inferior) | https://www.facebook.com/ads/library/?id=2471122273412389 |
| Sueli Almeida (BRL) | 913897521798413 | "Postres de boutique desde tu casa" | 25 | 7,5 | https://www.facebook.com/ads/library/?id=1404167268589740 |
| Mundo Creativo | 1004349699421673 | "Pack +2000 Moldes de Goma Eva" | 14 | 5,4 | https://www.facebook.com/ads/library/?id=1091211326713642 |
| Richard Delgado | 136833262838624 | "¡Empezar ahora! / Commence maintenant! / Şimdi Başla / (árabe)" (incerto; veio em velas/jabones) | 33 | 3,8 | https://www.facebook.com/ads/library/?id=1792792165395180 |
| Cenzi Beauty Salons | 1321069997736828 | "Directorio Premium de Proveedores de Extensiones" (5 dos 8) | 8 | 3,5 | https://www.facebook.com/ads/library/?id=1409222934466487 |
| Chef Eli | 989650777564708 | "Primero recibes y luego pagas!" (numerados 6–15) + WhatsApp | 32 | 3,3 | https://www.facebook.com/ads/library/?id=28954269907510218 |
| Latinas Together | 219870772214056 | GastroKit: "Tu receta, tu precio, en segundos" / "Todo el GastroKit hoy por $57" | 13 | 1,5 | https://www.facebook.com/ads/library/?id=1057383214053948 |
| Mundo Foami | 1451706391348713 | "+2000 moldes de Goma Eva · S/ 12.90" (vender / aula) | 12 | 1,2 | https://www.facebook.com/ads/library/?id=2199268927598296 |
| Florencia Moreira | 1172869515903696 | "Método Aroma Queen — Guía completa + 9 bonos", "4,9 de 5 · 739 Reseñas" | 14 | 0,9 | https://www.facebook.com/ads/library/?id=1347787477182417 |
| Giulia Moretti (BRL) | 1058796797324269 | "+2.632 reseñas (4.95/5.0)" (crochet) | 9 | 0,5 | https://www.facebook.com/ads/library/?id=1427378629334609 |
| Hoshihana Shop | 722458774285309 | "+6.000 Patrones en PDF" | 9 | 0,4 | https://www.facebook.com/ads/library/?id=1447476493893273 |
| Herramientas PRO | 429125386950426 | "Kit de 7 Días para Tomar el Control de tu Negocio y Multiplicar tus Ganancias" | 8 | 0,4 | https://www.facebook.com/ads/library/?id=28955046107454054 |
| Aula Mágica | 934166036453158 | "Disponible" (incerto; veio em amigurumi) | 34 | 0,3 | https://www.facebook.com/ads/library/?id=2421581784918061 |
| Tejidos y Crochet | 1222570877617282 | "+1000 Patrones Verificados en Español + 6 Bonos"; "Pruébalo 15 días…" | 6 | 0,3 | https://www.facebook.com/ads/library/?id=1432152345461217 |
| Sello Propio | 1310658882133067 | "360 Diseños - Revendedoras Natura" | 10 | 0,3 | https://www.facebook.com/ads/library/?id=2156814638591939 |
| Entre Mujeres | 1180416348492259 | "Acceso exclusivo a 200+ patrones digitales en PDF" | **153** (230 no histórico ALL) | 0,1 (lote recém-criado) | https://www.facebook.com/ads/library/?id=909768015290442 |
| Especialista Sofia Zantini | 1277309992142835 | "Primero Recibes Las Recetas y Después Pagas." | 9 | 0,1 | https://www.facebook.com/ads/library/?id=2132493034287794 |
| Ajudando Laurinha (BRL) | 1380315488479842 | "Quiero saber más" (incerto; veio em velas/jabones) | 19 | 0,1 | https://www.facebook.com/ads/library/?id=1013218625063771 |
| Mini Postres Virales (BRL) | 1222476140938267 | "Recetario de Mini Postres +615 recetas" | 1 | 0,05 | https://www.facebook.com/ads/library/?id=1403402902003047 |

## 3. Notas por território

### 3.1 Recetas para vender
- "postres para vender" 1.120 / "recetas para vender" 3.042 / "gelatinas" 104 / "paletas" 180.
- Páginas de recetario digital vistas (≥20): Mini Postres Virales, Academia Repostera Emprendedora ("Recetario digital de Mini Cheesecakes"), Academia Dulce Emprende ("LIBRO DIGITAL DE POSTRES"), Academia de Repostería Gourmet, Especialista Sofia Zantini, Chef Eli, Caixa Academy, Dulce Encanto Pastelería, Universo Digital, Mundo Fácil, Sofía Mendoza ("100 Recetas de Tiramisú Coreano + 4 Bonos por $9 USD", https://www.facebook.com/ads/library/?id=1418570293571960), Dolchere, Postre Negocios Dulces ("Ebook Rolls & Sushi Dulce"), Recetas desde Casa, ProAcademy ("Ebook Recetario Cheesecakes"), Sueli Almeida, Snacks Saludables Sofi (6 ads), PostreVida ("Llévalo por sólo S/5 soles", https://www.facebook.com/ads/library/?id=1401344795528608), Universo Literario ("Recetario +100 Recetas hoy $2.500" CLP, https://www.facebook.com/ads/library/?id=983981794711862), Impulso Creativo (paletas, "4.9/5 +1,200 clientes"), El Club del Helado, Paletas Gourmet, Hi Pop.
- O núcleo é PDF (não E1), mas grande parte vende no modelo WhatsApp "primero recibes" (E3 no modelo, não no produto). Preço observado: US$1,3–9.
- Hotmart (WebSearch): "Postres en vaso ¡que venden!" https://hotmart.com/es/marketplace/productos/hagsxd-postres-en-vaso-que-venden-t9zfe/G100594932O ; "10 recetas de postres caseros + fórmulas de costeo" https://hotmart.com/es/marketplace/productos/ebook-10-recetas-de-postres-caseros-formulas-de-costeo/K105947860I ; "100 Recetas de Postres Rentables para Emprender desde Casa" https://hotmart.com/es/marketplace/productos/100-recetas-de-postres-rentables-para-emprender-desde-casa/T103881974V ; "Combo +230 recetas" https://pay.hotmart.com/C88387570B . Preços não verificados.

### 3.2 Artesanato em PDF
- **Moldes de costura** (873): Entre Mujeres 153 ativos, 1500 Moldes 113, Alma Costurera 47 (26,3d), Taidy Hernández "45 Patrones Digitales por $3.000 CLP" (https://www.facebook.com/ads/library/?id=2286881178731056), Moldes Únicos "Antes $4.050 Ahora $3.000" CLP (https://www.facebook.com/ads/library/?id=1490782679769765), Patrones en PDF "+120 Moldes Infantiles en PDF" (https://www.facebook.com/ads/library/?id=1124678266754398), Edukits x6, Taller de Recuerdos x8 (ursos de lembrança?). Hotmart: "Kit 25 Moldes Costura Criativa em PDF" US$4 (https://pay.hotmart.com/X61954338R); "El Gran Libro de Patrones para Bolsos" US$14 (https://pay.hotmart.com/Y106083554Y); faixa US$4–19,99 segundo o resumo do WebSearch; "+200 Moldes de Marroquinería" https://pay.hotmart.com/L98768526A ; "800 Patrones de costura PRO" https://hotmart.com/es/marketplace/productos/800-patrones-de-costura-pro/A100384202A .
- **Crochet/amigurumi** (353 + 202): Hoshihana "+6.000 Patrones en PDF" (9), Giulia Moretti (9, BRL), Tejidos y Crochet (6; ângulos "Batallando con el video cada 20 segundos con las manos ocupadas" = PDF vs vídeo, "CUANDO EL PATRÓN DECÍA 'TRADUCIDO AL ESPAÑOL'", "Pruébalo 15 días", "Convierte 2 ovillos de lana en $30.000 CLP"), DecorCraft "+100 patrones exclusivos", Mis Tejidos (catálogo de livros), Creando Amigurumis "-77%OFF", Cursos Mágicos "Curso + Bonos por Q40", Tu-Top Crochet "Pack 5 Patrones de Bolsos", Emprende Fácil y Rápido "Gano más tejiendo que con mi jubilación". Hotmart: +1000 patrones US$19,9 (de US$95) e várias listagens: https://hotmart.com/es/marketplace/productos/1-000-patrones-de-amigurumis/F100091725Q ; https://hotmart.com/es/marketplace/productos/1200-patrones-amigurumis-en-tendencia/C81814215L ; https://hotmart.com/es/marketplace/productos/1000-patrones-de-llaveros-y-mini-amigurumis/M100562970V .
- **Goma eva/foamy** (62): 5 páginas vendem "+2000 moldes": Mundo Foami ("S/ 12.90", ângulos "para vender" e "para tu aula"), Mundo Creativo (14), Mi Masterclass Online ("+2500 Moldes de Foamy en PDF a solo S/10", "¡No vuelvas a rechazar un pedido!", https://www.facebook.com/ads/library/?id=1826847468454898), Academia Online ("+500 MOLDES DE GOMA EVA | 19 Bs", https://www.facebook.com/ads/library/?id=1083927087587325) e Tus Moldes ("Recibe primero, paga después"). Fora da Meta: kitmoldeseva.site "+2.000 moldes" por US$3,99 (https://kitmoldeseva.site/). Hotmart: MEGAPACK MOLDES FOAMY 2023 https://hotmart.com/es/marketplace/productos/megapack-moldes-foamy-2023/F80990841T .
- **Velas/jabones** (1.691 / 1.236): muito curso (E1) e loja física. Digital: Velvet Ecommerce (curso), El Mundo de los Cursos (curso), Taller Creativo Academia "4.8/5.0", Ana Moraes "4.9/5.0 (2,178 reseñas)" (https://www.facebook.com/ads/library/?id=948666801622176), Bendiciones diarias "PACK DIGITAL $99 MXN" (https://www.facebook.com/ads/library/?id=28335327712804234), Estación Saludable. Hotmart: "Megaebook Velas y Jabones – Aroma y Glow" US$15 (de US$37), com calculadora de custos e fornecedores (https://hotmart.com/es/marketplace/productos/hagsxd-megaebook-velas-y-jabones-artesanales-aroma-y-glow-kscxu/V100266138S); "Combo de Recetarios de Velas" https://pay.hotmart.com/J99674018O .
- **Aromas** (achado lateral em "directorio de proveedores"): Florencia Moreira, "Método Aroma Queen — Guía completa + 9 bonos | Acceso inmediato", 14 ads, "739 Reseñas". Ângulos: "No es una receta: es el negocio", "Cuesta un delivery. Se vende caro.", "Una hora. Seis productos.", "Que lleve tu nombre". Também Aroma Queen (960420037162583), El Club de las Creativas ("Aprende a crear tu línea de aromas desde cero") e Amor por las fragancias. Hotmart: "Aromas Artesanales Pro" https://hotmart.com/es/marketplace/productos/aromas-artesanales-pro/R97302961W ; "Difusores de aromas" https://hotmart.com/es/marketplace/productos/difusores-de-aromas/C101383420C .
- **Resina, piñatas, globos, bisutería**: sinal fraco ou dominado por cursos presenciais/serviço físico. Esencia Artesanal vende "Aprende Joyería con Resina por Q40" (5 ads, curso). Mundo Creativo 1145607445303727 anuncia "+500 mujeres ya crean y emprenden con Miyuki".

### 3.3 Fornecedores
- Sinal fraco em ES. "proveedores China" é dominado por cursos e webinars de importação: Dany Travel 30+ ads "Evento Virtual Sin Costo", Método importador TIV 8 ads, Jose López "Entra por $50 al mes". Isso é E1 com funil high ticket.
- Diretório como produto: Cenzi "Directorio Premium de Proveedores de Extensiones" (5 ads, 3,5d), Reactor Químico "Manuales, videos y directorio de proveedores" (limpeza, 2 ads) e EmprendeSeguro "Proveedores Mayoristas de Ropa en Chile" (1 ad).
- Hotmart: forte só em PT-BR, com "Lista completa de fornecedores" (https://hotmart.com/pt-br/marketplace/produtos/lista-completa-secreta-de-fornecedores/C83336741X). Em ES há páginas externas, como a do Gumroad (https://logratusmetas.gumroad.com/l/proveedores-mayoristas-mexico).

### 3.4 Templates para pequenos negócios
- **Calculadora de preços/custos** (35 anúncios): Latinas Together (13; GastroKit US$57; ângulos "Calcula tu precio sin saber de Excel", "Deja de cobrar con miedo", "¿Sabes cuánto te cuesta esa receta?", "Asegura tu ganancia antes de temporada alta"), Herramientas PRO (8), Serendipity J&P (3; 12,9d), Vida Saludable Fuerza y Equilibrio ("¿Abriste tu pastelería… para pasar horas organizando cuadernos, pedidos y cuentas?", https://www.facebook.com/ads/library/?id=1146357144484667) e Organizando Tu Vida ("Optimiza tus costos"). Hotmart tem ≥10 listagens de "calculadora de costos repostería", uma a US$5 (de US$9,90) segundo o snippet: https://hotmart.com/es/marketplace/productos/calculadora-de-rentabilidad-para-galletas-ny/N99160088C ; https://pay.hotmart.com/N99160088C ; https://hotmart.com/es/marketplace/productos/calculadoras-de-costos-hoja-de-calculo-excel/D103000487M ; https://hotmart.com/es/marketplace/productos/plantilla-de-costos-y-precios-para-reposteria-excel/V104956697U .
- **Papelería creativa** (Q28 49 + Q29 54 + Q23 48 + Q18 159): é o **maior cluster multi-anunciante** do território, com ~25 páginas distintas. Ofertas: kit de plantillas editáveis em Canva (cajitas dulceras, toppers, letras 3D, fundos, etiquetas). Longevidade: Espacio Creativo 82,4d, DecoKit Shop 90,2d, Papelería Creativa BR 101,9d, cienacres 469,5d e Carojo 325,6d (produto incerto). Preços: Diseña Creativo MXN 89 (~US$4,8), PixelPlantillas.cl CLP 3.990 (~US$4,3, https://www.facebook.com/ads/library/?id=1640358390776171), Aprende & Emprende "Mega Kit de Lettering x $9.900 COP" (~US$2,5). Hotmart: https://hotmart.com/es/marketplace/productos/hagsxd-papeleria-creativa-osm6z/R102572444D ; https://hotmart.com/es/marketplace/productos/papeleria-creativa-magical-world-500-pantillas-editables-canva-2026/K103835542X ; https://hotmart.com/es/marketplace/productos/super-pack-de-cajitas-editables-en-canva/L103632656J ; https://pay.hotmart.com/V105005455Q . Preços não mostrados no snippet.
- **Revendedoras de catálogo**: Sello Propio "360 Diseños - Revendedoras Natura" (10 ads, só 1 anunciante).
- **Sublimação/vinil** (187): Mundo Diseño (737526259449202, 10+ ads "HOY SE TERMINA LA OFERTA"), Sublimador 360 ("Descubre qué plantillas están dentro del Kit", https://www.facebook.com/ads/library/?id=28434580712876917), Silvia Cruz Miranda ("Quiero acceder al MegaPack"), PixelKits (BRL), Buna Shop ("Miles de diseños para sublimar"), Vectores y Plantillas - Vice Design, Arte En Kits, Rita Silvana García ("PERSONALIZA Y VENDE MÁS"), Envinil ("2,000 diseños para vinil por $197 MXN", 28,8d).
- **Kits de regalo**: Mi Masterclass Online ("Vende más armando Kits de Regalo a solo S/10", "Transforma tus cosméticos en Regalos Premium a S/10", https://www.facebook.com/ads/library/?id=1109426881423561), Moldes Cajas Decorativas, Emprende y Regala, Cajitas De Amor (catálogo, 321d, provavelmente físico).
- Outros: ISA "Crea tus propios empaques-Canva" (5), Kit Anfitrión 5 Estrellas (1 ad, anfitriões Airbnb), Agendas Imprimibles "Nuevas agendas 2027", Navidad Creativa "Plantillas de conos navideños".

## 4. Ideias extraídas (resumo; detalhe no JSON)
1. Papelería creativa: kit Canva editável (cajitas, toppers, letras 3D) para vender detalhes e festas. **Sinal mais forte.**
2. Mega pack de moldes de goma eva/foamy (+2000 PDF).
3. Moldes/patrones de costura digitais em PDF.
4. Patrones de crochet/amigurumi em espanhol (+1000 PDF).
5. Recetario "postres para vender" com costeo (mini postres, cheesecakes, tiramisú coreano, paletas).
6. Calculadora de custos e preços para empreendedoras (confeitaria/gastronomia). É **ferramenta**.
7. Packs de designs para sublimar/vinil (PNG/SVG temáticos).
8. Moldes de cajitas + guia para montar kits de presente (revendedoras de cosméticos, desayunos sorpresa).
9. Guia "crea y vende tu línea de aromas" (difusores, home spray).
10. Recetario de velas e sabonetes com calculadora e fornecedores.
11. Templates de posts para revendedoras de catálogo (Natura/Yanbal/Ésika etc.).
12. Diretório de fornecedores de nicho (sinal fraco).

## 5. Falhas e limitações
- Nenhum erro ou rate limit da ferramenta Meta em ~45 chamadas.
- Sem corpo do anúncio e sem alcance, a relevância foi julgada por page_name + título + moeda. Páginas marcadas "incerto": Bonito Digital, Aula Mágica, Richard Delgado, Impulsa Tu Negocio, Carojo, De fiesta, Espacio Creativo, Cursos Virtual Pro e Ajudando Laurinha.
- Rotação diária de criativos faz "dias do anúncio mais antigo" subestimar a longevidade da oferta (ver §0).
- Entre Mujeres e 1500 Moldes passam de 50 ativos. Só os 50 mais novos são visíveis, então os dias são limite inferior não informativo.
- Preços do Hotmart vieram de snippets do WebSearch e **não foram verificados** nas páginas (WebFetch bloqueado).
- Conversões de moeda são estimativas.

## Apêndice: notas brutas da coleta (copiadas do scratch)

```
# notas brutas (scratch) - fase1 meta artesanato
NOW=1790095977 (dias = (NOW-start)/86400)
Paises padrao: MX,CO,AR,CL,PE,EC,GT,BO,UY,DO,US ; ACTIVE ; limit 50

## Q1 "postres para vender" est=1120
- Mini Postres Virales 1222476140938267 BRL "Recetario Mini Postres +615 recetas" ad 1403402902003047
- Academia Repostera Emprendedora 1057782127418715 USD "Recetario digital de Mini Cheesecakes" 1828167881869639 ; "Hoy 80% de descuento" 1021302667595797
- Academia Dulce Emprende 1302953309570574 "LIBRO DIGITAL DE POSTRES" 1410450964376310
- Academia de Reposteria Gourmet 675078309022165 "Recetario de Mini Postres" 2001774160943824
- Especialista Sofia Zantini 1277309992142835 USD "Primero Recibes Las Recetas y Despues Pagas" 2132493034287794 (9 ads no Q gelatinas)
- Chef Eli 989650777564708 COP "Primero recibes y luego pagas" numerados 6,7,8,10,14 -> 28954269907510218
- Caixa Academy 1169893866204452 "Primero recibes luego pagas" 1647459753666021
- Dulce Encanto Pasteleria 987089071144552 "Oferta por Tiempo Limitado" x5 1624558602536844
- Universo Digital 721458334380122 COP "Recibelo en tu celular ahora y paga despues" 1758721902125137
- Mundo Facil 1330537366811324 COP "Primero recibes luego pagas" 1697267259070391
- Sofia Mendoza 906082872581925 "100 Recetas de Tiramisu Coreano + 4 Bonos por $9 USD" 1418570293571960  <- PRECO
- Dolchere 770996249419507 "No necesitas gastar una fortuna para empezar" 1398684555066207
- Postre Negocios Dulces 1262127790321733 "Ebook Rolls & Sushi Dulce +5 bonos" 1476373420969984
- Recetas desde Casa 1161115463756937 "Primero recibis y despues pagas" 2161479101390064
- Academia Online Pro 277496115454595 "adquiere ahora" x4 ; Megapack Digital 1242267238975066 x2 ; Edufoods 722266267646615 (chat) ; Emprende con postres desde casa 143387618867021 (chat)
- Comer Sin Culpa 934551959748959 ARS

## Q2 "recetas para vender" est=3042
- ProAcademy 1261331087060816 MXN "Ebook Recetario Cheesecakes" 1629323351986382
- E Gustoso pastas 107960131886012 ARS "La guia mas completa a un precio especial" 1666405671483305
- Gourmet/Profesional 103221925279212 "Bolos Gourmet CLIC AQUI 10bs" 2359480581456991
- Chef Sofia Martinez 1239086859287425 BRL "(3.779)" reviews x5 1569600724446507
- Mariana Gutierrez 795255147012609 "4.8/5 +480 resenas" 1111253841584390
- Snacks Saludables Sofi 1296641070197191 "Emprende con snacks saludables desde casa" x6 1049569181418379
- Borda y emprende 1235918919614921 ARS "Sonas con emprender desde casa?" 1787796442536857
- Master de herreria 1268079449726604 (chat) ; David Medina 1327579360433183 (chat) ; Camila soarez 496439234431121

## Q3 "gelatinas para vender" est=104
- Sofia Zantini 9 ads (mesmo "primero recibes") 
- Comer Sin Culpa x5 ; Cecilia Garcia 655391117668859 "Conservas faciles" ; Sofia Torres 1302475096284151 "Conservas" x3
- Academia Online 1195036337018323 "Recibes primero y luego haces tu contribucion"
- Manos Emprendedoras 614237968432710 COP "POR SOLO 15.000 MIL PESOS" 1699689527795157
- PostreVida 830456013476155 "Llevalo por solo S/5 soles" 1401344795528608  <- PRECO
- Sueli Almeida 913897521798413 "Postres de boutique desde tu casa" 14+ ads 1404167268589740
- Mari Tanaka 966828429857927 "Panes y postres saludables"

## Q4 "paletas para vender" est=180
- Impulso Creativo 145700745291543 MXN "4.9/5 +1,200 clientes" x4 2125841961676366
- Hi Pop. 979642605232431 COP "Genera ingresos desde casa" 1702986864722667
- Universo Literario 336326432894287 CLP "Recetario +100 Recetas hoy $2.500" 983981794711862 <- PRECO CLP2500 (~US$2.7)
- Magia en tus manos 1262565670266751 "Te envio YA"
- Manitos Creativas 1229346300271007 "Escribenos ahora" x4
- El Club del Helado 1318891407974552 "Queres emprender con helados..." 1802624841158291
- Paletas Gourmet 1329466910256737 ARS "Aprende a crear Paletas Gourmet desde casa" 1418982656854647 (start 1790032578? creation 1789568548)
- Barkery en casa 155619625248201 "Empieza a hornear desde casa" (galletas perro) 1999061337460510
- Grupo Refriar / Moratto (maquinaria/mayorista - fisico, irrelevante)

## Q5 "velas artesanales" est=1691 (mistura lojas fisicas de velas + cursos)
- El Mundo de los Cursos 413460908527026 COP "Curso de Velas Artesanales" 28393293640334539 (E1)
- Richard Delgado 136833262838624 USD "Empezar ahora! | Commence maintenant! | Simdi Basla | (arabe)" -> MULTI-IDIOMA 1792792165395180
- Velvet Ecommerce 520723561134297 USD "Curso online de velas y jabones artesanales" 1091586696587011 (E1)
- Ajudando Laurinha 1380315488479842 BRL "Quiero saber mas" MUITOS ads (20+ nas 2 queries) 1013218625063771
- Taller Creativo Academia 537460616120250 COP "4.8/5.0" x3 1385259879923199
- Anchetas y regalos Decofest 370065529534166 COP "Aprende desde cero" / "Separa tu cupo" (taller presencial?) 1073092305473049
- Emprende con Creatividad 646306871888833 COP "HABLAR CON UN ASESOR" x3
- Estacion Saludable 1366460066531164 ARS "Aprende y genera ingresos desde casa" 1397248242608483
- lojas fisicas: Maky Velas, ava.velasaromaticas, velasleon.cl, La marie Deco (velas recordatorios)
## Q6 "jabones artesanales" est=1236
- Ajudando Laurinha (de novo, ~15 ads)
- Emprende Aprendiendo 1222543597616906 BOB chat
- Ana Moraes 904944262713054 USD "4.9/5.0 (2,178 resenas)" 948666801622176
- De todo y desde casa 110616521450005 USD "Obten la oferta HOY" x3 4482761148632993
- Bendiciones diarias 601498429704485 MXN "PACK DIGITAL $99 MXN" 28335327712804234 ; "Primero recibe y paga despues" <- PRECO MXN99 (~US$5)
- Jaboncitos de amor rd "Taller de Jabones" (presencial)
## Q7 "amigurumi patrones" est=353
- Tejidos y Crochet 1222570877617282 CLP "+1000 Patrones Verificados en Espanol + 6 Bonos" 1432152345461217 ; "Convierte 2 ovillos de lana en $30.000 CLP desde tu propia casa" 1837920730745406
- Aula Magica 934166036453158 PEN "Disponible" ~22 ads na query 2421581784918061
- Mundo Virt 1029364793603128 USD "ENTREGA INMEDIATA" x6 1582730076249513
- Creando Amigurumis 1346103741912687 USD "-77%OFF PROMO" x3 1072331222065481
- Cursos Magicos 392230117304954 GTQ "Curso + Bonos por Q40" (~US$5) 905899072385929
- Alma Costurera 1269214432943794 COP "Descargalos ahora" x6 2281866275980423
- Manualidades Geniales 1313863351804542 USD "+331 Clientes estan emprendiendo" x3 1100706279316470
- Mundo Crochet 1116632328195736 "Amigurumi Gigante" ; Ensena Plus 843833395473720 "+BONOS"; Maria Elena 950433964813401 BRL
## Q8 "resina epoxica" est=1433 (maioria fisico/insumos/talleres presenciais)
- Mentoria Global 957547620766738 USD "Oficios Pro" 16+ ads 1108748044939908 (bundle de cursos de oficios -> E1 provavel)
- Disenarte 3D 109290785001916 chat x5 ; Idea Lista 1239004642633093 COP ; Bruma Arte Epoxico (taller presencial "15 lugares")
- Superdealy6161 = dropship fisico (irrelevante)

## Q9 "moldes de pinatas" est=17 (baixo)
- PRIME EDUCA 1156807557517280 x2 ; Mara Cursos y Packs Online 266903246508014 "ACCESO INMEDIATO" 1811079533360719 ; Conexion Emprendedora 514896881696720 "ACCESO INMEDIATO" (start 1783560708 -> ~76 dias) 27459940186981397 ; De fiesta 1193895630474335 x5 (start ~1781638883 -> ~167 dias?) 
## Q10 "arreglos con globos" est=452 (maioria servico fisico de decoracao)
- Arte y Decoraciones con Globos 187287057794045 USD "DECORA FIESTAS AHORA!!!" x3 1061313440038844 (curso?)
- Desde cero con Fer 987672827764499 "CLASE GRATIS EN VIVO" (E1) ; Elyon Yireh "Curso 4x1 de Decoracion" ; CETEC (escola presencial)
## Q11 "lista de proveedores" est=10418 (ruidoso - match amplo)
- Mundo de recursos digitales 1251927058007442 COP "+2959 han comprado" 28307266108932898
- Saber Mas 1212386861968126 COP "Recibelo en tu celular ahora y paga despues" 1859945098501889
- Aprende Facil 667294843128271 COP idem x5 2040950423204593
- Educacion Online Creativo 933097826564485 "Planificador Secreto Wedding Planner" 4537656343168625
- Esencia Artesanal 847635798430593 GTQ "Aprende Joyeria con Resina por Q40" x5 1708873460176991
- Mundo Creativo 1145607445303727 "+500 mujeres ya crean y emprenden con Miyuki" 1525821499351626
- Jose Lopez 817099778154222 "Importa desde China y aprende a vender" / "Entra por $50 al mes" (assinatura/mentoria E1)
- Punch emprende 1249223508280731 "Aprende Punch Needle y empeza a vender"; El Club de las Creativas 1193223793874515 "linea de aromas"
## Q12 "proveedores China" est=1508
- Metodo importador TIV 485496491324385 "Haz click aqui" x8 1758803608571159 (curso importacao E1)
- Dany Travel Importaciones 113463494929246 "Evento Virtual Sin Costo" 30+ ads (webinar -> high ticket, E1)
- ABK Imports Logistics (servico 1688), Dalimport (servico) -> E3
## Q13 "directorio de proveedores" est=116
- Reactor Quimico 109903180717902 MXN "Manuales, videos y directorio de proveedores" x2 1117082450653946 (productos de limpieza)
- Cenzi Beauty Salons 1321069997736828 USD "Directorio Premium de Proveedores de Extensiones" x4 1409222934466487
- EmprendeSeguro 777487498792570 CLP "Proveedores Mayoristas de Ropa en Chile" 28633064256323286
- Florencia Moreira 1172869515903696 UYU "Metodo Aroma Queen - Guia completa + 9 bonos | Acceso inmediato" x7 1347787477182417 ; Aroma Queen 960420037162583
## Q14 "proveedores mayoristas para emprender" est=85 -> so atacadistas fisicos (ClosetUp, Panda...) irrelevante

## Q15 "plantillas Canva editables" est=775
- Inu studio 1314966641691125 USD "Elegi, imprimi, vende" x3 1560138291980476 (imprimiveis p/ revender)
- ISA 354089922027154 MXN "Crea tus propios empaques-Canva" x5 1617882330129331 (templates de embalagem)
- Cursos Virtual Pro 577825088744546 PEN "Escribenos" 22+ ads na query 1097746246321980 (produto nao identificavel; tambem apareceu em postres)
- Megapack Digital 1242267238975066 USD "OBTEN AHORA" x5+ 1064473093160902
- Descarga con nosotros 1072165559323244 PEN "Mega Pack Hot Wheels" (WhatsApp) x7 1093024673226496
- Cursoteca Literaria 299286973269776 "eliges, personalizas, imprimes y armas" / "Quiero mi Mega Pack" 1630144588779632
- Kit Anfitrion 5 Estrellas 1351681281357350 USD (kit p/ anfitrioes Airbnb) 1644197900660279
- Mundo de recursos digitales 1251927058007442 "+2959 han comprado"; Recursos Digitales M 684531784749400 MXN; Mundo Creativo 1029611470231168 "Entrega Inmediata"
## Q16 "calculadora de precios emprendedores" est=35
- Herramientas PRO 429125386950426 COP "Kit de 7 Dias para Tomar el Control de tu Negocio y Multiplicar tus Ganancias" x7 28955046107454054
- Latinas Together 219870772214056 USD "Tu receta, tu precio, en segundos" / "Todo el GastroKit hoy por $57" / "Deja de cobrar con miedo" 2972385876428289
- Serendipity J&P Detalles con amor 2286687988232447 MXN "Calculadora de Precios para Emprendedores" x3 1606182844545250 (start 1788980141 -> ~13d)
- Vida Saludable Fuerza y Equilibrio 870147239525607 USD (organizador p/ pastelaria) 1146357144484667
- Carrera en Accion 1233605339845306 PEN "conoce todo lo que incluye el kit" x3 ; 4rtesanias C0n Luplta 1150051218186509 "Recibe en whatsapp HORA" x6
- Organizando Tu Vida 344489875424147 PEN "Optimiza tus costos" 3284411875281349 ; Impulsa Tu Negocio 1172504619283595 COP (start 1783862493 -> ~72d) 2793112167740267
- Dolchere 770996249419507 (pastelaria) aparece de novo
## Q17 "moldes de costura" est=873  *** FORTE
- Entre Mujeres 1180416348492259 USD "Acceso exclusivo a 200+ patrones digitales en PDF" x11 909768015290442
- 1500 Moldes de Costura 841929342339578 USD "DESCARGAR" x6 2471122273412389
- Taidy Hernandez Designer 106560037662504 "45 Patrones Digitales por $3.000 CLP" x2 2286881178731056 <- PRECO ~US$3
- Moldes Unicose La Molderia 112778345422906 CLP "Antes $4050 Ahora $3.000" 1490782679769765
- Patrones en PDF 1210181845507553 PEN "+120 Moldes Infantiles en PDF" 1124678266754398
- Alma Costurera 1269214432943794 COP "Descargalos ahora" x8 1089525300129906
- Edukits 1133629293161885 CLP "ACCEDE AHORA" x6 934817369252223
- Taller de Recuerdos 1192471487290475 USD "Un abrazo que dura para siempre" x8 2442867473152730 (ursinhos de memoria?)
- Atelier Clarice Rodrigues BRL "Lucre com Roupas Pet"
## Q18 "imprimibles para vender" est=159
- Bonito Digital 1253683197834637 MXN 17+ ads (sem titulo) 1093233046382548
- Mega Plantillas Digitales 1154408571089804 USD "Mira como funciona" x3 2205298640865792
- Sello Propio 1310658882133067 USD "360 Disenos - Revendedoras Natura" x5 2156814638591939  <- templates p/ revendedoras de catalogo
- Agendas Imprimibles 637552659437337 MXN "Nuevas agendas 2027" 3378411482331799
- Navidad Creativa 1280098841856961 PEN "Plantillas de conos navidenos" 1632288341805543
- Club recursos digitales 1153061331231120 MXN "PRIMERO RECIBES EL MATERIAL, DESPUES HACES UNA APORTACION VOLUNTARIA" 1646974250380367
- Planeta Creativo Kids 1136065496257319 "CREA TITERES FACILES" x3
- Eduka 1293455397188271 COP "Vende tus munecos"/"Crochet que si se vende" x5 ; Biblioteca Digital 1265614099971268 "Bolsos y carteras a Crochet"; Zona Educativa MX 1217787384755774 "Aprende Crochet y Empieza a Vender" x5; Myrlo Educa 1184365788089370 "Primero recibes, luego decides tu aporte"
- CarpinteriaPro 900 898271436696064 "ACCESO INMEDIATO" (planos de carpintaria?)

## Q19 "plantillas para redes sociales emprendedoras" est=3 (quase nada)
## Q20 "desayunos sorpresa emprender" est=34
- Decoracion Con Globos 163208480219527 COP "5 PROGRAMAS VIRTUALES POR $15.000" (~US$3.7) 2661719944261376 ; "Curso Virtual" start 1785237480 (~56d) 1382299087338977 (E1)
- Emprende y Regala 122032564157643 "Mas vendido de Latinoamerica" 1056771267271385 ; Cajitas De Amor 702507589606613 (start 1762315946 -> ~321d, template {{product.name}} = catalogo)
## Q21 "recetario" est=7249 (inclui saude/fitness; nao so negocio)
- Fitsaludable1 610373358825525 "120 recetas + plan de 21 dias por US$9,99" (fitness, nao renda)
- Recetas Sin Culpa 1253852341148968 BRL "Recibe Todo Primero..." x5 ; Recetas Al Rescate 1137837066084763 "255 Recetas de Especias"; Cakesicles Irresistibles 895308567009767 MXN
- Rociojulca "+600 recetas proteicas"; Aurora Bianchi "60 recetas + porciones en gramos" (pet)
## Q22 "patrones crochet pdf" est=202
- Hoshihana Shop 722458774285309 COP "+6.000 Patrones en PDF" x10 1447476493893273
- Giulia Moretti 1058796797324269 BRL "+2.632 resenas (4.95/5.0)" x9 1427378629334609
- Tejidos y Crochet 1222570877617282 x4 (+ "Batallando con el video cada 20 segundos con las manos ocupadas" -> angulo PDF vs video!) 1668014264759661
- DecorCraft Academy 120219254362754 MXN "+100 patrones exclusivos" 1100092012563882
- Mis Tejidos 1212860208573381 USD catalogo livros digitais (gorros, blusa, ponchos) 1070957858880376
- Estudio de Produccion Martinez 1176468978894281 "QUIERO LA OFERTA" x6 ; MundoAula360 1018218164698078 x4 ; Tu-Top Crochet "Pack 5 Patrones de Bolsos"; Emprende Facil y Rapido 1374710735716979 "Gano mas tejiendo que con mi jubilacion"

# MEDICOES POR page_ids (ACTIVE, limit 50) - dias = (1790095977 - min start)/86400
- Sofia Zantini 1277309992142835: est=9 ativos; todos criados ~0.3-0.7d atras; min start 1790083348 -> 0.15d. Mesmo titulo "Primero Recibes Las Recetas y Despues Pagas" (9 variacoes). Churn diario de criativos.
- Entre Mujeres 1180416348492259: est=153 ATIVOS (50+ limite). 50 vistos todos criados 1790066548-1790067792 (~8h atras), start 1790084316+ ; mesmo titulo "Acceso exclusivo a 200+ patrones digitales en PDF". -> volume massivo, recriacao em lote. dias do mais antigo visto: ~0.14d (limite inferior NAO informativo: so vemos os 50 mais novos)
- Hoshihana Shop 722458774285309: est=9 ativos; min start 1790057867 -> 0.44d; "+6.000 Patrones en PDF"
- Entre Mujeres ALL status: est_total=230 (153 ativos) -> quase todo o historico esta ativo agora => pagina recem-escalada (lote de ~150 ads criados em ~1790066548)
- 1500 Moldes de Costura 841929342339578: est=113 ATIVOS (50+ limite); 50 vistos; menor start visto 1789451176 -> 7.5d (limite inferior; ha 63 mais antigos nao vistos). Titulo "DESCARGAR" + alguns com link api.whatsapp.com. Lotes de criacao: 1789430554, 1789605851, 1789690453, 1789796120, 1790052808 (recria a cada ~1-2 dias)
- Alma Costurera 1269214432943794: est=47 ativos (todos vistos); min start 1787822740 -> 26.3d ; "Descargalos ahora" (47 variacoes)
- Tejidos y Crochet 1222570877617282: est=6 ativos; min start 1790073176 -> 0.26d. titulos: "Pruebalo durante 15 dias: si no te encanta, te devolvemos el 100%" 1405370991720158 ; "CUANDO EL PATRON DECIA 'TRADUCIDO AL ESPANOL'..." 4016431831821123 ; "El muneco que le teje su abuela..." 938588189320580
- Chef Eli 989650777564708: est=32 ativos; min start 1789807321 -> 3.3d ; "Primero recibes y luego pagas!" numerados 6..15 + "Chatea con nosotros"/"Escribenos aqui" (WhatsApp)
- Sueli Almeida 913897521798413: est=25 ativos; min start 1789452203 -> 7.5d ; "Postres de boutique desde tu casa" + "Converse conosco" (anunciante BR vendendo em ES)
- Mini Postres Virales 1222476140938267: est=1 ativo (novo, 0.05d) BRL
- Giulia Moretti 1058796797324269: est=9 ativos; min start 1790051856 -> 0.51d ; "+2.632 resenas (4.95/5.0)" BRL (anunciante BR vendendo crochet em ES)
- Ajudando Laurinha 1380315488479842: est=19 ativos; min start 1790090418 -> 0.06d ; "Quiero saber mas" BRL (produto incerto: velas/jabones? nome sugere pagina reaproveitada)
- Bonito Digital 1253683197834637: est=27 ativos (todos vistos); min start 1789305365 -> 9.2d ; sem titulo (MXN) -> produto nao identificavel so pelo titulo (apareceu na busca "imprimibles para vender")
- Sello Propio 1310658882133067: est=10 ativos; min start 1790072101 -> 0.28d ; "360 Disenos - Revendedoras Natura" (9) + 1 sem titulo
- Herramientas PRO 429125386950426: est=8 ativos; min start 1790057718 -> 0.44d ; "Kit de 7 Dias para Tomar el Control de tu Negocio y Multiplicar tus Ganancias" (8)
- Cenzi Beauty Salons 1321069997736828: est=8 ativos (5 do "Directorio Premium de Proveedores de Extensiones"; resto = servico de salao EUA); min start diretorio 1789795988 -> 3.5d
- Florencia Moreira 1172869515903696: est=14 ativos; min start 1790016810 -> 0.9d ; "Metodo Aroma Queen - Guia completa + 9 bonos | Acceso inmediato" ; "4,9 de 5 - 739 Resenas" 1653911773135551 ; angulos "No es una receta: es el negocio", "Cuesta un delivery. Se vende caro.", "Una hora. Seis productos.", "Que lleve tu nombre" (marca propria de aromas)
- Richard Delgado 136833262838624: est=33 ativos; min start 1789769913 -> 3.8d ; "Empezar ahora!" em ES + FR + TR + AR (mesma oferta multi-idioma; produto nao identificavel pelo titulo; apareceu em velas/jabones)
- Impulsa Tu Negocio 1172504619283595: est=10 ativos; min start 1783859598 -> 72.2d (!!) ; sem titulo, COP; apareceu em "calculadora de precios emprendedores" (produto incerto; match pode ser so "emprendedores")
- Conexion Emprendedora 514896881696720: est=3 ativos; min start 1783560159 -> 75.6d (!!) ; "ACCEDE AHORA"/"ACCESO INMEDIATO" USD; apareceu em "moldes de pinatas" (produto digital provavel de moldes; incerto)
- Decoracion Con Globos 163208480219527: est=5 ativos; min start 1785237480 -> 56.2d ; "CURSO VIRTUAL" / "5 PROGRAMAS VIRTUALES POR $15.000" COP (~US$3.7) -> curso (E1)
- De fiesta 1193895630474335: est=5 ativos; min start 1781635685 -> 97.9d (!!) sem titulo MXN; apareceu em "moldes de pinatas" (pode ser loja fisica de fiesta; INCERTO)
- Aula Magica 934166036453158: est=34 ativos; min start 1790068356 -> 0.3d ; "Disponible" PEN ; produto nao identificavel (apareceu em amigurumi)
- Latinas Together 219870772214056: est=13 ativos; min start 1789968800 -> 1.5d ; GastroKit (calculadora de custo de receitas) "Todo el GastroKit hoy por $57" ; angulos "Calcula tu precio sin saber de Excel", "Deja de cobrar con miedo", "Sabes cuanto te cuesta esa receta?", "Asegura tu ganancia antes de temporada alta" 1057383214053948

## Q23 "moldes de cajas para imprimir" est=48
- Moldes Cajas Decorativas 413447005190625 USD "+300 Moldes de Cajitas Decorativas" / "Arma y Vende Cajitas Decorativas" / "Basta de Buscar Moldes Sueltos" x5 1097880062567915 (start 1788087860 -> 23.2d)
- Carojo Aprende y Emprende 152908757899058 COP "4.9/5.0" x6; start mais antigo 1761967823 -> 325.6d (!!) 1498175651393089
- Veronica Ventas 1276073018925773 + Veronica MX 1267079633165871 (2 paginas mesma oferta) "Moldes de fiesta listos para imprimir" 2235751947248872 / 1048944484680958 (start 1787938235 -> 25.3d)
- Aprende & Emprende 729512666900981 COP "Mega Kit Creativo | Cartillas de Lettering | Moldes para Cajitas y Empaques" ; "Mega Kit de Lettering x $9.900 COP" (~US$2.4) 1103843828671680
- Mi Masterclass Online 114562433706332 PEN "Vende mas armando Kits de Regalo a solo S/10" / "Transforma tus cosmeticos en Regalos Premium a S/10" 1109426881423561 (S/10 ~US$2.7)
- Editables al Toque 1221815361021145 x5 ; Lola Detalles 1265855156608481 "50%OFF" x4 ; CreatiMia.pe 1045492865308219 "+251 Personas lo adquirieron" ; Mundo Creativo Digital 1068130303039496 "+10,000 recursos listos para editar en Canva" ; MagicKids 1206394795893194
## Q24 "moldes goma eva" est=62  *** multi-anunciante mesma oferta
- Mundo Foami 1451706391348713 PEN "+2000 moldes de Goma Eva - S/ 12.90" (~US$3.5) ; angulos "para vender" / "para tu aula" x13 2199268927598296
- Mundo Creativo 1004349699421673 USD "Pack +2000 Moldes de Goma Eva" x10+ 1091211326713642
- Mi Masterclass Online 114562433706332 "+2500 Moldes de Foamy en PDF a solo S/10" / "No vuelvas a rechazar un pedido! +2500 Moldes a S/10" 1826847468454898
- Academia Online 123123674103257 "+500 MOLDES DE GOMA EVA | 19 Bs" (~US$2.7) 1083927087587325
- Tus Moldes 523030987570701 COP "Recibe primero, paga despues" x3 2102082670699134
- Papeleria Creativa 733950036462396 ; Planeta Creativo Kids (titeres) ; Educa Mentes 670447516146943 ; Mundo Papel 103962705295548
- Carojo Aprende y Emprende 152908757899058: est=9 ativos; starts: 1761967823 (325.6d!!), 1775921242 (163.9d), 1776797828 (153.7d), 1778167897 (137.9d), 1787725874/1787726608 (26.3d), 1789132694.. (11.1d). titulo "4.9/5.0" COP; apareceu em "moldes de cajas para imprimir" (produto exato nao verificado)
- Mundo Creativo 1004349699421673: est=14 ativos; min start 1789627477 -> 5.4d ; "Pack +2000 Moldes de Goma Eva" (14 variacoes, lotes a cada ~2d)
- Mundo Foami 1451706391348713: est=12 ativos; min start 1789991523 -> 1.2d ; "+2000 moldes ... S/ 12.90" angulos vender/aula/goma eva

## Q25 "plantillas para revendedoras" est=2 (so Sello Propio) ; Q26 "kit imprimible cumpleanos editable" est=3 (so cienacres)
- cienacres.imprimibles 461588617027210: est=4 ativos; starts 1749533288 (469.5d!!), 1749572419, 1749608660, 1750098330 (463d) USD ; kits imprimibles festa (produto exato nao verificado)
## Q27 "bisuteria miyuki patrones" est=4 (baixo): Creatuidea.ar, Pao Manantial Aprendiz, Aprende con maju
## Q28 "etiquetas escolares editables" est=49  *** cluster "papeleria creativa" (kits de plantillas editaveis p/ vender)
- Disena Creativo 1162766426927858 MXN "Consigue tus plantillas por solo $89 MXN!" (~US$4.8) x5 ; "4.9/5" start 1789028096 -> 12.4d 1270026136202268
- Espacio Creativo 510930015432339 USD "Chatea con Nosotros" x6; start mais antigo visto 1782972950 -> 151.9d 1651569109650285
- Papeleria Creativa 1070020366204559 BRL "La promo termina pronto... y aun no descargaste tu kit." start 1781290531 -> 101.9d 1517888309821966
- Papeleria Creativa - Kit Completo de Plantillas Editables en Canva 1296601010204782 BRL x2 1623928529451881
- Envinil.com 221014007754159 MXN "Mas de 2,000 disenos para vinil por solo $197 MXN + Bonus" (~US$10.6) start 1787605253 -> 28.6d 1741139417615425
- Universo Creativo Online / Crea&emprende online 613506495180789 COP x5 ; Pack Digital Emprendor 104462436003652 ARS "50%off" x3 ; Universo Kids 1020915651110034 "PEDI TU PACK AHORA" ; Corazon de Emprendedora 885339807991741 ; Disenando Eventos 104933269211198
- anunciantes BR vendendo em ES: Joao Carlos 1325445310650753 (x5), Leticia Souza 1511160735880595, Bella Collins 123719130823291, CreaFiesta 1218822567991386, disenoypapeleria.creativa 190139387513956 -> oferta BR traduzida p/ ES
- Espacio Creativo 510930015432339: est=14 ativos (todos vistos); min start 1782972950 -> 82.4d (!!) ; outros 1783059634 (81.4d), 1783836824 (72.5d), 1784081582..1784511727 (65-70d), 1788416314 (19.4d), 1788721566, 1788790808, 1789168105, 1789886918 ; "Chatea con Nosotros" USD (venda via WhatsApp) ; apareceu em "etiquetas escolares editables"

## Q29 "papeleria creativa kit plantillas" est=54 ; ~25 paginas distintas  *** MAIOR CLUSTER MULTI-ANUNCIANTE
- Mundo Creativo Digital 1068130303039496 USD "+10,000 recursos listos para editar en Canva" x8+; start mais antigo visto 1786861589 -> 37.4d 2291254541708920
- DecoKit Shop 737352542803130 USD "Tu negocio puede empezar con esto" start 1782306979 -> 90.9d 1477793531027394
- PixelPlantillas.cl 2988822531158336 CLP "POR TAN SOLO $3.990" (~US$4.3) x6 1640358390776171
- Charlotte Smith 1349924631529482 BRL "Mas de 100 cajitas dulceras + Letras y numeros 3D + +7500 fondos tematicos ... listo para personalizar" 2704639403285880
- Sofia Valenzuela - Papeleria Creativa 1356746230846288 BRL "Pack 1.000+ Plantillas Editables en Canva para Papeleria Creativa e Infinito Contenido 3D" 1055192427293262
- Bruno Lero 839455215916257 BRL "Pack +200 Plantillas Editables Acceso De Por Vida" 933352599458140
- Cool Disenos - Tiana 103199885926993 ARS "Pack Moldes Editables en Canva + Video de Edicion!" 1640551444090825
- Deco Mundo 746385791884775 USD "Mas pedidos sin disenar desde cero" 982298908231907
- Papeleria Premium 1220068147861987 USD "50% OFF | +500 Moldes de Squishy" 2560361191061036
- Kit Digital 433531919848589 CLP "Obten el tuyo ahora" x3 ; Ruiz Lizz 656908514176552 MXN (porta platos, toppers, stickers) ; artcreativa.sbs 108822024345900 BRL ; Ana Rosa 1224017970804067 BRL ; Edson Ladiv 1260005750536433 BRL ; Metodo CVP 1223090887551080 BRL ; Papelaria Creeativaa 1280627705125380 BRL ; Arte & Criatividade 103014168975534 BRL ; ALx Academia Digital 235067803533141 ; MagicKids 1206394795893194 ; Party Stationary MagicPresent 718558624666454 ; Papeleria Creativa MXN 106615188785905 ; Mundo digital 307716332654906
- => varios anunciantes BRL (operacao BR "Papelaria Criativa" traduzida p/ ES)
```
