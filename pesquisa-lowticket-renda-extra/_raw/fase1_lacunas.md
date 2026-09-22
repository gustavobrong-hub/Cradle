# Fase 1 — Rodada de lacunas (anotações brutas)

Data da coleta: 2026-09-22 (referência de "agora" para dias ativo: epoch 1790095977).
Fonte principal: Biblioteca de Anúncios da Meta (MCP `ads_library_search`, ad_active_status=ACTIVE, limit 50).
Países padrão nas buscas por termo: MX, CO, AR, CL, PE, EC, GT, BO, UY, DO, US.
Dias ativo = (1790095977 - ad_delivery_start_time) / 86400. Com 50+ anúncios na página, o "mais antigo" é limite inferior (a ferramenta devolve do mais novo para o mais antigo e não pagina).

## 0. Falhas e limitações desta rodada

- **WebSearch esgotado**: as 3 tentativas retornaram "this session has used its web search budget (200 of 200)". Não foi possível: identificar o produto da Daniela Michilena, abrir/confirmar checkouts da Hotmart (K102179105D, O101247541J, T102280557H), confirmar preços de Hotmart de sublimação/amigurumi/costura/calculadora/velas/convites, nem buscar domínios dos concorrentes (qlovy, iloveyou.gift, miyogift, gifft.me).
- **WebFetch/curl/navegador bloqueados** (não tentados, conforme instrução). Snapshots `facebook.com/ads/library/?id=` não podem ser abertos → sem corpo de anúncio.
- **Busca por domínio na Meta não funciona**: "qlovy" = 0; "iloveyou.gift" foi tokenizado como "i love you gift" e trouxe 102 anúncios de presentes físicos em EN (ruído).
- **Paginação**: a ferramenta não tem cursor. Truque testado: repetir a busca por `page_ids` filtrando países pequenos (UY, BO, GT, DO), onde os lotes novos às vezes não entregam → aparecem anúncios mais antigos. Funcionou para DecoKit Shop (ver seção 5). Não funcionou para 1500 Moldes e Aprende en casa (0 anúncios nesses países).
- Todos os preços abaixo vêm do título do anúncio (quando o anunciante escreve o preço) ou de outros arquivos `_raw` citados. Nada de preço de checkout foi verificado nesta rodada.

## 1. Queries rodadas (termo → estimated_total_count)

