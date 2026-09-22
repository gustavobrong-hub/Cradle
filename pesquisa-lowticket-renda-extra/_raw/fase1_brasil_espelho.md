# Fase 1 — Fonte "Brasil como espelho" (arbitragem PT -> ES)

Data da coleta: 2026-09-22. Referência "agora" = epoch 1790095977. Dias ativo = (1790095977 - ad_delivery_start_time)/86400.
Ferramenta: `mcp__Meta_Ads__ads_library_search`, sempre ad_active_status=ACTIVE (exceto 1 busca marcada ALL).
BR: countries=["BR"]. ES: countries=["MX","CO","AR","CL","PE","US"].

## Como ler estes números (limitações)

- `estimated_total_count` é **proxy** e é ruidoso: mesmo com aspas a busca NÃO é frase exata (ex.: "cardápio digital" = 17.719 porque pega restaurante; "lista de proveedores" = 10.085 pega qualquer coisa). Só comparo PT x ES quando o ruído é parecido, e digo quando não é.
- BR = 1 país; ES = 6 países somados. O BR tem um mercado de infoproduto low ticket muito mais denso, então o mesmo count significa mais saturação no ES do que no BR.
- A ferramenta devolve do anúncio mais novo pro mais antigo. Com 50+ anúncios ativos, o "mais antigo" visível é só um limite inferior (marcado "50+ (limite)").
- Não há corpo do anúncio nem alcance. A relevância vem de page_name + link_title + moeda. Moeda BRL num anúncio em espanhol = **anunciante brasileiro já fazendo a arbitragem PT->ES**. Isso é um achado importante (seção 5).
- Muitos anunciantes BR trocam criativos toda semana. Por isso "mais antigo ativo" costuma subestimar há quanto tempo a oferta roda. Registro o número mesmo assim.
- Preço: só via snippet do WebSearch ou do link_title do anúncio. Hotmart, Kiwify e checkouts não abrem nesta sessão (bloqueados).

## 1. Log de buscas — BRASIL (countries=BR)

| # | termo | estimated_total_count | nota |
|---|---|---|---|
| B1 | convite digital (sem aspas) | 2.309 | muito ruído (escolas, agendamento), mas acha Convitia, ConviteLândia, JoHerinher e várias conviterias |
| B2 | kit festa editável | 74 | Melhores Noticias (+1.000 kits), Pack sublimação (R$3,99), Festa 550, Chá de Langerie Pronto, Kit Dia da Criança Pronto |
| B3 | convite interativo | 598 | dezenas de conviterias pequenas (serviço via WhatsApp) + Convitia |
| B4 | página personalizada | 986 | ruído (placa NFC, dieta). Acha "Crie Sua História" (livro) |
| B5 | presente digital | 4.450 | ruído |
| B6 | "retrospectiva namorados" | 2 | lovecupido_ofc (ativo há 101,6 d), Presentim (144,5 d). É a categoria do próprio Mimo |
| B7 | "pack canva" | 1.265 | Cabine Lucrativa, Pack Canva Para Você, Calendários 2027, Universo dos moldes, Drink Pack's |
| B8 | "topo de bolo" | 1.307 | a maioria é confeitaria física; digital: Artes Digitais (1.600 topos), Pack sublimação (20 mil topos R$1,49) |
| B9 | "arquivos de corte" | 353 | Biblioteca do Corte (18 ads), Giullia Pereira (+100 mil projetos), Zona Digital, Central Premium |
| B10 | "artes para sublimação" | 280 | Pack Pronto (R$19,90), Vinics (+150 artes R$39,90), CorelBot, Flor de Cactos (kits Halloween/Dia das Crianças "pra vender"), KIT Estamparia |
| B11 | "renda extra" | 25.578 | só mapeamento: revenda, MLM, cursos. Sem uso direto |
| B12 | "prontos para vender" | 6.146 | Gabi Tato e Nana, Júlia Castanhari (serralheria), Buquês para floriculturas, PSD Flyer |
| B13 | "vídeo personalizado do Papai Noel" | 39 | Recado do Noel (24 ads, do Natal 2025, status ainda ATIVO), Recadinho do Noel ("10 Mil Pais Já Confiaram") |
| B14 | "livro personalizado" | 888 | Sua Historinha (95 ads), Make My Memo, Arca dos Livros |
| B15 | "projetos prontos" | 4.444 | ruído. Júlia Castanhari, Vinícius Augusto ("Pegue Seus Projetos") |
| B16 | "molduras" | 2.190 | ruído (quadros, gesso). Cabine Lucrativa |
| B17 | "cardápio digital" | 17.719 | ruído (restaurantes). Descartado |
| B18 | "lista de fornecedores" | 2.948 | LISTA Fornecedor, Fornecedores Vip, Pivot Pack. E2 provável |
| B19 | "música personalizada" | 3.333 | lotado: Felicidade em Música (R$19,90), Música Express (R$29,90), MusicaViva (a partir de 5,99), Homenagem em Canção (R$9,99), Music s2, Vixion, Quero Fazer Música (R$15) |
| B20 | "ensaio com IA" | 3.162 | Marcos Studio IA (54 ads), Studio Boss (R$10,90), WB Studio, Arthur Tomaz |
| B21 | "site de casamento" | 2.093 | Caseaki, Clube das Noivas (R$19,90) |
| B22 | "currículo pronto" | 1.285 | Currículo ideal 2.0 (a partir de R$10), Currículo Up (feito por profissionais -> E3) |

