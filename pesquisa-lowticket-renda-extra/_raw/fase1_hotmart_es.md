# Fase 1 — Hotmart em espanhol (anotações brutas)

Data da coleta: 2026-09-22. Referência de "agora" para dias ativos: epoch 1790095977.
Fonte: WebSearch com operadores site:pay.hotmart.com / site:hotmart.com/es/marketplace + Biblioteca de Anúncios da Meta (ACTIVE, MX/CO/AR/CL/PE).

## Falhas / limitações
- **WebSearch esgotou o orçamento da sessão (200/200) depois da 18ª busca desta fase.** As buscas 19 e 20 (`site:pay.hotmart.com mega pack productos digitales para revender`, `site:go.hotmart.com kit imprimible`) voltaram "Web search was not performed". Meta pedida era 25–40; consegui 18 válidas + 2 recusadas. Não deu para cobrir: site:go.hotmart.com, CV (retornou vazio de CV), menú digital (sem match direto), cuentos personalizados (sem match direto).
- WebFetch/curl bloqueados (não tentado, conforme instrução). Preços só quando vieram no resumo do WebSearch; resto = "não verificado".
- Order bump / "oferta especial": nenhum snippet mostrou order bump explicitamente. Menções a "bonos", "acceso de por vida/vitalicio", "PROMO50/PROMO70", "70% OFF" aparecem em títulos/URLs (offDiscount=) — anotado por produto.
- Meta Ads Library não retorna corpo do anúncio: relevância julgada por page_name + link_title + moeda. Muitos anunciantes do mesmo termo são negócios locais (serviço), não infoprodutos — separei quando possível.
- Moeda BRL em anúncios em espanhol = provável produtor/afiliado brasileiro rodando ES.

## Buscas WebSearch rodadas (20 tentativas: 18 com resultado, 2 recusadas por orçamento)
1. site:pay.hotmart.com kit imprimible para vender
2. site:hotmart.com/es/marketplace invitaciones digitales
3. site:pay.hotmart.com plantillas editables canva emprende
4. site:pay.hotmart.com sublimación diseños pack
5. site:pay.hotmart.com recetas para vender postres negocio desde casa
6. site:pay.hotmart.com velas artesanales jabones recetario
7. site:pay.hotmart.com moldes patrones pack
8. site:pay.hotmart.com lista de proveedores mayoristas
9. site:pay.hotmart.com proveedores México directorio emprende
10. site:pay.hotmart.com cuentos personalizados niños
11. site:pay.hotmart.com menú digital restaurante plantilla
12. site:pay.hotmart.com stickers imprimibles pack
13. site:pay.hotmart.com amigurumi patrones pack
14. site:pay.hotmart.com resina epóxica emprende
15. site:pay.hotmart.com plantillas CV currículum editable
16. site:pay.hotmart.com catálogo digital editable WhatsApp
17. site:pay.hotmart.com "derechos de reventa" pack
18. site:pay.hotmart.com "ingresos extra" kit listo para vender
19. (falhou – orçamento) site:pay.hotmart.com mega pack productos digitales para revender
20. (falhou – orçamento) site:go.hotmart.com kit imprimible

## Produtos Hotmart encontrados, por TIPO

Legenda núcleo: K = kit/ferramenta/entregável pronto; C = curso/aulas; M = misto (ebook+bônus).