| # | Termo (ES, ACTIVE) | est. total | Leitura |
|---|---|---|---|
| 1 | regalos digitales para vender | 76 | packs de imprimíveis (Bonito Digital MXN ≥18 ads; Recursoslandia "+1.500 Diseños para el Día de la Madre"; Aprende en casa; SabeViva "ENTREGA INMEDIATA"); cristão: Papelería Cristiana (BRL) "Empieza con papelería cristiana", Luciana Cross (BRL) "150 adhesivos católicos para imprimir". Nenhuma revenda de página-presente. |
| 2 | negocio de regalos digitales | 72 | ruído (MLM de catálogo Betterware/Esika, eventos) + Herramientas Digitales Profesionales (COP "⭐⭐⭐⭐⭐ 4.9/5"), Consciencia Emprendedora "Accede al ebook creator pro" (EUR). Nenhuma revenda de página-presente. |
| 3 | página personalizada para tu pareja | 130 | ruído (amarres/videntes, cursos elétrica). |
| 4 | qlovy (+ES) | 0 | busca por domínio não funciona. |
| 5 | iloveyou.gift (+ES) | 102 | ruído EN (presentes físicos). |
| 6 | regalo digital sorpresa con fotos | 14 | ruído (dramas curtos). |
| 7 | PROMOCION POR TIEMPO LIMITADO | 45.014 | termo genérico; confirma a rede de páginas (seção 3). |
| 8 | fichas didácticas | 122 | material para docentes (seção 6, N7). |
| 9 | cuadernillos para vender | 10 | fraco; Criador de Apostila Visual (BRL), Mis Cuadernillos "Aprende y Vende Amigurumis". |
| 10 | lotería personalizada | 147 | ruído (loterias, apostas, advogados). |
| 11 | juegos para baby shower | 493 | quase tudo serviço local (palhaços, animação). Nenhum kit imprimível no top 50. |
| 12 | juegos imprimibles | 382 | domina imprimível infantil educativo (N5), Mentes Magicas (N6), Sonrisas De Fe (N2), Mundo Info Digital (ARS) "Cumple Resuelto + 3 bonos GRATIS". |
| 13 | dinámicas para fiestas | 337 | serviço local. |
| 14 | diplomas editables | 13 | fraco (Detalles Creativos USD, material escolar). |
| 15 | logo con inteligencia artificial | 185 | ruído/cursos de IA. |
| 16 | carta de Santa Claus personalizada | 0 | fora de temporada. |
| 17 | video de Santa Claus personalizado | 1 | El Mundo del Tío May (GTQ), 33,1 d, produto não identificado. |
| 18 | calendario personalizado con fotos | 27 | invita.fun (UYU) "Armá la invita con IA"; Edición Videos (ARS) "Invitaciones Interactivas con botones y música!"; Confirm the date (USD); Micaela Bali (BRL) "6 regalos para mamá, listos para vender"; Franco Peña (ARS, calendário, provável físico). |
| 19 | cupones de amor | 150 | ruído. |
| 20 | etiquetas editables para emprendedores | 14 | fraco. |
| 21 | mockups | 1.742 | global/EN, sem sinal ES. |
| 22 | libros para colorear para vender | 46 | Dayanne Personalizados (BRL, 20+ ads sem título), Paula Fukuda "Crea tu ebook hoy" (N10), Paka Diseno. |
| 23 | preguntas para parejas | 599 | ruído; Las Cartas Sobre La Mesa (BOB, jogo físico); KitListo (N3); Elaine Féliz (sexualidade, provável expert). |
| 24 | dinámicas para grupos | 865 | ruído (escolas de inglês) + cluster cristão (Luz de la Palabra, Momento con Cristo, Carmen Rodríguez, Sonrisas De Fe, KitListo). |
| 25 | catequesis material imprimible | 7 | Sonrisas De Fe; Book Digital (EUR) "La Misa explicada para niños" (6 ads). |
| 26 | dinámicas bíblicas | 190 | Leticia Mariane (BRL) "230 dinámicas listas, una por página"; Carmen Rodríguez (BRL) "280 dinámicas bíblicas para el Ministerio Femenino"; Crea Fácil (USD, 142 ads); Size Shop; Vida Exitosa; Tu Mundo Cristiano; Reino Digital. |
| 27 | escuela dominical | 692 | Bendiciones creativas (USD, 58–60 ads); Marilú y los Niños – Escuela Dominical; Raíces de Fe; Camila Núñez; Crea Fácil. |
| 28 | moldes navideños | 165 | L24 (seção 4). |
| 29 | recetas navideñas para vender | 31 | L28 (seção 4). |
| 30 | mapa de las estrellas personalizado | 4 | L52: Kindred (CLP "Mapa Estelar", provável físico, 275,1 d). Fraco. |
| 31 | documentos importantes familia organizador | 17 | L50: tudo Baggutendencias (COP), 17 ads, 195,2 d; provável produto físico (bolsa/pasta de documentos) — não verificado. |
| 32 | libro personalizado de nuestra historia de amor | 4 | L53: ruído/físico. |
| 33 | plantillas Notion | 28 | L55: Claridad y Acción (USD, painel freelancer, 5 ads), Pablo Coach, Academia Online (curso). Fraco. |
| 34 | menú digital QR | 170 | L36: SaaS/serviço (Tumenu.promo BRL "Tu menú QR, gratis"; LX Diseño Web "Menú digital desde $6,99"; Nedify; Platillo; Foodiq; Meny Mat; Sisas Studio). Nenhum kit de revenda. Todos < 5 d. |
| 35 | retrato de tu mascota | 176 | L43: artistas/produtos físicos (Vincent Van Guauu "Retratos de mascotas desde $650" MXN; Artella "$1,350 al mes"; Mora Studio chaveiros/capas). Nenhum retrato IA digital instantâneo. |
| 36 | carta digital interactiva | 11 | ruído (menus, convites). |
| 37 | regalo virtual para mi novia | 48 | ruído (dramas). |
| 38 | juego de misterio para fiestas | 7 | ruído (Pocket FM). Kit "murder mystery" adulto sem demanda ES visível. |
| 39 | caligrafía para niños | 486 | imprimível infantil (N5) + cadernos Montessori físicos (Pulpería Urbana, Kavel Nova, Market Reeda – "Pagas al Recibir"). |
| 40 | actividades imprimibles para niños | 594 | ≥20 anunciantes de imprimível infantil (N5). |
| 41 | stickers de WhatsApp personalizados | 790 | físico (gráficas). |
| 42 | mensajes para vender por WhatsApp | 1.274 | ruído. |
| 43 | formatos editables contratos | 42 | N9. |
| 44 | recursos terapéuticos para psicólogos | 114 | N8 (≥12 anunciantes). |
| 45 | kit de marca para emprendedoras | 25 | ruído (MLM/beleza). |
| 46 | fondos digitales para fotografía | 13 | ruído (estúdios). |

