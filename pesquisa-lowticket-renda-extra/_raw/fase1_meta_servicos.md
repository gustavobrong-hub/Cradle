# Fase 1 — Meta Ad Library (ES) — território "serviços digitais montados com ferramenta e revendidos" + produtos personalizados prontos

Data da coleta: 2026-09-22. Referência "agora" = epoch 1790095977. Dias ativo = (1790095977 - ad_delivery_start_time)/86400.
Todas as buscas: `ad_active_status=ACTIVE`, `limit=50`, países = MX, CO, AR, CL, PE, EC, GT, BO, UY, DO, US (salvo indicação).
A ferramenta NÃO retorna corpo do anúncio nem alcance → relevância julgada por page_name + link_title + currency (conservador; quando incerto está marcado).
`estimated_total_count` é da Meta e é PROXY (a busca é por palavras soltas, não frase exata → termos genéricos inflam a contagem com ruído).
Nenhum faturamento/ROAS foi inferido. "não verificado" = não conseguimos checar.

---

## 1. Resumo das ideias (proxy de demanda)

| # | Ideia (PT-BR) | Proxy principal | Anunciante mais longo | Preço observado | Eliminatória suspeita |
|---|---|---|---|---|---|
| 1 | Editor de convite web interativo (RSVP, contagem, mapa, música) — usar ou revender convites | "invitación interactiva" est 200 (~25 anunciantes nos 50 mais novos); "invitación web" est 654 | Tarjetas Interactivas 10 ativos / 126.5d; Miboda.love 16 ativos / 108.9d | B2C US$5 (Jose Jwtm), Bs 50≈US$7, $99 MXN≈US$5, S/95.90–125.90; kits Hotmart US$5–14.99 | E2 se só ângulo "negocio"; E5 baixo |
| 2 | Mega pack de convites editáveis (Canva) "listos para vender" | "vender invitaciones digitales" est 88 (≥10 anunciantes de kit); ≥12 produtos Hotmart | Kit Digital 17 ativos / 118.8d; Genios Online/Morador 77d; Mega Plantillas 10 / 49.5d | US$6 (rede "6U$D"), CLP 3.500≈US$3.7, US$5–10 (pay.hotmart) | E2 forte; E4 leve (packs de revenda); comoditizado |
| 3 | Pack de vídeo-convites animados prontos p/ editar e vender | "video invitación" est 1.955 (ruidoso); 2 packs Hotmart | Web Online 21.4d (curso + "+1200 invitaciones") | B2C $350 MXN≈US$19 (Den y Lastra); kit não verificado | E2; risco IP (personagens) |
| 4 | Canção personalizada com IA (form → música em minutos) | "canción personalizada" est 4.235; Diego Hernandez ~151 ativos; Alimenta tu Vida ~157 ativos | Cántale MX ~18 ativos / 101d | MX$279≈US$15 (My Forever Songs); faixa US$20–39 | E3 (API por música; muitos via WhatsApp); E5 médio |
| 5 | Conto infantil personalizado com IA (PDF/vídeo, criança protagonista) | "cuento personalizado" est 1.339 (ruidoso); Mi Cuento 25 ativos | Mi Cuento Infantil Personalizado 43.3d | 3,99€ PDF (cuentoconlaia); Mi Cuento não verificado | E3 leve; IP (Toy Story/K-POP) |
| 6 | Sessão de fotos com IA (aniversário/formatura a partir de selfies) | "sesión de fotos con IA" est 424; ~12 anunciantes (maioria BR em ES) | Luciana Duarte 9.8d (resto 0–2d) | AI Selfi 40 fotos US$29 | E3 (WhatsApp/manual); Gemini grátis substitui |
| 7 | Página-presente digital (espaço do Mimo em ES) | Meta: não isolado (buscas só ruído); ≥4 concorrentes web ES | não verificado | iloveyou.gift "desde $5" | nenhuma (é o case) |
| 8 | Kit menu digital QR p/ vender a restaurantes | "menú digital QR" est 169 (~12 anunciantes, B2B/SaaS) | não medido | "Menú digital desde $6,99" (LX Diseño Web) | E2; E3 (suporte B2B) |
| 9 | Arte IA p/ quadros ("30 imágenes para cuadros") pronta p/ imprimir | 1 anunciante, longevidade extrema | Neurartica 8 ativos / ~991–997d | $29 MXN≈US$1.6; "desde $99" MXN≈US$5 | E2 se ângulo revenda; sobrepõe imprimíveis |
| 10 | Desenho/retrato a partir de foto (pessoa/pet) | "retrato de tu mascota" est 177 (maioria físico); "caricatura personalizada" est 44 | Tu Caricatura 18.9d | US$10 (El arte del dibujo); $650 MXN pet (físico) | E3 se desenho humano |
| 11 | CV/currículum pronto (template + gerador IA) | "plantillas de currículum" est 26 (fraco) | CV perfecto ~101d (2 ads) | ARS 10.000 packs (serviço) | E3 se manual; demanda fraca |
| 12 | Cartão digital (fidelidade / visita) p/ pequenos negócios — ferramenta p/ revender | Educacion nexus testando "Crea tarjetas digitales de fidelización..." | Educacion nexus 24 ativos / 62d (página multi-oferta) | não verificado | E2; E3 |

---

## 2. Queries rodadas (Meta Ad Library, ES, ACTIVE, 11 países)

| Q | termo | estimated_total_count | nota |
|---|---|---|---|
| Q1 | invitaciones digitales | 1.286 | B2C local + 3 kits |
| Q2 | invitación digital | 1.592 | ruído alto |
| Q3 | video invitación | 1.955 | ruído alto |
| Q4 | vender invitaciones digitales | 88 | melhor sinal de kit de revenda |
| Q5 | invitación web | 654 | B2C invitação web c/ RSVP |
| Q6 | regalo digital | 7.556 | ruído; achados: canção, desenho US$10 |
| Q7 | página personalizada para tu pareja | 129 | ruído (videntes) |
| Q8 | página de amor | 3.835 | ruído total |
| Q9 | cuento personalizado | 1.339 | ruído; Mi Cuento |
| Q10 | canción personalizada | 4.235 | sinal forte B2C |
| Q11 | video de Santa Claus personalizado | 1 | fora de temporada |
| Q12 | mensaje de Santa Claus | 24 | ruído; achado Neurartica |
| Q13 | menú digital QR | 169 | B2B SaaS |
| Q14 | catálogo digital WhatsApp | 2.893 | ruído |
| Q15 | plantillas de currículum | 26 | fraco |
| Q16 | fotos con inteligencia artificial | 1.712 | ruído; ensaios IA BR |
| Q17 | sesión de fotos con IA | 424 | ~12 anunciantes |
| Q18 | vende desde tu celular | 1.288 | ruído (coaches) |
| Q19 | canciones con IA | 205 | B2C + cursos |
| Q20 | sorpresa digital | 998 | ruído |
| Q21 | caricatura personalizada | 44 | maioria físico |
| Q22 | crea tu invitación | 734 | ruído (dramas) |
| Q23 | sorprende a tu pareja | 83.227 | ruído total |
| Q24 | invitación interactiva | 200 | ~25 anunciantes, low ticket |
| Q25 | tarjeta digital de cumpleaños | 66 | Tarjetas Interactivas 126d |
| Q26 | invitaciones interactivas para vender | 18 | kits/cursos 49–77d |
| Q27 | video personalizado cumpleaños | 184 | ruído; vídeo-convite $350 MXN |
| Q28 | Cancióname (marca) | 14 | 32.8d |
| Q29 | Cántale canción (marca) | 42 | Cántale MX 101d |
| Q30 | retrato de tu mascota | 177 | maioria físico |
| Q31 | negocio digital desde tu celular | 1.406 | ruído (MLM/coaches) |