### T1. Invitaciones digitales (templates Canva/PPT, web interativa, curso p/ vender)
| Produto | URL | Preço | Núcleo | Obs |
|---|---|---|---|---|
| INVITACIONES DIGITALES (Heiner Alejandro) | https://hotmart.com/es/marketplace/productos/invitaciones-digitales-2/K66340223D | não verificado | K | |
| Invitaciones Digitales Interactivas para Eventos | https://hotmart.com/es/marketplace/productos/invitaciones-digitales-interactivas-para-eventos/K102179105D | não verificado | K (web interativa: música, fotos, mapa, RSVP, contagem regressiva — segundo resumo) | DNA mais próximo do Mimo Gift |
| Invitaciones digitales personalizables (Dayanne) | https://hotmart.com/es/marketplace/productos/invitaciones-digitales-personalizables/G101480474F | não verificado | K/serviço? | pode ser feito-sob-encomenda (E3?) |
| Invitaciones Digitales – Productos Digitales Premium | https://hotmart.com/es/marketplace/productos/invitaciones-basico/N97875409T | não verificado | K | |
| Invitaciones Digitales EDITABLES (Karla Zambrano) | https://hotmart.com/es/marketplace/productos/invitaciones-digitales-editables/A74555329D | não verificado | K | resumo cita "+1000 opções editáveis em PowerPoint" (não sei qual produto) |
| INVITACIONES DIGITALES TIPO SITIO WEB (Paola Llamas) | https://hotmart.com/es/marketplace/productos/invitaciones-digitales-tipo-sitio-web/O101247541J | não verificado | K ou C (não verificado) | |
| PACK DE INVITACIONES DIGITALES (Hugo Arce) | https://hotmart.com/es/marketplace/productos/pack-de-invitaciones-digitales/Y87524037A | não verificado | K | |
| Plantillas de Invitaciones Digitales: Celebra con Estilo | https://hotmart.com/es/marketplace/productos/plantillas-de-invitaciones-digitales-celebra-con-estilo-y-eficiencia/K101349449U | não verificado | K | resumo cita "200 modelos editáveis Canva" |
| Invita y Emprende (vender invitaciones en Etsy con Canva) | https://hotmart.com/es/marketplace/productos/invita-y-emprende-aprende-a-vender-invitaciones-digitales-en-esty-con-canva/J103942328O | não verificado | C | E1 |
| Curso para emprender con invitaciones digitales interactivas | https://hotmart.com/es/marketplace/productos/curso-para-emprender-con-invitaciones-digitales-interactivas/L83087551J | não verificado | C | E1 |
Contagem: 10 produtos distintos (8 kit/template, 2 curso).

### T2. Kits de festa / papelaria editável Canva (cumpleaños, eventos)
| Produto | URL | Preço | Núcleo | Obs |
|---|---|---|---|---|
| Kits para fiestas 100% editables en Canva (258 diseños) | https://pay.hotmart.com/F103010959C?off=a1kavqsu&checkoutMode=10 | não verificado | K | "acceso inmediato" |
| Kit Festa 100% Editável no Canva 2.0 (PT) | https://pay.hotmart.com/Q103662817T?checkoutMode=10 | não verificado | K | BR, referência espelho |
| Kit Empresarial Event Planner | https://pay.hotmart.com/H100030235D | não verificado | K | propostas/apresentações p/ decoradora |
| MEGA KIT IMPRIMIBLE PREMIUM EMPRESARIAL (Pandita Digital Store) | https://pay.hotmart.com/Y59467636N | US$ 8,99 (resumo diz "/week" — não verificado se é assinatura) | K | |
| Kit Festas Personalizadas (resumo: etiquetas, lembrancinhas, acesso vitalício) | (URL não isolada no resumo) | não verificado | K | "acesso vitalício" |
Contagem: 4–5 produtos.

### T3. Plantillas Canva para emprendedoras (redes, agenda, lista de preços, catálogo)
| Produto | URL | Preço | Núcleo |
|---|---|---|---|
| Kit Plantillas Editables en CANVA (agendas/planners) | https://pay.hotmart.com/X102093674P | não verificado | K |
| Emprende desde casa con plantillas profesionales de Canva (Maria Victoria Menoni) | https://pay.hotmart.com/K103856475B | US$ 9,99 | K |
| Pack de Plantillas Editables en Canva (El Atajo Meta Ads) | https://pay.hotmart.com/K102983255Y | US$ 11,00 | K |
| 700 plantillas editables (Mari impulso digital) | https://pay.hotmart.com/L105358969Y | US$ 9,00 | K |
| InstaPremium Pack Canva (+50 modelos, +1100 reels) | https://pay.hotmart.com/S91413703M | não verificado | K + **direitos de revenda** (E4) |
| Kit de Plantillas Editables para Emprendedores | https://pay.hotmart.com/I105979560V | não verificado | K |
| Pack de 15 plantillas premium para Instagram + virales | https://pay.hotmart.com/P105361973X | não verificado | K |
| Paquete de plantillas editables RED 2.0 | https://pay.hotmart.com/E105652530H | não verificado | K |
| Plantillas IA-Ready listas en 5 minutos | https://pay.hotmart.com/Q104646259P | não verificado | K |
| Plantilla Premium: Lista de Precios Editable | https://pay.hotmart.com/Y105449623O | não verificado | K |
| Pack de Plantillas de Ads | https://pay.hotmart.com/R105047258O | não verificado | K |
| Kit Muestra de Fin de Año: Guía + 8 Plantillas | https://pay.hotmart.com/L105648881C | não verificado | M |
| Catálogo Digital p/ Produtos ou Serviços 100% Editável (PT) | https://pay.hotmart.com/m54255506s | US$ 5,00 | K |
| 20 Mil Plantillas de Mockup Editables | https://pay.hotmart.com/T82088109K | não verificado | K |
| Portifólio profissional editável (PT) | https://pay.hotmart.com/N106401332W | não verificado | K |
Contagem: ~15 produtos (13 ES). Faixa observada: US$ 5–11.

