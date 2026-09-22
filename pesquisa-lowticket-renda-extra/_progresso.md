# Progresso da pesquisa (para retomar se a sessão cair)

Data de início: 2026-09-22 (UTC)

## Ferramentas/fontes disponíveis nesta sessão
- Biblioteca de Anúncios da Meta via MCP (`mcp__Meta_Ads__ads_library_search`): FUNCIONA. Retorna anúncios do mais novo pro mais antigo, com page_name, link_title, data de início de veiculação (epoch) e link de snapshot. Não retorna texto do corpo nem alcance. Busca por `page_ids` lista os anúncios ativos da página (dá pra medir nº de variações e o anúncio ativo mais antigo).
- WebSearch: FUNCIONA (títulos + URLs + resumo de snippets).
- WebFetch / curl / navegador: BLOQUEADOS pela política de rede da sessão (hotmart.com, pay.hotmart.com, facebook.com, transparency.meta.com, etsy.com, trends.google.com, google.com, wikipedia). Consequência: preços e bumps da Hotmart só via snippet de busca; Google Trends e TikTok Creative Center não verificáveis diretamente → links prontos gerados pra o usuário abrir.

## Fases
- [ ] Fase 1 — Long list
- [ ] Fase 2 — Eliminatórias
- [ ] Fase 3 — Scorecard
- [ ] Fase 4 — Deep dive top 3
- [ ] Fase 5 — Decisão + validação

## Log
- 2026-09-22 16:55 UTC — Fase 1 lançada (workflow wf_cc6e8dd8-e30): 7 agentes de fonte + políticas + demanda/objeções → consolidação → lacunas. Anotações brutas em _raw/fase1_*.md.
- 2026-09-22 17:05 UTC — Baseline real do Mimo Gift puxado do UTMify → _privado/mimo_baseline.md (dado sensível, fora do git via .gitignore: NÃO subir pro repositório público sem o usuário autorizar; o repo gustavobrong-hub/Cradle é PÚBLICO).