Consultas por page_ids (medição de variações/longevidade): 1154408571089804, 1387388674447383, 1105601812626238, 1104144052790356, 1286388787896891, 1344499118746066, 834469756417930, [977127798806735+880660968473155+1059405740583332+721005884426009], 977127798806735, 721005884426009, 545586678647486, 884289721444858, 111838966897600, [1066875966514393+1171913759344035+1182482924959305+910548272142445], 166953813165193, [1201543313041313+109307358787674+1319212884610126], 896661073520377, [1173011945891969+433531919848589+303780449964646], [1347870235072690+553991364473786+523034281110309+1287127391155612], 1138492386003949, [103961612783471+103001559484790+1250088564854288+1223217640878201].

WebSearch: `site:hotmart.com invitaciones digitales para vender pack editables`; `site:hotmart.com canciones personalizadas con inteligencia artificial vender`; `site:hotmart.com sesiones de fotos con IA ensayos para vender prompts`; `"invitaciones digitales" pack para vender Hotmart precio USD "listas para vender" video`; `página web personalizada para tu pareja regalo digital con fotos y mensaje sorpresa precio`; `cuento infantil personalizado digital PDF ... "Mi Cuento Infantil Personalizado"`; `"Emprende con invitaciones digitales" curso precio`; `site:pay.hotmart.com invitaciones digitales`; `canción personalizada con IA regalo precio dólares ...`; `cuento personalizado con IA para niños digital precio "en minutos" ...`; `sesión de fotos con IA precio "ensayo" cumpleaños ...`; `site:hotmart.com menú digital QR para vender a restaurantes plantillas kit`.

---

## 3. Tabela consolidada — anunciantes medidos por page_id

| Anunciante | page_id | moeda | ativos | mais antigo (dias) | títulos / nota | snapshot |
|---|---|---|---|---|---|---|
| Tarjetas Interactivas | 553991364473786 | ARS | 10 | 126.5 | sem link_title (convite/cartão interativo) | https://www.facebook.com/ads/library/?id=1290146059969674 |
| Kit Digital | 433531919848589 | CLP | 17 | 118.8 | "Solo a $3500💜", "Obtén el tuyo ahora💜", "Revisa nuestro material exclusivo" (apareceu em "vender invitaciones digitales") | https://www.facebook.com/ads/library/?id=1376630554316244 |
| Miboda.love – Invitaciones Inteligentes | 303780449964646 | MXN | 16 | 108.9 | "Control total de tus invitados ✨", "La invitación perfecta para sus XV ✨" | https://www.facebook.com/ads/library/?id=847134201787134 |
| Cántale MX Canciones personalizadas | 977156042151735 | MXN | ~18 nos 50 (busca Q29) | 101.0 | "Su historia hecha canción", "El regalo que hará llorar a mamá ❤️" | https://www.facebook.com/ads/library/?id=1309304448042711 |
| CV perfecto | 711178682079280 | PEN | 2 | 101.3 | sem título | https://www.facebook.com/ads/library/?id=1731701878026959 |
| Neurartica | 109307358787674 | MXN | 8 | ~991–997 | "Crea tu imagen desde $99", "30 imágenes para cuadros por $29" (longevidade extrema, possível gasto baixo) | https://www.facebook.com/ads/library/?id=584841497159973 |
| Genios Online | 103961612783471 | COP | 4 (loja multi-oferta) | 77.2 (convites) | "EMPRENDE CON INVITACIONES DIGITALES" | https://www.facebook.com/ads/library/?id=2004948203720677 |
| Morador marketer | 103001559484790 | COP | ~14 (loja multi-oferta) | 77.3 (convites) | "CURSO EMPRENDE CON INVITACIONES DIGITALES" (3 ads) — mesmo dono de Genios Online | https://www.facebook.com/ads/library/?id=1529789795491834 |
| Educacion nexus | 1138492386003949 | COP | 24 | 61.9 | multi-oferta: "Invitaciones Interactivas que Sorprenden 🎉" (59.9d), "🎶 Tu Canción 100% Personalizada..." (57.2d), "Crea tarjetas digitales de fidelización..." | https://www.facebook.com/ads/library/?id=1015627584605774 |
| Mega Plantillas Digitales | 1154408571089804 | USD | 10 | 49.5 | "Mira como funciona📱", "Ver invitaciones digitales ✨" | https://www.facebook.com/ads/library/?id=1708910720392963 |
| Mi Cuento Infantil Personalizado | 166953813165193 | MXN | 25 | 43.3 | Toy Story 5, superhéroe, princesa, "Guerrera K-POP", "Quiero mi Video Personalizado" | https://www.facebook.com/ads/library/?id=1756985529330960 |
| Canciónname.com | 1120025564535589 | CLP | 14 | 32.8 | "Canciones Personalizadas IA", "Canción + Video Personalizado para Regalar 🎬" | https://www.facebook.com/ads/library/?id=927896453075887 |
| Web Online | 1105601812626238 | PEN | 8 | 21.4 | "CURSO PASO A PASO +1200 INVITACIONES listas para VENDERr✨🎉" | https://www.facebook.com/ads/library/?id=2313998366006369 |
| Tu Caricatura | 1018451794916049 | COP | 2 (na busca) | 18.9 | sem título | https://www.facebook.com/ads/library/?id=2202083827390612 |
| TarjetaViva | 1217892654751932 | PEN | 1 (na busca) | 15.1 | "Invitaciones digitales interactivas — Desde S/ 100" | https://www.facebook.com/ads/library/?id=2669722426776063 |
| Invictationes Digitales | 1250088564854288 | BRL | 3 | 13.5 | "💸 Emprende desde casa vendiendo invitaciones digitales" (BR vendendo em ES) | https://www.facebook.com/ads/library/?id=1591072372564444 |
| Alimenta tu Vida | 721005884426009 | COP | est 157 (50+ limite) | ≥13.2 (limite inferior) | "¡¡Recibe tu canción primero y paga despues!! 🎵🤍" | https://www.facebook.com/ads/library/?id=1102133392160134 |
| Limasystem | 896661073520377 | PEN | 10 | 10.4 | "Invitación web + sistema RSVP desde S/125.90", "Tu invitación de boda desde S/ 95.90" | https://www.facebook.com/ads/library/?id=1066163912961541 |
| Luciana Duarte | 884289721444858 | BRL | 7 | 9.8 (ES: 0.4) | "Tu cumpleaños merece fotos increíbles ✨" | https://www.facebook.com/ads/library/?id=2324262644777918 |
| Invitaciones | 1223217640878201 | PEN | 2 | 9.0 | "Empieza tu negocio digital 💻" | https://www.facebook.com/ads/library/?id=992844500497103 |
| Diego Hernandez | 977127798806735 | USD | est 151 (50+ limite) | ≥7.4 (limite inferior) | "Una canción para recordarlos.", "Dales un regalo que nunca dejarán de reproducir." | https://www.facebook.com/ads/library/?id=2199447094246646 |
| Impulsodigital360 | 1344499118746066 | USD | 10 | 4.5 | "Ultimos cupos a 6U$D" | https://www.facebook.com/ads/library/?id=1390677909271457 |
| Creativa Pack Studio | 1173011945891969 | USD | 1 | 4.4 | "Invitaciones premium listas para vender 💍" | https://www.facebook.com/ads/library/?id=1450835596895541 |
| Music Creator Pro | 1171913759344035 | USD | ~45+ | ~4.5 | "🏆 Crea música con IA desde cero" (curso → E1) | https://www.facebook.com/ads/library/?id=929866986846204 |
| Laprofesióndelfuturo | 1286388787896891 | USD | 8 | 3.6 | "Accede al MEGAPACK mas completo por solo 6U$D" | https://www.facebook.com/ads/library/?id=1053810084318032 |
| Asesoría digital | 1104144052790356 | USD | 4 | 3.0 | "SOLO POR 6U$D" | https://www.facebook.com/ads/library/?id=2433925800352136 |
| DedicatieMuzicala | 834469756417930 | USD | 34 | 2.4 | canções personalizadas, títulos multilíngues (EN/AF/SQ/VI...) | https://www.facebook.com/ads/library/?id=1820082555679408 |
| Eugenia Silva | 111838966897600 | BRL | 10 | 2.0 | "🚨 ¡ÚLTIMOS 6 LUGARES DISPONIBLES!" (relevância incerta) | https://www.facebook.com/ads/library/?id=1560213738575632 |
| Yuyay Invitaciones | 523034281110309 | USD | 5 | 1.7 | convites interativos | https://www.facebook.com/ads/library/?id=1600169768573635 |
| Craedis | 1287127391155612 | USD | 1 | 1.6 | "Más de 1000 clientes satisfechos" | https://www.facebook.com/ads/library/?id=1377867674327543 |
| Jose Jwtm | 1347870235072690 | USD | 1 | 0.9 | "Invitaciones digitales para boda, quince, baby shower y cumpleaños - desde $5" | https://www.facebook.com/ads/library/?id=2258326214989459 |
| Invita Kairós | 1201543313041313 | MXN | 1 | 0.8 | "Tu invitación web por solo $99" | https://www.facebook.com/ads/library/?id=1593301982261896 |
| Canva para novias | 1387388674447383 | USD | 6 | 0.3 | "Papelería para casamiento lista en Canva | Invitación, menús y carteles" | https://www.facebook.com/ads/library/?id=1090593597009231 |
| Aurelia Studio | 545586678647486 | BRL | 9 | 0.1 | "Envíame un mensaje por WhatsApp. 🟢" (ensaio IA) | https://www.facebook.com/ads/library/?id=1097273206598018 |
| El arte del dibujo | 1319212884610126 | COP | 4 | 0.0 | "Convierte tus ideas en dibujos reales por solo $10 USD! 🎨" | https://www.facebook.com/ads/library/?id=1113283544981176 |