## 2. Anunciantes BR — nº de anúncios ativos e anúncio mais antigo (via page_ids)

| página (page_id) | oferta | ativos | mais antigo (dias) | exemplo | nota |
|---|---|---|---|---|---|
| Convitia - Convite Digital Interativo (628646776989656) | editor de convite interativo (SaaS freemium) | 33 | 76,9 | https://www.facebook.com/ads/library/?id=1042494484973953 | Dois ângulos: B2C ("Crie seu convite grátis", "Veja seu convite antes de pagar") e renda extra ("Fature até R$250 por Convite Digital!", "150+ Modelos Profissionais para Lucrar Hoje Mesmo!", "Ganhe até R$200 por convite de 15 anos") |
| Canva Para Noivas (663864766819174) | papelaria de casamento editável no Canva + convite interativo | 35 | 88,9 | https://www.facebook.com/ads/library/?id=1313617404312022 | Preços no título: "Convites digitais interativos por R$47", "6 convites digitais por R$47", "Sua papelaria inteira por R$67" |
| Sua Historinha (1081357198384337) | livrinho infantil personalizado ("Criar livrinho agora") | 95 (50+ limite) | 0,3 (mais antigo VISÍVEL; o real não aparece) | https://www.facebook.com/ads/library/?id=1095623402814655 | moeda USD, texto em PT. Volume de teste de criativo muito alto = forte sinal de escala (proxy) |
| Crie Sua História (1238080412713855) | livro personalizado ("Uma aventura só dele(a)") | 15 | 75,6 | https://www.facebook.com/ads/library/?id=1054382503830812 | |
| Marcos Studio IA (1090747747457250) | ensaio fotográfico com IA | 54 (50+ limite) | 0,3 (visível) | https://www.facebook.com/ads/library/?id=1238647358439864 | ângulos por público: "mulheres", "mães", "pessoas", "Mais de 6.697 ... aprovaram" |
| Studio Boss - Ensaio fotografia IA (1332960623232891) | ensaio IA "a partir de R$10,90" | 2 | 0,2 | https://www.facebook.com/ads/library/?id=1422812729803055 | moeda USD |
| Felicidade em Música (1138539246004090) | música personalizada R$19,90 | 16 | 4,7 | https://www.facebook.com/ads/library/?id=1111863218428916 | |
| Música Express (1089799627555585) | música personalizada R$29,90 | 1 | 0,0 | https://www.facebook.com/ads/library/?id=1601512678336992 | |
| Recado do Noel (920009151189259) | vídeo personalizado do Papai Noel | 24 | 275,3 | https://www.facebook.com/ads/library/?id=2366097457137335 | todos do Natal 2025 e ainda marcados ACTIVE. Provavelmente não entregam fora de dezembro (não verificado) |
| Festa 550 / Papelê - Papelaria digital (1287384654447351) | "550 convites editáveis no Canva" | 17 | 35,7 | https://www.facebook.com/ads/library/?id=1043999145023859 | ads mais novos em USD |
| Pack sublimação (288216651031190) | "20 Mil Topos de Bolo por R$ 1,49" + "Kit Festa na Mesa a partir de R$ 3,99" | 10 | 33,5 | https://www.facebook.com/ads/library/?id=1579502953724620 | preço ultra baixo (front-end de funil) |
| Melhores Noticias (1068200046374559) | "+1.000 modelos de Kit Festa prontos" (+ atividades fônicas) | 21 (6 de kit festa) | kit festa 0,5; página 26,3 | https://www.facebook.com/ads/library/?id=3201795946877411 | kit festa é teste novo |
| Artes Digitais (1243175122220507) | "1.600 Topos de Bolo Prontos pra Imprimir" | 4 | 0,1 | https://www.facebook.com/ads/library/?id=2155772475373199 | USD |
| Chá de Langerie Pronto (1350370221483938) | kit de brincadeiras para chá de lingerie | 8 | 38,2 | https://www.facebook.com/ads/library/?id=1422855243093646 | |
| Kit Dia da Criança Pronto (1380109951842990) | kit para professor(a) | 11 | 4,2 | https://www.facebook.com/ads/library/?id=1078616054658222 | sazonal (12/out) |
| Cabine Lucrativa (747177161823363) | "+500 molduras editáveis para PHOTOBOOTH" | 9 | 4,1 | https://www.facebook.com/ads/library/?id=4627474187578843 | público B2B (dono de cabine) |
| Biblioteca do Corte (1273210592538710) | arquivos de corte | 18 | 2,1 | https://www.facebook.com/ads/library/?id=1117671573961502 | |
| Pack Pronto (1379510091905867) | artes para canecas R$19,90 | 4 | 0,2 | https://www.facebook.com/ads/library/?id=1393874426262954 | |
| Universo dos moldes (1318099178050157) | "+100 moldes de caixas para copos twister" | 5 | 0,4 | https://www.facebook.com/ads/library/?id=2986895848313204 | |
| Bastidores da Tarcy (384246601435972) | "Calendários 2027 prontos pra vender" | 1 | 0,1 | https://www.facebook.com/ads/library/?id=1110358568012679 | |
| Pack Canva Para Você (103882709114280) | posts prontos por nicho profissional (neuropsicólogas, clínicas) | 14 | 10,3 | https://www.facebook.com/ads/library/?id=1597858968452709 | R$59,90 (acima do low ticket) |
| Júlia Castanhari (1358866073965586) | "+5.000 Projetos de Serralheria Prontos" | 2 | 0,1 | https://www.facebook.com/ads/library/?id=1768623144465990 | USD |
| ConviteLândia (1240838915789852) | convite digital 15 anos/casamento + lista de presentes | 3 | 0,1 | https://www.facebook.com/ads/library/?id=1084505564292498 | |
| Clube das Noivas (1201041136435812) | "Apenas R$19,90" | 3 | 1,7 | https://www.facebook.com/ads/library/?id=2026322778025027 | |
| lovecupido_ofc (1176480235546962) | retrospectiva de namorados (tipo Mimo) | 1 visto | 101,6 | https://www.facebook.com/ads/library/?id=888647297597053 | referência da categoria do Mimo |
| Presentim (1103529692842159) | retrospectiva de namorados (tipo Mimo) | 1 visto | 144,5 | https://www.facebook.com/ads/library/?id=946262721505177 | idem |