### T4. Mega packs de diseños para sublimación / DTF / tazas
| Produto | URL | Preço | Obs |
|---|---|---|---|
| Pack de 100.000 Diseños Sublimación, DTF y Vinilo | https://pay.hotmart.com/D105211812J | US$ 7,00 | |
| Pack Diseños Cristianos DTF/Sublimación | https://pay.hotmart.com/Y104137153R | US$ 10,00 | nicho cristão |
| Mega Pack Diseños DTF/Sublimación +100.000 archivos | https://pay.hotmart.com/H101163908P | não verificado | |
| 33 Plantillas Sublimar Tazas – Placas Vehiculares México | https://pay.hotmart.com/B101865987D | não verificado | micro-nicho |
| MEGA PACK DE PLANTILLAS DE SUBLIMACIÓN | https://pay.hotmart.com/D100661020K | US$ 4,00 | |
| Mundial 2026 Plantillas PNG Tazas 11oz (20 diseños) | https://pay.hotmart.com/R105948040E | não verificado | sazonal (passado) |
| + 200 PACK PREMIUM Sublimación | https://pay.hotmart.com/F103515649H | US$ 4,99 | |
| SÚPER MEGA PACK PREMIUM DE SUBLIMACIÓN + BONOS | https://pay.hotmart.com/M66665665I | US$ 19,99 | "+ BONOS" |
| Mega Pack Innovador (300 estampas camisetas futebol, CorelDraw + 4 bônus) | https://pay.hotmart.com/Y95284425V | US$ 11,99 | |
| Pack 5 Diseños Suplementos | https://pay.hotmart.com/S104823809U | não verificado | |
Contagem: 10 produtos. Faixa: US$ 4–20 (moda ~US$ 5–10).

### T5. Recetarios "postres para vender" / repostería rentable
| Produto | URL | Preço | Núcleo |
|---|---|---|---|
| Postres que Venden Desde Casa: +200 Recetas + Sistema | https://pay.hotmart.com/K105541910U | não verificado | M |
| Pastelería Desde Cero Para Emprender | https://pay.hotmart.com/N61635687U | não verificado | C (E1) |
| Kit Repostero Premium (+200 recetas sin horno) | https://pay.hotmart.com/S97774874C | não verificado | K/M |
| El Secreto de la Repostería Rentable: 80 Recetas | https://pay.hotmart.com/R97219280T | não verificado | M/C |
| La biblia de galletas New York | https://pay.hotmart.com/Q98681610C | não verificado | K (ebook) |
| Postres en Vaso Premium | https://pay.hotmart.com/B100038967M | não verificado | K? |
| POSTRES PARA VENDER (5 módulos) | https://pay.hotmart.com/Q96198091W | não verificado | C |
| Combo Ideal: +230 Recetas de postres | https://pay.hotmart.com/C88387570B | não verificado | K |
| Libro de Recetas de Rebanadas de Pastel | https://pay.hotmart.com/E104804072Q | não verificado | K |
| El Negocio de los Cake Roll | https://pay.hotmart.com/G68200251C | não verificado | C |
| Cocina Rentable +200 | https://pay.hotmart.com/V102712435L | não verificado | M |
| E-Book: Emprende con Conos Trufados + 4 Bonos | https://pay.hotmart.com/P84920276B | não verificado | K + bonos |
| Emprende con Galletas New York | https://pay.hotmart.com/B104871981X | não verificado | K? |
| Calculadora de Precios de Repostería y Gastronomía (Excel) | https://pay.hotmart.com/P83579553T | não verificado | K (ferramenta) |
| Paquete Lite – Plantilla de Costos de Producción | https://pay.hotmart.com/J104782701Y | US$ 10 | K (ferramenta) |
| MASTERCLASS DE INGRESOS EXTRA CON COOKIES | https://pay.hotmart.com/L105475025Q | não verificado | C |
Contagem: 13 recetarios/cursos + 2 ferramentas de custo.

