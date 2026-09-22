# Fase 1 — Fonte GLOBAL (EUA / Etsy / TikTok / Gumroad) -> o que ainda não chegou na LATAM em espanhol

Data da coleta: 2026-09-22. Referência de "agora": epoch 1790095977. Dias ativo = (1790095977 - ad_delivery_start_time) / 86400.
Ferramenta: `mcp__Meta_Ads__ads_library_search`, ad_active_status=ACTIVE, limit 50.
- Lado EUA: termo em inglês, countries=[US].
- Lado ES: termo em espanhol, countries=[MX, CO, AR, CL, PE, US] ("ES6") ou só LATAM, sem US, quando o US poluía com anúncio em inglês ("ES5" = MX, CO, AR, CL, PE; "ES10" = MX, CO, AR, CL, PE, EC, GT, BO, UY, DO).

## 0. Limitações (ler antes dos números)

1. **WebSearch indisponível nesta fonte.** A cota da sessão (200/200) já estava esgotada quando este agente começou. As 4 primeiras buscas falharam: "best selling Etsy digital downloads 2026 trending", "trending digital products 2026 faceless no expert", "eRank Everbee top selling digital products Etsy 2026 list" e "AI personalized storybook for kids trend 2026 sales". Por isso **não há links de artigos, Etsy, eRank, Everbee, Gumroad nem TikTok Creative Center**. O "lado EUA" foi medido **só pela Biblioteca de Anúncios da Meta com countries=US e termo em inglês**. É um proxy de demanda paga, não de venda orgânica. Produto que vende bem no Etsy por SEO pode não aparecer aqui.
2. **A busca por palavra-chave é "unordered" e muito ruidosa.** Termos genéricos em inglês ("video from Santa", "savings challenge", "coloring book from your photos", "done for you digital products", "in case of emergency binder", "star map") trouxeram dramas, novels e cassino, com estimated_total_count entre 2 mil e 370 mil. Esses counts não servem para comparar. Só uso o count quando o topo é majoritariamente relevante, e digo quando não é.
3. **Rotação diária de criativos.** Os grandes anunciantes (Tell My Tale, ReadyExcels, Knowhow Co.) recriam anúncios todo dia. Por isso "dias do anúncio mais antigo no top 50" **subestima** a longevidade. Quando aparece anúncio com 30+ dias, é sinal forte.
4. Sem texto do corpo do anúncio, o tipo de entrega (digital ou físico) foi inferido pelo título. Exemplos: "Free Fast Shipping" indica físico, "Download" e "Pay once" indicam digital. Onde há incerteza, está marcado.
5. **Preços** só aparecem quando estão no título do anúncio. O resto está marcado como "não verificado".
6. Moeda BRL em anúncio escrito em espanhol indica operador brasileiro vendendo em ES (arbitragem PT->ES, igual ao achado de `fase1_brasil_espelho.md`).

## 1. Queries rodadas (Meta Ad Library, ACTIVE)

