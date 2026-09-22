# L29 · Calculadora de costos y precios: custo por unidade, preço sugerido e lista de preços para quem vende comida e doces em casa

Data: 22/09/2026. Consolida pesquisa, build, oferta, criativo e red team (notas de trabalho privadas, fora do repositório), já com as correções do red team. Onde os documentos divergiam (preço, bumps, ofícios, medidas, líquido, regras de corte), vale a versão unificada abaixo.

**Convenções:**
- **[medido]**: Biblioteca de Anúncios da Meta (só ACTIVE, 22/09/2026) ou página com link.
- **[estimativa]**: conta aberta, feita na calculadora do usuário (`_raw/calc_economia.py`).
- **[inferência]**: leitura minha.
- **não verificado**: não confirmado.

Contagem de anúncios e dias no ar são proxies: ACTIVE não prova gasto nem venda, e a Fase 1 achou anúncios de temporada passada ativos há 287–366 d, possivelmente esquecidos. Do Mimo Gift entram só quatro números: líquido por comprador ~US$ 9,4, adesão do bump principal ~1/3, reembolso < 1% e gasto > R$ 2.600/dia (dado do usuário).

## Resumo em 5 linhas

1. **O produto.** É um web app no celular, sem planilha e sem cadastro para começar. A pessoa digita os insumos como compra e como usa, o rendimento e os custos escondidos (embalagem, gás/luz, o próprio tempo), e vê de graça o custo por unidade, o preço mínimo, o preço sugerido e a margem. Pagando (A/B de US$ 7,90 × 5,90 em moeda local, pagamento único, licença de 12 meses), guarda até 200 produtos, recalcula tudo quando um insumo sobe e exporta a lista de preços em imagem para o estado do WhatsApp e a ficha técnica em PDF. São 4 bumps de US$ 3,90–4,90.
2. **A evidência [medido; proxy].** Existem anunciantes longevos em espanhol, mas são pequenos e quase todos de comida para restaurante. O maior, Fer Rendon, tem 36 anúncios de "costeo" (22 com ≥ 30 d) e vende **Excel B2B para restaurante**. Para a confeiteira de casa, o máximo é a Chef Anna: 17 anúncios, **só 1** com 119 d, e produto não identificado. A âncora paga fica em US$ 3–6, há 8+ calculadoras grátis, e artesanato não mostrou sinal.
3. **A economia [estimativa].** A US$ 7,90, o líquido por comprador fica em 6,40 / 7,24 / 8,14 (conservador / base / otimista), ~77% do Mimo no base. O CPA para ROI 1,5 com conta em BRL fica em 3,81 / **4,31** / 4,85, contra ~5,60 do Mimo. No funil freemium ilustrativo (2,1% de compra por clique), a conta só fecha com CPC ≤ US$ 0,09.
4. **O teto [estimativa, confiança baixa].** Em espanhol, US$ 80–250/dia (base de 150), ou ~16–49% do Mimo (> R$ 2.600/dia ≈ US$ 506). Com PT-BR, EN e FR, US$ 130–560 (base de ~290). É palpite de ordem de grandeza: as frações de público não têm fonte.
5. **O veredito.** É um segundo produto barato de testar, não um substituto do Mimo. O build real leva 11 dias até o vendável, não os 4–6 da pesquisa, e com isso já falha o critério da própria pesquisa (build ≤ 5 d). Se for feito, que seja com teto de US$ 600 de teste e os cortes K0–K10 na régua BRL. O desfecho mais provável é um CPA acima de 4,31.

## O que o comprador recebe e o mecanismo (por que é diferente do que já existe)

**Mecanismo: "calcula grátis, paga para guardar e exportar".** É o princípio do Mimo e da Convitia (ver antes de pagar), com uma diferença importante. No Mimo, a prévia grátis cria desejo por algo que só passa a existir depois do pagamento. Aqui, o "aha" (o número) já é boa parte do entregável [inferência; ver a última seção].

**Grátis, sem cadastro.** O rascunho fica só no navegador, então o grátis tem custo zero de servidor.
- 1 produto com o resultado completo: custo por unidade, preço mínimo, preço sugerido, lucro por unidade, e margem e markup lado a lado.
- "¿A cuánto lo vendes hoy?", com a diferença para o sugerido.
- Prévia da lista de preços e da ficha com a marca d'água "VISTA PREVIA".
- Opcional: "Enviarme este resultado" por e-mail, que captura o lead com consentimento.

**Pago (front "Calculadora de Costos y Precios (app)").** Licença de **12 meses**, pagamento único, **sem renovação automática**:
- até 200 produtos salvos, com acesso em até 3 aparelhos;
- **livro de ingredientes com recálculo em cascata**: a pessoa muda o preço do ovo, todos os produtos se atualizam, e o app avisa quais ficaram com margem baixa;
- **lista de preços** em PNG 1080×1920 para o estado, mais o texto para copiar no WhatsApp, com nome e logo do negócio;
- **ficha técnica em PDF** por produto;
- ajustes do negócio: valor da hora (padrão zerado, sem sugerir renda), gastos % e arredondamento por moeda;
- depois de vencer, a conta fica em modo leitura com exportação CSV. O cliente nunca perde o que digitou.

**Fluxo:**
1. Anúncio → landing do ofício → escolha de ofício e país. O país define a moeda, o formato numérico ("1.500" é mil e quinhentos na AR/CO/CL; "1.5" é um e meio no MX/PE) e o arredondamento.
2. Editor: cada insumo com preço do pacote, tamanho e quantidade usada, em **g, kg, ml, l, unidad ou docena**. **Taza e cucharada ficam para a v1.1**, porque exigem gramas por ingrediente. A pesquisa punha a conversão no MVP; vale o build.
3. Rendimento ("rinde 12 porciones") e custos escondidos: empaque, gás/luz em %, minutos × valor da hora.
4. Resultado ("aha") e prévia com marca d'água → checkout Hotmart em lightbox com os bumps.
5. Página de obrigado: código de 6 dígitos por e-mail, digitado no mesmo navegador (a compra acontece no navegador interno do Instagram), que importa o rascunho e abre o painel.

**Motor (função pura, num módulo único de cálculo):** `costo_unit = (costo_lote + indirectos) / rendimiento + empaque_unit + mano_obra_unit`; `precio_minimo = costo_unit / (1 − comisiones%)`; `precio_sugerido = costo_unit / (1 − margen% − comisiones%)`, arredondado para cima ao múltiplo da moeda. Tem 12 golden tests numa rota de admin.

**Ofícios.** O MVP lança com **Repostería** e **Comida** (almuerzos, empanadas, pizzas, menú del día), que têm a evidência mais longa. *Velas y jabones* e *Tejido y crochet* são só arquivos de configuração (vocabulário e insumos sugeridos, sem preço), então podem entrar sem custo de build relevante. **Não têm sinal de demanda**, porém: a busca "cobrar tus manualidades calculadora" só trouxe ruído ([busca no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=cobrar%20tus%20manualidades%20calculadora&search_type=keyword_unordered); o link reproduz um país, e a leitura dos 11 países ES + US foi feita via API em 22/09/2026). No criativo recebem no máximo 2 vagas por semana, cortadas em 3 semanas sem vencedor.

**Onde é diferente e onde não é:**