### T6. Velas / jabones artesanales (recetarios + cursos)
| Produto | URL | Preço | Núcleo |
|---|---|---|---|
| Elaboración de Jabones y Velas Artesanales (Instituto ISE) | https://pay.hotmart.com/G36636504P | US$ 148 | C |
| Combo de Recetarios de Velas Artesanales | https://pay.hotmart.com/J99674018O | não verificado | K |
| El Combo de Jabones artesanales rentables +50 recetas | https://pay.hotmart.com/H98036488O | US$ 5,99 | K |
| Velas y Jabones Artesanales OFERTA 3x1 | https://pay.hotmart.com/T96306980O | US$ 35 (de 100) | M |
| Velas artesanales para emprender | https://pay.hotmart.com/M81391748N | não verificado | M |
| Aroma y arte: emprende con jabones | https://pay.hotmart.com/X101770695V?offDiscount=PROMO50 | não verificado | C? |
| CREA TUS PROPIOS JABONES SAPONIFICADOS | https://pay.hotmart.com/Q85886144W | não verificado | M |
| Jabones DIY Pack 7x1 | https://pay.hotmart.com/T88444403F | não verificado | K |
| Bouquets florales en velas | https://pay.hotmart.com/R100000004S?offDiscount=PROMO70 | não verificado | C? |
| Crea tus propios moldes de silicona | https://pay.hotmart.com/R90770794E | não verificado | C |
| LISTA DE PROVEEDORES VELAS | https://pay.hotmart.com/H105378449O | não verificado | K (lista) |
Contagem: 11. Nota: produto físico do comprador tem custo de insumo (não do vendedor) — ok p/ E3; mas a maioria é curso (E1).

### T7. Moldes / patrones de costura (PDF)
| Produto | URL | Preço |
|---|---|---|
| PACK 100 PATRONES Y MOLDES DE ROPA (infantil) | https://pay.hotmart.com/Y97589514K | não verificado |
| Patrones Vestidos de Niña | https://pay.hotmart.com/V94924758X | não verificado |
| Pack Premium de Moldes + Cursos de Costura | https://pay.hotmart.com/J105175215T | US$ 9,90 |
| EL ARCHIVO MAESTRO DE LA COSTURA +199 Patrones + 3 Bonos | https://pay.hotmart.com/S105446386J | US$ 14,99 |
| Super Pack de Moldes de Ropa Infantil | https://pay.hotmart.com/K105391759T | US$ 6,90 |
| +60 Moldes Tiernos para Decoración de Bebés | https://pay.hotmart.com/D105847990H | não verificado |
| Patronaje de Ropa Interior | https://pay.hotmart.com/N46827001G | não verificado (curso?) |
| Patronaje Digital desde Cero para Emprender | https://pay.hotmart.com/K60646380H | não verificado (curso) |
| Mega Pack Innovador de Patrones y Moldes | https://pay.hotmart.com/I87018880F | não verificado |
Contagem: 9. Faixa: US$ 6,90–14,99.

### T8. Amigurumi – mega packs de patrones
| Produto | URL | Preço |
|---|---|---|
| MegaPack Premium +5.000 Patrones Amigurumis | https://pay.hotmart.com/D101346455I | US$ 20 |
| MAS DE 10 MIL PATRONES AMIGURUMIS | https://pay.hotmart.com/K102403576S | não verificado |
| 4500 Patrones de Amigurumi | https://pay.hotmart.com/H99738190G | US$ 9,90 |
| Libro digital: patrones de amigurumis (500+200) | https://pay.hotmart.com/I95897688R | não verificado (62% off) |
| AMIGURUMIS ADORABLES +1.000 patrones | https://pay.hotmart.com/H81274136B | US$ 14,99 (70% off) |
| App Universo Mágico Amigurumi | https://pay.hotmart.com/Y97692871L | US$ 1/mês |
| Comunidad Secreta – Reino Mágico Amigurumi | https://pay.hotmart.com/P98199610X | não verificado |
| Amigurumis que Venden | https://pay.hotmart.com/Y104052887F | não verificado |
| Patrón Amigurumi – Rusty el Zorro | https://pay.hotmart.com/P93640224D | não verificado |
Contagem: 9. Faixa: US$ 1/mês – 20. **Risco: packs de "10 mil patrones" quase certamente agregam padrões de terceiros (direitos autorais).**