| # | termo | países | est_total | leitura |
|---|---|---|---|---|
| G1 | personalized storybook | US | 675 | **relevante**: cerca de 14 páginas de livro infantil personalizado no top 50 |
| G2 | cuento personalizado | ES6 | 1.248 | ruído (dramas, estética). Relevante só "Mi Cuento Infantil Personalizado" |
| G3 | video from Santa | US | 374.971 | ruído total, fora de temporada |
| G4 | elf on the shelf printables | US | 6.796 | ruído. Só SleepyMommy "ELF KITS ONLY $39" (físico) |
| G5 | duende travieso | ES6 | 46 | ruído (cassino "Lucky Cascade") |
| G6 | digital planner | US | 887 | ruído. Relevantes: Emery, TeacherPlannerhq, Daily Thrive Digital, My Digital Darling |
| G7 | planner digital | ES6 | 1.074 | ruído. Relevantes: Meraki.planners (MXN), Mundo Digital (CLP "$3.500") |
| G8 | pet portrait | US | 4.708 | maioria POD físico. Digital com IA: Pawnted, Wag'n'Tails |
| G9 | retrato mascota | ES5 | 201 | só artesãos e produto físico. **Nenhum digital com IA** |
| G10 | savings challenge | US | 3.527 | ruído total (DramaBox) |
| G11 | reto de ahorro | ES5 | 178 | ruído total (concessionárias, universidades) |
| G12 | budget planner spreadsheet | US | 141 | **FORTE**: cerca de 14 páginas de planilha (orçamento, dívida, casamento) |
| G13 | plantilla excel control de gastos | ES6 | 161 | **relevante**: cerca de 15 páginas, várias em BRL |
| G14 | finanzas personales plantilla | ES10 | 88 | **relevante**: cerca de 15 páginas, várias em BRL |
| G15 | scavenger hunt printable | US | 12 | quase nada (activity books) |
| G16 | baby shower games printable | US | 2 | nada |
| G17 | in case of emergency binder | US | 20.470 | ruído. The Estate Kit apareceu pela G15 |
| G18 | party games download | US | 2.528 | ruído |
| G19 | documentos importantes si fallezco familia | ES6 | 0 | nada |
| G20 | star map | US | 2.862 | ruído, mas acha Astrography e Star Registration |
| G21 | nombre a una estrella | ES10 | 101.616 | ruído total |
| G22 | coloring book from your photos | US | 372.410 | ruído total |
| G23 | Notion template | US | 136 | fraco: Digihub (INR), GCC Market "Airbnb Host Notion Template" |
| G24 | prayer journal | US | 1.610 | misto: Alabaster Co (físico), St. Jonathan, Emily Carter "365 prayers" |
| G25 | diario de oración | ES10 | 903 | misto: El Club de Los E-books "Oraciones que el cielo responde" (ebook) |
| G26 | done for you digital products | US | 66.075 | ruído total (não deu para medir PLR/MRR aqui) |
| G27 | planificador de boda | ES10 | 11 | só 2 páginas: Educación Online Creativo e Mi Boda en Orden |
| G28 | salir de deudas plantilla | ES10 | 8 | Kuamma Growth (ARS), Amelia Charlotte, Zona365, Digitt (fintech) |
| G29 | personalized romance novel starring you | US | 2 | Ember Books ("What if the heroine had your name?") |
| G30 | libro personalizado de nuestra historia | ES10 | 21 | photobooks físicos + AdOptimizer AI "cuento con IA" (UYU, 31 d) |

## 2. Anunciantes medidos por page_id (ACTIVE, limit 50)

