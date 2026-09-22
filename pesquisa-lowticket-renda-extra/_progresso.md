# Progresso da pesquisa (para retomar se a sessão cair)

Data de início: 2026-09-22 (UTC)

## Ferramentas/fontes disponíveis nesta sessão
- Biblioteca de Anúncios da Meta via MCP (`mcp__Meta_Ads__ads_library_search`): FUNCIONA. Retorna anúncios do mais novo pro mais antigo, com page_name, link_title, data de início de veiculação (epoch) e link de snapshot. Não retorna texto do corpo nem alcance. Busca por `page_ids` lista os anúncios ativos da página (dá pra medir nº de variações e o anúncio ativo mais antigo).
- WebSearch: FUNCIONA (títulos + URLs + resumo de snippets).
- WebFetch / curl / navegador: BLOQUEADOS pela política de rede da sessão (hotmart.com, pay.hotmart.com, facebook.com, transparency.meta.com, etsy.com, trends.google.com, google.com, wikipedia). Consequência: preços e bumps da Hotmart só via snippet de busca; Google Trends e TikTok Creative Center não verificáveis diretamente → links prontos gerados pra o usuário abrir.

## Fases
- [x] Fase 1 — Long list
- [x] Fase 2 — Eliminatórias
- [x] Fase 3 — Scorecard
- [x] Fase 4 — Deep dive top 3
- [x] Fase 5 — Decisão + validação

## Log
- 2026-09-22 16:55 UTC — Fase 1 lançada (workflow wf_cc6e8dd8-e30): 7 agentes de fonte + políticas + demanda/objeções → consolidação → lacunas. Anotações brutas em _raw/fase1_*.md.
- 2026-09-22 17:05 UTC — Baseline real do Mimo Gift puxado do UTMify → _privado/mimo_baseline.md (dado sensível, fora do git via .gitignore: NÃO subir pro repositório público sem o usuário autorizar; o repo gustavobrong-hub/Cradle é PÚBLICO).
- 2026-09-22 18:31 UTC — Fase 1 concluída: 60 ideias (L01–L65, com lacunas de ID por fusões). Resultado bruto em _raw/fase1_result.json; digests em _raw/digest_politicas.txt e _raw/digest_demanda.txt; 01_longlist.csv gerado (coluna eliminada pendente). Achados: WebSearch dos subagentes esgotou a cota em parte da Fase 1 (hotmart_es, global e hipóteses ficaram com poucas buscas web); taxa Hotmart mudou em 21/09/2026 (Player US$1,49 extinto → taxa fixa US$1,00), não verificado na página oficial.
- Fase 2 lançada (eliminatórias E0 escopo + E1–E5, juiz + cético por lote de 12).
- 2026-09-22 ~19:00 UTC — Fase 2 concluída: 19 sobreviventes de 60 (41 eliminadas: 27 por E0 escopo "fora do nicho renda extra", 5 E5, 4 E2, 3 E1, 2 E4). O cético não derrubou nenhuma adicional. H1 (Mimo Gift Revenda, L01) eliminada por E2; H2 (Invitaciones web, L02) sobreviveu e absorveu o L03 (ângulo B2C). 4 reformulações "versão ferramenta" adicionadas (L66–L69). Resultado: _raw/fase2_result.json; 01_longlist.csv atualizado.
- Fase 3 lançada: 23 sobreviventes + L01 fora de concurso.
- 2026-09-22 ~19:45 UTC — Fase 3 concluída: 02_scorecard.md. Ranking final: L02 Invitaciones web 67,0; L67 Gerador de kit de festa 66,5; L09 Kit festa Canva 63,5; L29 Calculadora de custos 59,3; L66 Video-invitación 56,8. L01 (Mimo Revenda) fora de concurso 35,8. Top 3 p/ deep dive: L02, L67, L29 (L09 coberto como controle do L67). Nenhuma ideia verificada supera o Mimo em teto nem em líquido/comprador no modelo. Resultado: _raw/fase3_result.json.
- Fase 4 lançada (deep dive top 3).
- 2026-09-22 ~21:15 UTC — Fase 4 concluída: 03_top3/{invitaciones-web,kit-fiesta-personalizado,calculadora-costos-precios}.md. Versões completas em _privado/03_top3_completo/ (fora do git); intermediários em _privado/03_top3_intermediarios/. Versões públicas sanitizadas.
- 2026-09-22 ~21:45 UTC — Fase 5 (decisão): painel 3/3 no L02 como aposta limitada; 00_decisao.md escrito. Adendo no 02_scorecard.md (teto inflado; L29 não devia ser top 3). Plano de validação + crítico rodando.
- 2026-09-22 ~22:45 UTC — Fase 5 concluída: 04_validacao.md; crítico de completude + correções (vazamentos de dado privado/interno removidos dos arquivos públicos; JSONs brutos das Fases 2, 3 e 5 movidos para _privado/; links de busca da Biblioteca de Anúncios adicionados à long list; nota de reconciliação no dossiê do L02). ATENÇÃO: commits anteriores deste branch (já publicados) ainda contêm parte desses dados; o force-push para limpar o histórico foi bloqueado pela permissão da sessão; ver resumo final.