## 2. Buscas por page_id (contagem de ativos e anúncio mais antigo)

| Página | page_id | Moeda | Ativos | Mais antigo (d) | Títulos | Snapshot |
|---|---|---|---|---|---|---|
| Daniela Michilena | 688632704343010 | USD | 14 | 46,2 | "💝 El regalo que jamás olvidará" (10), "🥹 Un regalo que no olvidará" (4) — **produto não identificado** | https://www.facebook.com/ads/library/?id=1730980927837398 ; https://www.facebook.com/ads/library/?id=914427708152061 |
| Emprede y Genera + Abundancia Suprema + Verdades del Dinero | 1272269899306111 / 1312049798658357 / 1203724022834533 | USD | 186 (conjunto) | ≤0,5 nos 50 vistos | "PROMOCION POR TIEMPO LIMITADO" | https://www.facebook.com/ads/library/?id=948235781089890 ; https://www.facebook.com/ads/library/?id=2344071382794647 ; https://www.facebook.com/ads/library/?id=870644722802658 |
| Productos PARA TI + El Arte del Sabor + Crianza Inteligente | 632945946577857 / 716723351505799 / 746527218534288 | USD | 131 (conjunto) | ≥1,0 (limite) | "PROMOCION POR TIEMPO LIMITADO" | https://www.facebook.com/ads/library/?id=1585000283369888 ; https://www.facebook.com/ads/library/?id=1033550629741892 ; https://www.facebook.com/ads/library/?id=1170877712180460 |
| Docentes Proactivos + Aventuras Didácticas + Mentes Activas + Mat Store | 972208969314942 / 365358764191056 / 1095697386964770 / 112774595110551 | USD/CLP/PEN/USD | 82 (conjunto) | 18,3 (Mentes Activas), 14,5 (Docentes Proactivos), 8,3 (Mat Store), 0,3 (Aventuras) | "Planifica Fácil y Rapido", "Impulso Lector 2026", "OFERTA POR TIEMPO LIMITADO", "Química lista para enseñar" | https://www.facebook.com/ads/library/?id=1376943264066797 ; https://www.facebook.com/ads/library/?id=1964792297442837 ; https://www.facebook.com/ads/library/?id=2623986861404642 |
| Mentes Magicas | 1117276138133211 | USD | 53 (50+) | ≥6,3 (limite) | "🕵️20 casos de misterio · 10 + 10 bonus · +150 desafíos - 5 a 12 años" | https://www.facebook.com/ads/library/?id=3508835569320914 ; https://www.facebook.com/ads/library/?id=2411230622951489 |
| Papelería Cristiana | 1256242664245141 | BRL | 5 | 1,5 | "Empieza con papelería cristiana" | https://www.facebook.com/ads/library/?id=1123414036931102 |
| Luciana Cross | 563346880201775 | BRL | 7 | 1,5 | "150 adhesivos católicos para imprimir" | https://www.facebook.com/ads/library/?id=2164694427443278 |
| invita.fun | 1242601378944228 | UYU | 2 | 1,5 | "Armá la invita con IA", "Mandala por WhatsApp" | https://www.facebook.com/ads/library/?id=1575848001012368 |
| Edición Videos | 108944118567520 | ARS | 2 | 9,1 | "Invitaciones Interactivas con botones y música!", "Videos para eventos" | https://www.facebook.com/ads/library/?id=1387131426917819 |
| Micaela Bali | 1243863505474422 | BRL | 4 | 3,5 | "6 regalos para mamá, listos para vender" | https://www.facebook.com/ads/library/?id=1399201138344671 |
| Paula Fukuda + Paula Fukuda Content Creator | 104741895636839 / 793829720471120 | USD | 118 (conjunto) | 102,1 (Content Creator, "Crea tu ebook hoy") ; 28,7 (Paula Fukuda, "Crea tu ebook hoy") | também "Aprende a crear contenido para marcas", "Reserva tu lugar GRATIS" (expert/curso) | https://www.facebook.com/ads/library/?id=1602948634557244 ; https://www.facebook.com/ads/library/?id=1939300746736674 |
| KitListo | 1170197626183348 | USD | 10 | 12,3 | "Dinámicas para abrir la conversación", "Una guía para cada momento del encuentro", "Renová las propuestas de tu grupo", "★★★★★ (4,9/5) · +1.200 compras" (alegação), "Prepará tus flores antes de encapsular" | https://www.facebook.com/ads/library/?id=1619929066543936 ; https://www.facebook.com/ads/library/?id=1087553573757931 |
| Elaine Féliz | 266308696834568 | USD | 38 | ~9,2 | sexualidade/casal ("Hablen de lo que nunca hablan") — provável expert (E1) | https://www.facebook.com/ads/library/?id=1118976173963639 |
| Momento con Cristo | 1162427483623694 | USD | 20 | 0,4 | "¡Recibe tu material primero, paga después! 🎁" | https://www.facebook.com/ads/library/?id=1105096708599235 |
| Luz de la Palabra | 110777297813929 | BRL | 5 | 1,1 | idem | https://www.facebook.com/ads/library/?id=1501986058430305 |
| Sonrisas De Fe | 110976304108233 | MXN (1 lote USD) | 21 | **132,3** | "🎲 Juegos católicos en PDF", "⛪ Material para Monaguillos — $49 MXN", "🎲 La Gran Aventura de la Fe — $79 MXN", "Juegos Bíblicos para Niños" (64,2 d), "+10 juegos por solo $50 😳" | https://www.facebook.com/ads/library/?id=960747670184450 ; https://www.facebook.com/ads/library/?id=1807257463776916 ; https://www.facebook.com/ads/library/?id=945543148611521 |
| Carmen Rodríguez | 1334213733110650 | BRL | 3 | 0,2 | "280 dinámicas bíblicas para el Ministerio Femenino" | https://www.facebook.com/ads/library/?id=1448393503806981 |
| Bendiciones creativas | 1128535147014509 | USD | 58 (filtro "escuela dominical") / 60 (UY,BO,GT,DO,EC) — 50+ | ≥1,9 (limite) | "RECIBELO GRATIS HOY 🎁" (produto não identificado; aparece em "escuela dominical" e "plantillas editables") | https://www.facebook.com/ads/library/?id=2207771433416512 |
| Crea Fácil | 667918009748933 | USD | 142 (50+) | ≥0,2 (limite) | "Descarga aquí👉" (aparece em "dinámicas bíblicas" e "escuela dominical"; produto incerto) | https://www.facebook.com/ads/library/?id=1605578374250466 |
| Leticia Mariane / Marilú y los Niños / Raíces de Fe / Camila Núñez | 905305779341087 / 1631344880318490 / 1183594788167533 / 764504150083394 | BRL/USD/USD/USD | 43 (conjunto): Leticia 2, Marilú ~15, Raíces 6, Camila ~17 (+1 "Camila") | Marilú **46,0**; Camila Núñez **38,1**; Raíces 3,7; Leticia 0,0 | Raíces: "52 domingos resueltos", "52 lecciones listas para imprimir", "**Un año completo por US$ 12.90**"; Marilú: "¿Qué debe enseñar según la edad?", "Actividades con propósito para su EBV"; Camila: "RECIBELO GRATIS HOY", "DESCARGAR AHORA", "Converse conosco" (PT) | https://www.facebook.com/ads/library/?id=1065612009682467 ; https://www.facebook.com/ads/library/?id=1408284694545043 ; https://www.facebook.com/ads/library/?id=1339648501490124 ; https://www.facebook.com/ads/library/?id=1428392392568137 |
| Adorabook + MiBook + Mi Cuento Infantil Personalizado | 454878527708822 / 1161535813714856 / 166953813165193 | USD/—/MXN | 478 (conjunto) | Adorabook ≥6,8 (limite) | Adorabook: "38 pages, zero screens", "Order today, keep forever", "Use Coupon: FIRSTBOOK", "Search and Find Adventure" (EN/DE) → **livro impresso** (inferência forte pelo título). Mi Cuento: "Haz que tu pequeño sea parte de la película" (formato não determinado). MiBook não apareceu nos 50 mais novos. | https://www.facebook.com/ads/library/?id=27280826378260472 ; https://www.facebook.com/ads/library/?id=1105655501880438 |
| Mundo Mini Creativo | 1136521929553596 | PEN | 7 | **50,0** | "345 actividades listas para imprimir", "El kit perfecto para desarrollar la motricidad fina desde casa", "Imprime, juega y aprende con el mundo de los dinosaurios" | https://www.facebook.com/ads/library/?id=2018364095511500 ; https://www.facebook.com/ads/library/?id=1573902850908377 |
| Maestro PDF | 1043793655490148 | USD | 14 | 9,2 | "+ 872 copias vendidas🤩" (alegação) | https://www.facebook.com/ads/library/?id=1735363790907272 |
| Aprendo a Leer en Casa | 1328579090336504 | USD | 7 | 10,7 | "10 minutos por día, sin pantallas", "⭐⭐⭐⭐⭐ (4.8/5)" | https://www.facebook.com/ads/library/?id=2138688613526775 |
| Documentum | 264187770109193 | MXN | 3 | 1,1 | "Formatos laborales por $299 MXN", "Más de 300 formatos por $299 MXN" | https://www.facebook.com/ads/library/?id=930229583043672 |
| Navidad Creativa + Navidad creativa (x2) + Tu Rincón Artesano | 478408612020119 / 1212617528608366 / 1386530277867221 / 1346254331909575 | COP/COP/USD/MXN | 55 (conjunto) | Navidad Creativa 478… **24,1**; demais ≤0,9 | "CURSO VIRTUAL", "CLASE VIRTUAL", "⭐⭐⭐⭐⭐", "+360 moldes", "Primero recibe, luego pagas 📱", "🖨️ Imprime → ¡y comienza a crear!" | https://www.facebook.com/ads/library/?id=1064136079683757 ; https://www.facebook.com/ads/library/?id=1044361368569939 ; https://www.facebook.com/ads/library/?id=1103407975809211 |
| Event Builder Studio + Confirm the date | 655700850956283 / 800013626539565 | USD | 1 + 13 | 2,2 / 26,0 | Event Builder: "Crea invitaciones digitales para tus clientes"; Confirm the date: SaaS de convite + RSVP + mesas, "Solicita tu demo personalizado gratis", "Fiestas de XV 2026" | https://www.facebook.com/ads/library/?id=1056284580730092 ; https://www.facebook.com/ads/library/?id=1748439102723979 |