| página | page_id | país/moeda | nº ativos | mais antigo (dias) | o que vende (pelo título) | link exemplo |
|---|---|---|---|---|---|---|
| Tell My Tale | 620642177805989 | US, USD (títulos em EN, ES e IT) | **416** (est_total da página) -> 50+ (limite) | 1,4 no top 50 (rotação diária) | livro infantil personalizado. Título "Personalized Superhero Book, 30+ Illustrations, Free Fast Shipping" indica **físico** | https://www.facebook.com/ads/library/?id=1360738943787467 (ES "El regalo perfecto") / https://www.facebook.com/ads/library/?id=4573870149538288 |
| Tell My Tale, filtrada para MX, CO, AR, CL, PE | 620642177805989 | — | **0** | — | os anúncios em ES **não entregam** nesses 5 países (devem mirar hispanos nos EUA ou a Espanha; não verificado) | — |
| Fiktola | 1241381739066137 | US, USD | 12 | 0,5 (novo) | livro de 24 páginas a partir de 1 foto. Ângulos: "potty book", "Made for one reader. Her." | https://www.facebook.com/ads/library/?id=2423070578217852 / https://www.facebook.com/ads/library/?id=1084433280952882 |
| Ember Books | 935155233023535 | US, USD | 2 | 4,6 | romance em que a heroína tem o nome da compradora | https://www.facebook.com/ads/library/?id=1824630655370309 |
| AdOptimizer AI | 972141752647821 | UY, UYU | ≥4 | **31,0** | "Convierte su historia en un cuento con IA" | https://www.facebook.com/ads/library/?id=1363498955949233 |
| Pawnted | 1092672333918895 | US, USD | 6 | 0,5 (novo) | "Upload A Photo. Get A Portrait In Seconds." (retrato de pet com IA, instantâneo) | https://www.facebook.com/ads/library/?id=1651371953077138 |
| Wag'n'Tails | 471500509389658 | US, USD | 5 | 2,4 | retrato de pet a partir de foto ("See What Your Photo Becomes"; também ângulo de luto: "sympathy gift") | https://www.facebook.com/ads/library/?id=3235304540008955 |
| Ultimate Budget Planner | 485276957995076 | US, USD (também Índia, "₹499") | **≥33** | **72,1** | planilha de orçamento e quitação de dívidas, "$9 Once", "No Formulas. No Subscription." | https://www.facebook.com/ads/library/?id=1804776104232069 (72 d) / https://www.facebook.com/ads/library/?id=1713396137461636 ($9) |
| ReadyExcels | 545710845281579 | EUR | **50+ (limite)** (est 315 somando 4 páginas) | 14,6 (visto na busca G12), 0,8 no top 50 | "420+ Ready-to-Use Excel Templates" | https://www.facebook.com/ads/library/?id=1099021122635303 |
| The Sheetflow | 1177742422082457 | US, USD | 2 | 1,2 | planilha de orçamento "One number. Dark mode. Pay once." | https://www.facebook.com/ads/library/?id=1416818590424154 |
| Emily Parker | 893953403798866 | US, USD | ≥2 | 3,3 | "An Easier Way to Track Your Budgeting" | https://www.facebook.com/ads/library/?id=1582302953383635 |
| The Forever Planner | 664735763399792 | US, USD | ≥4 | 15,1 | "All-In-One Wedding Planner Spreadsheet" | https://www.facebook.com/ads/library/?id=1292553966214596 |
| The Knowhow Store | 1288632857660929 | US, USD | ≥7 | 1,1 | "Your Wedding Math, Automated" (planilha de orçamento de casamento) | https://www.facebook.com/ads/library/?id=1236779481978530 |
| Please Find Your Seat | 150148801517371 | AUD | 11 | 8,6 | mapa de mesas digital de casamento | https://www.facebook.com/ads/library/?id=1058321287010574 |
| The Knowhow Co. | 1002344749639699 | US, USD | ~150 (estimativa: 200 somando 3 páginas, menos Estate Kit e Knowhow Store) | 0,1 a 0,8 no top 50 | **fábrica multi-nicho de downloads**: moldes de renda de bilro "1,000+ Prickings", precificação para autônomos "Still Pricing Jobs By Eye?", jogos de festa "See a room with zero phones out", Natal | https://www.facebook.com/ads/library/?id=1851384539181033 / https://www.facebook.com/ads/library/?id=1636605181316151 |
| The Estate Kit | 1215301468337012 | US, USD | **41** | **52,8** | kit/pasta "se eu morrer" para a família, com versões localizadas "American Estate Kit" e "Aussie Estate Kit" | https://www.facebook.com/ads/library/?id=1049421337473285 (52,8 d) / https://www.facebook.com/ads/library/?id=1719777220150961 |
| Star Registration | 899256617081547 | US, USD (também IT "Regala una stella") | cerca de 14 no top 50 (est 231 somando 2 páginas) | 6,8 | "A star named for them", **"Free worldwide shipping"** indica kit físico | https://www.facebook.com/ads/library/?id=1091840433262853 |
| Astrography | 361004128229 | US, USD | cerca de 36 no top 50 | 6,6 | mapas estelares e lunares impressos | https://www.facebook.com/ads/library/?id=960233063104551 |
| JP37 Designs | 831562820346830 | **BRL**, anúncio em ES | 9 | 14,6 | "Control de Finanzas Personales" | https://www.facebook.com/ads/library/?id=1604762814349721 |
| Mis Diarios Shop | 162514907511457 | MXN | 3 | 14,4 | "Pago único de $99 MXN" (≈ US$5,4, estimativa a 18,5 MXN/USD) | https://www.facebook.com/ads/library/?id=1583604520109903 |
| Mis Finanzas Pro | 930127610190546 | USD e **BRL**, em ES | ≥9 | 15,5 | "¿Sientes que el dinero desaparece cada mes?", "pack de plantillas de Excel" para negócio | https://www.facebook.com/ads/library/?id=902487309322131 / https://www.facebook.com/ads/library/?id=948853507681690 |
| Dinero Con Foco | 1134927189714463 | **BRL**, em ES | 4 | 2,1 | "Controla las finanzas de tu negocio en un solo Excel" | https://www.facebook.com/ads/library/?id=1072733119070079 |
| Finanzas 360 | 1246860735182175 | **BRL**, em ES | 1 | 2,1 | "¿Tu dinero parece desaparecer antes de terminar el mes?" | https://www.facebook.com/ads/library/?id=961308283068282 |
| Atlas Digital | 564067083458135 | PEN | ≥9 | 7,2 | "70% DSCTO SÓLO HOY!" (planilha de finanças, incerto) | https://www.facebook.com/ads/library/?id=1415874787303695 |
| Kuamma Growth | 423231620870811 | ARS | ≥3 | **55,0** ("Aprendé a gestionar tus deudas", pode ser curso: E1?) | "Planilla de Presupuesto", "Cancelá tus Deudas" | https://www.facebook.com/ads/library/?id=1398969035659933 / https://www.facebook.com/ads/library/?id=958391360640944 |
| Digitt | 353094315043188 | MXN | 50+ | 62,6 (visto na G28) | "Paga tus tarjetas de crédito más fácil": **fintech**, não é planilha. Descartado como concorrente | https://www.facebook.com/ads/library/?id=1642313237353564 |