### T9. Stickers / álbum imprimible / agendas
| Produto | URL | Preço |
|---|---|---|
| Super Pack 3000 Stickers Imprimibles | https://pay.hotmart.com/M102998773E | US$ 3,90 |
| Mundial 2026 Álbum de Figuritas PDF + BONOS | https://pay.hotmart.com/T105853227Q | não verificado (sazonal passado; risco de marca FIFA/Panini) |
| 5 Libros de Plantillas para Stickers | https://pay.hotmart.com/K94892563U | não verificado |
| AGENDA 2025 + PLANIFICADORES IMPRIMIBLES | https://pay.hotmart.com/H94786552K | não verificado |
| PACK AGENDAS 2027 (cristiano: agendas, devocionales, stickers) | https://pay.hotmart.com/Y105994330R | não verificado |
Contagem: 5.

### T10. Plantillas p/ regalos personalizados (cuadros en pareja, imanes)
| Produto | URL | Preço |
|---|---|---|
| Pack de 30 Plantillas Editables en Canva – Cuadros en Pareja | https://pay.hotmart.com/M104164269T | US$ 3,90 |
| Plantilla de imanes personalizados | https://pay.hotmart.com/N103896032H | não verificado |
Contagem: 2 (baixa oferta = pouca concorrência ou pouca demanda — não verificado).

### T11. PLR / derechos de reventa / "productos listos para revender" (mapear E4)
| Produto | URL | Preço |
|---|---|---|
| Ingresos Extra con Productos Listos para Revender | https://pay.hotmart.com/G104996546M | US$ 6,90 |
| The PLR Market + Curso "5 pasos" c/ derechos de reventa | https://pay.hotmart.com/P93374740Q | US$ 19,99 |
| Curso de Marketing Digital + Derechos de Reventa | https://pay.hotmart.com/D94351027P | US$ 497 |
| CanvaPacks Español | https://pay.hotmart.com/H88493381C | não verificado |
| InstaPremium Pack Canva (c/ direitos de revenda) | https://pay.hotmart.com/S91413703M | não verificado |
| Ingresos extras desde casa (Trading + Hojas de vida) | https://pay.hotmart.com/Q104912855L | não verificado (trading = E4) |
Contagem: 6. Todos E4-suspeitos.

### T12. Resina epóxica (quase tudo curso)
O103806900M (US$ 9 a cada 2 meses), V74714773V, R46250850A, V87077753R (offDiscount=CRAFTWEEK), H79686100A, K106347440A, G91489053W, R69048300B, C92759479Q, S76094910B. 10 produtos, núcleo curso → E1.

### T13. Material didáctico infantil imprimible (não é renda extra, mas é o que domina "kit imprimible" na Meta)
V96267258X, U96267056Q, A95487523D, Y105542103F, A105951417I (álbum bíblico), L105527258Q (Cuentos para niños US$ 19). 6 produtos.

### Outros achados soltos
- Kit de 10 Herramientas de Masaje STL p/ impresión 3D: https://pay.hotmart.com/P106224859D
- Lista de fornecedores Atacado + Drop (PT): https://pay.hotmart.com/A104679635J ; Lista Fornecedores Premium China (PT): https://pay.hotmart.com/S103137718N
- El Negocio de los Regalos Sorpresa (curso): https://pay.hotmart.com/P60205685J
- Cuentos personalizados: nenhum produto de conto personalizado encontrado na Hotmart ES (só "Cuentos para niños" US$ 19) → lacuna de oferta, demanda não verificada.
- Menú digital: nenhum produto direto; só lista de preços/calculadora.
- CV: nenhum produto de CV no resultado.

## Biblioteca de Anúncios da Meta (ACTIVE; MX,CO,AR,CL,PE; limit 50) — 11 buscas por termo + 22 buscas por page_id