Observação: a rede "6U$D" (Asesoría digital, Digitalizaciónonline, Laprofesióndelfuturo, Impulsodigital360, + Formación Online) usa páginas novas (3–4.5d) com o mesmo padrão de título → parece um mesmo operador rotacionando páginas (ou afiliados); o produto exato não foi verificado (apareceu na busca "vender invitaciones digitales").

---

## 4. Log bruto por query

### Q1 "invitaciones digitales" -> est 1286
B2C local (serviço feito à mão por designer, WhatsApp): Yuriie Creations (104363902449374 MXN), Calixta Card (610766325453656 ARS "Invitaciones web para tus 15 años"), DAC Creations (1343647725487845 MXN), Personalízate (122481298351699 COP, 2), Pearl Atelier (1147648131763615 MXN), Miboda.love (303780449964646 MXN "Invitaciones Inteligentes para Bodas"), Subligraf (219315037923434 CLP, 2; + 106979068879691), Limasystem (896661073520377 PEN "Tu invitación de boda desde S/ 95.90"), Invi Digi (1029623536892040 MXN, 3), Corazón de Fiesta (954937514371674 MXN, 7 "Envíame Whats"), InvitaKids (108046048951319 MXN), Auras Estrategicas (1022956784229868 MXN "Invitaciones digitales desde $499 MXN"), StudioTres (1184038471458136 ARS), Clemix Boda (1112888928568332 CLP), Momento Bonito (311480782057266 MXN), LUNI Estudio, Nanette Inzunza design.
Kits p/ revender: Mega Plantillas Digitales (1154408571089804 USD "Mira como funciona📱", 3 nos 50), Ana Rosa (1224017970804067 BRL "Haz clic y descubre todo lo que incluye el kit."), Bruno Lero (839455215916257 BRL "Pack +200 Plantillas Editables ¡Acceso De Por Vida!").
Snapshots: https://www.facebook.com/ads/library/?id=2205298640865792 (Mega Plantillas) ; https://www.facebook.com/ads/library/?id=1871601350828706 (Calixta) ; https://www.facebook.com/ads/library/?id=28398285386504838 (Limasystem) ; https://www.facebook.com/ads/library/?id=1624182579230484 (Miboda.love) ; https://www.facebook.com/ads/library/?id=933352599458140 (Bruno Lero) ; https://www.facebook.com/ads/library/?id=1432927325454053 (Ana Rosa) ; https://www.facebook.com/ads/library/?id=1625294865810114 (Auras $499MXN)

### Q2 "invitación digital" -> est 1592
Muito ruído (coaches, dramas, salões). Relevante: Canva para novias (1387388674447383 USD, 5 ads nos 50, link title "Worker threw exception | canva-para-novias.impultienda.ar"), Invidi Digital (101744042671003 MXN), RD Diseño Creativo (204525276083646 MXN).