## 3. Lacuna "PROMOCION POR TIEMPO LIMITADO"

- Rede de pelo menos 6 páginas com o **mesmo título** "PROMOCION POR TIEMPO LIMITADO", tudo em USD, anúncios recriados em lotes diários (criações em 1790082xxx–1790095xxx):
  - Emprede y Genera + Abundancia Suprema + Verdades del Dinero: **186** ativos (conjunto).
  - Productos PARA TI + El Arte del Sabor + Crianza Inteligente: **131** ativos (conjunto).
  - Total ≥ **317** anúncios ativos.
- Os nomes das páginas cobrem nichos diferentes (dinheiro/abundância, receitas, criação de filhos, genérico). Leitura (inferência, **não verificada**): uma operação multi-nicho de low ticket (provavelmente ebooks) que troca apenas a página e o criativo. O produto da página "Emprede y Genera" continua **não identificado** (snapshot bloqueado, WebSearch esgotado). Suspeita E2 nas páginas "Abundancia Suprema" e "Verdades del Dinero".
- Snapshots para o usuário abrir: https://www.facebook.com/ads/library/?id=1063408609866794 ; https://www.facebook.com/ads/library/?id=1995527901381211 ; https://www.facebook.com/ads/library/?id=1142339368455421 ; https://www.facebook.com/ads/library/?id=1033550629741892 (El Arte del Sabor) ; https://www.facebook.com/ads/library/?id=1170877712180460 (Crianza Inteligente).