| Alternativa | Exemplo [medido] | Diferença real para o L29 |
|---|---|---|
| Planilha Excel/Sheets paga | [Emprendedores Digitales](https://www.facebook.com/ads/library/?id=1047240127991578), S/ 10 ≈ US$ 2,97; [Excel para Restaurantes Perú](https://www.facebook.com/ads/library/?id=1089104103530989), S/ 19 ≈ US$ 5,64; [Fer Rendon](https://www.ferrendonx.com/p/costeo-de-menu-excel/) (MXN, preço não verificado; exige Excel 2021+ no PC ou Mac, segundo o resumo da busca) | Roda no celular, sem fórmulas, e **sai uma imagem pronta para postar**, não uma célula. Custa mais que a âncora |
| Calculadora web grátis | [Supleo](https://www.supleo.app/calcular-costo/reposteria), [Simúlalo](https://simulalo.app/es/simulador/food/costos-panaderia), [gigiad](https://www.gigiad.com/?lang=en), [calculadoraderecetas.com.ar](https://calculadoraderecetas.com.ar/) e outras | **O cálculo em si não é diferencial.** O pago acrescenta recetario salvo, recálculo em cascata e lista com marca |
| App de gestão para confeitaria | [Dolchere](https://www.facebook.com/ads/library/?id=1742357790155181) ("La app de las pasteleras"; "Controlá tu pastelería desde el celular", 42,9 d, [link](https://www.facebook.com/ads/library/?id=2131547987779501)); [Repostery](https://www.facebook.com/ads/library/?id=1479382940908553); [PostrePro](https://play.google.com/store/apps/details?id=com.postrepro.app&hl=es) e [Pastri](https://apps.apple.com/pe/app/pastri-costos-de-recetas/id6777233315) nas lojas | **"App no celular" também não é exclusivo.** O L29 faz uma coisa só, com pagamento único e meios de pagamento locais via Hotmart. Preços e modelo de cobrança dos apps não verificados |
| Calculadora na Hotmart com bônus de WhatsApp | [Valeria Bonafini, "Calculadora + Guía + Bonus WhatsApp"](https://hotmart.com/es/marketplace/productos/sistema-de-precios-rentables-para-reposteria-calculadora-guia-bonus-whatsapp/X105453537A) | **A lista para WhatsApp já é bônus de concorrente**, não diferencial |
| Catálogo do WhatsApp Business | Grátis (não verificado nesta sessão) | Concorre com o bump B2 (catálogo web) |
| Kit de ticket alto | [Latinas Together, GastroKit US$ 57](https://www.facebook.com/ads/library/?id=1057383214053948) | Mesmo núcleo por US$ 7,90 + bumps |
| SaaS B2B de restaurante | [CostoChef](https://www.facebook.com/ads/library/?id=1553910179395667) ("¿Sabes cuánto pierdes en cada platillo?") | Outro público, com assinatura e POS |

**Defensibilidade: baixa.** A pesquisa e o build falavam num diferencial "defensável" (app no celular que se atualiza sozinho + lista para WhatsApp). O correto é **"diferencia hoje, copiável em dias"**: a lógica se clona num dia, a lista já é bônus de concorrente e "desde el celular" já é ângulo da Dolchere. Sobram a saída visual pronta (lista, catálogo, cotizador), o volume de criativo por ofício e data, e a troca de idioma.

## Comprador: perfil, dor e objeções (com evidência)

**Perfis.** As idades são inferência a partir dos títulos.

| Perfil | País | Evidência |
|---|---|---|
| **Confeiteira de casa** (tortas, postres, cupcakes): **público principal**. Mulher, 25–50 anos [inferência]. Já vende por encomenda no WhatsApp ou Instagram e cobra "a ojo" | MX, AR/UY (voseo), PE, CO | Gênero nos títulos: "Calcula tus recetas sin ser contadora" ([Latinas Together](https://www.facebook.com/ads/library/?id=1102297872765779)); "Tené tus números claros. Trabajá tranquila." ([Dolchere](https://www.facebook.com/ads/library/?id=1994490021269478)). 13 dos 17 anúncios da [Chef Anna](https://www.facebook.com/ads/library/?id=1276480471319495) são de "postres" |
| **Quem vende comida** (menú del día, viandas, fonda). Gênero misto, 30–55 anos [inferência] | PE, MX | "¿VENDES MENÚS Y NO SABES CUÁNTO REALMENTE GANAS?" ([Emprendedores Digitales](https://www.facebook.com/ads/library/?id=2286764062122944)); "Deja de adivinar tu food-cost" ([Cuentas Claras](https://www.facebook.com/ads/library/?id=1406549894774908)). O sinal mais longo é de **restaurante** (Fer Rendon: restaurantes, cafeterias, food trucks). **A transferência para quem vende em casa não foi verificada** |
| Latina nos EUA com negócio de comida | US | **Não verificado.** A base é 1 anunciante ([Latinas Together](https://www.facebook.com/ads/library/?id=1057383214053948), GastroKit US$ 57) com 12–13 anúncios de ~1,5 d. "Renda mais alta, aceita ticket maior" é hipótese |
| Artesã (crochê, velas): secundário | MX | **Sem prova.** Andrea Crochetea: 3 anúncios de 3,0 d (Fase 3). A busca de artesanato só trouxe ruído |

**Contexto [medido no digest]:** informalidade de 55,1% no MX ([INEGI via El Independiente](https://www.diarioelindependiente.mx/2026/08/tasa-de-informalidad-laboral-en-mexico-aumenta-a-551-en-el-segundo-trimestre-de-2026)) e de 69,8% no PE ([OIT](https://es.mercopress.com/2025/12/12/informalidad-laboral-afecta-a-casi-la-mitad-de-america-latina-dice-oit)); empreendedorismo inicial de 12,8% no PE ([GEM Peru](https://www.researchgate.net/publication/408517128_Reporte_GEM_PERU_2025-2026)). Quem vende comida em casa é muita gente, mas é **um recorte** do público de renda extra [inferência].

**Dor (títulos medidos; a leitura é inferência):**
- **Não sabe quanto sobra:** "¿Sabes cuánto te queda REALMENTE?" ([Latinas Together](https://www.facebook.com/ads/library/?id=1473992827892735)); "NO TODO LO QUE VENDES SE CONVIERTE EN GANANCIA" ([Emprendedores Digitales](https://www.facebook.com/ads/library/?id=2557290058030429)).
- **Medo de cobrar:** "Deja de cobrar con miedo" ([Latinas Together](https://www.facebook.com/ads/library/?id=1396505975315099)); "Deja de bajar tu precio por miedo" ([link](https://www.facebook.com/ads/library/?id=1073945475398048)).
- **Insumo sobe e o preço fica velho:** o preço do ovo varia por região no MX ([aviNews](https://avinews.com/precio-huevo-mexico-abril-2026/)). O cenário "ovo +30%, custo +21%" de um simulador online **não foi verificado** (fonte provável: [Simúlalo](https://simulalo.app/es/simulador/food/costos-panaderia)).
- **Números e planilha assustam:** "Calcula tu precio sin saber de Excel" ([Latinas Together](https://www.facebook.com/ads/library/?id=1079340274850581)).
- **Orçamento demora:** "Hacé tus presupuestos en minutos" ([Dulces Herramientas](https://www.facebook.com/ads/library/?id=1624450332359038)).

**Desejo:** ordem e tranquilidade ("Ordená tu negocio pastelero", [Dolchere](https://www.facebook.com/ads/library/?id=2150968492179995)); profissionalizar ("Profesionalizá tu pastelería", [Dolchere](https://www.facebook.com/ads/library/?id=2163072061251501)); rapidez ("Tu receta, tu precio, en segundos", [Latinas Together](https://www.facebook.com/ads/library/?id=949404011555129)).

**Objeções e resposta:**

| Objeção (ES) | Fonte | Resposta no produto ou na página |
|---|---|---|
| "Hay calculadoras gratis / lo hago en mi cuaderno" | [Supleo](https://www.supleo.app/calcular-costo/reposteria), [PostrePro](https://play.google.com/store/apps/details?id=com.postrepro.app&hl=es), [TikTok @pansitosyfermentos](https://www.tiktok.com/@pansitosyfermentos/video/7493564212191481093) | O primeiro cálculo é grátis. O pago libera o que o grátis não faz: guardar, recalcular tudo, lista com marca |
| "No sé de Excel / no soy buena con números" | [Latinas Together](https://www.facebook.com/ads/library/?id=1079340274850581) | Sem planilha; passos curtos no celular |
| "Si subo mis precios pierdo clientes" | [inferência] | Preço mínimo, sugerido e margem de cada um; a decisão é da pessoa. Nada de "gana más" |
| "¿Es suscripción?" | Apps e SaaS cobram mensalidade [inferência]; concorrente destaca "Único Pago" ([link](https://www.facebook.com/ads/library/?id=1089104103530989)) | "Pago único · acceso por 12 meses, sin renovación automática", no criativo, no checkout e no painel |
| "Pensé que era de por vida" | Concorrentes vendem "acceso de por vida" ([Fer Rendon](https://www.ferrendonx.com/p/costeo-de-menu-360-sheets/)) | O vencimento aparece no checkout, na página de obrigado e no painel; "para siempre" é o bump B1 |
| "¿Sirve con mi moneda y mis medidas?" | [inferência] | Moeda e formato numérico do país desde a tela 1, com eco formatado ("= 1.500,00 ARS") |
| "¿Hotmart es confiable? / cargo HTM*" | Digest de demanda; [Hotmart ajuda](https://help.hotmart.com/es/article/209033847/-como-identificar-un-cargo-de-hotmart-que-aparecio-en-mi-extracto-bancario-) | Acesso na página de obrigado e por e-mail; aviso do descritor da fatura |
| "Me cobraron varias veces" | [Trustpilot Hotmart](https://www.trustpilot.com/review/hotmart.com?page=4) | Bumps com nome e preço claros; um só upsell; sem downsell |
| "¿Pago con OXXO / PSE / Yape?" | Digest ([Quora](https://es.quora.com/Qu%C3%A9-pa%C3%ADses-no-pueden-comprar-en-Hotmart)) | Meios locais em texto, só onde estiverem ativos (não verificado por país); avisar que pagamento em dinheiro atrasa o acesso |

## Oferta: front por país (moeda local), bumps, upsell, garantia

**Paywall (ES):**
- "Calcula gratis. Paga solo si quieres guardar y compartir."
- "Pago único · sin suscripción · acceso por 12 meses, sin renovación automática."
- "Incluye: hasta 200 productos guardados, precios que se actualizan solos cuando sube un ingrediente, tu lista de precios lista para tu estado de WhatsApp y tu ficha de costos en PDF."
- "En tu estado de cuenta el cargo aparece como HTM* / HOTMART."

**Front: A/B de US$ 7,90 (controle) contra US$ 5,90.** Build e oferta concordam; o 7,90 × 9,90 da pesquisa fica para uma 2ª rodada.
- A âncora dos anúncios em espanhol é US$ 3–6 (ver Concorrentes) e puxa o preço para baixo; a taxa fixa da Hotmart puxa para cima (ver Sensibilidade, na seção Contas). O 7,90 é decisão de preço a validar no teste.
- **Não descer para 4,90:** a taxa fixa deixa só 59% do preço.
- Para empatar com o 7,90 em líquido por lead, o 5,90 precisa converter **1,31×** mais. O 9,90 empata mesmo convertendo até 19% menos.

| País | Moeda | A (controle) | ≈ US$ | B (teste) | ≈ US$ | C (2ª rodada) | Líquido por comprador no base, A / B / C [estimativa] |
|---|---|---|---|---|---|---|---|
| MX | MXN | MXN 139 | 8,07 | MXN 99 | 5,75 | MXN 169 | 7,31 / 5,32 / 8,79 |
| CO | COP | COP 24.900 | 7,99 | COP 18.900 | 6,07 | COP 29.900 | 7,27 / 5,63 / 8,65 |
| CL | CLP | CLP 7.490 | 7,81 | CLP 5.690 | 5,93 | CLP 9.490 | 7,16 / 5,56 / 8,95 |
| PE | PEN | S/ 26,90 | 7,99 | S/ 19,90 | 5,91 | S/ 32,90 | 7,26 / 5,48 / 8,78 |
| AR | USD (recomendado; oferta em ARS não verificada) | US$ 7,90 | 7,90 | US$ 5,90 | 5,90 | US$ 9,90 | 7,24 / 5,53 / 8,95. **Se o produtor pagar os 9,5% da conversão de ARS:** 6,31 / 4,79 |
| EC, DO, GT, BO, UY | USD | US$ 7,90 | 7,90 | US$ 5,90 | 5,90 | US$ 9,90 | 7,24 / 5,53 / 8,95 |
| US (hispanos) | USD | US$ 9,90 | 9,90 | — | — | US$ 12,90 | 8,95 / — / 11,52 |

Câmbio de 22/09/2026: 1 USD = 17,22 MXN · 3.116 COP · 959,5 CLP · 3,366 PEN · 5,14 BRL.

**Notas de implementação (Hotmart):**
- **Preço redondo em moeda local só se a Hotmart permitir ofertas em MXN/COP/CLP/PEN**, no principal e nos bumps (não verificado). Se não permitir, ficar em USD com conversão automática, **sem imprimir preço em moeda local** no anúncio ou na landing ("US$ 7,90 · se cobra en tu moneda"). Conferir a primeira venda real de cada país.
- **AR:** taxa de 9,5% na conversão de ARS para ofertas em USD ([Hotmart](https://help.hotmart.com/es/article/360015794612/-en-que-moneda-obtendre-mi-comision-); valor do resumo da busca). **Não verificado quem paga.** Se for o produtor, o CPA para ROI 1,5 cai para 4,21 (3,76 em BRL).
- **PE:** o braço B a S/ 19,90 testa direto a âncora "Único Pago S/. 19" do concorrente.
- **US:** oferta separada, com ≤ 5% da verba e sem A/B na 1ª rodada.
- **Tutorial de 3 min dentro do app**, não no Player da Hotmart, por precaução com a taxa do Player [inferência].
- **Decidir o A/B por líquido por lead**, com bumps. Lead = quem terminou o 1º produto grátis (evento `recipe_completed`). Com 8% de compra entre leads (hipótese), detectar 31% de diferença pede ~2.200 leads ou ~200 compras por braço. **Com o teto de teste de US$ 600, o A/B não fecha dentro do teste** [estimativa]: ele só vale se o produto passar dos cortes K4–K6 e for para a escala.

**Order bumps.** Unificados a partir da oferta. O build tinha 3; o B4 é só texto e é o mais barato de construir. As regras: nome e preço claros, sem preço riscado, sem timer, cada bump como produto digital entregável (formato Imagem/Foto da Hotmart). **As adesões são estimativas não verificadas.**

| # | Bump (ES, como aparece no checkout) | US$ | MX / CO / CL / PE | Entrega | Evidência | Adesão cons. / base / otim. |
|---|---|---|---|---|---|---|
| B1 | **"Acceso para siempre"**: "Tu calculadora no vence: tus productos y precios guardados sin fecha límite y sin pagos futuros." | 4,90 | MXN 79 · COP 14.900 · CLP 4.690 · S/ 15,90 | Remove o vencimento de 12 meses | Referência: o bump principal de um low ticket de presente adere ~1/3. Concorrentes vendem "de por vida". Deve aderir menos: comprador de ferramenta é mais racional, e há 4 bumps [inferência] | 15 / 24 / 33% |
| B2 | **"Catálogo web con pedidos por WhatsApp"**: "Una página con tu logo, tus fotos y tus precios. Tus clientes arman su pedido y te llega listo a tu WhatsApp. Incluye QR para imprimir." | 4,90 | igual ao B1 | Página pública do catálogo com "Arma tu pedido" → `wa.me` com itens e total; ativa enquanto a licença valer | [Intelia SB](https://www.facebook.com/ads/library/?id=1548914280065958), "Tu Catálogo Listo en Minutos", 9 ativos, 71,1 d. **Prova que alguém anuncia catálogo, não que alguém paga** (produto e preço não verificados). A busca "catálogo digital para tu negocio pedidos whatsapp" (144; [busca no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=cat%C3%A1logo%20digital%20para%20tu%20negocio%20pedidos%20whatsapp&search_type=keyword_unordered); o link reproduz um país, e a soma de 11 países ES + US foi feita via API em 22/09/2026) é quase toda agência e SaaS | 8 / 12 / 16% |
| B3 | **"Cotizador de encargos"**: "Presupuestos de tortas y pedidos especiales en PDF, con anticipo y fecha de entrega, listos para enviar por WhatsApp." | 3,90 | MXN 69 · COP 11.900 · CLP 3.790 · S/ 12,90 | Orçamento com cliente, data, itens, sinal % e validade → PDF + texto | "Hacé tus presupuestos en minutos", 11,0 d ([Dulces Herramientas](https://www.facebook.com/ads/library/?id=1624450332359038)). A busca "cotizar pasteles presupuesto anticipo" deu 0 em 11 países ES + US, somados via API em 22/09/2026 ([busca no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=cotizar%20pasteles%20presupuesto%20anticipo&search_type=keyword_unordered)): só como complemento | 4 / 7 / 10% |
| B4 | **"Mensajes listos para tus clientes"**: "25 mensajes para WhatsApp con tu nombre y tus precios: avisar un nuevo precio, responder '¿me haces descuento?', pedir anticipo, confirmar y recordar pedidos." | 3,90 | igual ao B3 | Modelos de texto no app, com botão "Copiar", preenchidos com os dados do negócio | "Deja de cobrar con miedo" ([Latinas Together](https://www.facebook.com/ads/library/?id=1396505975315099)); bônus de WhatsApp de concorrente na Hotmart. A busca "subir tus precios sin perder clientes" (19 em 11 países ES + US, somados via API em 22/09/2026; [busca no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=subir%20tus%20precios%20sin%20perder%20clientes&search_type=keyword_unordered)) só trouxe ruído | 4 / 6 / 9% |

- **Contingência de taxa:** se cada bump pagar taxa fixa de US$ 1,00 (regime R3, seção Contas), o bump de 3,90 fica com 64% do preço. Nesse caso, juntar B3 e B4 num "Pack Pedidos" a 5,90 (73%) ou subir os dois para 4,90.
- **Corte:** se atrasar, lançar com B1, B2 e B4. Se o MVP não estiver vendável no D14, só front + B1 (gate K0).
- **Fora por decisão:** "recetas base costeadas". Vender como "receitas para vender" puxa o nicho para risco E2 médio.

**Upsell de um clique, v1.1 (fora das contas principais): "Kit de Temporada", US$ 7,90** (MXN 139 · COP 24.900 · CLP 7.490 · S/ 26,90).
- **Copy:** "Tus listas de precios y tu catálogo con diseño de Día de la Madre, Halloween y Día de Muertos, Navidad, Rosca de Reyes y San Valentín, armados con tus productos. Incluye un calendario de cuándo abrir pedidos para cada fecha."
- **Evidência:** as datas já são ângulo pago no nicho ("No llegues tarde a las fechas que más venden", [Dolchere](https://www.facebook.com/ads/library/?id=1380669664237235); "Recetario de Halloween" a S/ 10, COP 14.999 e MXN 95, [Postres que Rentan](https://www.facebook.com/ads/library/?id=2373608776379748)).
- **Adesão:** 3 / 5 / 8% (estimativa). **Build:** +1 dia. Com OXXO ou dinheiro, **não verificado** se funciona. Um só upsell, sem downsell.
- O nome é "Kit de Temporada", não "fechas que más venden", para não soar como promessa de venda.

**Garantia de 7 dias** (o mínimo da Hotmart; na Europa, 15). Por que 7:
- o cálculo grátis já cumpre o papel de uma garantia longa;
- o que foi exportado (PNG, PDF) não volta: quanto maior o prazo, maior a janela para "configurar, exportar e pedir reembolso";
- o Mimo usa 7 dias e tem reembolso < 1%.

Só testar 15–30 dias se o paywall converter mal **e** o motivo apontado for confiança. Texto do FAQ (ES): "Tienes 7 días de garantía. Si pides el reembolso, tu cuenta y tu catálogo se desactivan; antes puedes descargar tus datos."

**O que não entra na oferta:**
- timer, "Solo hoy", preço riscado sem referência real;
- promessa de renda em anúncio, landing, nome de produto, bumps ou mensagens do B4;
- prova social inventada;
- "derechos de reventa" (licença só para o próprio negócio, E4).

## Build: stack, telas, dias até o MVP

**Stack:**

| Camada | Escolha |
|---|---|
| App | App novo no **Lovable** (stack padrão do Lovable), reaproveitando em nível funcional o fluxo do Mimo. Marca, domínio, página do Facebook, pixel/dataset, produtos Hotmart e dashboard UTMify **separados** do Mimo |
| Banco e auth | Supabase via Lovable Cloud, **backend novo**, com RLS por `user_id` (receitas são dado de negócio). **No D1, conferir que o projeto não aponta para o banco de outro produto** e que nenhum dado veio junto |
| Login | **Código OTP de 6 dígitos por e-mail**, sem magic link, porque o link abriria fora do navegador interno do Instagram. Limite de auth do Lovable Cloud **não verificado**: no Supabase com SMTP próprio, o padrão é 30 novos usuários/hora ([Supabase](https://supabase.com/docs/guides/auth/rate-limits)). Spike no D2; plano B: OTP próprio (código guardado com hash no banco), enviado pelo e-mail transacional do app |
| Arquivos | PDF, PNG e QR **gerados no aparelho**. Storage só para logos e fotos do catálogo (≤ 150 KB, caminho não adivinhável) |
| Pagamento | Hotmart: front + 4 bumps, checkout em lightbox. **Checkout próprio, com o botão bloqueado se a oferta não estiver configurada.** Principal como "Curso Online" com 2 aulas; bumps como "Imagem/Foto" |
| Liberação | Webhook Hotmart v2 novo: responde 200 sempre, idempotente por `transaction`. **Direito por e-mail** na tabela `licenses` (front → `expires_at` = aprovação + 365 d; B1 → `null`; B2/B3/B4 → flags). **Allowlist de product IDs; produto fora dela só é registrado.** Reembolso do front revoga tudo; o de um bump, só a flag dele. OXXO fica pendente |
| Atribuição | UTMify (dashboard novo); o parâmetro de rastreio do checkout leva um prefixo próprio da calculadora, o id do rascunho e a variante do A/B; Meta CAPI com dataset novo |
| E-mail | E-mails transacionais: acesso, código, pagamento pendente, carrinho abandonado, "tu resultado" e aviso de vencimento 30 e 7 d antes |
| IA e vídeo | **Nenhum no produto** (custo zero por uso) |

**Telas:**
1. Landing `/es` e `/es/<oficio>`: vídeo de tela, CTA "Calcula tu primer producto gratis" e FAQ.
2. Onboarding: ofício + país, em 2 toques.
3. "Tu primer producto": nome, rendimento, foto opcional.
4. Editor grátis: ingredientes, empaque, tempo, gastos %, margem (slider), com resultado ao vivo.
5. Resultado ("aha"): "Tu torta te cuesta $X por porción. **Con 40% de margen**, véndela a $Z", mais "¿A cuánto la vendes hoy?". **O build trazia "Para ganar 40%"**, que viola a regra do próprio build e aparece em anúncio e landing: trocar.
6. Prévia do pago com "VISTA PREVIA", o que a licença inclui (12 meses, até 200 produtos) e o que cada bump faz. Sem timer nem preço riscado.
7. Checkout Hotmart (lightbox) com 4 bumps e e-mail pré-preenchido.
8. Obrigado: código de 6 dígitos → importa o rascunho → painel; aviso de OXXO pendente.
9. "Mis productos": custo, preço, margem com semáforo, duplicar, aviso de margem baixa.
10. Livro de ingredientes: editar um preço → "Se actualizaron 7 productos".
11. Exportar: lista PNG + texto para WhatsApp; ficha técnica em PDF.
12. Ajustes do negócio: nome, logo, WhatsApp, valor da hora, gastos %, arredondamento.
13. Entrega dos bumps no painel (selo "para siempre", cartões desbloqueados).
14. B2, editor do catálogo: produtos, fotos (≤ 30), mensagem, QR para imprimir.
15. B2, catálogo público (página própria de cada negócio): "Arma tu pedido" → `wa.me`; rodapé "Hecho con {marca}" e "Reportar". Nunca mostra custo nem margem.
16. B3, orçamentos: cliente, data, itens, sinal %, validade → PDF + texto.
17. B4, mensagens prontas com "Copiar".
18. Entrar / recuperar acesso / Termos / Privacidade / Licença; admin com os golden tests, licenças, A/B e eventos Hotmart.

**Cronograma (uma pessoa, D1 = 23/09/2026) [estimativa]:**

| Dia | Entrega | Pronto quando |
|---|---|---|
| D1 | **Criar front + 4 bumps na Hotmart** (entram em análise; é o caminho crítico). Projeto novo, checagem da configuração de ambiente, Knowledge, remoções, marca e domínio, webhooks separados por produto | Projeto só em ES, sem backend nem dados do Mimo |
| D2 | Motor + parse por país + unidades + 12 golden tests; spike de OTP (Gmail, Outlook/Hotmail, Yahoo, < 1 min) | Testes verdes; OTP entregue nos 3 provedores |
| D3–D4 | Onboarding, editor, resultado ao vivo, modo grátis em `localStorage`, configs de ofício | 1º produto completo no celular, testado em ARS e MXN |
| D5 | Schema + RLS + login + importação do rascunho + painel + livro de ingredientes | Trocar 1 insumo atualiza N produtos; a conta B não lê a conta A |
| D5–D7 | **Portão obrigatório** (a oferta e o red team discordam do "opcional" do build): landing + calculadora grátis no ar, 3 criativos, US$ 60–100, com "Guardar" levando a uma lista de espera honesta. Decide pelos gates K1–K3 | Go/no-go antes de B2/B3 |
| D6 | Exportar lista PNG + texto + ficha PDF; tela de prévia | PNG legível no estado; PDF sem cortes |
| D7 | Checkout + webhook (licenças, flags, reembolso, OXXO, allowlist), A/B, UTMify, CAPI | Compra de teste libera tudo, inclusive bump antes do front |
| D8 | B2 catálogo | O pedido chega no WhatsApp com itens e total certos |
| D9 | B3 + B4 (só texto) + ajustes + aviso de vencimento + PWA | Orçamento em PDF; mensagens preenchidas |
| D10 | Landings, FAQ, termos, licença, e-mails, admin | Textos sem promessa de renda |
| **D11** | **QA de ponta a ponta:** compra real em 2 países + OXXO; reembolso → bloqueio; navegador interno do Instagram/Facebook no iOS e no Android; números AR × MX; golden tests. **MVP vendável (03/10)** | — |
| D12 | Negócios de exemplo marcados "Ejemplo", gravações de tela, fábrica de criativos | 12–16 variações prontas |
| D13 | Soft launch (05/10) | Primeiras vendas liberadas sem intervenção |
| D14 | Folga (06/10) | — |

- **Correção do red team:** a pesquisa estimava 4–6 dias e dizia que o teste só se justificava com build ≤ 5 d. O plano real tem 11 dias até o vendável, com OTP, RLS, licenças, catálogo público, cotizador, A/B e PWA. **Pelo critério da própria pesquisa, o teste não se justifica**, e "build fácil" não descreve o escopo.
- **Pedido da fábrica de criativos (~0,5–1 dia, estimativa):** exportar o motor, o formatador numérico e os componentes do cartão de resultado e da lista de preços para o Remotion (ou uma página de demonstração), e incluir as receitas de exemplo dos anúncios nos golden tests.

**Ordem de corte se atrasar:**
1. B3 → v1.1;
2. landings por ofício → 1 landing com chips (`?oficio=`);
3. "Arma tu pedido" do B2 → botão único "Pedir por WhatsApp";
4. Velas e Tejido fora;
5. A/B → preço único de US$ 6,90;
6. PWA e e-mails de vencimento → v1.1.

**Nunca cortar:**
- motor com golden tests e parse por país;
- OTP no mesmo navegador;
- webhook 200-sempre, idempotente, com allowlist;
- reembolso → bloqueio;
- vencimento de 12 meses aplicado e informado (sem ele, o B1 é vazio);
- RLS testada com 2 contas;
- landing sem promessa de renda, timer ou preço riscado.

**Separação por produto (antes do D7).** Os produtos, os webhooks e o fluxo de liberação da calculadora são separados por produto: cada venda libera só o produto comprado. Configurar webhooks por produto (se a Hotmart permitir filtro, **não verificado**) e usar um prefixo próprio no parâmetro de rastreio do checkout. Boa prática de segurança: recuperar acesso sempre com código enviado ao e-mail.

**Custo marginal por venda [estimativa]:** ~US$ 0,005–0,03 no 1º ano (banco ~0,001; banda do catálogo 0,005–0,016; e-mails 0–0,008); pior caso ~0,2–0,5 com catálogo muito visitado. O preço por GB do Lovable Cloud não é publicado. Diferente do Mimo, **o custo é recorrente**, porque o cliente usa o app por meses. Calibrar pela fatura do Cloud ÷ usuários ativos no mês.

**Riscos técnicos que viram reembolso:**
- parse numérico por país ("1.500");
- confusão entre margem e markup;
- OTP no navegador interno e caindo no spam (Hotmail/Yahoo);
- limite de auth no pico de lançamento;
- venda liberando o produto errado (erro de configuração de webhook);
- projeto novo herdando dados de outro produto;
- RLS mal feita;
- regressão no motor ou no webhook causada pelo agente do Lovable;
- demora na aprovação da Hotmart.

## Criativo: 15 ganchos em espanhol, 5 formatos, 30 variações/semana

**Princípio.** O anúncio mostra três momentos do produto:
1. a pessoa digita o que comprou e o que usou;
2. aparecem o custo por porção, o preço sugerido e a margem;
3. ela digita "a cuánto lo vendes hoy", e a margem atual aparece em **vermelho** ao lado da sugerida em **verde**.

O fecho é a lista de preços se montando com o nome do negócio, ou o aviso "Se actualizaron 7 productos". Três dos cinco formatos são só demonstração. Os outros dois usam uma **apresentadora virtual com o rótulo "Presentadora virtual · IA"**, que demonstra a tela e nunca finge ser confeiteira nem cliente. **Nenhum criativo mostra o nosso preço** enquanto o A/B roda. Todo valor em dinheiro na tela é **por unidade/porção**, de uma receita de exemplo com o selo "Ejemplo · precios de ejemplo", e **sai do motor do app**, nunca digitado à mão.

**O que os títulos longevos dizem [medido; proxy], com a correção do red team.** Em 5 páginas ES há 37 anúncios com ≥ 30 d. Por ângulo: entregável nomeado ("Descarga tu plantilla", "Calculadora … PRO") 16; margem/rentabilidade 7; pergunta por ofício ("¿Estás cobrando bien por tus postres?") 6; custo real 3; "adivinar"/perdas 2; click-to-chat 2; tempo 1.
- **22 desses 37 são de uma página B2B que vende Excel para restaurante** (Fer Rendon), e 6 são da Chef Anna, com produto não identificado. **A transferência para a confeiteira de casa não foi verificada.**
- **O "ângulo mais provado" é 1 anúncio.** O "¿Estás cobrando bien por tus postres?" da Chef Anna tem 119,2 d, mas os outros 16 anúncios dela têm 76,2 d (1), 60,0 d (3), 32,2 d (1), 28,0 d (1), 14,7–18,0 d (8) e 1,1 d (2).
- **O criativo dizia que nenhum título com ≥ 30 d usa "ganas" ou "ingresos". Isso não se sustenta:** "…y mejora tus ganancias 📊" tem 49,7 d ([Fer Rendon](https://www.facebook.com/ads/library/?id=1712957136670895)); "Calcula el costo real de tu menú y mejora tus ganancias", 38,5 d ([link](https://www.facebook.com/ads/library/?id=1389106856011395)); "Calcula y gana más", 216,7 d ([Pau Regalos](https://www.facebook.com/ads/library/?id=1232865344959275), Fase 3). A leitura correta é que a maior parte da longevidade está em clareza de produto e de custo. O ângulo de renda é proibido para nós de qualquer forma.

**15 ganchos (0–3 s).** Regras: texto de tela com até 8 palavras; nunca quanto a pessoa vai ganhar; nada de "gana", "ganancias", "ingresos", "emprende" ou "desde casa"; nenhuma marca de terceiro (nem "Excel"); `{producto}` troca por ofício e país. O frame 0 de cada gancho está nas notas de trabalho privadas, fora do repositório.

| # | Ângulo | Texto de tela (ES) | Voz 0–3 s (ES) | Evidência / condição |
|---|---|---|---|---|
| H01 | Ofício · pergunta | ¿Cobras lo justo por tus {pasteles}? | "¿Cobras lo justo por tus {pasteles}? Míralo aquí." | Estrutura do anúncio de 119,2 d da [Chef Anna](https://www.facebook.com/ads/library/?id=1276480471319495) (1 anúncio; produto não identificado). Texto próprio, sem copiar o título |
| H02 | Demo | Pon tus ingredientes. Mira tu precio. | "Pones lo que compraste y te sale el precio." | "Define precios conociendo el costo real de tus recetas", 38,5 d ([Fer Rendon](https://www.facebook.com/ads/library/?id=1378962954379131), B2B) |
| H03 | Custo escondido | El costo que no ves en tu receta | "Hay costos que no están en tu receta." | "Deja de adivinar tu food-cost", 41,1 d ([Cuentas Claras](https://www.facebook.com/ads/library/?id=1696683294754899)); só a frase "Deja de regalar tu trabajo" do [Pau Regalos](https://www.facebook.com/ads/library/?id=1232865344959275) |
| H04 | Recálculo | Subió el huevo. ¿Y tus precios? | "Subió el huevo. Mira qué pasa con tus precios." | **Exploração**, sem longevidade medida. No MX: "Subió el precio del huevo" (duplo sentido); na AR: "Aumentó la harina" |
| H05 | Entregável | Tu lista de precios, lista para tu estado | "Tu lista de precios, con tu nombre, lista." | Entregável nomeado é o ângulo mais longevo (com o peso B2B acima). Mostrar só a imagem gerada, nunca a interface do WhatsApp |
| H06 | Objeção: números | Sin fórmulas y sin hojas de cálculo | "Sin fórmulas ni hojas de cálculo. Desde el celular." | "Controlá tu pastelería desde el celular", 42,9 d ([Dolchere](https://www.facebook.com/ads/library/?id=2131547987779501)). Nunca citar "Excel" |
| H07 | Objeção: assinatura | Pago único. Sin mensualidades. + "Acceso por 12 meses" | "Pagas una vez. Sin cobros cada mes." | "Único Pago S/. 19" ([link](https://www.facebook.com/ads/library/?id=1089104103530989)). **A linha "Acceso por 12 meses" é obrigatória** |
| H08 | Objeção: grátis | Calcula gratis tu primer producto | "Tu primer producto lo calculas gratis. Mira." | Verdadeiro no build. Se o anúncio mostrar a lista (paga): "Lista y guardado en la versión completa" |
| H09 | Data | Día de la Madre: ¿ya tienes tus precios? | "Día de la Madre: ¿ya calculaste tus precios?" | AR 18/10 ([LA NACION](https://www.lanacion.com.ar/sociedad/cuando-es-el-dia-de-la-madre-2026-en-la-argentina-nid22092026/)), só de 1 a 15/10, com voseo ("¿ya tenés…?"); MX/PE/CL/GT 10/5, de 15/4 a 5/5 ([Milenio](https://www.milenio.com/negocios/pastelerias-en-torreon-incrementan-ventas-el-dia-de-las-madres)). A data é da temporada de pedidos, nunca prazo de oferta |
| H10 | Temporada | {Navidad}: calcula tus precios antes de los pedidos | "Antes de los pedidos de {Navidad}, calcula tus precios." | Pan de muerto (MX, 12–28/10), Navidad (15/10–20/11), Rosca (MX, 15/12–4/1), San Valentín (20/1–7/2) |
| H11 | Ofício: comida | ¿Cuánto te cuesta cada {empanada}? | "¿Cuánto te cuesta cada {empanada}? Sácalo aquí." | "PLANTILLA GASTRONÓMICA PRO", 91,9 d ([Emprendedores Digitales](https://www.facebook.com/ads/library/?id=1047240127991578)); "…tus comidas?", 28,0 d ([Chef Anna](https://www.facebook.com/ads/library/?id=1068204112335166)). `{empanada}` = tamal, menú, vianda, almuerzo |
| H12 | Encomenda | Te piden un pastel para 40. ¿Cuánto cobras? | "Te pidieron un pastel para cuarenta… ¿cuánto cobras?" | "Hacé tus presupuestos en minutos", 11,0 d. **Exploração.** O PDF do B3 só aparece como "Opcional" |
| H13 | Uso próprio | ¿Cuánto te cuesta tu pastel casero? | "¿Sabes cuánto te cuesta de verdad tu pastel?" | Sem evidência; ≤ 1 por semana, para medir se atrai quem não vende |
| H14 | Contraste | 30% más no es 30% de margen | "Sumarle 30% no te da 30% de margen." | Fato aritmético: 0,30 ÷ 1,30 = 23,1% de margem. "Sube tu margen, platillo por platillo", 41,1 d ([Cuentas Claras](https://www.facebook.com/ads/library/?id=1049958477946465)) |
| H15 | Artesanato | Velas: cera, frasco, mecha… y tu tiempo | "¿Cuánto cobrar por tus velas? Suma también tu tiempo." | **Sem sinal de demanda.** Só com o ofício no ar, ≤ 1 por semana. Variante: "Amigurumi: hilo, relleno, ojitos… y tu tiempo" |

**Variantes por país.** Vocabulário regional ([GASDA](https://gasda.com.ar/como-se-dice-pastel-en-cada-pais/)). No MX, "torta" é sanduíche ([Larousse Cocina](https://laroussecocina.mx/palabra/torta/)). Ingredientes por país não verificados um a um.

| Locale | Tratamento | Bolo | Ingredientes (exemplos) | Número | H01 |
|---|---|---|---|---|---|
| es-MX (GT, US) | tú | **pastel** (nunca "torta") | mantequilla, azúcar glass, fécula de maíz | $1,250.50 | "¿Cobras lo justo por tus pasteles?" |
| es-AR / es-UY | vos | torta | manteca, azúcar impalpable, crema de leche | $1.250,50 | "¿Cobrás lo justo por tus tortas?" |
| es-CO | tú | torta / ponqué | mantequilla, crema de leche | $12.500 | "¿Cobras lo justo por tus tortas?" |
| es-PE | tú | torta / queque | mantequilla | S/ 12.50 | idem |
| es-CL | tú | torta / queque | mantequilla, azúcar flor | $12.500 | idem |

Ingredientes sempre genéricos: "fécula de maíz", não "Maizena"; "leche condensada", não "La Lechera".

**Texto do anúncio (ES), sem o nosso preço:**
- **A (demo):** "Pones lo que compras y lo que usas. Te muestra cuánto te cuesta cada porción, un precio sugerido y tu margen. El primer producto lo calculas gratis y sin registrarte. Con la versión completa guardas todos tus productos, se actualizan solos cuando sube un ingrediente y armas tu lista de precios con el nombre de tu negocio. Pago único · acceso por 12 meses."
- **B (custo escondido):** "El empaque, el gas y tu tiempo también cuestan. Los pones una vez y la calculadora los suma en cada producto. Tú decides el precio: te mostramos el mínimo, el sugerido y tu margen."
- **Títulos:** "Calcula gratis tu primer producto" · "Tu precio, con tus números" · "Costo por porción, desde el celular". Botão: "Más información", com destino na landing do mesmo ofício.

**5 formatos.** Todos em 9:16 (1080×1920, 30 fps), com versão 4:5 no mesmo anúncio. Áudio da gravação sempre mudo; trilha licenciada; **sem som de caixa registradora**.

| # | Nome | Duração | Rosto | Estrutura | End card |
|---|---|---|---|---|---|
| F1 (C1) | "Del ingrediente al precio" | 13–15 s (corte de 10 s) | Não | Gancho → editor acelerado 2× com selo → rendimento + empaque, gás e tempo → resultado contando → margem de hoje em vermelho × sugerida em verde | "Calcula gratis tu primer producto" |
| F2 (C2) | "Subió un insumo" | 12–15 s | Não | Gancho → livro de ingredientes, o preço do ovo muda → "Se actualizaron 7 productos" → 2 produtos em âmbar/vermelho → preço novo ao lado do antigo | + linha pequena "Guardado y recálculo en la versión completa" |
| F3 (C3) | "Tu lista de precios" | 15–18 s | Não | Gancho → painel com 6 produtos → "Exportar lista" com "Dulces de Casa · Ejemplo" → imagem final parada 2 s (telefone "000 000 0000") → catálogo só se o B2 estiver no ar | Corte em "Imagen guardada ✓", nunca na folha de compartilhar |
| F4 (C4) | "Presentadora virtual: te muestro" | 20–25 s | IA rotulada | Close com o gancho → ela vira um círculo no canto superior enquanto roda o C1 → close final "El primer producto lo calculas gratis" | Fala "te muestro", "con [Marca]". Sem avental, dólmã, nome de persona ou "mi pastelería" |
| F5 (C5) | "Tres dudas" | 25–30 s | IA rotulada | 3 de 6 dúvidas sorteadas: ¿y si hay gratis? / ¿es suscripción? / ¿sirve con mi moneda? / ¿kilos y gramos? / ¿necesito computadora? / ¿cómo entro después de pagar? | "Pago único, acceso por 12 meses. El primer producto, gratis." Serve para frio e remarketing (`recipe_completed`) |

Os formatos com IA ficam em ~1/5 do volume (teto de 8 por semana): a Meta põe o rótulo "AI info" ([Meta](https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/)); um estudo mediu queda de 31,5% no CTR com aviso de IA ([NYU Stern](https://www.stern.nyu.edu/experience-stern/faculty-research/ai-advertising-paradox)) e outro não achou efeito ([MediaScience](https://www.marketingdive.com/news/ai-disclosure-labels-dont-hurt-ad-performance-heres-what-the-numbers-say/822711/)).

**30 variações por semana.** Os módulos:
- 15 ganchos, mais ~3 novos por semana, tirados dos comentários e dos títulos novos dos concorrentes (checar por `page_ids` toda segunda);
- 5 corpos;
- ofícios REP, COM (VEL e TEJ condicionais);
- 9 receitas de exemplo (PCH, CUP, GAL, EMP, TAM, MEN, PIZ, VFR, AMI);
- 6 locales (MX, AR, CO, PE, CL, US);
- com ou sem apresentadora.

São ~28 pares úteis de gancho × ofício, ~130 com os corpos e ~330 com as receitas antes do país [estimativa]. **O limite é gancho, não combinação.**

| Semana 1 (S41, 05–11/10), bloco | Nº | Anúncios |
|---|---|---|
| Exploração de gancho no C1 | 12 | H01 (REP, COM), H02, H03, H06, H07, H08, H11, H12, H13, H14 (REP, COM), no MX |
| Recálculo (C2) | 4 | H04 (REP, COM), H03, H02 |
| Lista (C3) | 4 | H05 (REP, COM), H01, H08 |
| Apresentadora (C4) | 3 | H01, H14, H03 |
| Dúvidas (C5) | 3 | H08, H07, H06 |
| Data e localização | 3 | H09 AR no C1 e no C3 (voseo, "tortas", ARS); H11 PE (menú del día) |
| Artesanato | 1 | H15 VEL, só se o ofício estiver no ar; senão, H01 COM CO |

**Da semana 2 em diante:** 6 de iteração de gancho (o melhor anúncio com 6 ganchos novos) · 6 de iteração de corpo · 6 de exploração · 4 de fadiga (outra receita ou outro modelo de lista, só re-render) · 4 de localização/ofício · 4 de data (fora de janela, voltam para exploração).

**Ressalva do red team:** com os US$ 60–100/dia do teste, cada um dos 30 anúncios recebe ~US$ 2–3/dia, e a Meta concentra a entrega em poucos [inferência]. **"30 variações testadas por semana" é otimista**: na fase de teste, subir as 30 mas ler só as que receberem entrega.

**Pipeline (detalhes e comandos nas notas de trabalho privadas, fora do repositório):**
- **Nível 1:** gravação nativa da tela de um celular real, 4 clipes por receita × locale numérico (MX e AR), ~72 clipes em ~4 h.
- **Nível 2 (pedido ao build):** o Remotion desenha as telas com os componentes e o motor do próprio app, e trocar país ou moeda vira só re-render. Conferir lado a lado com um print real.
- **Preços das receitas de exemplo:** anotados num site de supermercado do país, com fonte e data no JSON da fixture; margem padrão de 30–40%.
- **Voz e legenda:** TTS por locale (sem clonar voz real); legenda queimada (`@remotion/captions`).
- **Apresentadora:** um rosto sintético genérico, checado por busca reversa, sem remover C2PA/IPTC.
- **Trilha:** Meta Sound Collection (termos lidos só via resumo de busca), com o ID de cada faixa no CSV.
- **Validação automática** no script que monta os dados de cada render, que barra "gan…", "ingreso", "emprend", "desde casa", total por período, urgência, "Excel", "para siempre" sem o B1, "pago único" sem "acceso por 12 meses", "torta" em es-MX e valores que não batem com o motor.
- **Render** H × C em segmentos, concatenados com ffmpeg, com ducking e loudness.

**QA antes de subir.** Qualquer "sim" barra o anúncio:
1. Algum ganho, "ingresos", "emprende" ou total por período?
2. Valor sem o selo "Ejemplo" ou que não bate com o motor?
3. Urgência falsa?
4. IA sem rótulo, falando como confeiteira ou com nome de persona?
5. Marca de terceiro ou interface do WhatsApp?
6. Personagem licenciado?
7. "Pago único" sem os 12 meses, ou função paga mostrada como grátis?
8. "Torta" em es-MX?
9. Atributo pessoal?
10. Promessa de tempo não medida, ou "tazas" antes da v1.1?
11. Telefone ou nome de negócio que possa ser real?
12. URL de outro ofício?

**Nomenclatura para o UTMify:**
- campanha `CAL_{OBJ}_{AAWW}`;
- conjunto `CAL_{OF}_{PAIS}_{PUBLICO}`;
- anúncio `CAL_{H}_{C}_{OF}_{FX}_{LOC}_{PRES}_W{AAWW}_v{n}` (ex.: `CAL_H04_C2_REP_PCH_MX_NA_W2641_v1`).

Parâmetros de URL padrão do UTMify. A variante de preço vai no parâmetro de rastreio do checkout, não no nome, e anúncio no ar não se renomeia.

**Regras de pausa por anúncio, na régua BRL do cenário base.** As versões anteriores usavam o cenário conservador do build com 3 bumps.
- **Pausar com gasto ≥ 2× o CPA-alvo sem venda: US$ 8,62 a 7,90 (2 × 4,31) ou US$ 6,58 a 5,90 (2 × 3,29).** Um anúncio exatamente no alvo tem 13,5% de chance de zero venda nesse gasto (Poisson, média 2): ~1 em 7 anúncios bons morre por azar.
- **Gasto mínimo para descartar os 30:** ~US$ 197–259. O criativo chamava isso de "teto de perda", mas **não é teto**, porque todo anúncio com 1 venda continua gastando.
- Pausar também com CTR de link < 0,7× a mediana da semana depois de 3.000 impressões.
- Vencedor provisório: ≥ 3 vendas com CPA ≤ 4,31. É sinal de direção, não prova.

**Calendário:**

| Semanas | Datas | Criativo |
|---|---|---|
| S40 | 28/09–04/10 | Portão: só C1, **sem lista, recálculo, "pago único" nem "12 meses"** (ainda não existem) |
| S41–S42 | 05–18/10 | Lançamento. AR: H09 até 15/10 (otimista: ver a última seção). MX/PE: H01, H11, H02. Pan de muerto a partir de S42 |
| S43–S47 | 19/10–22/11 | H10 "Navidad" em todos os países |
| S48 | 23–29/11 | Black Friday: não escalar nem subir teste |
| S49–S52 | 30/11–27/12 | Só vencedores; Rosca (MX) a partir de 15/12 |
| S53–S06 | 28/12/2026–14/02/2027 | Escalar vencedores (CPM mais barato: 40–60% menor até ~15/01, dados dos EUA, LATAM não verificado; [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [Clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics)); H04 e "Empieza el año con tus números claros"; San Valentín. **Nunca "cuesta de enero"** |
| S16–S18 (2027) | 15/04–05/05 | Maior pico: Día de la Madre MX, PE, CL, GT |

## Ângulos proibidos

Valem para o vídeo, o texto, o título, a landing, a página da Hotmart e as telas do app que aparecem nos anúncios. A Meta revisa o destino, e produto do anúncio diferente do da página é [burla de sistemas](https://transparency.meta.com/km-kh/policies/ad-standards/deceptive-content/circumventing-systems).

| Não pode | Exemplo proibido (ES) | Motivo | Reescrita segura (ES) |
|---|---|---|---|
| Promessa de renda, valor de ganho ou total por período | "Calcula y gana más 💰" ([Pau Regalos](https://www.facebook.com/ads/library/?id=1232865344959275), 216,7 d); "💰 Generá ingresos reales" ([Dolchere](https://www.facebook.com/ads/library/?id=1886078219071457)); "Vende 50 empanadas y gana $3,000 a la semana" | [Resultados irreais (Meta)](https://transparency.meta.com/en-gb/policies/ad-standards/deceptive-content/unrealistic-outcomes/); [uso responsável (Hotmart)](https://hotmart.com/en/legal/responsible-use-policy). Estar no ar há meses não prova que é permitido | "Mira cuánto te cuesta cada empanada y a cuánto venderla." |
| "Ganancias"/"gana" mesmo no sentido de margem | "…y mejora tus ganancias 📊" ([Fer Rendon](https://www.facebook.com/ads/library/?id=1712957136670895), 49,7 d); "¿CUÁNTO GANAS REALMENTE POR CADA MENÚ…?" ([link](https://www.facebook.com/ads/library/?id=1475097697788648)); "Asegura tu ganancia antes de temporada alta" ([Latinas Together](https://www.facebook.com/ads/library/?id=1442397034654894)); tela do build "Para ganar 40%" | Puxa para oportunidade econômica (digest de políticas); a regra do próprio build proíbe "gana" na interface | "Con 40% de margen, véndela a $Z"; "Mira tu margen por producto" |
| "Emprende", "negocio desde casa", "ingresos extra" | "Hoy arrancás tu emprendimiento 🎂" ([Dolchere](https://www.facebook.com/ads/library/?id=1092823393187578)); "Tu cocina, Tu negocio." ([link](https://www.facebook.com/ads/library/?id=4474952049433628)) | [Fraude e golpes (Meta)](https://transparency.meta.com/policies/ad-standards/fraud-scams/fraud-scams-deceptive-practices/); eliminatória E2 | "Para quien ya vende postres o comida." |
| Print de ganho, notificação de venda, som de caixa | "Nuevo pedido 🔔 $850" | [Funcionalidade inexistente](https://www.facebook.com/business/help/655450495896770) | Painel com "Ejemplo": custo, preço e margem por unidade |
| Números de exemplo irreais | Margem de 80%; "antes cobraba $30, ahora $60" | Resultado irreal; publicidade "veraz y comprobable" (art. 32 da [LFPC](https://www.profeco.gob.mx/juridico/pdf/l_lfpc_ultimo_camdip.pdf)) | Preços anotados de supermercado, margem de 30–40%, "precios de ejemplo" |
| Depoimento inventado | "Majo subió sus precios y ahora le alcanza ⭐⭐⭐⭐⭐" | [FTC (2024)](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials) para o público US; LFPC no MX | "Cambias un precio y se actualizan todos" |
| Avatar de IA como cliente, confeiteira ou especialista | "Yo tenía mi pastelería y cobraba mal…"; "Chef Ana" de dólmã; "Te lo dice una contadora" | Enganoso (digest de políticas; FTC) | "Te muestro cómo calcular el costo con [Marca]", com rótulo de IA |
| Rosto parecido com famoso; cenário de telejornal | Avatar "inspirado" numa confeiteira de redes | Isca de celebridade ([Meta 2024](https://about.fb.com/news/2024/10/testing-combat-scams-restore-compromised-accounts/), [Meta 2026](https://about.fb.com/news/2026/02/meta-takes-legal-action-against-scam-advertisers/)) | Rosto sintético genérico checado por busca reversa; mesa neutra |
| Prova social ou autoridade sem base | "Miles de reposteras ya la usan"; "La calculadora #1"; "Aprobada por contadores" | Precisa ser comprovável (art. 32 da LFPC) | "Hecha para quien vende postres y comida." |
| Escassez ou urgência falsa | "Ultimas Horas!" ([Dolchere](https://www.facebook.com/ads/library/?id=924813996978839)); "Solo hoy por $5" ([Dulce Gestion](https://www.facebook.com/ads/library/?id=1668745884875469)); preço riscado sem preço anterior real. Se os deles são falsos: não verificado | [Profeco multa ofertas falsas](https://www.infobae.com/mexico/2026/05/28/las-ofertas-falsas-saldran-caras-profeco-aplicara-multas-a-negocios-infractores-hasta-por-6-millones-de-pesos/) | "Antes de los pedidos de Navidad, calcula tus precios." |
| Personagens licenciados em bolo, fixture ou B-roll | "Pastel de Frozen · $450" na lista | [Copyright e marcas (Meta)](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/copyright-and-trademarks/). Na confeitaria, o risco maior está no B-roll e nos nomes das fixtures | "Pastel temático infantil", decoração lisa |
| Marcas de terceiros | "Sin Excel", "Mejor que Excel"; "Maizena", "Nutella"; logo ou interface do WhatsApp; "mejor que Dolchere" | [PI de terceiros](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/third-party-infringement/); [marca WhatsApp](https://www.meta.com/brand/resources/whatsapp/whatsapp-brand/). Uso nominativo de "Excel": não verificado, cortado por prudência | "Sin fórmulas ni hojas de cálculo"; "para tu estado de WhatsApp" só em texto |
| Atributo pessoal | "¿No te alcanza con lo que vendes?"; "Mamá, ¿vendes postres para salir adelante?"; "Cuesta de enero: ajusta tus precios" | [Atributos pessoais (Meta)](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/) | "¿Sabes cuánto te cuesta cada porción?"; "Empieza el año con tus números claros." |
| "Sin esfuerzo" e tempo não medido | "En 1 minuto", "se calcula solo". A meta de < 3 min do build não foi medida | Enriquecimento rápido; tempo não "comprobable" | "Paso a paso, desde el celular." "En minutos" só depois de medir no QA |
| Função que o produto não tem (ou não tem no grátis) | "Convierte tazas a gramos"; "Acceso para siempre" sem o B1; lista ou recálculo como se fossem grátis; "Pago único" sem os 12 meses | Publicidade enganosa; produto do anúncio ≠ página | "Pago único · acceso por 12 meses"; "Primer producto gratis. Guardado, recálculo y lista en la versión completa." |
| Interface falsa | "Toca aquí 👆", play desenhado, chat falso de cliente | [Funcionalidade inexistente](https://www.facebook.com/business/help/655450495896770) | A mão toca dentro do vídeo |
| Deriva para "receitas que vendem" | "Recetas que se venden", "Postres que rentan" | Risco Meta e Hotmart MÉDIO (digest) | Receita só como exemplo de cálculo |
| Dados reais de terceiros | Lista ou preços de uma cliente real | Privacidade (lei por país não verificada) | "Dulces de Casa · Ejemplo", telefone "000 000 0000" |
| Esconder que é IA | Remover C2PA, recortar o rótulo | [Transparência de IA](https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/) | Rótulo na tela + marcação no Gerenciador |
| Copiar título de concorrente (regra do projeto) | "¿Estás cobrando bien por tus postres? 📊" literal | Confunde com a Chef Anna | "¿Cobras lo justo por tus pasteles?" |

## Contas (definição de ROI explícita; AOV, líquido, reembolso, CPA de break-even, CPA para ROI 1,5)

**Definição de ROI:** faturamento líquido (depois das taxas da Hotmart e dos reembolsos) ÷ gasto em anúncios.
- CPA de break-even = líquido por comprador (ROI 1,0).
- CPA para ROI 1,5 = líquido ÷ 1,5.
- **Com conta de anúncio em BRL** (o UTMify soma 12% de imposto ao gasto; é a régua provável): break-even = líquido ÷ 1,12; ROI 1,5 = líquido ÷ 1,68.

**Taxas (modelo do usuário, `_raw/calc_economia.py`):**
- **Front:** 10,95% + US$ 1,49. A 7,90 sobram 5,54 (70,2%); a 5,90, 3,76 (63,8%); a 4,90, 2,87 (58,6%).
- **Bumps:** 88% líquido.
- **Reembolso:** aplicado sobre o líquido total. Se a Hotmart não devolver as taxas no reembolso (não verificado), a perda é um pouco maior.
- **Upsell:** calculado com a taxa do front; a 7,90 deixa 5,55.

**Reembolso estimado para o nicho.** Não há benchmark público de reembolso de low ticket na Hotmart; os números são julgamento, ancorados no Mimo (< 1%) e nos outros finalistas (3% no base).
- **Por que acima do Mimo:** arrependimento por esforço (o valor só aparece depois de digitar os insumos); descoberta posterior de uma calculadora grátis; erro de cálculo percebido (formato numérico); 4 bumps; confusão com a licença de 12 meses; desconfiança da categoria ("Hotmart es estafa", digest).
- **Por que abaixo da renda extra:** não há promessa de ganho; o resultado aparece antes de pagar; o ticket é baixo.

| Cenário | Reembolso |
|---|---|
| Conservador | 6% |
| **Base** | **4%** |
| Otimista | 2% |
| Cético (red team) | 6%, com só o B1 a 15% |

**Front US$ 7,90 (regime de taxas R1).** Adesões e reembolso são estimativas, não verificadas.

| US$ por comprador de front | Conservador | **Base** | Otimista | Cético | Sem bumps |
|---|---|---|---|---|---|
| Adesão B1 / B2 / B3 / B4 | 15 / 8 / 4 / 4% | 24 / 12 / 7 / 6% | 33 / 16 / 10 / 9% | 15 / 0 / 0 / 0% | — |
| Reembolso | 6% | 4% | 2% | 6% | 6% |
| **AOV bruto** (front + bumps) | 9,34 | **10,17** | 11,04 | 8,63 | 7,90 |
| Líquido do front | 5,54 | 5,54 | 5,54 | 5,54 | 5,54 |
| Líquido dos bumps | 1,27 | 2,00 | 2,77 | 0,65 | 0 |
| **Líquido por comprador** | **6,40** | **7,24** | **8,14** | **5,82** | **5,21** |
| CPA de break-even, sem imposto / BRL | 6,40 / 5,71 | **7,24 / 6,46** | 8,14 / 7,27 | 5,82 / 5,20 | 5,21 / 4,65 |
| CPA para ROI 1,5, sem imposto | 4,27 | **4,83** | 5,43 | 3,88 | 3,47 |
| **CPA para ROI 1,5, BRL** | **3,81** | **4,31** | **4,85** | **3,46** | **3,10** |
| *Com upsell (v1.1; 3 / 5 / 8%): líquido* | *6,56* | *7,51* | *8,57* | — | — |
| *Com upsell: CPA ROI 1,5, sem imposto / BRL* | *4,37 / 3,90* | *5,00 / 4,47* | *5,72 / 5,10* | — | — |

Conta do cenário base:
- Bumps: 4,90 × 0,24 + 4,90 × 0,12 + 3,90 × 0,07 + 3,90 × 0,06 = 2,271. AOV: 7,90 + 2,271 = 10,17.
- Líquido: 7,90 × 0,8905 − 1,49 = 5,54; mais 2,271 × 0,88 = 2,00; soma 7,54.
- Depois do reembolso: 7,54 × 0,96 = **7,24**.

A pesquisa (7,47) e o build (7,32) chegaram a números parecidos, com 3 bumps e premissas diferentes. **O número que vale é 7,24.**

**Front 5,90 e 9,90 (mesmos bumps e reembolsos):**

| Front | Líquido por comprador (cons. / base / otim.) | CPA de break-even BRL (base) | CPA ROI 1,5, sem imposto (base) | CPA ROI 1,5, BRL (cons. / base / otim.) |
|---|---|---|---|---|
| 5,90 | 4,73 / **5,53** / 6,40 | 4,94 | 3,69 | 2,82 / **3,29** / 3,81 |
| **7,90** | 6,40 / **7,24** / 8,14 | **6,46** | **4,83** | 3,81 / **4,31** / 4,85 |
| 9,90 | 8,08 / **8,95** / 9,89 | 7,99 | 5,97 | 4,81 / **5,33** / 5,89 |

**Sensibilidade ao preço do front (base):**

| Front | Líquido do front (% do preço) | Líquido por comprador | CPA ROI 1,5, BRL | Conversão para empatar com o 7,90 |
|---|---|---|---|---|
| 4,90 | 2,87 (58,6%) | 4,68 | 2,79 | 1,55× |
| 5,90 | 3,76 (63,8%) | 5,53 | 3,29 | 1,31× |
| 6,90 | 4,65 (67,5%) | 6,39 | 3,80 | 1,13× |
| 7,90 | 5,54 (70,2%) | 7,24 | 4,31 | 1,00× |
| 9,90 | 7,33 (74,0%) | 8,95 | 5,33 | 0,81× |
| 12,90 (US, 2ª rodada) | 10,00 (77,5%) | 11,52 | 6,85 | 0,63× |

A âncora de mercado (US$ 3–6) empurra o preço para baixo; a taxa fixa empurra para cima. Entre 7,90 e 4,90, o preço cai 38% e o líquido do front cai 48%.

**A taxa da Hotmart pode ter mudado em 21/09/2026 (não verificado).** Segundo o digest, a taxa do Player (os US$ 1,49 do modelo) teria sido absorvida numa taxa fixa por transação de US$ 1,00 ([Hotmart](https://help.hotmart.com/es/article/208298448/-cuales-son-las-tarifas-cobradas-por-hotmart-)). A microtransação (≤ US$ 15) era de 9,9% + 0,10.

| Regime | Front / cada bump | Líquido por comprador a 7,90 (cons. / base / otim.) | CPA ROI 1,5, sem imposto / BRL (base) | Líquido a 5,90 / 9,90 (base) |
|---|---|---|---|---|
| R1: modelo do usuário | 10,95% + 1,49 / 88% | 6,40 / **7,24** / 8,14 | 4,83 / 4,31 | 5,53 / 8,95 |
| R2: Player extinto, microtransação a 9,9% + 0,10 | 9,9% + 0,10 / igual | 7,79 / **8,65** / 9,59 | 5,77 / 5,15 | 6,92 / 10,38 |
| R3: taxa fixa de US$ 1,00 em toda transação, inclusive em cada bump | 9,9% + 1,00 / igual | 6,68 / **7,37** / 8,10 | 4,91 / 4,39 | 5,64 / 9,10 |

- **O R2 melhora o L29 em termos absolutos:** a régua BRL sobe para 5,15, e o 5,90 precisaria converter só 1,25× para empatar.
- **Correção do red team:** a oferta dizia que, no R2, o L29 chegaria "perto do Mimo". Ela comparava o L29 no R2 com o Mimo no R1. O Mimo também melhora no R2 pelo mesmo modelo, e **a razão L29/Mimo fica praticamente igual (~75–78%)** [estimativa]. O R2 não muda a posição relativa.
- **O R3 atinge os bumps de 3,90** (64% líquido): aplicar a contingência do Pack Pedidos.
- **Como confirmar:** abrir o detalhe da primeira venda real (front + bump) e ver a linha de taxa fixa em cada transação. Refazer a tabela antes de decidir o A/B.

**Variantes (base, R1):**

| Variante | Líquido por comprador | CPA ROI 1,5, sem imposto / BRL | Nota |
|---|---|---|---|
| AR em USD, produtor paga 9,5% da conversão (não verificado quem paga) | 6,31 (7,90) · 4,79 (5,90) | 4,21 / 3,76 · 3,19 / 2,85 | Perda = 9,5% × AOV bruto antes do reembolso |
| Front vitalício, sem o B1 | 6,25 | 4,17 / 3,72 | Só compensa se converter ≥ 1,16× o front de 12 meses + B1. Gatilho de troca: muitos reembolsos por "pensé que era de por vida" |
| US hispanos a 9,90 | 8,95 | 5,97 / 5,33 | CPM maior (não medido) |

**O que precisa ser verdade.** CPA = CPC ÷ (compras por clique). O CPC deste público na LATAM **não foi verificado**. A oferta calculava o break-even sem os 12% do BRL (7,24); corrigido abaixo para 6,46.

| CPC hipotético | Compras por clique para ROI 1,5 BRL (CPA 4,31) | Idem para break-even BRL (CPA 6,46) | CPA com o funil ilustrativo de 2,1% |
|---|---|---|---|
| US$ 0,10 | 2,3% | 1,5% | 4,76 |
| US$ 0,15 | 3,5% | 2,3% | 7,14 |
| US$ 0,20 | 4,6% | 3,1% | 9,52 |
| US$ 0,30 | 7,0% | 4,6% | 14,29 |

O funil ilustrativo (todas as taxas são hipóteses) é: 50% dos cliques começam a calculadora × 35% terminam o 1º produto × 12% pagam = **2,1% de compras por clique**. Com ele, **ROI 1,5 em BRL exige CPC ≤ US$ 0,09**, e com CPC de 0,20 o CPA (9,52) passa do break-even. O produto depende de um onboarding muito curto e de um paywall forte; é por isso que o portão é obrigatório.

**Comparação com o Mimo:** ~9,4 de líquido; CPA para ROI 1,5 de ~6,27 sem imposto e **~5,60 em BRL**. O L29 base a 7,90 fica em **77%** do líquido do Mimo (conservador 68%, otimista 87%), e o CPA-alvo fica **23% menor** (4,31 contra 5,60). **Não há folga para pagar o CPA que o Mimo paga.**

## Teto (gasto diário sustentável, premissas, faixa de confiança, comparação com o Mimo Gift)

**Conta de baixo para cima, só no MX.** Só as duas bases oficiais foram lidas (e só no resumo da busca); **todas as frações e a penetração são chutes sem fonte**. O red team pediu que a faixa final fosse tratada como palpite de ordem de grandeza.

| Grupo (MX) | Base | Fração relevante | Pessoas / negócios |
|---|---|---|---|
| (a) Unidades de preparação de alimentos e bebidas | 772.442 [medido via resumo; [Data México](https://www.economia.gob.mx/datamexico/es/profile/industry/food-services-and-drinking-places), [INEGI CE 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/ce/CE2024_def.pdf)] | 60% (micro, o dono decide o preço) [chute] | ~460 mil |
| (b) Vendedores ambulantes de alimentos | 805 mil pessoas, 1º tri de 2025 [medido via resumo; [Data México](https://www.economia.gob.mx/datamexico/es/profile/occupation/vendedores-ambulantes-de-alimentos)] | 30% [chute] | ~240 mil |
| (c) Quem vende por encomenda em casa | **Não medido.** Referência: 33,1 M de informais no MX (digest) | 1,5–4,5% [chute] | 0,3–1,5 M |
| **Total MX** | | | **1,0 / 1,6 / 2,2 M** (cons. / base / otim.) |

- Extrapolação para ES + US: ×1,95 [estimativa, mesma conta do L02 e do L67] → público ES de ~3,1 M no base.
- Penetração anual via anúncio: 0,5 / 1 / 2% [chute] → 27 / 86 / 235 compradores/dia → **~US$ 115 / 410 / 1.280 por dia** (a CPA para ROI 1,5 sem imposto; com conta BRL, ~11% menos).
- A oferta também fez uma checagem de cima para baixo, pela razão entre o público do Mimo e o da calculadora. O red team mostrou que é a razão entre dois números sem fonte; ela não entra aqui.

**Por que o teto fica abaixo da conta de baixo para cima:**
1. **1% de penetração ao ano faria do L29 o maior player em ES, de longe.** Para confeitaria de casa, o maior tem 17 anúncios (Chef Anna); o maior no geral (Fer Rendon, 36) é B2B de restaurante [proxy].
2. **Compra por dor com substituto grátis:** o funil freemium vaza, porque o número já apareceu na tela.
3. **O grupo (c), o mais alinhado ao produto, é o menos medido.** O grupo (a) inclui negócios que preferem Excel ou SaaS.
4. **Não há vantagem de lance:** o CPA-alvo é 23% menor que o do Mimo.

**Estimativa final, só espanhol, na régua BRL (CPA 4,31 a 7,90):**

| Faixa | Gasto/dia | Compradores/dia (gasto ÷ 4,31) | Penetração anual implícita (~3,1 M) | Confiança |
|---|---|---|---|---|
| Piso | **US$ 80** | ~19 | ~0,2% | **Baixa.** A oferta dava "média"; só sobe depois de um teste com CPA ≤ 4,31 |
| **Base** | **US$ 150** | ~35 | ~0,4% | **Baixa** |
| Topo | **US$ 250** | ~58 | ~0,7% | **Baixa** |
| Nível do Mimo | ≥ US$ 506 | ≥ 117 | ≥ 1,4% | **Muito baixa**, mesmo com PT-BR |

- **Margem sobre a mídia a ROI 1,5:** 0,50 × o gasto, sem imposto [estimativa]: ROI 1,5 devolve 1,5 de líquido por dólar gasto, então sobram 0,5. US$ 150/dia deixam ~US$ 75/dia antes de ferramentas e impostos sobre a renda. O Mimo, se rodasse a ROI 1,5, deixaria ~US$ 253/dia com US$ 506/dia. (Na régua BRL, a sobra é 1,68 − 1,12 = 0,56 por dólar de anúncio: ~US$ 84 e ~283/dia.)
- **Laço viral:** fraco. O rodapé "Hecho con {marca}" do catálogo é visto por clientes da confeiteira, que em geral não vendem comida [inferência]. Medir com `utm_source=catalogo`, sem contar no teto.

**Distribuição da base de US$ 150/dia [estimativa]:**

| País | % | US$/dia | Sinal do nicho [medido] | Observação |
|---|---|---|---|---|
| MX | 40% | 60 | Chef Anna (MXN), Fer Rendon (B2B), Cuentas Claras | OXXO atrasa o acesso |
| PE | 15% | 22 | Emprendedores Digitales (S/ 10), Excel para Restaurantes (S/ 19) | Braço B testa a âncora |
| AR | 15% | 22 | Dolchere, Dulces Herramientas | Día de la Madre em 18/10. **Otimista:** com MVP em 03/10, sobram ~10 dias, e a aprovação da Hotmart não tem prazo verificado. Se não estiver no ar até 08/10, tirar a célula AR e redistribuir |
| CO | 12% | 18 | Impulsa Tu Negocio (produto incerto) | PSE/Efecty |
| CL | 8% | 12 | Nenhum anunciante longevo medido | Renda maior |
| EC, GT, DO, BO, UY | 5% | 8 | Impulso digital (UYU, 0,8 d) | USD |
| US (hispanos) | 5% | 8 | Latinas Together (1,5 d) | Front de 9,90; público não verificado |

**Sazonalidade [estimativa; curvas do Google Trends não verificadas].** O produto é mais perene que os outros finalistas: quem vende comida define preço o ano todo. Os picos vêm das encomendas de data e da alta de insumos.

| Período | Fator | Motivo |
|---|---|---|
| 1–15/out | ~1,2× na AR | Día de la Madre AR (18/10), o único dentro de Q4 |
| 15/out–20/nov | ~1,1× | Encomendas de Natal; Kit de Temporada no ar |
| Semana da Black Friday | ~0,6× | CPM 2–3× maior (dados dos EUA; LATAM não verificado; [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [Clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics)) |
| Dezembro | ~0,6× | A confeiteira está produzindo, não configurando ferramenta [inferência] |
| 26/dez–fev | ~1,3× | CPM 40–60% menor até ~15/01 (dados dos EUA; LATAM não verificado; [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [Clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics)); "subió el huevo", Rosca, começo de ano |
| 15/abr–5/mai | ~1,4× | Día de la Madre em 10/5 (MX, PE, CL, GT): maior dia de venda de bolo do ano no MX ([Milenio](https://www.milenio.com/negocios/pastelerias-en-torreon-incrementan-ventas-el-dia-de-las-madres)) |
| Resto | ~1,0× | Base perene |

**Outros idiomas [estimativa]:**

| Idioma | Evidência | Acréscimo | Confiança |
|---|---|---|---|
| PT-BR | [Débora Vasconcelos](https://www.facebook.com/ads/library/?id=2018345395489206): 119 anúncios ativos hoje, mas **45 dos 50 mais novos subiram em ~65 s com o mesmo título**. É volume alto por duplicação em lote; o nº de criativos distintos e a longevidade não foram verificados. O produto é **curso + planilha** ([site](https://www.deboravasconcelos.com.br/curso-precificacao-confeitaria-cpd)). "Aplicativo de precificação" tem 217 ativos no BR ([busca](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=aplicativo%20de%20precifica%C3%A7%C3%A3o&search_type=keyword_unordered)), com vários apps (seção Concorrentes). A oferta chamava isso de "espelho mais forte de todos os finalistas"; o correto é **mercado pago existente e já disputado** | +US$ 50–200/dia | Baixa |
| EN | Não medido | +0–80 | Baixa |
| FR | Não verificado | +0–30 | Muito baixa |

**Total com todos os idiomas: US$ 130–560/dia, base ~US$ 290 (confiança baixa).** No BR, o formato talvez precise mudar para curso + ferramenta.

**Comparação com o Mimo Gift:**

| | Mimo Gift | L29 (estimativa) |
|---|---|---|
| Gasto/dia | > R$ 2.600 ≈ US$ 506+ (dado do usuário) | ES: US$ 80–250 (base 150); com PT/EN/FR: 130–560 (base ~290) |
| Líquido por comprador | ~US$ 9,4 | 6,40–8,14 a 7,90 (base 7,24); 5,53 a 5,90 |
| CPA para ROI 1,5, sem imposto / BRL | ~6,27 / ~5,60 | 4,83 / 4,31 (base), −23% |
| Gatilho | Impulso emocional, qualquer dia | Dor de quem já vende; comparação com o grátis |
| Público | Amplo [inferência] | Só quem vende comida ou doces; tamanho não medido |
| Âncora de preço | Sem âncora forte [inferência] | US$ 3–6 nos anúncios; US$ 5–20 na Hotmart (não verificado) |
| "Aha" do criativo | Reação emocional à página | Um número e uma lista de preços |
| Vantagens próprias | — | Build sem IA nem vídeo; risco de política baixo; picos em jan e mai |

**Veredito: o teto do L29 é menor, cerca de 16–49% do Mimo em espanhol (base ~30%); com todos os idiomas, a base vai a ~57%.** O que faria o L29 surpreender, em ordem de probabilidade:
1. taxa real no regime R2 (régua BRL de 5,15; não muda a posição relativa ao Mimo);
2. PT-BR com CPA dentro da régua;
3. CPA ≤ US$ 3,9 no MX escalando;
4. adesão ao B1 perto de 1/3.

Mesmo com os quatro, o teto provável fica **perto do Mimo, não acima**.

## Concorrentes diretos (links)

Medição por `page_ids`, só ACTIVE, 22/09/2026. Dias = idade do anúncio ativo mais antigo. **ACTIVE não prova gasto.** Das seis páginas ES com ≥ 30 d, só uma tem preço verificado (S/ 10) e só duas são de confeitaria. Os "~17 anunciantes ES" contam páginas com 1–2 anúncios de 0,8–8,8 d, uma operação em BRL e uma de produto incerto.

| Página | Produto | País / moeda | Ativos | Dias | Preço | Nota |
|---|---|---|---|---|---|---|
| [Chef Anna](https://www.facebook.com/ads/library/?id=1276480471319495) | **Não identificado** | MX / MXN | 17 | 119,2 (1 anúncio) | não verificado | Outros: 76,2 ([USD](https://www.facebook.com/ads/library/?id=2865981490401400)), 60,0 ×3, 32,2, 28,0, 14,7–18,0 ×8, 1,1 ×2 ([pizzas](https://www.facebook.com/ads/library/?id=3190017107875591)). Mesmo gancho trocando o ofício |
| [Fer Rendon](https://www.facebook.com/ads/library/?id=1246557617490162) | Excel/Sheets "Costeo de Menú" para restaurante | MX / MXN | **36** de costeo (a pesquisa mediu 32) | 67,6 | não verificado ([site](https://www.ferrendonx.com/p/costeo-de-menu-excel/)) | 22 com ≥ 30 d. **B2B, outro público e outro formato**; 4 títulos com "ganancias", 2 deles com ≥ 30 d. Não prova demanda para a confeiteira de casa |
| [Emprendedores Digitales](https://www.facebook.com/ads/library/?id=1047240127991578) | "PLANTILLA GASTRONÓMICA PRO" | PE / PEN | 18 | 91,9 | **S/ 10** ≈ US$ 2,97 | Os títulos com "¿CUÁNTO GANAS…?" têm só 2,0–11,1 d ([link](https://www.facebook.com/ads/library/?id=1475097697788648)) |
| [Excel para Restaurantes Perú](https://www.facebook.com/ads/library/?id=1089104103530989) | Planilha | PE / USD | 17 | 17,3 | **S/ 19** ≈ US$ 5,64 ("Único Pago") | 9 anúncios criados hoje |
| [Dolchere](https://www.facebook.com/ads/library/?id=1742357790155181) | App "La app de las pasteleras" + receitas | AR / USD | 74 | 42,9 (Fase 3; os 50 mais novos têm ≤ 4,7 d) | app não verificado; site: ARS 12.999–18.490 ([link](https://recetariosdolchere.shop/)) | ~10 anúncios novos por dia [proxy]. Escorrega em renda ([link](https://www.facebook.com/ads/library/?id=1886078219071457)) e urgência ([link](https://www.facebook.com/ads/library/?id=924813996978839)). **O mais bem posicionado para copiar a nossa saída visual** |
| [Pasión por la Cocina](https://www.facebook.com/ads/library/?id=1565461397804309) | "Calculadora Gastronómica PRO" | — / USD | 5 | 45,5 | não verificado | — |
| [Cuentas Claras](https://www.facebook.com/ads/library/?id=1696683294754899) | Costeo de menú | MX / MXN | 7 | 41,1 | não verificado | "Costea tu menú en 30 minutos" ([link](https://www.facebook.com/ads/library/?id=1356914146422197)) |
| [Latinas Together](https://www.facebook.com/ads/library/?id=1057383214053948) | GastroKit | US / USD | 12–13 | 1,5 | **US$ 57** | Bons ângulos, sem longevidade |
| [Dulces Herramientas](https://www.facebook.com/ads/library/?id=1398453758901163) | Precios + presupuestos | AR/UY / USD | 5 | 22,8 | não verificado | [presupuestos](https://www.facebook.com/ads/library/?id=1624450332359038) |
| [Serendipity J&P](https://www.facebook.com/ads/library/?id=1606182844545250) | "Calculadora de Precios para Emprendedores" | MX / MXN | 6 | 12,9 | não verificado | — |
| [Impulsa Tu Negocio](https://www.facebook.com/ads/library/?id=1533541694900092) | **Incerto** | CO / COP | 10 | 72,2 | — | Sem título. **Não conta como prova** |
| [Repostery](https://www.facebook.com/ads/library/?id=1479382940908553) | App/SaaS de confeitaria | MX / MXN | 1 | 8,8 | não verificado | — |
| [Dulce Gestion](https://www.facebook.com/ads/library/?id=1668745884875469) | — | BRL (operação BR em ES) | 3 | 3,0 | "Solo hoy por $5" | — |
| [Impulso digital](https://www.facebook.com/ads/library/?id=1642380330729354) | Calculadora | UY / UYU | 2 | 0,8 | não verificado | — |
| [CostoChef](https://www.facebook.com/ads/library/?id=1553910179395667) | SaaS B2B | — | — | — | assinatura | Outro público |
| Fase 3, não re-medidos | [Juli Rosemberg](https://www.facebook.com/ads/library/?id=3102872796589183) · [Andrea Crochetea](https://www.facebook.com/ads/library/?id=1529067728905420) · [Pau Regalos Valentino](https://www.facebook.com/ads/library/?id=1232865344959275) | — | 6 / 3 / 1 | 5,0 / 3,0 / 216,7 | — | Pau Regalos: "Calcula y gana más" (proibido para nós) |

**Hotmart ES.** Os preços vêm do resumo do WebSearch, **não verificados na página**. A busca "calculadora de costos repostería" deu só **31 ativos** em ES + US ([busca no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=calculadora%20de%20costos%20reposter%C3%ADa&search_type=keyword_unordered); o link reproduz um país, e a soma de 11 países ES + US foi feita via API em 22/09/2026), quase todos receituários e cursos, e nenhum identificável como estas listagens. **Não há prova de que vendam.**
- US$ 5 em promoção, de 9,90 ([N99160088C](https://pay.hotmart.com/N99160088C)) · US$ 7 ([J104799257A](https://pay.hotmart.com/J104799257A)) · US$ 10 ([J104782701Y](https://pay.hotmart.com/J104782701Y)) · US$ 12 ([P83579553T](https://pay.hotmart.com/P83579553T)) · US$ 19,99, com orçamentos ([N96918657O](https://pay.hotmart.com/N96918657O)).
- Sem preço: [U105164875U](https://hotmart.com/es/marketplace/productos/calculadora-de-costos-para-reposteria-guia-paso-a-paso-recetario-de-regalo/U105164875U), [H103235284N](https://hotmart.com/es/marketplace/productos/calculadora-automatica-de-costos-y-precios-para-reposteria/H103235284N), [D103000487M](https://hotmart.com/es/marketplace/productos/calculadoras-de-costos-hoja-de-calculo-excel/D103000487M), [X105453537A](https://hotmart.com/es/marketplace/productos/sistema-de-precios-rentables-para-reposteria-calculadora-guia-bonus-whatsapp/X105453537A) (bônus WhatsApp), [K95490413E](https://hotmart.com/es/marketplace/productos/calculadora-de-precios-pasteleria-y-reposteria/K95490413E), [V104956697U](https://hotmart.com/es/marketplace/productos/plantilla-de-costos-y-precios-para-reposteria-excel/V104956697U), [N93778262F](https://hotmart.com/es/marketplace/productos/plantilla-de-excel-calculadora-de-costo-para-reposteria/N93778262F), [U94626349S](https://pay.hotmart.com/U94626349S).

**Substitutos grátis (o maior risco de conversão):**
- Web: [Supleo](https://www.supleo.app/calcular-costo/reposteria), [CalculadoraPrecios.com](https://calculadoraprecios.com/precios-para-manualidades), [Identidad Rural](https://identidadrural.es/recursos/calcular-precio-artesania/), [Simúlalo](https://simulalo.app/es/simulador/food/costos-panaderia), [gigiad](https://www.gigiad.com/?lang=en), [frutimail](https://frutimail.com/), [calculadoraderecetas.com.ar](https://calculadoraderecetas.com.ar/), Excel grátis do [ingenieriademenu](https://ingenieriademenu.com/producto/formato-para-costeo-de-recetas-excel/).
- Apps (modelo de cobrança não verificado): [PostrePro](https://play.google.com/store/apps/details?id=com.postrepro.app&hl=es), [Precio de Recetas y Menú](https://play.google.com/store/apps/details?id=com.f98k.profitablerecipe.android&hl=es), [Pastri](https://apps.apple.com/pe/app/pastri-costos-de-recetas/id6777233315), [Calcular Costos Recetas](https://apps.apple.com/us/app/calcular-costos-recetas/id6747908579?l=es-MX).
- Conteúdo que ensina a conta: [Vainilla Molina](https://vainillamolina.com/blog/guia-basica-para-fijar-el-precio-de-tus-postres), [Aprende.com](https://aprende.com/blog/gastronomia/reposteria/aprende-a-calcular-el-precio-de-tus-pasteles/), [TikTok @sandra_jarufe](https://www.tiktok.com/@sandra_jarufe/video/7535839252085558534?lang=es).

**Catálogo (concorre com o B2):** [Intelia SB](https://www.facebook.com/ads/library/?id=1548914280065958) (9 ativos, 71,1 d; produto e preço não verificados), [TiendaLista](https://www.facebook.com/ads/library/?id=1685154086361147), [YoMeLlamo](https://www.facebook.com/ads/library/?id=1906455124071839); catálogo do WhatsApp Business (grátis, não verificado).

**Espelho BR:**
- [Débora Vasconcelos](https://www.facebook.com/ads/library/?id=2018345395489206): 119 ativos, "Planilha de Precificação para Confeitaria - Perpétuo"; lote duplicado (45 em ~65 s); curso + planilha ([site](https://www.deboravasconcelos.com.br/curso-precificacao-confeitaria-cpd)); preço não verificado.
- [PrecificaPRO](https://www.facebook.com/ads/library/?id=1373994478235963): 14 ativos, 13,8 d, "Pare de vender no achismo"; a página mistura renegociação de dívida.
- "Aplicativo de precificação" = **217 ativos** [medido, [busca no BR](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=aplicativo%20de%20precifica%C3%A7%C3%A3o&search_type=keyword_unordered)]: [PreciArte](https://www.facebook.com/ads/library/?id=39216762071241245), [Doce Preço Fácil](https://www.facebook.com/ads/library/?id=2367026897466899), [Isabela Dandaro](https://www.facebook.com/ads/library/?id=1442718327784403) ("Pare de cobrar no chute", 12+ num lote) e o padrão "Todo mecânico/detailer deveria usar" ([Oficina Lucrativa](https://www.facebook.com/ads/library/?id=1374666888082672), [Ajuda Estética Automotiva](https://www.facebook.com/ads/library/?id=2236425793802856), [Ajuda Técnico](https://www.facebook.com/ads/library/?id=1068872962601746)). Parece um app de preço multiplicado por ofício; produto e operador não verificados. **Operadores do BR podem "tropicalizar" para ES** [inferência].
- Hotmart BR: [X75547877U](https://hotmart.com/pt-br/marketplace/produtos/planilha-de-precificacao-rlnbs/X75547877U), [N52697618E](https://hotmart.com/pt-br/marketplace/produtos/planilha-de-precificacao-para-confeitaria-donos-de-bares-e-restaurantes/N52697618E), [N90508214V](https://hotmart.com/pt-br/marketplace/produtos/precificacao-correta-na-confeitaria/N90508214V), [N65213315V](https://hotmart.com/pt-br/marketplace/produtos/planilha-de-precificacao-para-confeitaria-2-2/N65213315V) (preços não verificados).

## O melhor argumento de por que vai falhar (e o que mataria a ideia)

**O argumento.** Para dar ROI 1,5, o L29 precisa de um CPA **~23% menor que o do Mimo** (US$ 4,31 contra ~5,60 em conta BRL). Só que vende para um público muito mais estreito, numa compra que nasce de uma dor, e o funil freemium entrega de graça justamente o que a pessoa veio buscar: **o número**.
- **O "aha" já é o entregável.** No Mimo, a prévia cria desejo por algo que só existe depois do pagamento (a página publicada). Aqui, um print da tela de resultado resolve. O que se paga (guardar, exportar, recalcular) é conveniência, e concorre com o caderno, o print, 8+ calculadoras grátis e o catálogo do WhatsApp Business.
- **A conta do próprio dossiê não fecha.** No funil ilustrativo (2,1% de compra por clique), CPC de US$ 0,20 dá CPA de 9,52, acima do break-even BRL (6,46). ROI 1,5 só com CPC ≤ US$ 0,09.
- **A evidência de demanda é fina.** 22 dos 37 anúncios longevos são de uma página B2B de Excel para restaurante. A "prova" do gancho de confeitaria é 1 anúncio de uma página com produto desconhecido. A âncora paga é S/ 10–19. O espelho BR é duplicação em lote de um funil de curso.
- **Mesmo dando certo, o ganho é pequeno.** Base de US$ 150/dia ≈ US$ 75/dia de margem (0,50 × o gasto, sem imposto; 84 na régua BRL), ao custo de 11–14 dias de build, 30 criativos por semana e suporte recorrente por 12 meses, tirados do tempo de quem opera sozinho um Mimo que, a ROI 1,5, deixaria ~US$ 253/dia (283 na régua BRL).
- **Desfecho mais provável:** CPA acima de 4,31. O teste custa pouco, mas o custo de oportunidade do operador é alto.

**Os 5 maiores riscos e o sinal precoce de cada um:**

| # | Risco | Por quê | Sinal precoce |
|---|---|---|---|
| 1 | **Economia do funil:** o grátis entrega o valor e o paywall cobra por conveniência | O break-even depende da compra por clique. Os 7,24 dependem do B1 a 24% (não verificado); com o B1 a 15% e sem outros bumps, o líquido cai para 5,82 e o alvo BRL para 3,46. O reembolso base (4%) já é > 4× o do Mimo | Portão: cliques em "Guardar" ÷ cliques de link < CPC ÷ 1,72. "Enviarme este resultado" mais clicado que "Guardar". Primeiras 30 vendas: > 40% sem um 2º produto salvo em 48 h; ≥ 1/3 dos reembolsos por "gratis" ou "no lo necesito" |
| 2 | **Teto baixo × custo de oportunidade** | Só compra quem já vende comida ou doces; qualquer semana em que o Mimo deixe de escalar ou abrir idioma custa mais que o melhor cenário do L29 [inferência] | MX de US$ 60 para 100/dia: frequência de 7 d > 2,5 ou CPM +30% semana a semana com CPA +25%. Mimo com ROI caindo 2 semanas seguidas ou fila de tarefas parada |
| 3 | **Criativo e CPM:** "aha" numérico e ganchos importados de B2B | A igual CPM, bater 4,31 contra 5,60 exige CTR × compra por clique ≥ 1,3× o do Mimo. 60% da evidência de ângulo é de restaurante. Os líderes giram estoque de anúncio em dias | Semana 1: CTR de link mediano abaixo do Mimo no mesmo país e posicionamento; CPC > US$ 0,15; hook rate abaixo do Mimo; nenhum anúncio com ≥ 3 vendas e CPA ≤ 4,31 depois de US$ 150 |
| 4 | **Build maior que o prometido, suporte recorrente, reembolso técnico** | 11 dias até o vendável, não 4–6. Uso por 12 meses gera dúvidas de cálculo, formato numérico e login, um suporte recorrente que não entrou em nenhuma conta | Não vendável até 06/10; OTP > 1 min em > 5% dos testes; > 10% dos compradores sem login em 24 h; > 1 ticket a cada 10 vendas; reembolso > 5% nas primeiras 60 vendas ou qualquer preço calculado errado em AR/CO/CL |
| 5 | **Cópia e âncora de US$ 3–5** | A lógica se clona num dia. Dolchere já tem app e volume de anúncios; Fer Rendon opera de forma contínua; 217 anúncios de apps de precificação no BR | Concorrentes com "lista de precios", "se actualizan todos" ou "catálogo" 2–4 semanas depois dos nossos vencedores; conversão do paywall caindo com CTR estável; concorrente oferecendo app por ≤ US$ 5 |

Fora do top 5: **conta e política**, com risco baixo (digest: ferramenta de preço, Meta BAIXO / Hotmart BAIXO). Pontos de atenção: o nicho escorrega para "gana" e "ingresos", e a tela 5 do build dizia "Para ganar". Sinal: 2 ou mais reprovações por "oportunidad económica" ou "atributos personales" na semana 1 → revisar a landing antes de gastar mais.

**O que mataria a ideia.** Regras gerais:
- Recalcular a régua com o líquido medido: alvo = líquido ÷ 1,68; break-even = líquido ÷ 1,12. Os números abaixo são do base (7,24).
- **Teto do teste: US$ 600 gastos com checkout no ar** (≈ R$ 3.100, da ordem de um dia de gasto do Mimo, que passa de R$ 2.600/dia). Não existe "mais US$ 150 iterando" depois disso.
- Estes cortes substituem as regras anteriores, que ignoravam os 12% da conta BRL. O "continuar com CPA ≤ 6,0" da oferta dá ROI 1,08; o break-even era 6,46, não 7,24 (oferta) nem 5,59/7,32 (build). Entre 6,46 e 7,24, o teste perdia dinheiro sem acionar corte nenhum. Os cortes do portão do build (25% terminam / 8% clicam em "Guardar") aprovavam um produto que perde dinheiro: com 25% × 8% × 40% pagando, a compra por clique é 0,8% e o CPA fica em 125 × CPC.

| # | Quando | Métrica | Mata se… | De onde vem o limiar |
|---|---|---|---|---|
| K0 | Build | Data em que fica vendável | Não vendável até **D14 (06/10/2026)** → cortar para front + B1. Não vendável até **D18 (10/10)** → **arquivar** | O plano diz D11 + 3 de folga |
| K1 | Portão (US$ 60–100, ≥ 300 cliques de link) | CPC de link | **> US$ 0,25** | A 0,25, o alvo exige ≥ 5,8% de compra por clique e o break-even ≥ 3,9%; o funil do dossiê dá 2,1% |
| K2 | Portão | Cliques em "Guardar" ÷ cliques de link | **< CPC ÷ 1,72** (< 5,8% a CPC 0,10; < 8,7% a 0,15; < 11,6% a 0,20) | Compra por clique ≥ CPC ÷ 4,31, supondo que 40% de quem clica em "Guardar" pague (hipótese otimista) |
| K3 | Portão | Quem termina o 1º produto ÷ cliques de link | **< 25%** | Mantido do build, agora com a base definida |
| K4 | Primeiros US$ 150 com checkout (≥ 12 criativos, ≥ 2 ofícios, MX) | CPA combinado | **> 6,46** → arquivar | Se o CPA real fosse 4,31, a chance de ver > 6,46 com US$ 150 é de ~2,2% (Poisson, λ = 34,8, k ≤ 23) |
| K5 | Primeiros US$ 150 | (CTR de link × compra por clique) ÷ o mesmo no Mimo, mesmo país e posicionamento | **< 1,0×** → arquivar | A igual CPM, é preciso ≥ 1,3× |
| K6 | US$ 300 acumulados | CPA combinado | **> 5,39** (ROI 1,2 em BRL) → arquivar | 7,24 ÷ (1,2 × 1,12) |
| K7 | US$ 600 acumulados | CPA dos últimos US$ 300 | **> 4,31** → arquivar | Régua do usuário para subir verba |
| K8 | Após 50 compras | Líquido medido por comprador | **< 6,40** → recalcular o alvo; se o CPA atual > líquido ÷ 1,68, arquivar | O B1 a 24% não foi verificado |
| K9 | Primeiras 100 vendas | Reembolso / chargeback | Reembolso > 7% ou chargeback > 0,5% → pausar. Reembolso > 10% → arquivar | Limite da Hotmart: 0,9% de chargeback |
| K10 | Semanas 3–4 | Gasto/dia sustentável com CPA ≤ 4,31 | **< US$ 100/dia** → arquivar | Margem < ~US$ 50/dia (0,50 × o gasto, sem imposto; 56 na régua BRL), que não paga 30 criativos por semana + suporte [estimativa] |

**Regras de pausa por anúncio** (não matam a ideia): gasto ≥ US$ 8,62 sem venda (US$ 6,58 no braço de 5,90); CTR de link < 0,7× a mediana da semana depois de 3.000 impressões. **Escalar** +20–30% a cada 48–72 h só com CPA ≤ 4,31.

**Janela da AR:** se a célula não estiver no ar até **08/10**, tirar o Día de la Madre (18/10) e não contar a AR no veredito.