Vistos na busca, sem checagem por page_id: Recadinho do Noel (791986520667180, "10 Mil Pais Já Confiaram"), MusicaViva (106369625809348, "A PARTIR DE 5,99"), Homenagem em Canção (1218083858062903, "R$ 9,99", USD), Caseaki (435775502963307), Giullia Pereira (711089028764072), CorelBot (1355684424291092), Flor de Cactos Personalizados (310606938808530, "Kit Halloween Completo - Arquivos Prontos"), LISTA Fornecedor (256590867547295), Fornecedores Vip (1249118418294648), Curriculo ideal 2.0 (213301308544213, "a partir de R$10").

## 3. Log de buscas — ESPANHOL (countries = MX, CO, AR, CL, PE, US)

| # | termo | estimated_total_count | anunciantes relevantes vistos (nos mais novos) |
|---|---|---|---|
| E1 | "invitación digital interactiva" | 129 | quase tudo serviço feito por encomenda: Invi Digi (1029623536892040, MXN), Eventika digital (546667088540899, "INVITACIÓN DIGITAL $119" MXN), Invytia (1001960896340970, "$399" MXN), TarjetaViva (1217892654751932, "Desde S/100"), Casa Taro (1186126027917061, 1 ad, 9,9 d, "La Invitación Digital Interactiva #1 de México"), Craedis (USD), Momenta CL, Valen Struber (ARS), Mudix, Invitarahora (COP), Tarjetas Interactivas (ARS). **Nenhum editor self-service low ticket visto** |
| E2 | "cuento personalizado" | 1.240 | muito ruído. Relevante: Mi Cuento Infantil Personalizado (166953813165193) |
| E2b | "libro personalizado" niño protagonista | 15 | Adorabook (454878527708822, USD, 11 ads, 52,2 d), MiBook (1161535813714856, "Regalá", 3 ads, 60,0 d), Erase 1 vez (487649404435884, COP). Parecem livro impresso (não verificado) |
| E3 | "canción personalizada" | 4.003 | lotado: Diego Hernandez (977127798806735, USD, muitos ads), DedicatieMuzicala (834469756417930, multi-idioma), Ana Alice (1275562858967632, **BRL**), Tinos Records (COP), Mejor Digital (COP), UrbanBeat (COP), AudioMarca Estudio (ARS), CorridosRoman (MXN) |
| E4 | "sesión de fotos con IA" | 414 | **dominado por anunciantes brasileiros (moeda BRL)**: Aura IA Studio (186078587924004), Aurelia Studio (545586678647486), Ensaio IA Premium (1047092538485241), Milena • Ensaios com IA (1027467803783017), Yasmim & Hiago Ensaios IA (907515899119155), Luciana Duarte (884289721444858), Gabriel Marketing IA (951019321421660), Eugenia Silva (111838966897600), Juan Carlos Ia, Carla Rodrigues. Locais: Alana Estudio de IA (PEN), Watson Estudio (MXN). Vários vendem via WhatsApp (manual) |
| E5 | "video personalizado de Santa Claus" | 0 | fora de temporada. "video de Santa Claus" (status ALL) = 1.902, tudo ruído -> **não verificado** |
| E6 | "toppers para pastel" | 55 | a maioria é confeitaria ou topper físico. Digital: Emilia Creativa (104514041971206, "+1.200 Cake Toppers Profesionales", USD, 11,5 d), Activa Academy (881747588346031, "Mega Kit de Fiesta: +10,000 Diseños", MXN, 33,1 d), Cajitasencasa (BRL) |
| E7 | "archivos para corte láser" | 126 | Paquete De Diseños (107416171593294, USD, 33 ads, 7,4 d, "+2,100 Moldes en MDF"), Mega Pack Deseños Laser (1307717249096976, **BRL**), Mega Pack Cortes a Laser (1130294380173670, **BRL**), Maria Rosa (EUR), DigitNova (USD), Corte laser y melamia (USD, "+100 GB"), Files NC (PEN), Nomen Design, Biblioteca Digital de Reventa (CLP) |
| E8 | "marcos para photobooth" | 7 | Cabina de Fotos Lucrativa (536403069546446, **BRL**, 4 ads, 7,8 d, "4 productos en 1 para tu Photobooth"). O resto é serviço de cabine |
| E9 | "juegos para despedida de soltera" | 27 | nenhum kit digital visto (shows, dramas) |
| E9b | "juegos para baby shower" | 451 | ruído (palhaços, eventos). Nenhum kit digital visto |
| E10 | "invitaciones editables" | 345 | Mundo Creativo Digital (1068130303039496, USD, "+10,000 recursos listos para editar en Canva"), Editables al Toque (1221815361021145, USD), Fiesta Digital (1264134926791458, **BRL**, "+10.000 Diseños para Fiestas"), Fiesta Lista (1164503133403168, **BRL**), Bruno Lero (**BRL**, "+200 Plantillas Editables"), Diseña Creativo ("$89 MXN"), Web Online (PEN, "+1200 INVITACIONES listas para VENDER"), Aura creativa digital ("Empezá a vender deco para cumpleaños"), Detalles Creativos, Liz Rodriguez, MagicKids |
| E11 | "kit imprimible" | 855 | virou atividades infantis e educação (outro nicho) |
| E12 | "proyectos de herrería" | 716 | ruído (serralherias físicas). Digital: Planos y Diseños de Herrería (1197011490158539, MXN), Alejandro García (1180365315170592, **BRL**, "SOLO HOY POR SOLO $6!"), Carlos Mendoza (1261299827062029, **BRL**, "SOLO HOY POR $5"), Profe teo (COP, "10.000 pesos") |
| E13 | "lista de proveedores" | 10.085 | ruído. Descartado |
| E14 | "plantillas para psicólogos" | 43 | ferramentas clínicas (Psicoresumen, Psicología & Recursos, Miss Sami, Kits Digitales). **Pack de posts pra Instagram por nicho não apareceu** |
| E15 | "kit para novias" | 78 | ruído (maquiagem, roupão). Descartado |
| E16 | "papelería de boda" | 48 | Canva para novias (1387388674447383, USD, **6 ads, 0,3 d**: clone em ES de "Canva Para Noivas", loja impultienda.ar), PRO Rsvp (570945829440708, USD), papelarias físicas |
| E17 | "diseños para tazas" | 852 | Sublimador 360 (114741977104223, USD), Mundo Digital (CLP, "$3.500"), PP Studio (USD, "Quien se adelanta, vende con más tiempo 🎄"), Sublimastery, Mi Vida Perfecta. Muita loja física |

