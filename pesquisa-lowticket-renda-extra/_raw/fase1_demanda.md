# Fase 1 — Demanda, sazonalidade, objeções e reação a rosto de IA (anotações brutas)

Data de referência: 2026-09-22 (epoch 1790095977). Dias ativo = (1790095977 - start)/86400.
Ferramentas: WebSearch (ok), Meta Ads Library (`ads_library_search`, ok). Google Trends, WebFetch, facebook.com, hotmart.com: BLOQUEADOS (não tentado fetch).

---

## 1. Queries rodadas

### WebSearch (resumo)
1. "ingresos extra" búsquedas Google Trends aumento México 2025 -> nada específico
2. "qué vender en navidad" ideas negocio diciembre 2025 México -> artigos de ideias (emprendedor.com, altonivel, seccionamarilla, nubimetrics)
3. "cuesta de enero" búsquedas "ganar dinero" aumento enero Google -> nada útil
4. aguinaldo 2025 emprender... -> ABC Noticias (ideas para emprender con aguinaldo), EMICRON DANE
5. encuesta uso del aguinaldo ... Condusef 2025 -> Research Land 2025: 49% deudas, 27% compras/regalos; 4 de 10 ocupados reciben aguinaldo
6. "cuesta de enero" mexicanos ... 2026 -> Research Land: 60% afectados; Líder Empresarial; Político polls
7. Google Año en Búsquedas 2025 ... -> sem "cómo ganar dinero" nos tops
8. latinoamericanos buscan ingresos extra ... -> Argentina set/2026: 38,6% combinam trabalhos/bicos; 43% buscam mais trabalho por renda insuficiente; 12,2% pluriempleo (INDEC Q4 2025)
9-16. Objeções: hotmart es estafa / no me llegó / reembolso / imprimibles estafa / invitaciones digitales estafa / kit para emprender PLR / funciona en mi país / Profeco
17-20. Reddit/ReclameAqui/Trustpilot/página personalizada estafa
21-28. Rosto IA: Columbia/Taboola, NIQ, Meta AI info, MediaScience, NYU/Emory, LATAM influencers virtuais, México percepção, AI avatar vs UGC
29-35. Público: DataReportal MX/CO/AR/PE/CL, OIT informalidad, INEGI, GEM, Pew hispanos
36-41. Sazonalidade: Hotmart picos, Meta CPM Q4, prima CO, gratificación PE, cuesta de enero outros países, propósitos año nuevo
42-47. Extras: cargo HOTMART, invitaciones curso, MRR/PLR crítica, deepfake anuncios, NYU 31.5%, AI avatar benchmarks
48-50. site:hotmart.com/es invitaciones digitales; site:hotmart.com/es moldes navidad; páginas personalizadas parejas negocio

### Meta Ads Library (todas ACTIVE salvo indicado; países ES = MX,CO,AR,CL,PE,EC,GT,BO,UY,DO,US)
| Query | Países | estimated_total_count | Observação |
|---|---|---|---|
| ingresos extra | 11 ES+US | 7.617 | muito ruído: empregos, MLM (Farmasi, Novaventa, Vitnik), cassino, cursos Aprende Institute |
| ingresos extra | MX | 3.099 | |
| ingresos extra | AR | 1.687 | |
| ingresos extra | CO | 1.657 | |
| ingresos extra | PE | 1.116 | |
| ingresos extra | CL | 1.005 | |
| ingresos extra | US | 850 | |
| ganar dinero desde casa | 11 ES+US | 12.349 | ruído (dramas, jogos); rede "PROMOCION POR TIEMPO LIMITADO" |
| emprender desde casa | 11 ES+US | 5.133 | cursos de ofício, livros digitais (postres), agendas |
| vender en navidad | 11 ES+US | 934 | já em setembro: moldes/patrones/velas/recetas para vender en Navidad |
| invitaciones digitales | 11 ES+US | 1.283 | maioria são prestadores de serviço (clientes finais do "kit"); Mega Plantillas Digitales |
| agenda 2027 | 11 ES+US | 7.292 | ruído total (carros, escolas) — descartado |
| cuesta de enero ingresos (ALL status) | MX,CO,AR,CL,PE | 528 | ruído (política, dramas) — não serve p/ sazonalidade |
| aguinaldo emprender (ALL status) | MX,CO,AR,CL,PE | 65 | "El Sabor de la Nochebuena — 🎄 500 Recetas para Negocio" (dez/2025) |

