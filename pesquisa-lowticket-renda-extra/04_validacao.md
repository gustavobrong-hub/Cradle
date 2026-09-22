# 04 · Validação: L02 Invitaciones web

Data: 22/09/2026.

**A decisão da Fase 5.** Lançar primeiro o **L02**, um editor de convite web com envelope animado, música, contagem, fotos, "Cómo llegar" e confirmação de presença com painel. O lançamento é **só em espanhol** e é uma **aposta limitada**, com teto de aprendizado de US$ 2.000. Não é um segundo Mimo. O painel votou 3/3 no L02, mas nenhuma finalista tem teto estimado acima do Mimo: o L02 fica em US$ 150–400/dia em ES (base 250) e em 200–750 com PT/EN/FR, com confiança baixa [estimativa].

**Convenções:**
- [premissa]: número assumido, a confirmar na Etapa 2;
- [estimativa]: conta do dossiê;
- [inferência]: leitura de prática, sem fonte;
- [medido]: Biblioteca de Anúncios ou página com link.

Os valores estão em US$; entre parênteses vai o valor em R$ ao câmbio de 22/09/2026 (1 US$ = R$ 5,14), porque a conta de anúncios é em BRL e o UTMify mostra BRL. Refazer a conversão se o câmbio andar mais de 5%. Produto, oferta, ganchos (H01–H15) e formatos (F1–F5) estão detalhados em `03_top3/invitaciones-web.md`.

## Resumo

1. **Etapa 1 (26/09–02/10, ~US$ 340, sem checkout).** Campanha de cadastro no México levando a uma página de "acceso anticipado". A página tem convites de exemplo reais e navegáveis e diz com todas as letras que o editor está em construção e que nada é cobrado agora. Para isso, o build é reordenado: a página pública do convite e o RSVP de exemplo saem no D2–D3, antes do editor (seção 5). Roda em paralelo ao build e decide antes do soft launch:
   - os ganchos;
   - apresentadora de IA ou só demo;
   - se o ângulo de revenda tem gancho (teste só de lead, sem venda). Passar é condição para abrir o conjunto REV, que só entra depois do K2;
   - o peso de cada evento.

   Se nem a premissa otimista pagar o break-even, a ideia morre antes de gastar o K2.
2. **Etapa 2 (a partir de 05/10).** O MVP vai à venda: front de US$ 9,90 em moeda local, com o preço travado (sem o A/B 9,90 × 7,90 do dossiê; seção 3.2), 4 bumps e sem upsell. São 3 conjuntos ABO (MX · CO+PE+CL · AR+EC+GT+DO) a US$ 70/dia. Marcos: K2 em ~11–13/10; K4 e K5 em 15/11; escala de 28/12 a 28/02; teste de teto em 28/02/2027.
3. **Toda régua sai de duas contas:** CPA para ROI 1,5 = 5,23 e break-even = 7,85 (conta BRL, líquido base de 8,79). Aos 100 compradores, refazer as duas com o líquido medido.
4. **A infra fica separada do Mimo em tudo que a Meta e a Hotmart permitem:** portfólio, conta de anúncios, cartão, dataset, domínio, página e Instagram, produto Hotmart, backend e dashboard UTMify. O perfil pessoal e a conta de produtor da Hotmart continuam os mesmos, então quem protege o Mimo de verdade é o compliance, não a separação.
5. **Janeiro:** a força do L02 vem das bodas de fev–mai e do CPM mais barato. A "cuesta de enero" não entra: é ângulo proibido (atributo pessoal) e não combina com um produto vendido para uso próprio.

## 1. Réguas (de onde saem todos os cortes)

| Régua (conta BRL, front 9,90) | Conta | US$ | R$ |
|---|---|---|---|
| Líquido por comprador, cenário base [estimativa] | front 7,33 + bumps 1,73, menos 3% de reembolso | 8,79 | 45,18 |
| **Break-even** (ROI 1,0) | 8,79 ÷ 1,12 | **7,85** | 40,35 |
| Continuar pequeno (ROI 1,25) | 8,79 ÷ 1,40 | 6,28 | 32,28 |
| **Alvo** (ROI 1,5) | 8,79 ÷ 1,68 | **5,23** | 26,88 |
| Pausa de anúncio sem venda | 2 × alvo (= 1,33 × break-even) | 10,46 | 53,76 |