Anunciantes ES checados por page_ids:
- Mi Cuento Infantil Personalizado (166953813165193): 25 ativos, o mais antigo com 43,3 d (MXN). Ângulos: Toy Story 5, super-herói, princesa, "Guerrera K-POP", "Quiero mi Video Personalizado". Exemplo: https://www.facebook.com/ads/library/?id=1756985529330960 . Formato (impresso ou digital) não verificado.
- Cabina de Fotos Lucrativa (536403069546446): 4 ativos, 7,8 d, BRL. https://www.facebook.com/ads/library/?id=1710483000052810
- Casa Taro (1186126027917061): 1 ativo, 9,9 d. https://www.facebook.com/ads/library/?id=2281478862393729
- Canva para novias ES (1387388674447383): 6 ativos, 0,3 d, USD. https://www.facebook.com/ads/library/?id=1090593597009231
- Paquete De Diseños (107416171593294): 33 ativos, 7,4 d, USD. https://www.facebook.com/ads/library/?id=1114178547856206

Buscas ES que outro agente já tinha rodado (fase1_meta_kits.md) e cito como referência: "invitaciones digitales para vender" 88; "kit de cumpleaños editable" 26; "fiesta en Canva plantillas" 150; "diseños para sublimar" 189; "plantillas para tazas sublimación" 109; "moldes cajas para vender" 60; "cajitas personalizadas moldes para vender" 20; "agendas 2027 para vender" 107; "archivos de corte cricut" 15; "cake topper editable" 0.