Observação: contagens por país se sobrepõem (um anúncio pode mirar vários países). `keyword_unordered` casa palavras soltas -> contagem é proxy grosseiro de "barulho publicitário", não de demanda.

---

## 2. Tabela de anunciantes investigados (page_ids)

| Página | page_id | Nº ads ativos | Mais antigo (start) | Dias ativo (mais antigo) | Título/oferta | Links |
|---|---|---|---|---|---|---|
| Abundancia Suprema | 1312049798658357 | 39 | 2026-09-17 | 5,3 | "PROMOCION POR TIEMPO LIMITADO" (USD) — oferta não verificada | https://www.facebook.com/ads/library/?id=1063408609866794 ; https://www.facebook.com/ads/library/?id=2344071382794647 |
| Emprede y Genera + Verdades del Dinero (consulta conjunta) | 1272269899306111 / 1203724022834533 | 158 (conjunto; 50 vistos) | limite: 2026-09-21 (entre os 50 mais novos) | 50+ (limite) | mesmo título "PROMOCION POR TIEMPO LIMITADO" (USD) — provável mesma operação em várias páginas; produto não verificado | https://www.facebook.com/ads/library/?id=1995527901381211 ; https://www.facebook.com/ads/library/?id=1142339368455421 |
| Mega Plantillas Digitales | 1154408571089804 | 10 | 2026-08-04 | 49,5 | "Mira como funciona📱" / "Ver invitaciones digitales ✨" (USD) — pack de plantillas de invitaciones | https://www.facebook.com/ads/library/?id=1708910720392963 ; https://www.facebook.com/ads/library/?id=2205298640865792 ; https://www.facebook.com/ads/library/?id=3711236485701842 |
| Aprende en casa | 110643181782006 | 212 (50 vistos) | limite: 2026-09-21 (entre os 50 mais novos) | 50+ (limite) | "Descargar +800 Moldes Fieltro ✂️" (PEN) e "🔥 ¡OBTENERLO AHORA! 👇" (USD) | https://www.facebook.com/ads/library/?id=1862851984699832 ; https://www.facebook.com/ads/library/?id=4658212711078060 |
| El Sabor de la Nochebuena | 919566217896325 | 4 (ALL; provavelmente inativos) | 2025-12-03 | n/a (sazonal) | "🎄 500 Recetas para Negocio" (USD) | https://www.facebook.com/ads/library/?id=1392173199187558 |

Outros vistos (não investigados por page_id), relevantes como ideias:
- Tejidos y Crochet (1222570877617282) "+1000 Patrones Verificados en Español + 6 Bonos" (CLP) https://www.facebook.com/ads/library/?id=1432152345461217
- Cleo Cursos (107918535377642) "🔥 20 PATRONES DE POSAVASOS + BONO DE NAVIDAD 🎁" (ARS) https://www.facebook.com/ads/library/?id=1121049337157661
- Manos que Emprenden (1031472580052420) "Aprende a crear velas y prepárate para Navidad" (COP) https://www.facebook.com/ads/library/?id=1407368758190740
- Academia Dulce Emprende (1302953309570574) "LIBRO DIGITAL DE POSTRES🧁" (USD) https://www.facebook.com/ads/library/?id=1410450964376310
- Estudio de Producción Martínez (1176468978894281) "QUIERO LA OFERTA AHORRA 👉" (USD, 8+ ads no mesmo dia) https://www.facebook.com/ads/library/?id=2969218963427160
- Bruno Lero (839455215916257) "Pack +200 Plantillas Editables ¡Acceso De Por Vida! 🎁" (BRL) https://www.facebook.com/ads/library/?id=933352599458140
- Calixta Card (610766325453656) "✨ Invitaciones web para tus 15 años ✨" (ARS) https://www.facebook.com/ads/library/?id=1871601350828706
- Limasystem "Tu invitación de boda desde S/ 95.90" (PEN) https://www.facebook.com/ads/library/?id=28398285386504838
- Auras Estrategicas "Invitaciones digitales desde $499 MXN" https://www.facebook.com/ads/library/?id=1625294865810114
- Miboda.love "¿Te casas en noviembre o diciembre?" https://www.facebook.com/ads/library/?id=1624182579230484