### Buscas por termo (estimated_total_count)
| Termo | est. total | Observação sobre o top 50 |
|---|---|---|
| invitaciones digitales | 1.139 | Maioria = negócios locais que vendem convite feito-sob-encomenda (Corazón de Fiesta, Invi Digi, Subligraf, Pearl Atelier, Calixta Card "Invitaciones web para tus 15 años", Miboda.love). Infoprodutos: Mega Plantillas Digitales (USD), Bruno Lero (BRL, "Pack +200 Plantillas Editables ¡Acceso De Por Vida!"), Ana Rosa (BRL, kit). |
| invitación web | 547 | Serviços de convite web a consumidor final: Invita Kairós "Tu invitación web por solo $99" (MXN), Limasystem "Invitación web + sistema RSVP desde S/125.90" / "desde S/95.90", Auras Estratégicas "desde $499 MXN", Arte Invita "Aparta con $199", My Invite, Weddify, She Said Web, Elegance site, Invitio "Pago único Álbum digital + Invitación Digital". |
| plantillas de invitaciones | 262 | Vendedores de template: Mega Plantillas Digitales, Liz Rodriguez (USD, 45 ads), Mundo Creativo Digital ("+10,000 recursos listos para editar en Canva"), Mega pack para la Fiesta de tus Sueños ("Todo para el cumple"), Fiesta en Casa (BRL, "100 fiestas + 800 plantillas editables"), Diseña Creativo ("plantillas por solo $89 MXN"), Kit Digital ("Solo a $3500" CLP), Imprimibles Creativos, Corazón de Emprendedora. |
| sublimación | 3.013 | Maioria insumos/equipamentos/gráficas locais. Infoprodutos: Sublimador 360 (USD, "Descubre qué plantillas están dentro del Kit"), Silvia Cruz Miranda (USD, "Quiero acceder al MegaPack"), El Manual Profesional De Sublimación (USD), LFCA-Diseños ("Masterpack 600 diseños", ARS), Publimolde (moldes full print). |
| plantillas editables | 1.635 | Excel para Restaurantes Perú ("Único Pago S/. 19"), Inu studio ("Elegí, imprimí, vendé" / "Agendas 2027 listas"), Inmobiliarios Digitales ("Kit Clientes Inmobiliarios por $147 MXN"), Documentum ("Formatos laborales por $299 MXN"), Capacitameya (kit prevención de riesgos), Bendiciones creativas (55 ads, "RECIBELO GRATIS HOY"). |
| postres para vender | 977 | Denso em infoproduto: Mini Postres Virales (BRL, "+615 recetas"), Academia Dulce Emprende ("LIBRO DIGITAL DE POSTRES"), Academia de Repostería Gourmet, Sofía Mendoza ("100 Recetas de Tiramisú Coreano + 4 Bonos por $9 USD"), Postre Negocios Dulces ("+50 Recetas de Rolls y Sushi Dulce + 5 Bonos"), Chef Eli, Caixa Academy, Mundo Fácil, Recetas desde Casa, Universo Digital (todos "Primero recibes y luego pagas" = pagamento pós-entrega, fora da Hotmart?), Dulce Encanto, Dolchere, Comer Sin Culpa, Kit Fitness 360 ("Recetas para ahorrar y ganar dinero", BRL), Crear y vivir ("Quiero ingresos extra"). ~15 anunciantes distintos no top 50. |
| moldes de ropa | 508 | 1500 Moldes de Costura (USD, 113 ads), Premium Master Academy ("+de 700 Costureras compraron", CRC), Patrones en PDF ("+120 Moldes Infantiles en PDF", PEN), Guías que Transforman ("Más de 100 Moldes para tu Negocio"/"Emprende con Ropa para Mascotas", COP), Academia Creativa ("QUIERO EL PACK"), SabeViva, Osito de la Memoria (BRL, "Una prenda para abrazar") e Taller de Recuerdos ("Un abrazo que dura para siempre") — molde de urso-memória, ângulo emocional. |
| kit imprimible | 848 | Dominado por material infantil (Mundo Mini Creativo "345 actividades listas para imprimir", Crianza Inteligente, Elefantil, Grupo Educare, Educa M Recursos), psicologia (Psicoresumen "Kit Clínico $19.99"), Maestro PDF ("+872 copias vendidas"), Paola Hernández ("Primero recibe después paga"). Pouco renda-extra. |
| patrones amigurumi | 339 | Creando Amigurumis ("-77%OFF PROMO"), Tejidos y Crochet ("+1000 Patrones Verificados en Español + 6 Bonos" / "Convierte 2 ovillos de lana en $30.000 CLP"), Aula Mágica (PEN, 34 ads, relevância incerta), Alma Costurera ("Descárgalos ahora"), Manualidades Geniales ("+331 Clientes están emprendiendo"), El Rincón del Tejido ("Recibe los moldes y paga después"), Crochet Studio, Mundo Creativo ("+160 Patrones"), Enseña Plus ("+BONOS"). |
| velas artesanales emprender | 253 | Quase tudo curso/escola presencial (CETEC, Creart, Creaconmarce, Casa Van Gogh) → E1. Bianca.Rojas Handmade ("+217 Descargas", CLP) é o único com cara de entregável. |
| derechos de reventa | 44 | Crea Y Multiplica Online ("Premium Pack PLR $3.99 usd"), NovaFolio.digital ("Ebooks PLR en inglés: gana en dólares desde $9.99"), Laprofesióndelfuturo ("MEGAPACK... por solo 6U$D"), Emprende y Gana Online ("Tu negocio digital con productos listos"), Creator Hub ("+10k reels aesthetic"), AutoCash WA, Yohan Palacio (packs marketing afiliados), Marketing con Eli Hansen. → E4. |

