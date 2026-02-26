# Integração — Supabase (PostgREST)

## REST API / Segurança
- Supabase auto-gera REST API via PostgREST e suporta segurança via RLS/roles/grants. [14](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=31e70c09-bfcf-4bf8-b115-552dceb11b3a&cid=ca00acb247e603aa)
- Operadores de filtro incluem eq, gt, gte, ilike, in, is, etc. [15](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=65a20906-8203-4702-9285-6268d424c3bb&cid=ca00acb247e603aa)

## Tools MCP
- supabase_list_tables
- supabase_query_table (filtros + limit/offset)
- supabase_insert_row
- supabase_update_row
- supabase_delete_row (destructive + reason)

## Regras
- Sempre aplicar limit/offset para evitar retornos massivos.
- Não usar SQL arbitrário no MVP; preferir filtros estruturados.