## 4. Tabela PRINCIPAL — PT (BR) x ES lado a lado

Saturação ES: "pouco explorada" = 0–2 anunciantes digitais e nenhum com 10+ ads ou 30+ dias; "média" = 3–8 anunciantes, ou 1–2 fortes; "saturada" = muitos anunciantes, vários com 10+ ads, e/ou anunciantes brasileiros (BRL) já arbitrando.

| # | ideia | BR: count / anunciantes / melhor anunciante (ads, dias) | ES: count / anunciantes / melhor anunciante | saturação ES | DNA Mimo | eliminatória suspeita |
|---|---|---|---|---|---|---|
| 1 | Livro/conto infantil personalizado digital (a criança vira protagonista, editor -> PDF/flipbook) | "livro personalizado" 888; ≥4 (Sua Historinha 95 ads [limite]; Crie Sua História 15 ads/75,6 d; Make My Memo; Arca dos Livros) | "libro personalizado" niño protagonista 15; "cuento personalizado" 1.240 (ruído); 4 (Mi Cuento Infantil Personalizado 25/43,3 d; Adorabook 11/52,2 d; MiBook 3/60 d; Erase 1 vez) | **média** (a maioria parece livro impresso e caro, não verificado; versão digital instantânea low ticket não foi vista) | alto: personalizado, demonstrável na tela, ângulos (personagem, data, idade) | E3 leve (custo de IA por livro, se gerar ilustração); E5 (consistência do personagem via IA em 14 dias) |
| 2 | Editor de convite digital interativo (self-service: preenche e recebe o link) | "convite interativo" 598; Convitia 33/76,9 d; Canva Para Noivas vende "convite interativo R$47"; dezenas de conviterias | "invitación digital interactiva" 129; ~12 anunciantes, quase todos serviço sob encomenda ($119–399 MXN, S/100); nenhum editor self-service | **pouco explorada** (formato ferramenta); média (formato serviço) | altíssimo: editor -> página, música, contagem regressiva, RSVP; ângulos boda, XV años, baby shower, bautizo, cumpleaños | E3 se virar serviço manual; E5 moderada (editor + templates) |
| 3 | Papelaria de casamento editável no Canva (convite + menu + placas + convite interativo) | Canva Para Noivas 35/88,9 d (R$47–67); Clube das Noivas 3 (R$19,90); JoHerinher "CANVA PARA CASAMENTO"; Hotmart "Kit de Papelaria de Casamento Editável" | "papelería de boda" 48; clone "Canva para novias" 6 ads/0,3 d; PRO Rsvp | **pouco explorada** (1º clone acabou de entrar) | médio-alto: pronto na hora; demonstrável; bump (convite interativo, save the date) | nenhuma óbvia; teto limitado a noivas |
| 4 | Pack de convites e kit festa editável no Canva (aniversário, temas infantis) | "kit festa editável" 74; Festa 550 17/35,7 d; Pack sublimação "Kit Festa na Mesa R$3,99"; Melhores Noticias (+1.000 kits, novo); Hotmart "Kit Festa 2.0" US$5 | "invitaciones editables" 345; ≥10 anunciantes (3 BRL); Hotmart ES "Kits para fiestas 100% editables en Canva" US$17; Activa Academy 33,1 d | **saturada** | médio (demonstrável, ângulos por tema) | E2 se vendido como "para revender" |
| 5 | Topos de bolo prontos para imprimir (mega pack) | "topo de bolo" 1.307 (maioria física); Pack sublimação "20 Mil Topos R$1,49" 5 ads/33,5 d; Artes Digitais "1.600 Topos" (novo, USD) | "toppers para pastel" 55 (maioria física); Emilia Creativa "+1.200 Cake Toppers" 2 ads/11,5 d; "cake topper editable" 0 | **pouco explorada** | médio (demonstrável; ângulo mãe que faz a festa ou confeiteira que vende) | E2 parcial (ângulo "pra vender"); E4 se virar PLR revendável |
| 6 | Arquivos e projetos para corte a laser/MDF | "arquivos de corte" 353; Biblioteca do Corte 18/2,1 d; Giullia Pereira "+100 mil projetos"; CorelBot | "archivos para corte láser" 126; ≥9 anunciantes (2 BRL); Paquete De Diseños 33/7,4 d | **saturada** | baixo-médio (público precisa ter máquina) | E2 (vende "pra lucrar"); teto limitado a donos de máquina |
| 7 | Artes para sublimação (canecas etc.) | "artes para sublimação" 280; Pack Pronto R$19,90; Vinics R$39,90; KIT Estamparia; Bru Artes | "diseños para tazas" 852 (ruído); ref. "diseños para sublimar" 189; Sublimador 360, Mundo Digital, PP Studio, Sublimastery | **saturada** | baixo (precisa ter a máquina) | E2 |
| 8 | Molduras editáveis para photobooth/cabine de fotos | Cabine Lucrativa 9/4,1 d ("+500 molduras") | "marcos para photobooth" 7; só Cabina de Fotos Lucrativa (**BRL**, 4 ads/7,8 d) | **pouco explorada** (o 1º arbitrador BR já entrou) | médio (demonstrável), mas nicho B2B pequeno | E2 parcial; teto baixo |
| 9 | Kit de brincadeiras imprimível para chá (lingerie, bebê, revelação, despedida) | Chá de Langerie Pronto 8/38,2 d; no web, kits de 3 a 6 jogos (Elo7, Estúdio Creatus) | "juegos para despedida de soltera" 27 e "juegos para baby shower" 451: **nenhum kit digital visto** | **pouco explorada** (demanda ES não verificada) | médio-alto: compra por impulso, ângulos (chá bar, bebê, revelação, despedida, XV), bumps baratos | nenhuma óbvia; E5 baixo (dá pra montar no Canva) |
| 10 | Ensaio fotográfico com IA (selfie -> fotos temáticas) | "ensaio com IA" 3.162; Marcos Studio IA 54 ads (limite); Studio Boss R$10,90; WB Studio; Arthur Tomaz | "sesión de fotos con IA" 414; ≥12 anunciantes, **≥10 em BRL (arbitragem PT->ES já em curso)** | **saturada** | alto (demonstrável, ângulos: aniversário, gestante, mães, formatura) | E3 (muitos entregam à mão via WhatsApp; API tem custo por pedido) |
| 11 | Música/canção personalizada com IA | "música personalizada" 3.333; ≥10 anunciantes (R$5,99–29,90); Felicidade em Música 16/4,7 d | "canción personalizada" 4.003; ≥8 anunciantes (Diego Hernandez com muitos ads; DedicatieMuzicala; Ana Alice em **BRL**) | **saturada** | alto (reação emocional, ângulos) | E3 (custo de geração por música + revisão) |
| 12 | Vídeo personalizado do Papai Noel | "vídeo personalizado do Papai Noel" 39; Recado do Noel 24 ads (Natal 2025, ainda ACTIVE, 275 d); Recadinho do Noel ("10 Mil Pais") | "video personalizado de Santa Claus" 0; "video de Santa Claus" (ALL) só ruído: **não verificado** (fora de temporada) | **não verificado** | alto (reação da criança), mas sazonal (nov–dez) | E5 moderada (template de vídeo + voz IA); sazonalidade limita o teto |
| 13 | Posts prontos no Canva por nicho profissional (psicóloga, nutri, clínica) | Pack Canva Para Você 14/10,3 d (R$59,90); Adestra Pack; Templates para Veterinárias; Packs Profissionais (USD) | "plantillas para psicólogos" 43 (ferramentas clínicas, não posts); ref. "plantillas canva para emprendedoras" 77 | **pouco explorada** (formato "posts pra Instagram por profissão") | médio: ângulo por profissão; demonstrável; pouco impulso | E2 leve; preço BR acima da faixa |
| 14 | Projetos prontos de serralheria/marcenaria | "projetos prontos" 4.444 (ruído); Júlia Castanhari "+5.000 Projetos" (2 ads, novo) | "proyectos de herrería" 716 (ruído); Planos y Diseños de Herrería (MXN); Alejandro García e Carlos Mendoza (**BRL**, "$5–6"); ref. CarpinteriaPro 900 | **média** (arbitradores BR presentes) | baixo | E2; E4 se for PLR |
| 15 | Kits sazonais "prontos pra vender" (Halloween, Dia das Crianças, Natal, calendário 2027) | Flor de Cactos (Kit Halloween e Kit Dia das Crianças "prontos pra vender"); Bastidores da Tarcy (Calendários 2027, 1 ad); Kit Dia da Criança Pronto 11/4,2 d (professor) | PP Studio (Navidad); ref. "agendas 2027 para vender" 107; "navidad para vender diseños" 270 | **média** | médio (sazonal, repetível a cada data) | E2 (promessa de venda) |
| 16 | Moldes de caixinhas personalizadas (copo twister, festa) | Universo dos moldes 5/0,4 d | ref. "moldes cajas para vender" 60; "cajitas personalizadas moldes para vender" 20 | **média** | baixo-médio | E2 |