Outras páginas relevantes vistas uma vez, sem medição por page_id:
- Livro personalizado (EUA): Sundayfawn, StorybookYou, Talewix ("Their Name, Their First Bible"), YanYan, Magic Story ("Turn your child into a hero in 60 Seconds", https://www.facebook.com/ads/library/?id=1400883891512374), Librio, Dreamy Little Books (anúncio de listing do Etsy). Há também o cluster "The Perfect Gift": Faith Over Fear, Amazing kid gifts, Margaret Turner, Kathleen Murphy e Patricia Williams, com o mesmo título e anúncios criados no mesmo segundo, ou seja, um operador com várias páginas.
- Planilhas (ES): Orlando Aliaga "Plata Clara | Plantilla de Finanzas Personales en Excel" (PEN, https://www.facebook.com/ads/library/?id=1083488794424989), Familia sin deudas "Plantilla Metodo 50/30/20 + Bonos" (CLP, https://www.facebook.com/ads/library/?id=2073944130155683), Eden Store "30+ Plantillas de Excel por solo $3!" (https://www.facebook.com/ads/library/?id=958657899907731), Iglesia Control PRO (BRL, "Organiza tu iglesia por solo US$ 12.90"), Presupuesta (MXN), Manual de Finanzas (COP, "Controla tu sueldo en 5 minutos"), Tu plantilla perfecta (ARS), Imperio Digital (COP, 9 anúncios, 6,2 d), Amelia Charlotte ("Organiza mejor tus finanzas").
- Casamento (ES): Educación Online Creativo, com "Planificador Secreto Wedding Planner" e "Eleva tus ganancias". É o negócio de wedding planner, não a planilha dos noivos (E2?) (https://www.facebook.com/ads/library/?id=1060663986758984). Mi Boda en Orden (PEN, 1 anúncio, https://www.facebook.com/ads/library/?id=1390966772626553).
- Retrato de pet (ES), só físico ou feito à mão: Vincent Van Guauu "Retratos de mascotas desde $650" (MXN, https://www.facebook.com/ads/library/?id=2446503752546737), Peludolandia (COP), Sofiamigurumii (amigurumi), Artella Atelier, vários tatuadores.
- Planner digital: Emery Guilt-Free Planner (https://www.facebook.com/ads/library/?id=1066876329290262), TeacherPlannerhq (EUR), Daily Thrive Digital "Complete bundle in just $4.99" (https://www.facebook.com/ads/library/?id=4063908807246549). No ES: Meraki.planners (MXN, https://www.facebook.com/ads/library/?id=2809259032789250), Mundo Digital "SOLO X HOY $3.500" (CLP, https://www.facebook.com/ads/library/?id=1611918817128930).
- Oração: Alabaster Co (https://www.facebook.com/ads/library/?id=1792545215214078, físico), Emily Carter "365 prayers for someone lost" (EUR, https://www.facebook.com/ads/library/?id=28000670769632875). No ES: El Club de Los E-books "Oraciones que el cielo responde" (8 anúncios, https://www.facebook.com/ads/library/?id=1150490140976805).
- Notion: Digihub "ADHD Daily Planner -- Notion Template" (INR, https://www.facebook.com/ads/library/?id=1661567358725931), GCC Market "The Airbnb Host Notion Template" (https://www.facebook.com/ads/library/?id=1558452698928843).

Dados de outro agente, reaproveitados sem nova medição (fonte: `_raw/fase1_brasil_espelho.md`): Mi Cuento Infantil Personalizado (166953813165193) com 25 anúncios e 43,3 d; Adorabook com 11 e 52,2 d; MiBook com 3 e 60 d. "video personalizado de Santa Claus" = 0 em ES (fora de temporada).

## 3. Ideias: evidência nos EUA x chegada em ES

| # | ideia | EUA (proxy Meta) | ES (proxy Meta) | status em ES |
|---|---|---|---|---|
| 1 | Planilha de orçamento e quitação de dívidas (Google Sheets/Excel, pagamento único) | G12 = 141, cerca de 14 páginas. UBP com ≥33 anúncios e **72,1 d**, "$9 Once". ReadyExcels 50+ | G13 = 161 e G14 = 88: cerca de 15 páginas pequenas, **várias em BRL** (arbitragem BR). Mais antigo de planilha: 15,5 d. Preço visto: $99 MXN e "30+ por $3" | **chegando** (muitos players pequenos, nenhum dominante nem antigo) |
| 2 | Livro infantil personalizado com IA (PDF/flipbook instantâneo) | G1 = 675, cerca de 14 páginas. Tell My Tale 416 (físico, também em ES e IT). Fiktola e Magic Story digitais, "in 60 seconds" | Mi Cuento Infantil Personalizado 25/43 d, Adorabook 11/52 d (outro agente), AdOptimizer AI 31 d (UY). Tell My Tale = 0 em MX/CO/AR/CL/PE | **chegando** |
| 3 | Kit "si me pasa algo" (pasta de emergência da família, PDF preenchível + planilha) | The Estate Kit: 41 anúncios, **52,8 d**, versões locais US e AU | G19 = 0. Nenhum player visto | **ainda não chegou** (termos ES alternativos não testados) |
| 4 | Planilha de casamento + mapa de mesas digital | cerca de 8 páginas (Forever Planner 15 d, Knowhow Store, Please Find Your Seat com 11 anúncios, Wedding Sage, Matron of Order, Your Wedding Mate, Ever Vow's/Etsy, My Digital Darling) | G27 = 11: só 1 player da planilha dos noivos (Mi Boda en Orden, 1 anúncio) | **ainda não chegou** |
| 5 | Retrato de pet com IA, instantâneo e digital | Pawnted (6 anúncios, novo), Wag'n'Tails (5, 2,4 d). Muitos POD físicos | G9 = 201, só artesãos e físico | **ainda não chegou** (a versão digital com IA) |
| 6 | Estrela registrada / mapa estelar digital | Star Registration (≈14 anúncios, físico, também IT), Astrography (≈36, impresso). est 231 | ruído, nenhum player visto | **ainda não chegou** (não verificado: busca ES ruidosa) |
| 7 | Romance personalizado ("ela é a protagonista") | Fiktola (12), Ember Books (2, 4,6 d): emergente | G30 = 21, só photobooks físicos | **ainda não chegou** (também emergente nos EUA) |
| 8 | Planner digital (GoodNotes/PDF hiperlinkado) | fraco no Meta (Emery, TeacherPlannerhq, Daily Thrive $4,99) | Meraki.planners, Mundo Digital CLP 3.500; outro agente: "agendas 2027 para vender" 107 | **chegando** (demanda paga fraca nos dois) |
| 9 | Devocional/diário de oração digital | Alabaster (físico), Emily Carter "365 prayers", St. Jonathan | El Club de Los E-books (8 anúncios, ebook) | **chegando** (formato ebook já existe em ES) |
| 10 | Templates Notion | fraco (Digihub INR, GCC Market) | não rodado | **não verificado** (demanda paga fraca nos EUA) |
| 11 | Jogos de festa imprimíveis / caça ao tesouro | **sem evidência no Meta** (G15 = 12, G16 = 2): canal Etsy/Pinterest orgânico | outro agente: "juegos para baby shower" 451 de ruído, nenhum kit | **não verificado** |

Observação de modelo: **The Knowhow Co.** mostra que nos EUA há operadores com uma "fábrica" de downloads de nicho (renda de bilro, precificação para autônomos, jogos de festa, Natal) rodando cerca de 150 anúncios em rotação diária. É o equivalente americano dos "packs" BR. Não é uma ideia isolada.

## 4. Suspeitas de eliminatórias (só sinalizadas)

- #1 Planilha: E2 baixa (vende controle e economia, não renda). Mas o nicho do usuário é "renda extra", e isso é adjacente. Se virar "kit de planilhas para revender", entra em E2/E4 (MRR/PLR).
- #2 Livro com IA: E3 moderada (custo de geração de imagem por livro, estimativa de centavos a ~US$1; não verificado). E5 moderada (manter o personagem consistente entre páginas).
- #3 Estate kit: E5 baixa. Risco jurídico se prometer valor legal (testamento). Varia por país; não verificado.
- #4 Casamento: nenhuma. Sazonalidade leve.
- #5 Pet com IA: E3 baixa (custo de API por imagem; estimativa: centavos). Risco de qualidade da IA.
- #6 Estrela: risco de política e engano se o anúncio sugerir "registro oficial" (Meta: práticas enganosas). Precisa deixar claro que é simbólico.
- #7 Romance personalizado: E3 baixa (texto por IA). E5 moderada (qualidade de texto longo). Risco de conteúdo adulto se for "romance".
- #9 Oração: vira ebook (fora do DNA ferramenta/kit).
- #11 Jogos: nenhuma, mas sem prova de demanda paga.

## 5. Falhas

- WebSearch: cota da sessão esgotada (200/200). As 4 buscas planejadas não rodaram, então não há evidência de Etsy/eRank/Everbee/Gumroad/TikTok. **Todas as afirmações "EUA" desta fonte são proxy da Meta Ad Library em US.**
- WebFetch/curl: não tentados (bloqueados, segundo a instrução).
- Buscas ruidosas sem utilidade: G3, G4, G5, G10, G11, G17, G18, G21, G22, G26.
- Sazonais (Papai Noel, elf, calendário do Advento) não medíveis agora (setembro): **não verificado**.
- A Tell My Tale roda em espanhol, mas com 0 anúncios entregues em MX/CO/AR/CL/PE. Não foi possível ver para onde vai (a ferramenta não retorna alcance por país).
- Preços dos EUA só onde aparecem no título (UBP $9; Daily Thrive $4,99). O resto: não verificado.