### Q3 "video invitación" -> est 1955
Ruído alto (fotógrafos, dramas curtos, DavidVas Academy). Pouco sinal de produto. Relevante: Yuriie Creations, Marketing Digital-Diseño y Arte - MM (169397756266680 PEN, 3), Yuju Creaciones (193102913890981 PEN).

### Q4 "vender invitaciones digitales" -> est 88  (MELHOR SINAL DE KIT DE REVENDA)
- Mega Plantillas Digitales (1154408571089804) USD "Mira como funciona📱"
- Web Online (1105601812626238) PEN "CURSO PASO A PASO +1200 INVITACIONES listas para VENDERr✨🎉" (4 nos 50)
- Kit Digital (433531919848589) CLP "Solo a $3500💜" (~US$3.7)
- Papelería Creativa - Kit Completo de Plantillas Editables en Canva (1296601010204782) BRL
- Asesoría digital (1104144052790356) USD "SOLO POR 6U$D" (4)
- Digitalizaciónonline (1294794033723838) USD "Ultimos cupos por 6U$D" (4)
- Laprofesióndelfuturo (1286388787896891) USD "Accede al MEGAPACK mas completo por solo 6U$D" (7)
- Impulsodigital360 (1344499118746066) USD "Ultimos cupos a 6U$D" (9)
- Formación Online (1054578807745528) USD "🔴Oferta solo por hoy" (2)
- Creativa Pack Studio (1173011945891969) USD "Invitaciones premium listas para vender 💍"
- Inteligencia artificial para docentes (406307182556070) USD "👉 Descubre el megapack." (9) [relevância incerta]
- EICAP (BOB) [escola]
Snapshots: https://www.facebook.com/ads/library/?id=28352880997740216 (Web Online) ; https://www.facebook.com/ads/library/?id=2433925800352136 (Asesoría 6U$D) ; https://www.facebook.com/ads/library/?id=3512065995633532 (Digitalizaciónonline) ; https://www.facebook.com/ads/library/?id=1053810084318032 (Laprofesión) ; https://www.facebook.com/ads/library/?id=1390677909271457 (Impulsodigital360) ; https://www.facebook.com/ads/library/?id=1450835596895541 (Creativa Pack Studio) ; https://www.facebook.com/ads/library/?id=975658698913214 (Kit Digital CLP)

### Q5 "invitación web" -> est 654
B2C invitação web c/ RSVP: Limasystem (896661073520377 PEN, 6+ nos 50: "Invitación web + sistema RSVP desde S/125.90", "Tu boda organizada en un solo enlace"), Invita Kairós (1201543313041313 MXN "Tu invitación web por solo $99"), Calixta Card (ARS), DLC.Invitaciones (110701228624767 ARS, 3), Atentamente Invitaciones (102626109245858 ARS, 2), She Said Web (1423649351056105 MXN), Invitaciones Digitales My Invite (104026075741755 MXN "confirmación de asistencia automática", 2), vivaboda (1331242963395871 COP), Arte Invita (567783516426441 MXN "Aparta con solo $199 pesos"), Miboda.love.
Snapshots: https://www.facebook.com/ads/library/?id=1066163912961541 (Limasystem RSVP) ; https://www.facebook.com/ads/library/?id=1593301982261896 (Invita Kairós $99) ; https://www.facebook.com/ads/library/?id=28833401089682471 (My Invite) ; https://www.facebook.com/ads/library/?id=1831108181577789 (She Said Web)

### Q6 "regalo digital" -> est 7556
Termo amplo, muito ruído (Temu, cursos IA, "Alivio en casa" 25+ ads "RECIBELO GRATIS HOY"). Relevantes: Mejor Digital (1059405740583332 COP "🎵 ¡REGALA UNA CANCIÓN PERSONALIZADA! 💖" 4), El arte del dibujo (1319212884610126 COP "Convierte tus ideas en dibujos reales por solo $10 USD! 🎨"), Inu studio (1314966641691125 USD "Elegí, imprimí, vendé" 3), aura_kitpdf (115325934952703 CLP).
Snapshots: https://www.facebook.com/ads/library/?id=1652343506902718 (Mejor Digital canción) ; https://www.facebook.com/ads/library/?id=1113283544981176 (El arte del dibujo $10)

### Q7 "página personalizada para tu pareja" -> est 129
Ruído (amarres/videntes "Armonía de Amor" 20+ ads; cursos). Nenhuma "página de amor" estilo Mimo visível nos 50 mais novos. Relevante: Alimenta tu Vida (canción).

### Q8 "página de amor" -> est 3835
Ruído total (Temu, lojas, videntes). Nenhum concorrente direto do Mimo visível nos 50 mais novos (NÃO conclusivo: busca por palavra solta).

### Q9 "cuento personalizado" -> est 1339
Muito ruído. Relevantes: Mi Cuento Infantil Personalizado (166953813165193 MXN, 3 nos 50: "¡No solo veas Toy Story 5... Haz que tu pequeño sea parte de la película!", "¡Tu hijo no verá a los superhéroes... Él será uno de ellos!"), Cuéntame - Cuentos Personalizados (639997205870953 PEN "PACK PERSONALIZADO S/220" - físico), Persandolo (823419404479754 COP "Un libro para soñar").
Snapshots: https://www.facebook.com/ads/library/?id=1105655501880438 (Mi Cuento Toy Story) ; https://www.facebook.com/ads/library/?id=1783143969573884 (Cuéntame S/220)

### Q10 "canción personalizada" -> est 4235  (SINAL FORTE B2C)
(resultado >limite de tokens, salvo em arquivo e resumido por script)
Páginas nos 50 mais novos: Ana Alice (1275562858967632 BRL "¡PIDE LA TUYA AHORA MISMO! 👉" 3), Arqe Media MID (MXN), Mejor Digital (COP 4), Tinos Records (880660968473155 COP "Obtén tu canción personalizada ahora! 👉" 5), AudioMarca Estudio (633560476510616 ARS "Video personalizado desde $15.000"), CorridosRoman (562676893606308 MXN), UrbanBeat (1196312973565295 COP "⭐⭐⭐⭐⭐" 2), DedicatieMuzicala (834469756417930 USD, 20 nos 50, títulos multilíngues "A Song With Her Name ❤️ | Một bài hát có tên nàng..."), Suri.joyas (MXN, ruído), Animás (USD), Diego Hernandez (977127798806735 USD "Una canción para recordarlos." 8).
Snapshots: https://www.facebook.com/ads/library/?id=1559532402129216 (Diego Hernandez) ; https://www.facebook.com/ads/library/?id=1112639781340643 (Tinos) ; https://www.facebook.com/ads/library/?id=1820082555679408 (DedicatieMuzicala) ; https://www.facebook.com/ads/library/?id=2151202165754635 (Alimenta tu Vida) ; https://www.facebook.com/ads/library/?id=3674131392734876 (Ana Alice)
Page checks:
- DedicatieMuzicala 834469756417930: 34 ativos; mais antigo 2.4d (rotaciona criativos; multilíngue).
- Diego Hernandez 977127798806735: est 151 ativos (50+ limite); mais antigo visto 7.4d (limite inferior).
- Alimenta tu Vida 721005884426009: est 157 ativos (50+ limite); mais antigo visto 13.2d (limite inferior); títulos "¡¡Recibe tu canción primero y paga despues!!" / "¡¡Primero recibe y luego pagas!!" (modelo paga-depois ⇒ atendimento WhatsApp).
- Consulta combinada Mejor Digital + Tinos + Diego + Alimenta: est 331 ativos no total.