### Aprofundamento por anunciante (page_ids, ACTIVE, limit 50)
| Anunciante | page_id | Oferta (link_title) | Moeda | Nº ads ativos | Dias do mais antigo | Link exemplo |
|---|---|---|---|---|---|---|
| Mega Plantillas Digitales | 1154408571089804 | "Mira como funciona📱" / "Ver invitaciones digitales ✨" | USD | 10 | 49,5 | https://www.facebook.com/ads/library/?id=1708910720392963 ; https://www.facebook.com/ads/library/?id=3711236485701842 |
| Liz Rodriguez | 1367484466448886 | "OBTÉN AHORA 📲" (apareceu em "plantillas de invitaciones"; conteúdo incerto) | USD | 45 | 3,6 | https://www.facebook.com/ads/library/?id=1681720626708730 |
| Fiesta en Casa | 1409357392250487 | "100 fiestas + 800 plantillas editables" / "Crea tu fiesta sin ser decoradora" | BRL | 4 | 2,9 | https://www.facebook.com/ads/library/?id=2609589409466590 |
| Mega pack para la Fiesta de tus Sueños | 1317853361405992 | "Todo para el cumple, en un solo lugar" / "Tu fiesta con efecto WOW, sin diseñadora" | USD | 4 | 1,5 | https://www.facebook.com/ads/library/?id=1439431521425758 |
| Bruno Lero | 839455215916257 | "Pack +200 Plantillas Editables ¡Acceso De Por Vida!" | BRL | 1 | 0,5 | https://www.facebook.com/ads/library/?id=933352599458140 |
| Sublimador 360 | 114741977104223 | "Descubre qué plantillas están dentro del Kit" | USD | 4 | 6,0 | https://www.facebook.com/ads/library/?id=28434580712876917 |
| Silvia Cruz Miranda | 1280553028479061 | "Quiero acceder al MegaPack" / "Descargar Ahora" | USD | 7 | 2,9 | https://www.facebook.com/ads/library/?id=936941819469646 |
| Inu studio | 1314966641691125 | "Elegí, imprimí, vendé" / "Agendas 2027 listas ✅" | USD | 12 | 4,2 | https://www.facebook.com/ads/library/?id=1560138291980476 ; https://www.facebook.com/ads/library/?id=2232346370955983 |
| Bendiciones creativas | 1128535147014509 | "RECIBELO GRATIS HOY 🎁" (produto incerto) | USD | 50+ (limite; est. 55) | ≥3,0 (limite inferior) | https://www.facebook.com/ads/library/?id=1104075275505979 |
| Excel para Restaurantes Perú | 562263973643184 | "Único Pago S/. 19 soles" / "Descarga INMEDIATA" | USD | 15 | 17,3 | https://www.facebook.com/ads/library/?id=2195610874318293 |
| 1500 Moldes de Costura | 841929342339578 | "DESCARGAR" | USD | 50+ (limite; est. 113) | ≥7,5 (limite inferior) | https://www.facebook.com/ads/library/?id=2471122273412389 ; https://www.facebook.com/ads/library/?id=2813161522391035 |
| Premium Master Academy | 102147529349249 | "+de 700 Costureras compraron" (ads de costura: 0,8 d) + "+De 2000 alumnos aprobados" (outra oferta, até 32 d) | CRC | 27 | 32,0 (conta toda) / 0,8 (costura) | https://www.facebook.com/ads/library/?id=1602519041532064 |
| Guías que Transforman | 1145672191967271 | "Más de 100 Moldes para tu Negocio" / "Emprende con Ropa para Mascotas" | COP | 10 | 0,7 | https://www.facebook.com/ads/library/?id=2306095493579759 |
| Chef Eli | 989650777564708 | "Primero recibes y luego pagas!" (numerados 6–15) / "Chatea con nosotros" | COP | 32 | 3,3 | https://www.facebook.com/ads/library/?id=28954269907510218 |
| Sofía Mendoza | 906082872581925 | "100 Recetas de Tiramisú Coreano + 4 Bonos por $9 USD" | USD | 1 | 0,3 | https://www.facebook.com/ads/library/?id=1418570293571960 |
| Mini Postres Virales | 1222476140938267 | "Recetario de Mini Postres +615 recetas" | BRL | 1 | 0,0 | https://www.facebook.com/ads/library/?id=1403402902003047 |
| Tejidos y Crochet | 1222570877617282 | "+1000 Patrones Verificados en Español + 6 Bonos" / garantia 15 dias | CLP | 6 | 0,3 | https://www.facebook.com/ads/library/?id=1432152345461217 |
| Aula Mágica | 934166036453158 | "🟢Disponible🟢" (relevância a amigurumi incerta) | PEN | 34 | 0,3 | https://www.facebook.com/ads/library/?id=2421581784918061 |
| Emprende y Gana Online | 112360574923451 | "Tu negocio digital con productos listos" (PLR provável) | USD | 4 | 31,7 | https://www.facebook.com/ads/library/?id=2232442147328123 |
| Crea Y Multiplica Online | 586758177851572 | "Premium Pack PLR $3.99 usd" | COP | 4 | 144,2 | https://www.facebook.com/ads/library/?id=2130482384464112 |
| (visto na busca) Marketing con Eli Hansen | 488011341055753 | "Hacé clic en el botón y empezá HOY mismo" (conteúdo incerto) | ARS | ≥4 | ≥132,9 | https://www.facebook.com/ads/library/?id=27382851287977994 |
| (visto na busca) Yohan Palacio | 210643508808615 | Packs Marketing Digital "Sistema Dorado" afiliados | COP | ≥1 | 353,6 | https://www.facebook.com/ads/library/?id=824212100070940 |