## 4. Resultado por lacuna do consolidador

- **L01 (Mimo Gift Revenda)**: +3 termos, 0 anunciantes de revenda de página-presente (76, 72 e 130 resultados, todos ruído ou packs de imprimíveis). Busca por domínio não funciona na ferramenta. Daniela Michilena: 14 ativos, mais antigo **46,2 d**, 2 títulos, USD; produto segue não identificado. Achado lateral: Micaela Bali (BRL) "6 regalos para mamá, listos para vender" (4 ads, 3,5 d) — kit de presentes para revender, tipo de produto não verificado.
- **L08 (página-presente B2C ES)**: busca por domínio impossível; "carta digital interactiva" (11) e "regalo virtual para mi novia" (48) = ruído. Continua sem evidência na Meta ES por palavra-chave. Concorrentes web existem (outro arquivo), mas não aparecem em anúncios buscáveis por termo. Não verificado.
- **L02/L03 (editor web de convite)**: checkouts da Hotmart **não abertos** (ferramentas bloqueadas). Novas evidências Meta: invita.fun (UYU, editor de convite com IA para o consumidor, 2 ads, 1,5 d); Edición Videos (ARS, "Invitaciones Interactivas con botones y música!", 2 ads, 9,1 d); Confirm the date (USD, SaaS de convite com RSVP e mesas, 13 ads, **26,0 d**, venda por demo — não é low ticket); Event Builder Studio segue com 1 anúncio (2,2 d); Limasystem (PEN) "Toda la información de tu boda en un solo enlace".
- **Longevidade de páginas 50+**: truque de filtro por país pequeno:
  - DecoKit Shop (737352542803130): 55 ativos em UY/BO/GT/DO; mais antigo visível **136,6 d** (antes: 81–90 d). Ainda limite inferior (5 anúncios mais antigos não aparecem). Títulos antigos: "🎉 El secreto de las mamás que decoran como pros", "💰 Empieza a vender sin saber diseñar", "🌸 La temática más tierna del momento". Snapshot do mais antigo visto: https://www.facebook.com/ads/library/?id=1964080760865418
  - Diego Hernandez (977127798806735): 104 ativos em UY/BO/GT/DO; mais antigo visível 20,2 d (limite).
  - Entre Mujeres (1180416348492259): 31 ativos em UY/BO/GT/DO, todos visíveis; mais antigo **6,9 d** → operação recente.
  - 1500 Moldes (841929342339578) e Aprende en casa (110643181782006): 0 anúncios nos países pequenos → não medido.
  - Tell My Tale, Sua Historinha, Alimenta tu Vida: não refeitos nesta rodada.