### Q11 "video de Santa Claus personalizado" -> est 1
El Mundo del Tío May (511813145354747 GTQ, ~33d, sem título — relevância incerta). Fora de temporada (setembro); sem sinal.

### Q12 "mensaje de Santa Claus" -> est 24
Ruído (viagens, decoração). Achados laterais: Neurartica (109307358787674 MXN "Crea tu imagen desde $99", anúncios ativos desde ~jan/2024) https://www.facebook.com/ads/library/?id=899915708069358 ; Santaclausysusamigos (182276768299155 MXN "Santa Navidad", start 1783826094 = 72.6d) https://www.facebook.com/ads/library/?id=1319807633199709

### Q13 "menú digital QR" -> est 169
B2B SaaS/serviço: Tumenu.promo (1016465034887412 BRL "Tu menú QR, gratis" 3), Nedify (624716884837194 ARS 3), LX Diseño Web (969088226295681 USD "Menú digital desde $6,99"), Platillo (1267843499749210 MXN "Recibe Pedidos A Tu Menú Digital Ahora"), Imagine & Stamp (638565032669305 MXN "Menú Digital QR • Pedidos a tu WhatsApp"), Sisas Studio (706679589205478 MXN), Meny Mat (1183835301470992 COP "Tu menú digital en menos de 15 minutos👉"), Foodiq (PEN), Menu Digital Mac (MXN), Menú Animado (ARS), UrbanDisplay (MXN "$1,500 Único pago"), Loggro/CostoChef (SaaS).
Snapshots: https://www.facebook.com/ads/library/?id=2161817697787903 (LX $6,99) ; https://www.facebook.com/ads/library/?id=1834916980858375 (Tumenu) ; https://www.facebook.com/ads/library/?id=1467921485204409 (Meny Mat)

### Q14 "catálogo digital WhatsApp" -> est 2893
Ruído altíssimo. Laterais: Herramientas DM (112070511501562 USD 4), Estilo Store (106898044882020 USD "GENERA INGRESOS DESDE CASA 💸✨"), Mundo Digital 2.0 (1252845801237648 CLP "$3.500 SOLO POR HOY !!" 3), Bonito Digital (1253683197834637 MXN 5), Descarga con nosotros (1072165559323244 PEN "Mega Pack Hot Wheels"), Mercado digital (569054419627923 MXN "Super oferta $50 pesos"), Silvia (1346528465216765 COP "Atiende y vende por WhatsApp 24/7").

### Q15 "plantillas de currículum" -> est 26 (demanda fraca no Meta ES)
Tu.CurriculumYa (687171827803315 ARS "💼 Servicio Pago de CV (Packs desde $10.000)"), CV perfecto (711178682079280 PEN, anúncio desde 1781339762 = 101.3d, 2 ads), Jc mdp (ARS "Armado de Curriculum Vitae"), Enhancv (SaaS USD), Chambas AI (MXN), Academia Crecer (ARS "📄 Tu experiencia merece ser vista" 2).
Snapshots: https://www.facebook.com/ads/library/?id=1731701878026959 (CV perfecto ~101d) ; https://www.facebook.com/ads/library/?id=1547192227425638 (Tu.CurriculumYa)

### Q16 "fotos con inteligencia artificial" -> est 1712
Ruído. Relevantes: Js Ensaios (1143514792176101 BRL "⭐⭐⭐⭐⭐ + De 8.000 clientes satisfechos" 3), Juan Carlos Ia (1245549441974059 BRL "⚡ Entrega rápida"), Carla Rodrigues (1088777660993815 BRL "🟢En línea" 2), Aurelia Studio, APOB AI (USD app).

### Q17 "sesión de fotos con IA" -> est 424  (onda BR "ensaio com IA" exportada p/ LATAM em ES)
Páginas (50 mais novos): Aura IA Studio (186078587924004 BRL "Sesión completa en minutos" 2), Aurelia Studio (545586678647486 BRL "Envíame un mensaje por WhatsApp 🟢" 6), Ensaio IA Premium (1047092538485241 BRL "¡Escríbenos por WhatsApp!"), Hailuo AI Create (946004491918278 USD "Convierte tu foto en la tendencia del momento" 2), Carla Rodrigues, Juan Carlos Ia, Manuel Fernandez (274674485731337 USD "Un mes de contenido, sin fotos"), Milena • Ensaios com IA (1027467803783017 BRL "CONTÁCTANOS AHORA | HAZ TU SESIÓN" 3), Watson Estudio de diseño IA (1314888108377463 MXN "Tu selfie, en cualquier lugar del mundo"), Luciana Duarte (884289721444858 BRL "Tu cumpleaños merece fotos increíbles ✨" 6), Yasmim & Hiago Ensaios IA (907515899119155 BRL "¡HAZ TU SESIÓN DE FOTOS 👉" 2), Alana Estudio de IA (1114513805075665 PEN "Convierte su logro en un recuerdo eterno" 4 — formatura), Eugenia Silva (111838966897600 BRL "🚨 ¡ÚLTIMOS 6 LUGARES DISPONIBLES!" 6 — relevância incerta), Gabriel Marketing IA (951019321421660 BRL "¡Quiero crear mi sesión de cumpleaños!" 3), Blend App (INR).
=> ~12 anunciantes distintos, quase todos BR vendendo em ES via WhatsApp (atendimento humano). Todas as páginas novas (0.1–2d, Luciana 9.8d) → sem longevidade comprovada.
Snapshots: https://www.facebook.com/ads/library/?id=2336463247095806 (Aura IA) ; https://www.facebook.com/ads/library/?id=1097273206598018 (Aurelia) ; https://www.facebook.com/ads/library/?id=2324262644777918 (Luciana cumpleaños) ; https://www.facebook.com/ads/library/?id=2940019016330392 (Alana graduación) ; https://www.facebook.com/ads/library/?id=1421132206826187 (Milena) ; https://www.facebook.com/ads/library/?id=1579086490354447 (Yasmim & Hiago) ; https://www.facebook.com/ads/library/?id=1769849117397518 (Watson selfie)
Page checks: Aurelia Studio 9 ativos / 0.1d ; Luciana Duarte 7 ativos / 9.8d (1 ad PT antigo "Apresentações Profissionais"; ES = 0.4d) ; Eugenia Silva 10 ativos / 2.0d.