---

## 3. Sazonalidade — evidências
- Hotmart: out/nov = maior volume de vendas do ano; Black Friday +242% (dado da própria Hotmart, via imprensa) https://edomexaldia.com/el-consumo-digital-en-picos-estacionales-impulsa-mas-del-50-de-transacciones-transfronterizas-en-hotmart-en-america-latina/ ; https://hotmart.com/es/blog/black-week-hotmart-la-oportunidad-de-vender-mucho-en-una-semana
- Aguinaldo MX: prazo 20/dez; 49% usou p/ dívidas, 27% compras/regalos (Research Land 2025); só ~4 em 10 ocupados recebem https://grupoanimal.mx/explicaciones/deudas-ahorro-como-usar-aguinaldo ; https://www.capitalmexico.com.mx/nacional/encuesta-indica-que-cinco-de-cada-10-mexicanos-no-recibiran-aguinaldo-en-2025/
- Prima CO: até 20/dez https://www.cronista.com/colombia/finanzas-y-economia/hasta-cuando-pueden-pagar-la-prima-de-diciembre/
- Gratificación PE: até 15/dez https://rpp.pe/economia/economia/gratificacion-por-navidad-2025-cuanto-recibiras-la-fecha-limite-y-que-pasa-si-tu-empleador-no-la-deposita-a-tiempo-noticia-1665554
- Aguinaldo AR (SAC 2ª cuota): data não verificada nesta fase.
- Cuesta de enero 2026 MX: 60% afetados; 41% gastou demais; 37% vai pagar dívidas https://www.liderempresarial.com/cuesta-de-enero-2026-golpeara-a-60-de-mexicanos/amp/ ; https://polls.politico.mx/2026/01/01/cuesta-de-enero-2026-servicios-despensa-y-deudas-encabezan-los-gastos/
- Meta CPM (dados EUA): Q4 +26% vs média; nov +41%; BF 2–3x; 26/dez–15/jan CPM cai 40–60%; jan/2026 = mínimo de 13 meses https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns ; https://clouted.com/blog/meta-advertising-CPM-inflation-statistics ; https://paceads.com/research/meta-ads-statistics-2026 (LATAM não verificado)
- Ad Library: "vender en navidad" = 934 anúncios ativos já em 22/set (moldes/patrones/velas/recetas para vender).
- Google Trends: NÃO VERIFICADO (bloqueado). Links prontos abaixo.

## 4. Objeções — links
(ver JSON final; principais fontes)
- https://decidetucurso.com/hotmart-opiniones/ ; https://kursopro.com/blog/emprendimiento/estafa-hotmart/ ; https://www.trustpilot.com/review/hotmart.com ; https://es.quora.com/Alguien-sabe-si-Hotmart-es-seguro-o-es-una-estafa-o-hay-p%C3%A1ginas-falsas-de-Hotmart-que-son-falsos
- https://www.reclameaqui.com.br/hotmart/produto-nao-entregue-apos-pagamento_a4N34Fdqnwq4-yxN/ ; https://www.reclameaqui.com.br/hotmart/comprei-um-produto-horrivel-e-nao-consegui-pedir-reembolso_5VyTWY61xV8bZ_V9/
- https://help.hotmart.com/es/article/360038516312/-que-hacer-si-no-puedo-acceder-a-mi-compra- ; https://help.hotmart.com/es/article/209033847/-como-identificar-un-cargo-de-hotmart-que-aparecio-en-mi-extracto-bancario-
- https://help.hotmart.com/es/article/25648853025037/-cuales-son-los-metodos-de-pago-disponibles-para-comprar-en-hotmart- ; https://es.quora.com/Qu%C3%A9-pa%C3%ADses-no-pueden-comprar-en-Hotmart
- https://es.linkedin.com/posts/juanacervio_en-las-redes-muchos-est%C3%A1n-diciendo-que-podes-activity-7080577536010633216-322- ; https://lalibertadfinanciera.online/cuidado-con-la-estafa-de-los-productos-de-licencia-plr/
- https://www.infobae.com/mexico/2024/04/10/aguas-con-las-estafas-profeco-alerta-por-trabajos-falsos-con-likes-en-redes-sociales/?outputType=amp-type ; https://consumer.ftc.gov/consumer-alerts/2025/06/how-avoid-work-home-job-scams ; https://latam.kaspersky.com/blog/work-proposal-schemes/26600/
- https://www.semana.com/tecnologia/articulo/alerta-por-peligrosa-estafa-con-ia-suplantan-a-famosos-para-enganar-a-seguidores-y-cometer-fraudes/202524/ ; https://itwarelatam.com/2025/04/30/estafadores-usan-ia-para-hacerse-pasar-por-celebridades-y-estafar-a-sus-victimas-alerta-kaspersky/
- https://www.infobae.com/mexico/2026/08/29/necesidad-o-tendencia-profeco-advierte-sobre-compras-impulsivas-provocadas-por-redes-sociales/
- https://www.semana.com/tecnologia/articulo/pilas-con-las-estafas-en-amor-y-amistad-estas-son-las-senales-de-alerta-que-no-deberia-ignorar-al-comprar-un-regalo-por-internet/202603/