- **ROI = faturamento líquido ÷ gasto em anúncios somado aos 12% de imposto da conta BRL.** O líquido é o que sobra na Hotmart depois de taxas e reembolsos. Os CPAs da tabela são os que o Gerenciador mostra, sem imposto.
- **Aos 100 compradores:** alvo = líquido medido ÷ 1,68; break-even = líquido medido ÷ 1,12. Até lá, valem 5,23 e 7,85.
- **Taxa da Hotmart:** as réguas usam o modelo antigo (10,95% + US$ 1,49), mas o digest registra o fim da taxa do Player em 21/09/2026 ([Hotmart](https://help.hotmart.com/es/article/208298448/-cuales-son-las-tarifas-cobradas-por-hotmart-); não verificado). Abrir o detalhe da 1ª venda real (front + bump). Os regimes são os da seção Contas do dossiê:
  - **R3, taxa fixa em cada bump** (9,9% + US$ 1,00 por transação, inclusive em cada bump): o alvo até **melhora**, para 5,35. O problema é o B1 a 3,90, que fica com só 64% do preço (seção 3.6).
  - **R4, o cenário do red team:** os ~26% descontados do front vêm de imposto e conversão **e** a taxa fixa sobe para US$ 1,00. O líquido cai para ~8,0 e o alvo, para ~4,77. Se a 1ª venda indicar o R4, tratar 5,23 como cenário otimista.
- **Variações por país:**
  - hispanos nos EUA a US$ 12,90: alvo 6,77, break-even 10,16;
  - AR em USD: se o produtor pagar os 9,5% da conversão de ARS ([Hotmart](https://help.hotmart.com/es/article/360015794612/-en-que-moneda-obtendre-mi-comision-); quem paga não verificado), o líquido cai ~US$ 1,1. O alvo de AR vira 4,58 e o break-even, 6,87.

## 2. Etapa 1: gancho e ângulo antes de terminar o build (26/09–02/10)

### 2.1 Mecanismo

**O que vai ao ar:**
- **Página de "acceso anticipado"** no domínio novo, com **3 convites de exemplo reais e navegáveis**: XV años, cumpleaños infantil e baby shower.
  - No exemplo, o envelope abre ao toque, a música toca e a contagem corre. Há galeria, cartão "Cómo llegar" e uma confirmação de presença que mostra um painel com "Datos de ejemplo".
  - São a página pública do convite e o RSVP de exemplo, **antecipados para o D2–D3** no build reordenado (seção 5). No cronograma do dossiê eles ficavam no D5 e no D6, depois de 26/09. Depois viram os exemplos da landing e a matéria-prima dos criativos, então nada é jogado fora.
- **Lista de espera grátis**, com estes campos:
  - correo, obrigatório;
  - "¿Qué vas a celebrar?": XV años / Cumpleaños infantil / Baby shower / Boda / Otro;
  - "¿Cuándo es?": mês;
  - "¿Para quién es?": Para mi evento / Hago invitaciones para otras personas;
  - WhatsApp, opcional e com caixa de consentimento.
- **Textos da página (ES):**
  - "Estamos terminando el editor. Planeamos abrir en octubre."
  - "Cómo va a funcionar: la creas gratis desde el celular, la ves completa antes de pagar y pagas una sola vez para publicarla (link sin marca de agua, QR y lista de confirmaciones)."
  - "No cobramos nada ahora y no es una preventa. Te escribimos cuando abra; puedes darte de baja cuando quieras."
  - Botão: "Avísenme cuando abra".
- **Variante da página para a célula de revenda:** "¿Haces invitaciones para otras personas? Muy pronto vas a poder crearlas desde el celular y entregarlas con link, QR y lista de confirmaciones. Paquete de 5 invitaciones con licencia de uso para clientes. No incluye reventa del editor ni de los modelos."
- **Textos dos anúncios:**
  - Células A, B e C: "Muy pronto: invitaciones web con sobre animado, música, cuenta regresiva y lista de confirmados. Únete a la lista y te avisamos cuando abra." Título: "Acceso anticipado". CTA: "Registrarte".
  - Célula D: "Muy pronto: si haces invitaciones para otras personas, vas a poder crearlas desde el celular y entregarlas con link, QR y lista de confirmados."

**O que não existe na Etapa 1:**
- checkout e link da Hotmart: o produto fica em análise, sem link exposto;
- preço, pré-venda, desconto para a lista, "cupos limitados" e contador;
- "porta falsa", o botão "Comprar" que leva a "aún no disponible". Ela mede intenção, mas engana quem clicou.

**Regras de texto só desta etapa:**
- "Muy pronto" na 1ª linha do texto principal e no end card, mas fora dos 3 s iniciais. Assim o hook rate fica comparável com o da Etapa 2.
- Nenhum gancho diz "lista hoy" ou "créala ya":
  - o H04 vira "La invitación de sus XV, con música y cuenta regresiva";
  - o H10 vira "Vas a poder crearla gratis. Pagas solo si la publicas."

**Se a Etapa 1 matar a ideia:** mandar um e-mail à lista avisando que o produto não vai abrir e apagar os dados em até 30 dias.

### 2.2 Estrutura e orçamento

**Campanha `INV_E1_LEAD_2640`.**
- **Objetivo Cadastros**: conversão no site, com o evento Lead = inscrição na lista.
- **ABO** com orçamento igual por célula, porque o que se compara é célula contra célula.
- **Só MX**, 18+, sem interesses, posicionamentos Advantage+ (9:16, com versão 4:5 no mesmo anúncio).

**Por que só o MX:**
- é o maior público (93,5 M no Facebook, [DataReportal](https://datareportal.com/reports/digital-2026-mexico));
- tem a maior densidade de anúncios de "invitaciones digitales": 849 dos 1.283 de ES + US [medido, [busca no MX](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&q=invitaciones%20digitales&search_type=keyword_unordered); o link reproduz só o MX, e a soma de ES + US foi feita via API em 22/09/2026];
- pesa 45% da Etapa 2;
- fala um locale só ("tú", "XV años");
- tira o ruído de país da comparação.

| Conjunto | Célula | Corpo | Ganchos (na tela e na voz) | Página | US$/dia | Datas | Total US$ |
|---|---|---|---|---|---|---|---|
| E1-A | Uso próprio, só demo (controle) | F1 "El sobre", só tela, 15 s | H01, H04, H08 | uso próprio | 12 | 26/09–02/10 | 84 |
| E1-B | Uso próprio, apresentadora de IA | A mesma gravação, voz e duração do A. A apresentadora diz o gancho em close nos 0–3 s e depois fica num balão no canto, com o rótulo "Presentadora virtual · IA" | H01, H04, H08 | uso próprio | 12 | 26/09–02/10 | 84 |
| E1-C | Ganchos e eventos | F1 | H05 (infantil), H06 (baby shower), H10 (reescrito), H13 (contraste) | uso próprio | 12 | 26/09–02/10 | 84 |
| E1-D | Revenda (licença do B4) | F1 com end card da licença | H14 "¿Haces invitaciones para otras personas?", H15 "Te la piden por mensaje. Así la entregas.", H14b "Invitaciones web para tus clientes, hechas en el celular" | revenda | 17 | 28/09–02/10 | 85 |
| **Total** | 13 anúncios | | | | 36 → 53 | 7 dias | **~337 (≈ R$ 1.730)** |

**O que cada comparação isola:**
- **IA ou só demo (A × B):** o mesmo gancho de texto em 2 corpos que só diferem pela apresentadora. A diferença medida é da apresentadora, não do gancho nem da duração.
- **Ganchos (A + C):** o mesmo corpo (F1) com 7 ganchos diferentes.
- **Ângulo (A × D):** o mesmo corpo; D troca gancho, texto, end card e página. Comparar só nos dias em comum (28/09–02/10).
- **Eventos:**
  - pelo formulário de todos os leads (evento e mês);
  - pelo CPL dos ganchos de evento: H04 XV, H05 infantil, H06 baby shower.

  A boda aparece só como opção do formulário, para medir o interesse para jan–fev.

**Notas de operação:**
- **D começa 48 h depois das outras.** A conta nova ainda tem pouca confiança, e a revenda é o único ângulo que encosta em "oportunidade econômica" [inferência]. A, B e C precisam estar aprovados e entregando antes.
- **Se o limite de gasto inicial da conta nova for menor que US$ 53/dia,** reduzir **todos** os conjuntos na mesma proporção e estender até 04/10. Nunca cortar só uma célula.
- **O F2 (editor) fica para a Etapa 2**, porque o editor ainda não existe.

### 2.3 Métricas

| Métrica | Definição | Uso |
|---|---|---|
| Hook rate | reproduções de 3 s ÷ impressões | Diagnóstico, comparado com a mediana da semana |
| Hold | ThruPlays ÷ reproduções de 3 s | Diagnóstico |
| CTR e CPC de link | cliques no link ÷ impressões; gasto ÷ cliques no link | **Corte** (seção 2.4) |
| Clique → lead | inscrições ÷ cliques no link | Premissa da Etapa 2 |
| **CPL** | gasto ÷ inscrições | **Corte** e custo por resultado nas comparações |
| Abertura de exemplo | ViewContent ÷ visitas à página | Diagnóstico da demo |
| Evento e data | % de leads por evento; % com evento em 2–12 semanas | Peso dos eventos; premissa do público "em compra" |
| "¿Para quién es?" | % de "Hago invitaciones para otras personas" | Demanda orgânica pela licença |
| Comentários negativos | "estafa", "es IA", "¿es gratis?" por 1.000 impressões | Custo de confiança da IA |

### 2.4 Cortes derivados do break-even (a conta)

**Premissa de funil [premissa]:** clique → lead de 20–30% × lead → compra de 10–15% = **clique → compra de 2–4%**. O centro é 3% (25% × 12%). Por quê:
- É freemium em três passos: abrir o editor, deixar o e-mail para salvar a prévia e pagar para publicar.
- O dossiê do L29 usou 2,1% de compra por clique, com o mesmo mecanismo e um "aha" mais fraco.
- O L02 tem motivo mais forte para pagar: o convite só existe publicado e o evento tem data. Por isso o centro fica acima, em 3%.
- O lado otimista (4% e 15%) só entra nos cortes de morte.

**As contas:**
- CPC máx. = CPA × (clique → compra);
- CPL máx. = CPA × (lead → compra);
- **CTR mín. = CPM observado ÷ (1.000 × CPC máx.)**.

| Clique → compra | CPC máx. para ROI 1,5 (CPA 5,23) | CPC máx. para break-even (CPA 7,85) |
|---|---|---|
| 2% | 0,10 (R$ 0,54) | 0,16 (R$ 0,81) |
| **3% (centro)** | **0,16 (R$ 0,81)** | **0,24 (R$ 1,21)** |
| 4% (otimista) | 0,21 (R$ 1,08) | **0,31 (R$ 1,61)** |

| CPM observado na Etapa 1 | CTR mín. para ROI 1,5, a 3% | CTR mín. para break-even, a 3% | CTR mín. para break-even, a 4% (corte) |
|---|---|---|---|
| US$ 2 (R$ 10,3) | 1,27% | 0,85% | 0,64% |
| US$ 3 (R$ 15,4) | 1,91% | 1,27% | 0,96% |
| US$ 4 (R$ 20,6) | 2,55% | 1,70% | 1,27% |
| US$ 5 (R$ 25,7) | 3,19% | 2,12% | 1,59% |

| Lead → compra | CPL máx. para ROI 1,5 | CPL máx. para break-even |
|---|---|---|
| 10% | 0,52 (R$ 2,69) | 0,79 (R$ 4,03) |
| **12% (centro)** | **0,63 (R$ 3,23)** | **0,94 (R$ 4,84)** |
| 15% (otimista) | 0,78 (R$ 4,03) | **1,18 (R$ 6,05)** |

**Viés conhecido.** Os dois vieses da Etapa 1 vão em sentidos opostos:
- anúncio com "Muy pronto" tende a receber menos clique, então o CPC sai pior que o real [inferência];
- lead de lista de espera tende a comprar menos que o e-mail deixado dentro do editor, então o CPL parece melhor do que vale [inferência].

Por isso o corte de morte exige falhar mesmo com a premissa otimista, e o verde exige passar na premissa central.

**Pausa por anúncio (só no E1-C):**
- gasto ≥ US$ 2,83 (3 × 0,94; R$ 14,55) sem nenhum lead; ou
- ≥ 3.000 impressões com CTR abaixo da coluna "corte" para o CPM do próprio anúncio.

Em A, B e D, nenhum anúncio é pausado por desempenho durante os 7 dias, porque pausar um lado desequilibra a comparação. Nas quatro células, reprovação ou comentário que indique engano tira o anúncio do ar.

### 2.5 Decisões

Para ler a Etapa 1, cada conjunto precisa de ≥ US$ 70, e cada célula comparada precisa de ≥ 40 leads. Abaixo disso, a comparação é inconclusiva e vale o padrão: só demo, com a revenda fechada.

| Quando / pergunta | Regra | Ação |
|---|---|---|
| **29/09 (D7), checkpoint**, com ~US$ 36 por conjunto | A, B e C todos com CPL > 2,36 **e** CPC > 0,62 (2× o corte otimista) | Congelar o build antes do D7 (checkout, painel, PDFs) e ir direto para a rodada extra de ganchos. Poupa ~5 dias de build |
| **03/10: a ideia segue?** Olha o melhor conjunto de uso próprio (A, B ou C) | **Verde:** CPL ≤ 0,94 e CPC ≤ 0,24 · **Amarelo:** CPL ≤ 1,18 e CPC ≤ 0,31, sem ser verde · **Vermelho:** CPL > 1,18 ou CPC > 0,31 | **Verde:** Etapa 2 como planejada. **Amarelo:** Etapa 2 sem a célula de revenda, concentrada nos 3 melhores ganchos + novos. **Vermelho:** uma rodada extra de US$ 100 com 6 ganchos novos (03–05/10; o soft launch cai para ~08/10). Se continuar vermelho, não lançar |
| Vermelho: a culpa é do CPM ou do criativo? | CPM ≥ 1,3× o do Mimo no MX na mesma semana **e** CTR acima do "corte" calculado com o CPM do Mimo | Culpa do CPM: adiar para 26/12, quando o CPM fica mais barato. Senão: **matar**, avisar a lista e voltar a atenção para o Mimo |
| **IA ou só demo** (CPL de B ÷ CPL de A) | Com ~40–100 leads por célula, diferença < 25% é ruído [estimativa] | **B ≤ 0,8× A:** IA em até 1/3 do volume (teto da decisão). **0,8–1,25×:** empate; IA em ≤ 1/6, só para diversificar. **B ≥ 1,25× A**, hook rate ≤ 0,8× ou o dobro de comentários negativos: sem IA na onda 1; reavaliar em janeiro |
| **O gancho de revenda passa?** Teste só de gancho e lead, sem venda (CPL de D ÷ CPL de A, nos mesmos dias) | Passa se cumprir tudo: CPL de D ≤ 1,3× o de A; ≥ 40 leads em D; ≥ 50% dos leads de D marcando "Hago invitaciones para otras personas"; zero reprovação | **Passa:** o ângulo fica elegível para o conjunto REV, que só abre **depois que o B2C passar no K2**, com ≤ 20% da verba e só criativos de demonstração (seção 3.2). **Falha em qualquer item:** o REV não abre, e a licença segue só como o bump B4 |
| **Peso dos eventos** | % de leads por evento (XV, infantil, baby shower) | Volume de criativos da onda 1 proporcional a essa fatia, com piso de 20% por evento. Boda só a partir de 28/12 |
| **Público "em compra"** | % de leads com evento em 2–12 semanas | Se < 50%: usar 10% (e não 12%) de lead → compra nas contas da Etapa 2 |

### 2.6 O que a Etapa 1 não responde (fica para a Etapa 2)

| Premissa | Como a Etapa 2 confirma |
|---|---|
| Clique → compra de 2–4% | Funil do app: clique → editor → e-mail → prévia → checkout → compra |
| Lead de lista vale o mesmo que lead do editor | Comparar a compra da lista no lançamento (`utm_source=lista`) com a compra do lead do editor |
| Alguém paga US$ 9,90 quando existe o grátis e o designer a MXN 89 ([exemplo](https://www.facebook.com/ads/library/?id=1802415467419849)) | Só o K2 responde |
| Prévia → pagamento | K7, comparando com a taxa do Mimo |
| Adesão aos bumps, reembolso e regime de taxa | K3, aos 100 compradores |
| CPM de campanha de venda | Otimizar por compra costuma sair mais caro que por cadastro [inferência]: refazer o CTR mín. com o CPM da Etapa 2 (K6) |
| O ranking de ganchos vale com o end card real | Os vencedores da Etapa 1 entram trocando só o end card, que vira "Créala gratis y mírala antes de pagar" |

## 3. Etapa 2: teste de venda com o MVP (05/10 → 15/11; escala de 28/12 a 28/02)

### 3.1 Pré-requisitos (K0)

- **MVP vendável** no D11 (~03/10). Se não estiver vendável até o D14 (06/10), é **sinal de alerta**, não corte: o soft launch escorrega e o plano segue. **Limite duro: 20/10.** Depois disso, não lançar no Q4 e subir só em 26/12.
- **Música** tocando no iPhone dentro do navegador do WhatsApp e do Instagram.
- **Compra e reembolso reais:** compra em 2 países, OXXO ficando pendente e reembolso que tira o convite do ar.
- **Hotmart:** produto e 4 bumps aprovados; oferta em moeda local conferida. Se não houver moeda local, cobrar em USD e não mostrar preço local no anúncio nem na landing.
- **Rastreio:**
  - Purchase chegando ao dataset novo pelo navegador e pelo servidor, deduplicado;
  - a venda de teste aparece no UTMify com a UTM certa.
- **Temas:** 3 temas originais para cada evento (XV, infantil, baby shower), sem personagem licenciado e sem tema de casal ou presente.
- **Etapa 1:** decisões aplicadas.

### 3.2 Estrutura e orçamento

**Onda 1, de 05/10 até o K2 (~6 dias).** Campanha `INV_E2_VENDAS_2641`, objetivo **Vendas**.
- **Otimização por Purchase desde o dia 1.** A US$ 70/dia, com CPA de 5–8, saem ~9–13 compras/dia [estimativa], o que basta. Otimizar por um evento do meio do funil compra clique barato que não paga [inferência].
- **ABO com orçamento fixo até o K2.** CBO com dataset novo joga tudo no país e no anúncio mais baratos e esconde a leitura [inferência].
- **Preço travado em 9,90, sem o A/B 9,90 × 7,90 do dossiê.** Três motivos:
  - **Não há amostra.** O K2 sai com ~51 compras (US$ 400 ÷ 7,85). Para detectar uma diferença de 25% na conversão são precisas ~150–250 compras por braço [estimativa, dossiê], e com ~25 por braço o A/B não enxerga nada.
  - **Divide a régua.** Cada braço teria o seu break-even (7,85 a 9,90; 6,30 a 7,90) e só metade das compras; o K2 deixaria de ter uma leitura única.
  - **O 7,90 exige CPA de 4,20** para ROI 1,5 em BRL, 20% abaixo do alvo de 5,23. Ele só empata se converter ≥ 1,25× o 9,90.

  O 9,90 continua sendo decisão de preço a validar no teste. Depois do K2 aprovado, testar **para cima** (12,90; seção 3.4).
- **Público:** amplo, 18+, Advantage+. **Excluir os leads da Etapa 1** até o K2.

| Conjunto | Países | Preço | US$/dia | Anúncios | Por quê |
|---|---|---|---|---|---|
| USO_MX | MX | MXN 169 | 30 | 8 | Maior público ([DataReportal](https://datareportal.com/reports/digital-2026-mexico)) e maior densidade de anúncios longevos ([Invitio](https://www.facebook.com/ads/library/?id=1296962249316221) 112,5 d, [My Invite](https://www.facebook.com/ads/library/?id=1894344334607556) 116,3 d, [Miboda](https://www.facebook.com/ads/library/?id=847134201787134) 108,9 d); OXXO |
| USO_SUR | CO + PE + CL | COP 29.900 · S/ 32,90 · CLP 9.490 | 20 | 8 | Moeda e meios de pagamento locais (PSE/Efecty, PagoEfectivo); 685 anúncios somados (CO 194, PE 216, CL 275) [medido; soma feita via API em 22/09/2026; a [busca na CO](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=CO&q=invitaciones%20digitales&search_type=keyword_unordered) reproduz um país, troque `country=` por PE ou CL]; CL tem renda maior [inferência] |
| USO_USD | AR + EC + GT + DO | US$ 9,90 | 20 | 8 | AR tem 31,1 M de usuários no Instagram ([DataReportal](https://datareportal.com/reports/digital-2026-argentina)) e é o 2º país em anúncios de "invitaciones digitales" entre os medidos no dossiê (298 [medido, [busca na AR](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=AR&q=invitaciones%20digitales&search_type=keyword_unordered)]). Conferir o líquido de AR nas primeiras vendas |
| **Total** | | | **70** ≈ R$ 360 | 24 | |

O conjunto de revenda (REV) não entra na onda 1: ver "Depois do K2".

**Depois do K2:**
- **Revenda (REV)**, só se o B2C passou no K2 **e** o gancho de revenda passou na Etapa 1: conjunto próprio no MX, o país em que o gancho foi medido, com ≤ 20% da verba total (ex.: US$ 15/dia ao lado dos 70 do B2C), 4 anúncios só de demonstração, fora das réguas do B2C e sujeito ao K9 (seção 3.3).
- **Hispanos nos EUA a US$ 12,90**, com ≤ 6% da verba. Não entram antes: a US$ 4/dia não se aprende nada, o CPM é alto [inferência] e a oferta é própria.
- **Remarketing**, com ≤ 10% da verba e o F5 "Tres dudas".
- **Boda**, a partir de 28/12.

**Criativos da onda 1:**
- 8 por conjunto, localizados: AR com voseo e "casamiento"; CO/PE com "quince"; CL com "sus 15".
- F1 é o corpo principal; F2 e F3 são só tela. F4/F5, com a apresentadora rotulada, só na fração decidida pela Etapa 1, no máximo 1/3.
- Ganchos: os vencedores da Etapa 1 mais H01, H04, H05, H08, H10 e H13.
- Nenhum preço no criativo.
- Da 2ª semana em diante: 15–20 criativos novos por semana, e até 30 se a verba entregar. A US$ 70/dia, cada anúncio recebe só US$ 2–3/dia, então ler apenas os que tiverem entrega.

**Depois do K2 aprovado:**
- Criar a campanha **`ESCALA` (CBO)** com os anúncios que tiverem ≥ 3 vendas e CPA ≤ 5,23, mantendo o ID de post e usando um conjunto por grupo de país.
- O orçamento inicial da ESCALA é a soma dos conjuntos aprovados.
- A campanha de teste (ABO) fica com 20–30% da verba, para os criativos novos.

**Duração:** o K2 sai em ~6 dias, o K3 por volta da 2ª ou 3ª semana, e o K4 e o K5 em 15/11.

### 3.3 Regras de corte e de escala

| Nível | Regra | De onde vem |
|---|---|---|
| Anúncio sem venda | Gasto ≥ US$ 10,46 (R$ 53,76) → pausar | 2 × alvo = 1,33 × break-even |
| Anúncio com venda | CPA acumulado > 7,85 depois de ≥ US$ 23,55 (R$ 121) → pausar | 3 × break-even |
| Vencedor provisório | ≥ 3 vendas com CPA ≤ 5,23 → iterar: 6 ganchos novos no mesmo corpo e 3 corpos novos no mesmo gancho | Sinal de direção, não prova |
| País | CPA > 7,85 depois de US$ 150 no país → parar o país | Break-even |
| Conjunto, até o K2 | Orçamento fixo; só pausas de anúncio | Leitura limpa |
| Conjunto, depois do K2 | **Escalar +20–30% a cada 48–72 h** com ROI ≥ 1,5 nos últimos 3 dias e ≥ 10 compras na janela · manter com ROI de 1,25 a 1,5 · cortar 30% com ROI de 1,0 a 1,25 por 3 dias · pausar com ROI < 1,0 por 3 dias e ≥ US$ 60 gastos | ROI 1,5 = CPA 5,23; ROI 1,25 = CPA 6,28; ROI 1,0 = CPA 7,85 |
| Revenda | Desligar a célula com: 1 reprovação por resultados irreais, ou 0 vendas depois de US$ 100 (K9, desliga para sempre); CPA de front > 1,3× o do B2C depois de US$ 200; ou reembolso > 6% | — |

### 3.4 Gates

| Gate | Quando | Critério | Ação |
|---|---|---|---|
| **K2** | ≥ US$ 400 (R$ 2.056) na célula B2C e ≥ 20 anúncios com ≥ 1.000 impressões. Se faltar anúncio, seguir até US$ 550 | CPA de front **> 7,85** ou **< 25 compras** | **Morte** do L02 nesse formato, sem reteste. Com CPA de 7,85, US$ 400 compram ~51; mesmo com erro de −28%, o CPA seria 5,65, ainda acima de 5,23 |
| | | 5,23 < CPA ≤ 7,85 | Zona cinzenta: seguir com ganchos novos até o K4/K5 |
| | | CPA ≤ 5,23 | Aprovado: valem as regras de escala; entram EUA e remarketing |
| K6 | Junto com o K2 | CTR × (clique → compra) < CPM ÷ (1.000 × 5,23). Ex.: com CPM de 3, o mínimo é 0,057% | Diagnóstico: CTR bom com conversão ruim → o problema é a oferta; o contrário → o criativo |
| K3 | 100 compradores | Líquido < 7,60, reembolso > 6% ou chargeback > 0,5% | Parar. Se passar, reescrever as réguas com o líquido medido |
| K7 | 500 prévias | Prévia → pagamento < 50% da taxa do Mimo | Um único teste de "publica gratis limitado". Se não mexer, conta para o K2 |
| K8 | 100 convites publicados | < 50% com ≥ 1 confirmação em 7 dias | O RSVP não é o motivo da compra; reforça o corte |
| K4 | US$ 1.500 (R$ 7.710) gastos na Etapa 2, ou 15/11 | Nenhum conjunto sustenta 7 dias seguidos a ≥ US$ 50/dia com CPA ≤ 5,23 | Estacionar: só segue pequeno, com CPA ≤ 6,28 |
| K5 | 15/11 | Não aprovado no K2 (ficou na zona cinzenta) | Pausar até 26/12 e fazer um único reteste de US$ 400 até 20/01. Se falhar, morte |
| Teto | 28/02/2027 | Não sustentou ≥ US$ 250/dia por 7 dias com CPA ≤ 5,23 | Não é segundo motor: não construir o L67 nem o PT-BR. Manter com ROI ≥ 1,25 ou desligar |
| Mimo | Contínuo | ROI do Mimo caindo 2 semanas seguidas, ou abertura de idioma do Mimo parada por causa do L02 | Pausar o L02 |

**Teto de aprendizado: US$ 2.000 (R$ 10.280).** Entram na conta:
- a Etapa 1 (~340, ou +100 se houver rodada extra);
- o gasto da Etapa 2 enquanto o CPA acumulado estiver acima de 5,23;
- o reteste de janeiro (400).

Na zona cinzenta, a Etapa 2 para em US$ 1.250 de aprendizado, mesmo antes de 15/11, para sobrar dinheiro para o reteste.

**Depois do K2 aprovado:**
- **Preço:** teste A/B **para cima**, US$ 9,90 × 12,90 (MXN 219; alvo de 6,77), decidido pelo líquido por lead com bumps. Precisa de ~150–250 compras por braço, então a decisão sai na janela de jan–fev. Nesta fase, nunca testar para baixo.
- **L67:** a pré-condição é o B3 com adesão ≥ 8% entre ≥ 100 compradores de eventos infantis (cumpleaños infantil e baby shower, os eventos em que o B3 aparece). A decisão de construir fica para o teste de teto (28/02), para não dividir a atenção na janela de escala. Se o teto falhar, o L67 não sai.

### 3.5 O que medir no UTMify

**Configuração:**
- dashboard "INV", só do L02;
- conta de anúncios nova vinculada e webhook do produto novo;
- **imposto de 12% da conta BRL** cadastrado;
- custo por venda de ~US$ 0,05 (hospedagem, pior caso).

**ROI = faturamento líquido ÷ (gasto + 12%).** Conferir se o campo de ROI do dashboard usa essa fórmula; se não usar, calcular à parte.

**As decisões saem do UTMify.** A Meta serve só para diagnóstico (CPM, CTR, hook, hold), porque a atribuição por visualização dela tende a inflar as compras [inferência].

| Métrica | Onde | Observação |
|---|---|---|
| CPA de front, só tráfego pago | UTMify, por campanha, conjunto e anúncio (nomenclatura `INV_`) | Tirar `utm_source=lista` e `viral` do K2 e reportar à parte |
| Líquido por comprador e AOV | UTMify | Base: 8,79 |
| ROI por conjunto, país, posicionamento e dia | UTMify | Regras da seção 3.3 |
| Adesão por bump | UTMify / Hotmart | Seção 3.6; o B3 só entre infantil e baby shower |
| Reembolso e chargeback | Hotmart / UTMify | Seção 3.6 |
| Pagamentos pendentes (OXXO, PagoEfectivo) e taxa de compensação | Hotmart | Venda pendente não conta no CPA até compensar |
| Recusa de cartão por país | Hotmart | Comparar com a do Mimo nos mesmos países |
| Líquido real de AR | Primeiras vendas de AR | Descobrir quem paga os 9,5% da conversão |
| Funil do app: clique → editor → e-mail → prévia → checkout → compra | Analytics do app | Confirma a premissa de 2–4%; alimenta o K7 |
| Tempo mediano entre o e-mail e a compra | App | Acima de 72 h, a compra está sendo adiada (risco) |
| % de convites com ≥ 1 confirmação em 7 dias | App | K8 |
| Vendas vindas do rodapé "Crea la tuya" | `utm_source=viral` | Laço viral; a meta é ≥ 0,1 venda extra por venda |

### 3.6 Bumps e reembolso: mínimos

| Item | Base (sustenta o alvo de 5,23) | Piso (o alvo cai para ~4,77) | Abaixo do piso |
|---|---|---|---|
| B1 "Tu invitación para siempre", 3,90 | 22% | 15% | Alvo de ~4,53 (cenário cético), com o K3 perto de disparar |
| B2 "Versión para imprimir + QR", 4,90 | 12% | 8% | Idem |
| B3 "Kit de fiesta a juego", 4,90 | 5% do total | 8% entre infantil + baby shower, o mínimo para abrir o L67 | O L67 não abre |
| B4 "+5 invitaciones", 6,90 | 4% | 2% | A licença não tem demanda e a revenda não abre |
| Líquido dos bumps por comprador | 1,73 | 1,11 | < 0,68 = cenário cético |
| Reembolso | 3% | Alerta acima de 4% (ler os motivos) | **> 6% = parar (K3)** |
| Chargeback | ~0 | — | **> 0,5% = parar.** O limite da Hotmart é ~0,9% (não verificado), e um chargeback alto afeta a conta de produtor inteira |

O preço de um bump só muda antes do K2 se a 1ª venda mostrar taxa fixa por bump. Nesse caso, o B1 sobe para 4,90, ou B1 e B2 viram um "Pack Recuerdo" a 5,90.

## 4. Infra separada do Mimo

**Por que separar:**
1. **Risco de política.** O nicho de renda extra e a célula de revenda encostam em "oportunidade econômica" [inferência]. Uma restrição na conta do L02 não pode parar a conta que sustenta mais de R$ 2.600/dia.
2. **Aprendizado.** O comprador é outro: quem organiza uma festa, não quem dá um presente romântico. Otimizar por Purchase no dataset do Mimo misturaria os sinais e os públicos semelhantes, nos dois sentidos [inferência].
3. **Leitura.** O ROI do L02 fica sem se misturar ao do Mimo.

| Ativo | O que fazer |
|---|---|
| Portfólio empresarial (BM) | Novo, com a marca do L02 e dados reais iguais aos da Hotmart (nome, país, endereço, CNPJ se houver). 2FA ligado. Verificação da empresa iniciada no D1 |
| Perfil pessoal | O mesmo perfil real do usuário como admin. **Não criar um segundo perfil:** a Meta só permite um perfil por pessoa, e um perfil falso derrubado arrasta os portfólios ligados a ele [inferência; confirmar nos [Termos da Meta](https://www.facebook.com/terms)] |
| Conta de anúncios | Nova, dentro do BM novo, em BRL e no fuso de São Paulo. Moeda e fuso não mudam depois |
| Pagamento | Outro cartão, no nome do usuário |
| Dataset (pixel + API de Conversões) | Novo, com os eventos PageView, ViewContent (abriu um exemplo), Lead, InitiateCheckout e Purchase, deduplicados entre navegador e servidor. Credenciais novas |
| Domínio | Próprio, de marca nova, verificado no BM antes do 1º anúncio, com SSL. Rodapé com aviso de privacidad, términos, licencia e contacto |
| Página do Facebook + Instagram | Novas, da marca: foto, bio ("Invitaciones web con confirmación de asistencia") e link. Publicar 6–9 posts orgânicos de convites "Ejemplo" antes do 1º anúncio. Instagram ligado ao BM |
| Hotmart | Produto novo (software/app) e 4 bumps como produtos próprios, criados no D1: a análise é o caminho crítico. Página sem promessa de renda; garantia de 7 dias. As integrações do produto novo apontam só para a infra nova, e as do Mimo só para os produtos do Mimo |
| Backend | O app reaproveita o fluxo editor → página → Hotmart do Mimo, mas com banco, arquivos e funções próprios. No D1, conferir que nada aponta para o banco de outro produto |
| UTMify | Dashboard novo, com a conta nova vinculada, o webhook do produto novo, os 12% de imposto, a nomenclatura `INV_` e os parâmetros de URL padrão do UTMify |

**O que não fica separado:**
- o perfil pessoal que administra os dois portfólios;
- a conta de produtor na Hotmart, onde reembolso, chargeback e advertências dos dois produtos se somam.

A Meta também pode associar ativos por admin, cartão e dispositivo [inferência; confirmar nos [Termos da Meta](https://www.facebook.com/terms) e nos [Padrões de Publicidade](https://transparency.meta.com/policies/ad-standards/)]. A separação isola **ativos e aprendizado**, não a identidade. O que protege o Mimo de verdade é o anúncio limpo.

**Aquecimento e verificação:**
- **A Etapa 1 é o aquecimento:** gasto pequeno e constante (US$ 36–53/dia), com os anúncios de menor risco primeiro. A, B e C entram em 26/09; D só em 28/09.
- **Não editar anúncio no ar nas primeiras 24 h**, porque cada edição volta para revisão [inferência].
- **Verificação de anunciante:** se a Meta pedir, fazer na hora. Não passar de US$ 150/dia antes de o portfólio estar verificado.
- **Nada comprado:** nem conta "aquecida", nem perfil emprestado, nem engajamento.
- **Se a conta for restrita, recorrer.** Abrir outra conta para seguir anunciando o mesmo produto é [burla de sistemas](https://transparency.meta.com/km-kh/policies/ad-standards/deceptive-content/circumventing-systems) e costuma derrubar todos os ativos ligados, inclusive os do Mimo [inferência].

## 5. Calendário

**Build reordenado para a Etapa 1 (substitui o cronograma do dossiê).** No dossiê, o convite público sai no D5 (27/09) e o RSVP no D6 (28/09), depois do início da Etapa 1 em 26/09 (D4). Aqui os dois sobem para o D2–D3, alimentados pelos 3 convites "Ejemplo" com dados fixos, e o editor completo vem depois. O total de dias não muda: o MVP continua vendável no D11 (~03/10).

| Dia | Data | Entrega | No dossiê |
|---|---|---|---|
| D1 | 23/09 | Produtos e bumps na Hotmart (em análise; caminho crítico); BM, conta, página/IG, domínio, dataset e UTMify; base do app | D1 + parte do D2 |
| D2 | 24/09 | Página pública do convite (envelope → capa → contagem → galeria → "Cómo llegar"), com OG tags e música, para os 3 convites "Ejemplo" (XV, infantil, baby shower), sem editor. É também o primeiro teste da música no iPhone dentro do WhatsApp e do Instagram | D5 + parte do D2 |
| D3 | 25/09 | RSVP de exemplo ("¿Nos acompañas?", com rate limit e campo-isca) e painel com "Datos de ejemplo"; página de "acceso anticipado" com a lista de espera e os eventos ViewContent e Lead; gravação dos 13 criativos da Etapa 1 | Parte do D6 e do D12 |
| **D4** | **26/09** | **Etapa 1 no ar (A, B, C).** Build: onboarding e editor | D3–D4 |
| D5 | 27/09 | Editor (cont.): contagem com fuso, datas em ES e os demais temas | D3–D4 + parte do D2 |
| D6 | 28/09 | Editor ligado à página pública; tela de confirmados real e CSV | Resto do D5–D6 |
| D7–D10 | 29/09–02/10 | Checkout e liberação, bumps, reembolso → offline e OXXO pendente (D7); painel, créditos, travas e licença (D8); PDFs (D9); landing, FAQ, termos e e-mails (D10) | D7–D10, sem o A/B de preço |
| D11 | 03/10 | QA de ponta a ponta. **MVP vendável** | D11 |
| D12–D14 | 04–06/10 | Criativos da Etapa 2 (F2 com o editor real), soft launch em 05/10 e folga | D12–D14 |

| Semana | Datas | Build | Mídia | Decisão |
|---|---|---|---|---|
| S39 | 23–27/09 | **D1:** produtos na Hotmart (em análise), BM, conta, página/IG, domínio, dataset e UTMify. **D2:** página pública do convite com os 3 "Ejemplo". **D3:** RSVP de exemplo, página da lista e os 13 criativos. **D4–D5:** editor | Etapa 1 no ar em 26/09 (A, B, C) | — |
| S40 | 28/09–04/10 | D6–D12; QA de ponta a ponta no D11 (~03/10) | D entra em 28/09; a Etapa 1 vai até 02/10. **04/10:** e-mail único para a lista, antes de abrir ao público | **29/09:** checkpoint. **03/10:** leitura da Etapa 1 e K0 |
| S41 | 05–11/10 | D13–D14: criativos e folga | **Soft launch em 05/10**, a US$ 70/dia | K1 diário |
| S42 | 12–18/10 | Correções | K2 em ~11–13/10 | **K2:** morte, cinza ou aprovado. Se aprovado: escala por regra, EUA a 12,90 e remarketing |
| S43 | 19–25/10 | — | — | K3 (100 compradores) e réguas reescritas. **20/10: prazo do K0** |
| S44–S46 | 26/10–15/11 | Criativos de boda em produção | CPM subindo | K7 e K8. **15/11: K4 e K5** |
| S47 | 16–22/11 | — | Aumentos de no máximo +20% | — |
| S48 | 23–29/11 (Black Friday em 27/11) | — | **Sem escalar e sem testar** | — |
| S49–S51 | 30/11–20/12 | Boda pronta até ~20/12; renders antes de 24/12 | Demanda de ~0,7× [estimativa]; só dentro das réguas | — |
| S52 | 21–27/12 | — | Sem teste. **26/12:** lançamento, se o K0 falhou, ou início do reteste do K5 | — |
| S53–S08 | 28/12/2026–28/02/2027 | — | **Janela de escala:** CPM 40–60% menor até ~15/01 (dados dos EUA, [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns), [Clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics); LATAM não verificado) e compra de convites para as bodas de fev–mai (MX) e mar–abr (AR) | Reteste do K5 até 20/01; A/B 9,90 × 12,90. **28/02: teste de teto** |

**Dá para construir e validar em outubro?** Sim, com pouca folga.
- A Etapa 1 roda enquanto o build vai do D4 ao D10.
- O MVP fica vendável em ~03/10 e o soft launch é em 05/10.
- O K2 sai por volta de 11–13/10, antes do CPM de novembro (+41%) e da Black Friday (CPM 2–3×). Fontes: [benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns) e [Clouted](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics), com dados dos EUA; LATAM não verificado.

O caminho crítico tem dois pontos: a análise dos produtos na Hotmart e a música no iPhone dentro do WhatsApp e do Instagram.

**Quando o CPM subir (de 16/11 ao Natal):**
- **As réguas se ajustam sozinhas,** porque são de CPA e ROI: o CTR mínimo sobe na mesma proporção do CPM (CPM +41% → CTR mínimo +41%). Não afrouxar nenhuma régua.
- **A partir de 16/11:** aumentos de no máximo +20%, e pausar com ROI < 1,0 em 2 dias, não em 3.
- **Semana da Black Friday:** nada novo; manter só o que já está com ROI ≥ 1,5.
- **Dezembro:** demanda de ~0,7× [estimativa], porque as bodas de dezembro já compraram o convite e as posadas ficam com o grátis [inferência]. Rodar só dentro das réguas e usar o tempo para os criativos de boda.
- **Sem ângulo de Black Friday, desconto ou Natal:** não há desconto real e o preço está travado.
- **Se o K2 ficou na zona cinzenta,** não gastar o aprendizado com CPM caro: o reteste vai para janeiro.

**Janeiro e a "cuesta de enero":** a tese não vale para o L02. "Cuesta de enero" fala da situação financeira de quem vê o anúncio, um [atributo pessoal](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/) que a Meta proíbe, e o produto é vendido para uso próprio.
- **De onde vem a força de janeiro:** do CPM mais barato e da compra de convites para as bodas de fev–mai (MX, [bodas.com.mx](https://www.bodas.com.mx/articulos/meses-favoritos-para-casarse-en-mexico--c9837)) e mar–abr (AR, temporada de out–abr segundo a [CEMBA](https://cemba.com.ar/2025/10/13/comenzo-la-temporada-alta-de-casamientos/)). O H03 ("¿Boda en febrero o marzo?") ganha peso a partir de 28/12.
- **Revenda em janeiro:** se a célula estiver viva, pode ficar com até 20% da verba, com o mesmo texto neutro ("¿Haces invitaciones para otras personas?"). Pode pegar carona no clima de começo de ano, mas isso não foi medido, e nenhum texto fala em renda.

**A ideia continua viva depois da data?** Sim. ~82% dos eventos (XV e infantil) são perenes, e de março a setembro o fator é ~1,0× [estimativa]. Perder outubro custa pouco, porque novembro e dezembro são os piores meses do L02 [estimativa]. Duas coisas não se estendem: o teto de US$ 2.000 e o teste de teto em 28/02/2027.

## 6. Checklist de compliance antes de subir

**Criativo**
- [ ] Nenhum valor de ganho, nem "gana", "ingresos", "emprende", "negocio", "listas para vender", "sin esfuerzo" ou "en 1 minuto".
- [ ] Nenhum preço, timer, "solo hoy", "cupos limitados" ou preço "antes/ahora".
- [ ] Nenhum atributo pessoal ("¿no te alcanza?", "¿estás embarazada?", "cuesta de enero"). O evento vai na 3ª pessoa: "sus XV".
- [ ] Todo convite com o selo "Ejemplo" e sem rosto real de criança; público 18+.
- [ ] Apresentadora de IA:
  - rosto sintético genérico, checado por busca reversa, sem semelhança com famosos e sem cenário de telejornal;
  - rótulo "Presentadora virtual · IA" na tela, marcação de IA no Gerenciador e metadados de IA preservados;
  - fala "te muestro", nunca "yo la usé" nem "mi hija".
- [ ] Sem depoimento, "miles de familias" ou notificação de venda.
- [ ] Sem interface falsa ("toca aquí", play desenhado, caixa de seleção): a mão toca dentro do vídeo.
- [ ] Sem personagem licenciado, marca de terceiros ou logo alterado (Canva, WhatsApp, Maps, Waze).
- [ ] Sem tema de casal ou de presente.
- [ ] Música licenciada, com o ID registrado, e nenhum áudio vazando da gravação de tela.
- [ ] Nenhuma promessa que o produto não cumpra. Tempo de montagem só depois de medido no QA.

**Texto, título e CTA**
- [ ] Etapa 1: "Muy pronto" na 1ª linha e no end card, CTA "Registrarte", sem "lista hoy" nem "créala ya".
- [ ] Etapa 2: CTA coerente com a página ("Más información") e nenhum preço.
- [ ] Nenhuma categoria especial de anúncio: não é crédito, emprego, habitação, serviço financeiro nem tema social.
- [ ] Nenhum texto com cara de oferta de emprego, como "trabajo desde casa".

**Página de destino**
- [ ] O produto do anúncio é o da página, no domínio próprio verificado, sem redirecionamento e sem versão diferente para o revisor.
- [ ] Etapa 1: "en construcción", "no cobramos nada ahora" e "no es una preventa"; sem checkout nem botão de compra.
- [ ] Etapa 2, visível antes de pagar:
  - prévia grátis real e o preço;
  - "pago único · sin suscripción";
  - "el cargo aparece como HTM* / HOTMART";
  - garantia de 7 dias e "si pides el reembolso, tu invitación se desactiva".
- [ ] Rodapé com aviso de privacidad, términos, licencia (uso para clientes, sem revenda do editor nem dos modelos) e contacto; consentimento explícito para WhatsApp.
- [ ] Nenhum campo de "datos bancarios" em presentes no MVP.

**Hotmart e conta**
- [ ] O nome e a página do produto descrevem o entregável ("Editor de invitaciones web"), sem promessa de renda nem "derechos de reventa".
- [ ] Bumps com nome e preço claros, sem preço riscado.
- [ ] O anúncio sobe na conta nova, com o cartão novo e o dataset novo. Nada do Mimo selecionado por engano (página, pixel, público).
- [ ] QA das 10 perguntas do dossiê (`03_top3/invitaciones-web.md`, seção Criativo): qualquer "sim" barra o anúncio.