### Q18 "vende desde tu celular" -> est 1288
Ruído: cursos/coaches ("CORAL Mujaes M" "Conquista Tu Primer Million"), dramas, "Emprende con Fran" (evento), "Solucion digital" "🎁Llévate 5 bonos gratuitos" (8 ads), "Saber Mas"/"Universo Digital" "Recibelo En Tu Celular ahora y paga después" (COP), "Recetas desde Casa" "¡Primero recibís y después pagas!", Taidy Hernandez "✂️ 45 Patrones Digitales por $3.000 CLP". Sem produto-ferramenta claro no território.

### Q19 "canciones con IA" -> est 205
Musica con IA (910548272142445 COP "¡Convierte tu historia en una canción!" 2, ~2.4d), Suenabacan.cl (1103116539556076 CLP "Canciones Personalizadas IA" 2), Concancion.com (1216838598180058 PEN "Chatea con nosotros"), Sebastián Soria (1182482924959305 BOB "CANCIONES CON IA"), Mundo Digital IA / Negocios Online (1066875966514393 USD 5 "🎵 ¡Dale play y disfruta la música!"), Music Creator Pro (1171913759344035 USD "🏆 Crea música con IA desde cero" ~45+ ads, todos ~3.8–4.5d — curso, E1), Jukebox AI / Tune AI / Popmaker (apps), Ritmo Cordobé (781154615088916 USD "Canciones y videos creados para negocios."), TBM Studio IA (MXN).
Snapshots: https://www.facebook.com/ads/library/?id=1473915324566979 (Musica con IA) ; https://www.facebook.com/ads/library/?id=937167449467955 (Suenabacan) ; https://www.facebook.com/ads/library/?id=929866986846204 (Music Creator Pro)

### Q20 "sorpresa digital" -> est 998
Ruído total. Nada tipo página-surpresa.

### Q21 "caricatura personalizada" -> est 44
Majoritariamente físico. Tu Caricatura (1018451794916049 COP 2 ads, 18.9d).

### Page checks diversos
- Mi Cuento Infantil Personalizado 166953813165193: 25 ativos; mais antigo 43.3d (start 1786352139). Ângulos: Toy Story 5, superhéroe, princesa, "Guerrera K-POP", "Quiero mi Video Personalizado", "El Recuerdo Más Bonito de Su Infancia". Snapshots: https://www.facebook.com/ads/library/?id=1756985529330960 ; https://www.facebook.com/ads/library/?id=1376815594637808 ; https://www.facebook.com/ads/library/?id=1598692711963219
- Neurartica 109307358787674: 8 ativos; ~991–997d (desde jan/2024). "Crea tu imagen desde $99", "30 imágenes para cuadros por $29" MXN — longevidade extrema, possível gasto baixo. https://www.facebook.com/ads/library/?id=584841497159973
- El arte del dibujo 1319212884610126: 4 ativos; 0.0d.
- Invita Kairós 1201543313041313: 1 ativo; 0.8d.
- Music Creator Pro 1171913759344035: ~45+ (consulta combinada est 118); ~3.8–4.5d.
- Limasystem 896661073520377: 10 ativos; mais antigo 10.4d. "Invitación web + sistema RSVP desde S/125.90", "Tu invitación de boda desde S/ 95.90", "Una invitación única para sus 15 años", "Cotiza tu tarjeta web de boda".
- Kit Digital 433531919848589: 17 ativos; mais antigo 118.8d. Miboda.love 303780449964646: 16 ativos; mais antigo 108.9d. Creativa Pack Studio 1173011945891969: 1 ativo; 4.4d. (consulta combinada est 34)

### Q22 "crea tu invitación" -> est 734
Ruído (dramas curtos, Novelas AIES). Relevantes: Pearl Atelier, Canva para novias, Mundos Digitales (1316858754845087 PEN "⭐⭐⭐⭐⭐ 5/5" 3 — kit? não verificado), Lessenza.

### Q23 "sorprende a tu pareja" -> est 83227
Ruído total (apps de namoro, videntes). Inútil.

### Q24 "invitación interactiva" -> est 200  (B2C low ticket + rede de pequenos vendedores)
Páginas: Yuju Creaciones (PEN), Sirio Detalles (PEN), Invi Digi (MXN 3), InvitaKids (MXN), AT Design (USD), Creativa Alex (MXN), Creha. (MXN), Pixel Invitación (106467984432600 MXN "Cotiza tu invitación"), Jose Jwtm (1347870235072690 USD "Invitaciones digitales para boda, quince, baby shower y cumpleaños - desde $5"), Invitae (1347630301758357 USD "¿Querés ver una demo? Hablá con nosotros 📲"), Einvitados (597006526821388 ARS "✨ Tu evento empieza con la invitación"), Karen Studio, Momentos Click, Operación Fiesta MX, Wedly (1078808631978649 MXN), Gosto moments, Craedis (1287127391155612 USD "Más de 1000 clientes satisfechos"), Yuyay Invitaciones (523034281110309 USD 3), Tarjetas Interactivas (553991364473786 ARS 2), Momenta CL (446285881908404 PEN "Invitaciones digitales para bodas 💍"), Rodrigo Pericon (104321374494199 BOB "💌 INVITACIONES DIGITALES INTERACTIVAS DESDE Bs 50 ✨" ≈US$7), Amorea Estudio (995735520282901 AUD "Invitación Web de Boda en Canva 💖"), Ayayita (100599729007565 PEN "Invitación Web Interactiva de Winnie Pooh para tu Baby Shower."), Rocio Ynca (PEN 3), pixigrama (MXN 2).
=> ~25 anunciantes distintos nos 50 mais novos; preços visíveis US$5 (Jose Jwtm), Bs 50 (~US$7), $99 MXN (~US$5, Invita Kairós), S/95.90–125.90 (~US$25–33, Limasystem), $499 MXN (Auras).
Snapshots: https://www.facebook.com/ads/library/?id=2258326214989459 (Jose Jwtm desde $5) ; https://www.facebook.com/ads/library/?id=2277118933136485 (Rodrigo Pericon Bs 50) ; https://www.facebook.com/ads/library/?id=1425801376141613 (Ayayita Winnie Pooh) ; https://www.facebook.com/ads/library/?id=1401428364744114 (Amorea Canva web) ; https://www.facebook.com/ads/library/?id=1377867674327543 (Craedis)