Ideias descartadas nesta fonte: lista de fornecedores (E2, e o termo ES é só ruído), cardápio digital (ruído), currículo (serviço humano, E3), retrospectiva de namorados (é a categoria do próprio Mimo; lovecupido 101,6 d e Presentim 144,5 d confirmam que ela dura no BR).

## 5. Achado transversal: a arbitragem PT->ES já está acontecendo

Anunciantes com moeda BRL rodando criativos em espanhol, nos 50 mais novos de cada busca ES:
- Ensaio com IA: ≥10 páginas (Aura IA Studio, Aurelia Studio, Ensaio IA Premium, Milena • Ensaios com IA, Yasmim & Hiago Ensaios IA, Luciana Duarte, Gabriel Marketing IA, Eugenia Silva, Juan Carlos Ia, Carla Rodrigues)
- Canção: Ana Alice
- Corte a laser: Mega Pack Deseños Laser, Mega Pack Cortes a Laser
- Kit festa e convites: Fiesta Digital, Fiesta Lista, Bruno Lero
- Photobooth: Cabina de Fotos Lucrativa
- Serralheria: Alejandro García, Carlos Mendoza
- Outros: Cajitasencasa (topper), El Mundo de los Bloques (kit bíblico 3D), PixelKits (visto pelo outro agente)