- **Preços da Hotmart (sublimação, amigurumi, costura, calculadora, velas, convites)**: não verificados (ferramentas bloqueadas).
- **Music Creator Pro**: registrado como linha E1 (dados de `_raw/fase1_meta_servicos.md`: page_id 1171913759344035, ~45+ ads, ~4,5 d, título "🏆 Crea música con IA desde cero", snapshot https://www.facebook.com/ads/library/?id=929866986846204). Não remedido.
- **L24 (moldes natalinos)**: "moldes navideños" = 165. Anunciantes ≥8: Tu Rincón Artesano (MXN, 9 ads, 0,2 d, "Primero recibe, luego pagas"), Navidad Creativa 478408612020119 (COP, ~36 ads incluindo "CURSO VIRTUAL"/"CLASE VIRTUAL", **24,1 d**), Navidad creativa 1212617528608366 (COP, "+360 moldes", 6 ads, 0,9 d), Navidad creativa 1386530277867221 (USD, 1), Mentoría Global "🧵 Moldes Creativos" (USD, 3), Aprende en casa (PEN), Eduka "Vende tus muñecos 🎁" (COP, 2), Cerebritos en Acción (USD, 4), Paulina Morales (USD, 4), Academia Creativa (USD). Temporada começando (anúncios < 1 d em quase todos).
- **L28 (receituário sazonal)**: "recetas navideñas para vender" = 31. Conexión Digital "Pack Navideño + de 1084 descargas" (USD, 6 ads, 4,3 d), Rincón Creativo Digital-1 "Entrega Inmediata" (USD, 6), Dulce Negocio MX (2), Creaciones Sencillas "Por solo $10.000 pesos" (COP). Anúncios da temporada passada **ainda ativos**: Chefsito "🎄 Gana DINERO EXTRA esta Navidad" (COP) **366,5 d**; El Atelier de Cons 350,5 d; DulceVaso 316,8 d; Mundopdf 306,1 d; Repostería Master Class "+ DE 500 RECETAS DE POSTRES NAVIDEÑOS" (PEN) 287,1 d (https://www.facebook.com/ads/library/?id=4389069404657290 ; https://www.facebook.com/ads/library/?id=1096317955818454). Podem ser anúncios esquecidos com verba baixa (não verificado).
- **L45 (Papai Noel)**: "carta de Santa Claus personalizada" = 0; "video de Santa Claus personalizado" = 1 (El Mundo del Tío May, GTQ, 33,1 d, produto não identificado). Fora de temporada confirmado; repetir em novembro.
- **L50 (kit "si me pasa algo")**: "documentos importantes familia organizador" = 17, todos de Baggutendencias (COP, 102366569527594), 17 ads, mais antigo **195,2 d** ("Salva Tus Documentos Del Desastre 🔥", "Todo en un lugar 📂", "Protege El Legado Familiar Hoy 🕊️"). Pelo nome da página, provável produto físico (bolsa de documentos) — **não verificado**. Mostra que o ângulo "proteger documentos da família" roda há 6 meses. Snapshot: https://www.facebook.com/ads/library/?id=1369633248223786
- **L52 (estrela/mapa estelar)**: "mapa de las estrellas personalizado" = 4 (Kindred CLP "Mapa Estelar", 275,1 d, provável físico; InviVideo). Demanda ES fraca.
- **L53 (romance personalizado)**: "libro personalizado de nuestra historia de amor" = 4, ruído/físico (Xodó Gifts, Fotoregalos, Caja Mágica "PHOTOBOOK RECUERDOS").
- **L14 (jogos de festa imprimíveis)**: "juegos para baby shower" 493 e "dinámicas para fiestas" 337 = serviços locais; "lotería personalizada" 147 = ruído. Único kit de festa visto: Mundo Info Digital (ARS, 1269146306280476) "Cumple Resuelto + 3 bonos GRATIS" (4 ads). Demanda ES para jogos imprimíveis de festa: **fraca/não verificada**.
- **L56 (templates de presentes físicos)**: sem sinal novo (calendário 27; Micaela Bali).
- **L36 (menu QR)**: 170, dominado por SaaS/serviço; nenhum kit de revenda; todos < 5 d.
- **L55 (Notion ES)**: 28, fraco (Claridad y Acción USD, 5 ads, 0,5 d).
- **L39/L43**: Adorabook = livro impresso (título "38 pages, zero screens"; cupons). Mi Cuento Infantil Personalizado: formato não determinado. Retrato de pet ES = artesanal/físico, sem versão IA digital instantânea visível.

## 5. Padrões observados

- **Arbitragem BR → ES**: muitas páginas com moeda **BRL** anunciando em espanhol nos clusters cristão (Papelería Cristiana, Luciana Cross, Luz de la Palabra, Carmen Rodríguez, Leticia Mariane, Papel y Fe), infantil (Su Profe Alice, Mary Cakes, Emily Carter, Emotions Pack, Cajá Terapéutica) e terapeutas (Biblioteca Clínica Infantojuvenil, Kit de Herramientas Terapéuticas, Kit Duelo, Matrimonios Fuertes, Paola García). Isso indica operadores brasileiros traduzindo ofertas que já rodam no BR.
- **"Recebe primeiro, paga depois"** (Momento con Cristo, Luz de la Palabra, Tu Rincón Artesano, El Mundo de Lolita, Alimenta tu Vida): modelo de cobrança posterior por WhatsApp → exige atendimento humano (E3) se copiado.
- Rotação diária de criativos continua a regra; anúncios com 30+ d são exceção e valem como sinal forte: Sonrisas De Fe 132,3 d; DecoKit 136,6 d; Mundo Mini Creativo 50,0 d; Marilú 46,0 d; Daniela Michilena 46,2 d; Camila Núñez 38,1 d; Paula Fukuda 102,1 d (curso); Baggutendencias 195,2 d (físico?); formatos legais 103–310 d.

## 6. Ideias novas (distintas da long list de 56)

| ID | Ideia | Busca (est.) | Anunciantes | Máx. variações | Mais antigo (d) | Preço visto | Eliminatória suspeita |
|---|---|---|---|---|---|---|---|
| N1 | Kit de aulas prontas para Escola Dominical / EBV (52 lições + atividades imprimíveis) | "escuela dominical" 692 | ≥5 (Raíces de Fe, Marilú, Camila Núñez, Bendiciones creativas [produto incerto], Crea Fácil [incerto]) | 142 (Crea Fácil, incerto) / 58–60 (Bendiciones) / ~17 (Camila) | 46,0 (Marilú) | US$ 12,90 ("Un año completo") | nenhuma forte; fora do nicho renda extra (uso próprio) |
| N2 | Jogos e material católico em PDF (catequese, coroinhas, 1ª comunhão) | "catequesis material imprimible" 7; aparece em "juegos imprimibles" 382 e "dinámicas bíblicas" 190 | ≥3 (Sonrisas De Fe, Book Digital EUR, Papel y Fe BRL) | 21 (Sonrisas De Fe) | **132,3** | MXN 49–79 (~US$ 2,7–4,3); "+10 juegos por solo $50" | nenhuma; ticket abaixo de US$ 5 |
| N3 | Pack de dinâmicas prontas para ministérios e grupos (mulheres, jovens, células, encontros) | "dinámicas bíblicas" 190 | ≥5 (Carmen Rodríguez, Leticia Mariane, Momento con Cristo, Luz de la Palabra, KitListo) | 20 (Momento con Cristo) | 12,3 (KitListo) | não visto | E3 se usar "paga depois" |
| N4 | Papelaria/stickers cristãos e católicos para imprimir e vender | "regalos digitales para vender" 76 (2 anunciantes) | 2 (Papelería Cristiana, Luciana Cross — ambos BRL) | 7 | 1,5 | não visto | E2 leve (ângulo renda extra); evidência fraca |
| N5 | Kit de atividades imprimíveis para crianças (motricidade, leitura, pré-escola, emoções) | "actividades imprimibles para niños" 594; "juegos imprimibles" 382; "caligrafía para niños" 486 | ≥20 | 14 (Maestro PDF) | 50,0 (Mundo Mini Creativo) | US$ 9,99 (Emily Carter, inglês infantil); ~US$ 4,3 (Mega Kits "30 Bolivianos") | nenhuma; fora do nicho renda extra; saturado |
| N6 | Casos de mistério / jogo de detetive imprimível para crianças (5–12 anos) | dentro de "juegos imprimibles" 382 | 1 visível (Mentes Magicas) | 53 (50+) | ≥6,3 (limite) | não visto | E5 leve (escrever 20 casos); 1 anunciante só |
| N7 | Material didático pronto para professores (planejamentos e fichas por série/matéria) | "fichas didácticas" 122 | ≥10 (Docentes Proactivos, Mentes Activas, Mat Store, Aventuras Didácticas, Profe Listo, Material Digital 2026, Aula Digital Pro, Banco Educativo, Perú EduEbooks, Mi apoyo maestro) | ~18 (Docentes Proactivos) | 18,3 (Mentes Activas) | "Clases de Biología por solo Q35" (~US$ 4,5, Aventuras Didacticas USD) | E5 (currículo por país); fora do nicho renda extra |
| N8 | Kit de recursos clínicos prontos para psicólogos e terapeutas (sessões, TCC, luto, casal, infantojuvenil) | "recursos terapéuticos para psicólogos" 114 | ≥12 | 6 (Nebulosa Creativa, Biblioteca Clínica) | 4,6 | "¡Todo por solo 5 dólares!" (Paola García) | risco de política (saúde) e E5 (conteúdo técnico) |
| N9 | Pack de formatos/contratos editáveis para PMEs (RH, trabalhista, jurídico) | "formatos editables contratos" 42 | ≥6 | 3–5 | 309,9 / 308,7 (Línea de Aprendizaje / Super Compendio Legal; produto não identificado) | MXN 299 (~US$ 16, Documentum); MXN 99 (Media Center) | E4 (Media Center "+11.000 formatos + cursos" = cara de PLR); risco jurídico |
| N10 | Kit/ferramenta para criar e vender ebooks e livros de colorir com IA | "libros para colorear para vender" 46 | ≥3 (Paula Fukuda x2 páginas, Consciencia Emprendedora, Dayanne Personalizados [incerto]) | 118 (Paula Fukuda, conjunto) | 102,1 | não visto | E1 (Paula Fukuda = criadora/curso), E2 (promessa de ganho) |
| N11 | (linha E1 registrada) Curso de criar música com IA para vender | "canción personalizada" (outro arquivo) | 1 (Music Creator Pro) | ~45+ | ~4,5 | não visto | E1 (curso), E2 |

Links por ideia estão no JSON final e na seção 2.