### Q25 "tarjeta digital de cumpleaños" -> est 66
Ruído (fidelização, restaurantes). Relevantes: Tarjetas Interactivas (553991364473786 ARS), TarjetaViva (1217892654751932 PEN "Invitaciones digitales interactivas — Desde S/ 100", 15.1d), Convite.events (1186664371191025 MXN "Pase QR para cada invitado"), Tarjeta de invitacion (112433145132248 COP 2), Educacion nexus (COP "Invitaciones Interactivas que Sorprenden 🎉"), Mitarjeta.mx (1308218612364394 MXN, cartão de visita digital "Tu agenda de citas, en una tarjeta profesional"), GW Loyalty / VAOZ / Vol Loyalty (fidelização B2B).
Page checks: Tarjetas Interactivas 10 ativos / 126.5d ; Jose Jwtm 1 / 0.9d ; Yuyay 5 / 1.7d ; Craedis 1 / 1.6d ; Educacion nexus 24 ativos / 61.9d (página multi-oferta: "Invitaciones Interactivas que Sorprenden 🎉" 59.9d, "🎶 Tu Canción 100% Personalizada para Cualquier Ocasión" 57.2d, "Crea tarjetas digitales de fidelización con recompensas, puntos, cashback y cupones automáticos.", "3 Paneles de IA en 1 (85 Funciones)", "+50 Herramientas IA Para Abogados", "Dale a tu hijo un tutor con IA").
Snapshots: https://www.facebook.com/ads/library/?id=1290146059969674 (Tarjetas Interactivas 126d) ; https://www.facebook.com/ads/library/?id=1015627584605774 (Educacion nexus invit. 60d) ; https://www.facebook.com/ads/library/?id=1355850376629820 (Educacion nexus canción 57d) ; https://www.facebook.com/ads/library/?id=3985839308219013 (Educacion nexus fidelización) ; https://www.facebook.com/ads/library/?id=2669722426776063 (TarjetaViva S/100)

### Q26 "invitaciones interactivas para vender" -> est 18  (KIT/CURSO DE REVENDA COM LONGEVIDADE)
- Mega Plantillas Digitales (USD, 8 ads nos 18, mais antigo 49.5d)
- Formación Online (USD "🔴Oferta solo por hoy" 2)
- EICAP (BOB)
- Invitaciones (1223217640878201 PEN "Empieza tu negocio digital 💻" 2, 9.0d)
- Invictationes Digitales (1250088564854288 BRL "💸 Emprende desde casa vendiendo invitaciones digitales" 3, 13.5d) — BR vendendo em ES
- Genios Online (103961612783471 COP "EMPRENDE CON INVITACIONES DIGITALES", 77.2d)
- Morador marketer (103001559484790 COP "CURSO EMPRENDE CON INVITACIONES DIGITALES", 3 ads, 77.3d) — mesma oferta/mesmo dono de Genios Online (criativos criados no mesmo minuto); ambas vendem também "CURSO EMPRENDE CON TEJIDO", "CURSO ASISTENTE VIRTUAL", "MEGA CURSO CANVA 3 EN 1", "ChatGPT PLUS" (loja de infoprodutos COP).
(consulta combinada Genios+Morador+Invictationes+Invitaciones: est 24)
Snapshots: https://www.facebook.com/ads/library/?id=1529789795491834 (Morador 77d) ; https://www.facebook.com/ads/library/?id=2004948203720677 (Genios 77d) ; https://www.facebook.com/ads/library/?id=1591072372564444 (Invictationes BR) ; https://www.facebook.com/ads/library/?id=992844500497103 (Invitaciones PEN)

### Q27 "video personalizado cumpleaños" -> est 184
Ruído (eventos, Hailuo AI app). Relevantes: Diseños Den y Lastra (410380972164178 MXN "¡HAZ ÚNICA LA INVITACIÓN EN VIDEO DE TU PEQUE! Costo: $350 pesos"), InviVideo CUU (1043010785567740 MXN), Leslie Carolina Invitaciones (MXN).
Snapshot: https://www.facebook.com/ads/library/?id=28668551599495122

### Q28 "Cancióname" -> est 14
Todos da Canciónname.com (1120025564535589 CLP): "Canciones Personalizadas IA", "Canción + Video Personalizado para Regalar 🎬", "Música Personalizada para Regalar 🎵"; mais antigo 32.8d. https://www.facebook.com/ads/library/?id=927896453075887

### Q29 "Cántale canción" -> est 42
Cántale MX Canciones personalizadas (977156042151735 MXN, ~18 ads nos 50, mais antigo 101.0d; títulos "Su historia hecha canción", "El regalo que hará llorar a mamá ❤️", "Haz que escuche cuánto la amas", "Regala Una Canción", "Escucha tu canción hoy 🎧"), Cantale (1262908266910452 ARS "Una canción hecha con tu historia" 9, ~9.8d), TheblessingSong (103478879463997 USD "Este aniversario, cántale su historia", 10.1d).
Snapshots: https://www.facebook.com/ads/library/?id=1309304448042711 (Cántale MX 101d) ; https://www.facebook.com/ads/library/?id=2430569147437021 (Cántale "llorar a mamá") ; https://www.facebook.com/ads/library/?id=1642491524070156 (Cantale ARS)

### Q30 "retrato de tu mascota" -> est 177
~30 anunciantes, maioria produto FÍSICO (lienzo, joias, tattoo, amigurumi). Relevantes: Vincent Van Guauu (886165977924372 MXN "🎨 Retratos de mascotas desde $650"), Peludolandia (102971469440363 COP "Retrato Personalizado 🐶🖼️" 2), HECHO (893505163835163 USD "Pop Pet Portrait 🐶🎨"), Recuerdos en Lienzos (USD), Artella Atelier (MXN "Retrato de Mascotas | $1,350 al mes"), Qairo (PEN 3).
Snapshots: https://www.facebook.com/ads/library/?id=2446503752546737 (Van Guauu) ; https://www.facebook.com/ads/library/?id=1960279147972400 (HECHO)

### Q31 "negocio digital desde tu celular" -> est 1406
Ruído: coaches ("CORAL Mujaes M" "Conquista Tu Primer Million"), MLM Farmasi [E4], "Carlos Cárcamo-Negocios Digitales" "conoce cómo funciona este modelo digital y qué incluye" [suspeita MRR/E4], Mega Plantillas Digitales reaparece, Mundos Digitales (PEN), "Aprende y Emprende desde Casa" (USD 3).

---

## 5. WebSearch (Hotmart e concorrentes)