### Leitura rápida dos sinais (proxy, não faturamento)
- Padrão geral nos nichos "kit para vender": anunciantes sobem MUITAS variações (10–113) mas com ads jovens (<8 dias). Longevidade ≥30 d só apareceu em: Mega Plantillas Digitales (invitaciones/plantillas, 49,5 d), Emprende y Gana Online (PLR, 31,7 d), Crea Y Multiplica (PLR, 144 d), Premium Master Academy (outra oferta). Ou seja, o sinal de longevidade é fraco em quase todo o nicho; o sinal de volume/variação é forte em moldes (1500 Moldes: 113 ads) e em postres (≥15 anunciantes distintos no top 50).
- "Primero recibes y luego pagas" é um padrão recorrente em postres/moldes/tejido (Chef Eli, Caixa Academy, Mundo Fácil, Recetas desde Casa, Universo Digital, El Rincón del Tejido, Paola Hernández) → modelo pagamento pós-entrega via WhatsApp (não Hotmart, provavelmente). Não verificado.
- Convite web interativo tem demanda de consumidor final com ticket local alto (S/95–125, $99–499 MXN) vendido por dezenas de microempresas → espaço para um editor self-service low ticket (DNA Mimo) E para um "kit/editor para vender convites" (ângulo renda extra).