Reddit: buscas não retornaram threads do Reddit (só blogs/Quora/TikTok). Não verificado.

## 5. Rosto de IA — evidências
- Columbia/Harvard/TUM/CMU + Taboola (500M impressões): CTR IA 0,76% vs humano 0,65%; melhor quando NÃO parece IA; rosto humano grande = sinal de confiança https://investors.taboola.com/news-releases/news-release-details/new-study-ai-ads-match-human-creative-major-report-columbia/ ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5096969
- NYU Stern/Emory: divulgar "feito com IA" -> CTR -31,5% https://www.stern.nyu.edu/experience-stern/faculty-research/ai-advertising-paradox ; https://ppc.land/ai-ad-labels-cut-click-through-31-5-iab-framework-cites-nyu-study/
- MediaScience (900 EUA): rótulo de IA não reduziu métricas de marca https://www.marketingdive.com/news/ai-disclosure-labels-dont-hurt-ad-performance-heres-what-the-numbers-say/822711/
- NIQ (dez/2024, 2.000+ participantes, EEG): anúncios IA percebidos como "annoying, boring, confusing"; menor ativação de memória https://nielseniq.com/global/en/news-center/2024/niq-research-uncovers-hidden-consumer-attitudes-toward-ai-generated-ads/
- Meta: pessoa fotorrealista gerada por IA -> rótulo "AI info" ao lado de "Patrocinado"; detecção automática de ferramentas de terceiros desde jun/2026 https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/ ; https://www.socialmediatoday.com/news/meta-adds-updated-disclosure-tags-for-ai-generated-ads/824658/ ; https://coinis.com/blog/meta-ai-content-labeling-facebook-instagram-ads-2026
- AI UGC ~60–80% do desempenho de UGC real (benchmark de agência, não auditado) https://adlibrary.com/posts/ugc-ads-guide ; https://www.digitalapplied.com/blog/ai-avatar-ads-vs-real-ugc-creators-cost-trust-2026
- LATAM: 43% não confia em anúncios de IA (Adlatina; escopo não verificado) https://www.adlatina.com/publicidad/el-43-de-los-consumidores-no-confa-en-anuncios-creados-por-ia ; 52% seguem ao menos 1 influencer virtual (Expansión MX) https://expansion.mx/tecnologia/2025/07/24/en-redes-sociales-52-de-los-usuarios-siguen-al-menos-a-un-influencer-virtual ; Chile: desconfiança majoritária do uso de IA por empresas https://www.emol.com/noticias/Economia/2026/05/13/1199856/uso-ia-empresas-desconfianza-consumidores.html ; pequenos negócios MX apostando em "publicidade feita à mão" https://heraldodemexico.com.mx/nacional/2026/9/8/pequenos-negocios-rechazan-la-inteligencia-artificial-apuestan-por-publicidad-hecha-mano-884698.html
- Deepfakes de famosos em anúncios de "ganar dinero" (MX/CO) contaminam percepção de rosto IA no nicho de renda extra (inferência).