Leitura (inferência, não medição): onde já existem vários anunciantes BRL em ES, a janela de arbitragem está fechando (ensaio IA, canção, laser, kit festa). As categorias em que o BR tem anunciante com 30+ dias e o ES ainda não tem nenhuma versão self-service ou digital low ticket são: **editor de convite interativo (Convitia 76,9 d x 0 editores ES)**, **papelaria de casamento no Canva (Canva Para Noivas 88,9 d x clone ES de 0,3 d)**, **livro infantil personalizado digital (Crie Sua História 75,6 d e Sua Historinha 95 ads x ES com anunciantes de livro físico)** e **kit de brincadeiras de chá (38,2 d x 0 em ES)**.

## 6. Preços observados (snippets de busca, não verificados no checkout)

- Convite digital interativo BR (serviço): R$37 (convitedigitalinterativo.com.br), R$42 (Instagram), R$59,90–99,90 (Personalize Conviteria), R$60 (UniConvite), R$80 (Oh Personalizados). Fonte: WebSearch "Convitia convite digital interativo preço" -> https://convitedigitalinterativo.com.br/ , https://www.personalizeconviteria.com.br/digitais/convites1/convite-digital-interativo-compartilhe-com-links/ , https://uniconvite.com.br/produtos/convite-digital-interativo-com-links-para-direcionar-o-seu-convidado/
- Canva Para Noivas: R$47 (convites interativos, 6 convites), R$67 (papelaria inteira), pelo link_title dos anúncios.
- Convite interativo ES (serviço): $119 MXN (Eventika), $399 MXN (Invytia), S/100 (TarjetaViva), pelo link_title.
- Kit festa Hotmart: "Kit Festa 100% Editável no Canva - 2.0" US$5 (https://pay.hotmart.com/Q103662817T?checkoutMode=10); "Kits para fiestas 100% editables en Canva" US$17 (https://pay.hotmart.com/F103010959C?off=a1kavqsu&checkoutMode=10); "Kit de Papelaria de Casamento Editável (Canva)" (https://hotmart.com/pt-br/marketplace/produtos/kit-de-papelaria-de-casamento-editavel-canva/Q105352299G, preço não visto).
- Livro infantil com IA: ImaginaCuentos a partir de R$29,90 em PDF (https://imaginacuentos.com/en/livros-personalizados-para-criancas ; a marca tem nome espanhol, o que sugere presença em ES, não verificado); Livro Mágico Infantil ebook 6,99 € (https://livromagicoinfantil.pt/); FabulAI (https://fabulai.com.br/); ToonyStory R$24,90/mês (https://toonystory.com/pt).
- Kit de brincadeiras de chá de lingerie: produto digital com download imediato (https://estudiocreatus.com.br/produto/kit-com-6-brincadeiras-de-cha-de-lingerie-preto-e-vermelho/ , https://www.elo7.com.br/lista/kit-de-brincadeiras-cha-de-lingerie). Preço não visto.
- Música personalizada BR: R$5,99–29,90 (títulos de anúncio). Ensaio IA BR: "a partir de R$10,90".

## 7. Falhas e limitações

- "canción personalizada" (ES) devolveu 95.793 caracteres e estourou o limite. Salvei em arquivo e li com jq: count 4.003, 50 anúncios lidos por inteiro.
- "video personalizado de Santa Claus" = 0 e "video de Santa Claus" (ALL) = só ruído. Papai Noel em ES ficou **não verificado** (fora de temporada).
- As buscas entre aspas não são frase exata: cardápio digital, lista de proveedores, proyectos de herrería, kit imprimible, cuento personalizado e renda extra trazem muito ruído. Os counts dessas buscas não servem para comparar.
- Para páginas com 50+ anúncios (Sua Historinha 95, Marcos Studio IA 54), o anúncio mais antigo real não aparece.
- Preço, order bumps e faturamento de nenhuma oferta foram verificados em checkout (Hotmart, Kiwify e similares bloqueados). Tudo que está acima é proxy.
- Para Mi Cuento Infantil Personalizado, Adorabook e MiBook não deu pra saber se o livro é impresso ou digital (sem corpo do anúncio).