Kits de convites p/ revender na Hotmart (≥12 produtos; preços da maioria não verificados):
- https://hotmart.com/es/marketplace/productos/invitaciones-basico/N97875409T (200 invitaciones Canva, uso comercial)
- https://hotmart.com/es/marketplace/productos/hagsxd-invitaciones-digitales-con-canva-wuj26/B101653632U (+1000 invitaciones Canva "vender como servicio")
- https://hotmart.com/es/marketplace/productos/pack-de-invitaciones-digitales-lara-campos-editables-en-canva/Q102879932F
- https://hotmart.com/es/marketplace/productos/negocio-de-invitaciones-infantiles-de-principiante-a-experto/I86554392L ("PACK de Invitaciones en VIDEO listas para Vender")
- https://hotmart.com/es/marketplace/productos/mega-pack-100-invitaciones-digitales-editables-en-canva-boda-bautizo-cumpleanos-candy-bar-agendas-y-mas/V102193567R
- https://hotmart.com/es/marketplace/productos/mega-pack-de-invitaciones-digitales/N86477437U (+1000)
- https://hotmart.com/es/marketplace/productos/pack-emprendedor-de-invitaciones-editables-bonus/A105007145T
- https://hotmart.com/es/marketplace/productos/guia-completa-como-vender-invitaciones-digitales-desde-casa/H102322061B
- https://hotmart.com/es/marketplace/productos/pack-de-190-video-invitaciones-digitales-para-cumpleanos/N84722082H (190 video-convites em PowerPoint)
- https://hotmart.com/es/marketplace/productos/invitaciones-digitales-tipo-sitio-web/O101247541J ("INVITACIONES DIGITALES TIPO SITIO WEB")
- https://hotmart.com/es/marketplace/productos/super-pack-invitaciones-digitales-premium/U102321667R
- https://hotmart.com/es/marketplace/productos/curso-para-emprender-con-invitaciones-digitales-interactivas/L83087551J (curso, Naileth Pinto)

Preços pay.hotmart (via snippet de busca):
- "Invitaciones Digitales desde Cero: Aprende a Crearlas y Venderlas Online" — US$10 — https://pay.hotmart.com/V103706751K
- "Invitaciones Digitales Interactivas para Eventos" — US$14.99 — https://pay.hotmart.com/K102179105D
- "Negocio de Invitaciones Digitales: PACK BODA Y QUINCEAÑOS" — US$5 — https://pay.hotmart.com/T102280557H
- "Tarjetas de Invitacion Digital y Shaker" — US$5 — https://pay.hotmart.com/M102400480I
- "Invitaciones de boda (Personalizado)" — US$60 — https://pay.hotmart.com/H94034940L
- "Kit Empresarial Event Planner" (+70 invitaciones Canva) — preço não verificado — https://pay.hotmart.com/H100030235D
- "Tarjetas de presentación digitales" — preço não verificado — https://pay.hotmart.com/A70446027R

Outros cursos de convite interativo: https://diditarjetasdigitales.tiendup.com/curso/emprende-con-invitaciones-digitales-en-10-dias ; https://www.udemy.com/course/curso-invitaciones-digitales-interactivas/

Canção IA (Hotmart = cursos, E1): https://hotmart.com/es/marketplace/productos/monetiza-tu-musica-con-inteligencia-artificial-de-la-creacion-a-la-venta/A95508028H ; https://hotmart.com/es/marketplace/productos/produccion-musical-con-inteligencia-artificial/I101530758W
Canção IA automatizada (concorrentes B2C em ES): https://cancioname.com/ (3–5 min) ; https://www.cantale.mx/ (minutos) ; https://www.soundgift.app/es/ (<10 min por email) ; My Forever Songs MX$279 https://myforeversongs.com/es-mx/blog/ai-personalized-song-gift ; faixa US$20–39 citada em https://cantale.app/blog/cuanto-cuesta-una-cancion-personalizada

Conto IA automatizado: cuentoconlaia.com 3,99€ PDF 20 págs em 5–10 min https://cuentoconlaia.com/ ; https://toonystory.com/es ; https://www.cuentoslandia.com/ ; Cucucuentos desde 39,95€ (impresso) https://cucucuentos.com/ ; https://cuentista.mx/ ; https://www.cuenta-me.com/

Sessão de fotos IA: AI Selfi 40 fotos US$29 / 100 fotos US$39 https://aiselfi.es/sesion-de-fotos-con-ia ; https://www.fotosconia.ai/ (LATAM) ; imprensa sobre ensaio de aniversário com Gemini (grátis): https://www.nacion.com/tecnologia/prompts-para-ensayos-fotograficos-de-cumpleanos/XSWD6XPCRBAYLE57MFHRZO52ZU/story/ ; https://www.milenio.com/virales/como-hacer-fotos-de-cumpleanos-con-ia-gemini-guia
Hotmart ensaio IA (PT-BR): https://hotmart.com/pt-br/marketplace/produtos/ensaio-fotografico-com-ia/Q92906309T ; https://hotmart.com/pt-br/marketplace/produtos/studio-ia/V98408507U ; PLR (E4 suspeita) https://hotmart.com/pt-br/marketplace/produtos/plr-mini-curso-de-fotos-profissionais-com-inteligencia-artificial/J84241141N

Página-presente em ES (concorrentes do Mimo): QLovy https://qlovy.com/es/blog/regalo-digital-gratis (grátis 24h + 6 meses + vitalício, pagamento único) ; MiYo Gift https://miyogift.com/es ; iloveyou.gift https://iloveyou.gift/ ("desde $5") ; Gifft.me https://gifft.me/es

Menú digital (Hotmart): https://hotmart.com/es/marketplace/productos/menu-app-qr-para-restaurantes/D64832885T ; https://hotmart.com/es/marketplace/productos/carta-virtual/V68221977S ; https://hotmart.com/es/marketplace/productos/pack-reactivacion-experta/J98768913T

---

## 6. Falhas / limitações
- Busca da Meta é por palavras soltas: termos genéricos ("página de amor", "regalo digital", "sorpresa digital", "sorprende a tu pareja", "catálogo digital WhatsApp", "crea tu invitación") retornaram ruído → não foi possível isolar concorrentes diretos do Mimo (página-presente) na Meta ES. Isso NÃO prova ausência.
- Sem corpo de anúncio: produto exato de várias páginas não verificado (rede "6U$D", Kit Digital, Mundos Digitales, Eugenia Silva, Tarjetas Interactivas).
- Páginas com 50+ anúncios (Diego Hernandez, Alimenta tu Vida, Music Creator Pro): contagem = estimated_total_count; data mais antiga = limite inferior.
- Duas respostas excederam o limite de tokens (Q10 e page DedicatieMuzicala) → salvas em arquivo e resumidas por script (100% lido pelo script).
- Preços Hotmart: só via snippet de busca (WebFetch/curl bloqueados). Maioria "não verificado".
- Santa Claus / Papá Noel: setembro = fora de temporada; sem sinal ativo (não verificado para nov–dez).
- Longevidade de Neurartica (~997d) pode refletir anúncio esquecido com gasto baixo (proxy fraco).