## 6. Tamanho de público — proxies
- MX: Facebook 93,5M (70,7% pop), Instagram 53,6M, internet 110M https://datareportal.com/reports/digital-2026-mexico
- CO: Facebook 36,4M; internet 41,7M https://datareportal.com/reports/digital-2026-colombia
- AR: Instagram 31,1M; pop 45,9M; Facebook ~36M (fonte secundária, não verificado) https://datareportal.com/reports/digital-2026-argentina ; https://businesstats.com/top-25-countries-based-on-number-of-facebook-users/
- PE: Facebook ad reach 24,7M (71,3% pop) https://datareportal.com/reports/digital-2026-peru
- CL: Facebook 13,1M https://datareportal.com/reports/digital-2026-chile
- EC/GT/BO/UY/DO: não obtido.
- Hispanos EUA: 62% usam Instagram (Pew 2025) https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/
- Informalidade OIT 2025: média 47%; BO 82,2; EC 70,1; PE 69,8; CO 54,3; CL 25,1; UY 22,4 https://es.mercopress.com/2025/12/12/informalidad-laboral-afecta-a-casi-la-mitad-de-america-latina-dice-oit ; https://www.ilo.org/sites/default/files/2025-12/OIT-Informe-PANORAMA-LABORAL-2025.pdf
- MX informalidade 55,1% (Q2 2026) = 33,1M pessoas https://www.diarioelindependiente.mx/2026/08/tasa-de-informalidad-laboral-en-mexico-aumenta-a-551-en-el-segundo-trimestre-de-2026
- AR pluriemprego: 38,6% combinam trabalhos/bicos/apps; 43% procuram mais trabalho por renda insuficiente (set/2026) https://www.nueva-ciudad.com.ar/notas/202609/58321-un-solo-sueldo-ya-no-alcanza-casi-4-de-cada-10-trabajadores-argentinos-buscan-ingresos-extra.html ; https://www.ambito.com/economia/crece-el-pluriempleo-y-ya-4-cada-10-trabajadores-buscan-un-complemento-sus-ingresos-n6323854
- GEM: TEA PE 12,8%; EC 32,65% https://www.researchgate.net/publication/408517128_Reporte_GEM_PERU_2025-2026 ; https://uees.edu.ec/wp-content/uploads/2026/05/GEM-2025.pdf

## 7. Links prontos
### Google Trends
- https://trends.google.com/trends/explore?date=today%205-y&geo=MX&q=ingresos%20extra,ganar%20dinero%20desde%20casa,emprender%20desde%20casa,negocio%20desde%20casa,trabajo%20desde%20casa
- (idem CO, AR, CL, PE, US — ver JSON)
- https://trends.google.com/trends/explore?date=today%205-y&geo=MX&q=qu%C3%A9%20vender%20en%20navidad,negocios%20para%20diciembre,cuesta%20de%20enero,aguinaldo,ingresos%20extra
- CO: prima de diciembre; PE: gratificación; AR/CL: aguinaldo (ver JSON)
- https://trends.google.com/trends/explore?date=today%205-y&geo=MX&q=invitaciones%20digitales,plantillas%20editables,imprimibles,moldes,productos%20digitales
- https://trends.google.com/trends/explore?date=today%205-y&q=hotmart ; https://trends.google.com/trends/explore?date=today%205-y&q=hotmart%20estafa

### Biblioteca de Anúncios (ver JSON para lista completa)

## 8. Falhas / limitações
- Google Trends bloqueado: nenhuma curva verificada; só links.
- WebFetch bloqueado: Reddit/Trustpilot/Reclame Aqui lidos só via snippet do buscador.
- Reddit: nenhum thread encontrado pelas buscas.
- Ad Library: `keyword_unordered` muito ruidoso; sem texto do corpo; relevância julgada por page_name/título. Ferramenta retorna do mais novo ao mais antigo -> impossível medir sazonalidade histórica (nov–jan) via Ad Library.
- Páginas com 50+ ads: data mais antiga vista é só limite (e cai nos anúncios mais novos) -> longevidade real não medida (Aprende en casa, Emprede y Genera/Verdades del Dinero).
- Produto da rede "PROMOCION POR TIEMPO LIMITADO" não identificado.
- Números de pesquisas (Adlatina 43%, Research Land) vêm de resumos de busca; metodologia/escopo não verificados.
- Facebook users AR (secundário), EC/GT/BO/UY/DO não obtidos.
- Preços dos produtos Hotmart citados não verificados.
