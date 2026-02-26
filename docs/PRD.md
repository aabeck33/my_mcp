# PRD — MCP Server (Python) com 5 integrações (Google Calendar, Google Drive, Microsoft Drive, Microsoft Fabric, Supabase)

## 1) Visão Geral
Este projeto entrega um **MCP Server (Model Context Protocol)** em **Python** que expõe **tools** e **prompts** para permitir que **LLMs/Agentes** interajam com serviços externos de forma segura, auditável e confiável. O servidor deve ser medido pela capacidade de permitir tarefas reais com boa “agent experience” (descobribilidade das tools, respostas focadas, paginação e mensagens de erro acionáveis). [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)

### 1.1 Objetivos
- Expor um conjunto robusto de **tools MCP** para 5 integrações:
  1) Google Calendar [5](https://developers.google.com/workspace/drive/api/guides/file-metadata)[6](https://onedrive.live.com/?id=978199e2-c4c4-41c3-a652-d654a00c2f9a&cid=ca00acb247e603aa&web=1)  
  2) Google Drive [7](https://atalupadhyay.wordpress.com/2025/02/15/a-step-by-step-guide-with-pydantic-ai-and-langgraph-to-build-ai-agents/)[8](https://github.com/Tanujkumar24/LANGGRAPH-STRUCTURED-OUTPUT-AGENT)  
  3) Microsoft Drive (OneDrive/SharePoint via Microsoft Graph) [9](https://deepwiki.com/modelcontextprotocol/java-sdk/5.3-streamable-http-transport)[10](https://mcpindotnet.github.io/docs/concepts/architecture-overview/layers/transport-layer/streamable-http/)[11](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/blob/main/api-reference/beta/resources/driveitem.md)  
  4) Microsoft Fabric [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)[13](https://learn.microsoft.com/en-us/rest/api/fabric/articles/)  
  5) Supabase (PostgREST + RLS) [14](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=31e70c09-bfcf-4bf8-b115-552dceb11b3a&cid=ca00acb247e603aa)[15](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=65a20906-8203-4702-9285-6268d424c3bb&cid=ca00acb247e603aa)  
- Integrar um **agente** em **LangGraph** para orquestração segura, com **nós tipados** e **falha isolada por tool**. [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)
- Entregar documentação operacional: **CHECKLIST**, **SECURITY**, **ADRs**, **docs por integração**.

### 1.2 Não-Objetivos (fora de escopo inicial)
- Expor SQL arbitrário para Supabase (preferir operações estruturadas e filtradas).
- Retornar arquivos grandes como payload bruto sem limite/paginação (sempre impor limites).
- Qualquer fluxo que viole as regras obrigatórias (prompts hardcoded, output não tipado, tool failure derrubando o grafo). [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)

---

## 2) Regras Obrigatórias (não negociáveis)
### 2.1 Agentes
1) Agentes DEVEM ser implementados com **LangGraph** (state machine). [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  
2) Cada nó do grafo DEVE ter responsabilidade única e **saída tipada**. [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  
3) Respostas DEVEM usar **Structured Output (Pydantic)** — nunca texto livre para dados estruturados. [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  
4) Tools DEVEM ter **error handling individual** — falha de uma tool não derruba o grafo. [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  
5) Prompts DEVEM ficar em **arquivos separados** (versionados) — nunca hardcoded. [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  

### 2.2 Endpoints HTTP (se aplicável)
- Todas as rotas autenticadas (exceto health/públicas explícitas). [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  
- Validação Pydantic em TODAS as rotas. [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  
- Rate limiting por user_id em rotas sensíveis. [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  
- CORS restritivo apenas para domínios do frontend. [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  
- Upload valida MIME/ext/tamanho. [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  

### 2.3 Transport MCP (preferência)
- **Default**: `stdio` (local, simples e recomendado para clients quando possível). [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)  
- **Opcional**: `streamable-http` para servidores remotos. Se habilitado: validar `Origin` (anti DNS rebinding), bind em localhost no modo local e autenticação nas conexões. [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)  

---

## 3) Arquitetura e Estrutura Inicial do Projeto (definição “contribui para construção”)
### 3.1 Estrutura de repositório (obrigatória)
A separação abaixo é mandatória para manter o PRD limpo e permitir evolução segura (prompts/versionamento/schemas).
/docs
PRD.md
CHECKLIST.md
SECURITY.md
INTEGRATIONS/
google_calendar.md
google_drive.md
microsoft_drive.md
microsoft_fabric.md
supabase.md
ADR/
0001-transport.md
0002-authn-authz.md
0003-error-model.md
/prompts
_shared_guardrails.md
google_calendar.agent.md
google_drive.agent.md
microsoft_drive.agent.md
microsoft_fabric.agent.md
supabase.agent.md
/schemas
common.py
google_calendar.py
google_drive.py
microsoft_drive.py
microsoft_fabric.py
supabase.py
/tools
google_calendar_tools.py
google_drive_tools.py
microsoft_drive_tools.py
microsoft_fabric_tools.py
supabase_tools.py
/agents
graph.py
nodes/
plan.py
route.py
execute_tool.py
recover.py
summarize.py
server.py

### 3.2 Responsabilidades por pasta (regra de separação)
- `docs/PRD.md`: visão, escopo, decisões e links (não colocar schemas longos nem prompts).
- `docs/INTEGRATIONS/*`: detalhes de endpoints externos → tools, auth, paginação, limites, erros.
- `schemas/*`: contratos Pydantic (inputs/outputs) para tools e estados do LangGraph.
- `prompts/*`: prompts e guardrails (somente texto, sem lógica). [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  
- `tools/*`: implementação das calls externas + mapeamento de erros (cada tool isolada).
- `agents/*`: LangGraph e seus nós tipados. [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  

### 3.3 Instrução de contribuição
- Mudou algo em tools: deve adicionar/editar apenas em tools/<serviço>_tools.py + atualizar schemas correspondentes em schemas/ + atualizar docs em docs/INTEGRATIONS/ + atualizar docs/CHECKLIST.md.
- Mudou algo em prompts: deve editar somente em prompts/ (nunca hardcode em Python). [onedrive.live.com]
- Mudou transport/auth/error model? criar/atualizar ADR em docs/ADR/.
---

## 4) Implementação MCP Server (Python)
### 4.1 SDK recomendado (Python MCP/FastMCP)
O servidor deve usar o padrão do **MCP Python SDK** com `FastMCP`, registrando tools e prompts via decorators e executando via `mcp.run(...)` (stdio ou streamable-http). [16](https://learn.microsoft.com/en-us/rest/api/fabric/sqlendpoint/items/list-sql-endpoints)[17](https://deepwiki.com/microsoft/fabric-toolbox/6.1-sql-endpoint-and-warehouse-operations)[18](https://www.vojtechsima.com/post/programmatically-refresh-sync-sql-analytics-endpoint-metadata-in-microsoft-fabric)  

### 4.2 Naming e discoverability de tools (padrão)
- Prefixo por domínio + verbo + objeto (ex.: `gcal_list_events`, `msdrive_create_upload_session`).
- Descrição curta e objetiva.
- Suporte a paginação e filtros onde aplicável. [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)  

### 4.3 Modelo de erro e “erros acionáveis”
- Toda tool retorna erro estruturado e seguro, com `code`, `message`, `retryable`, `remediation`.
- Mensagens não devem vazar tokens/PII; devem orientar o agente ao próximo passo. [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)  

---

## 5) LangGraph (Agente)
### 5.1 Objetivo do agente
Orquestrar chamadas às tools MCP de forma robusta, com:
- nós com responsabilidade única e saída tipada
- error handling isolado por tool (falhas não derrubam o fluxo)
- prompts em arquivos separados para cada integração [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  

### 5.2 Nós mínimos do grafo (MVP)
- `plan`: interpreta intenção e gera plano tipado
- `route`: escolhe tool(s) apropriadas
- `execute_tool`: executa tool com isolamento de erro
- `recover`: aplica remediação (retry/backoff/alternativa segura)
- `summarize`: gera saída final (estruturada quando necessário)

---

## 6) Catálogo de Tools (MVP completo — 5 integrações)
> Os contratos completos estão em `schemas/*.py` e o mapeamento técnico de APIs em `docs/INTEGRATIONS/*.md`.

### 6.1 Google Calendar tools
- `gcal_list_calendars`
- `gcal_list_events` (time_min/time_max + paginação) [5](https://developers.google.com/workspace/drive/api/guides/file-metadata)  
- `gcal_create_event` (suporta `send_updates`) [6](https://onedrive.live.com/?id=978199e2-c4c4-41c3-a652-d654a00c2f9a&cid=ca00acb247e603aa&web=1)  
- `gcal_update_event`
- `gcal_delete_event` (destructive + auditoria)

### 6.2 Google Drive tools
- `gdrive_list_files` (pageToken/nextPageToken + fields mask opcional) [7](https://atalupadhyay.wordpress.com/2025/02/15/a-step-by-step-guide-with-pydantic-ai-and-langgraph-to-build-ai-agents/)[8](https://github.com/Tanujkumar24/LANGGRAPH-STRUCTURED-OUTPUT-AGENT)  
- `gdrive_get_file_metadata`
- `gdrive_download_file` (limite max_bytes)
- `gdrive_upload_file` (validação MIME/ext/tamanho) [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  
- `gdrive_delete_file` (destructive + auditoria)

### 6.3 Microsoft Drive tools (Graph)
- `msdrive_list_drives` [9](https://deepwiki.com/modelcontextprotocol/java-sdk/5.3-streamable-http-transport)  
- `msdrive_list_children` (paginado)
- `msdrive_get_item` (DriveItem) [10](https://mcpindotnet.github.io/docs/concepts/architecture-overview/layers/transport-layer/streamable-http/)  
- `msdrive_download_item` (limite max_bytes)
- `msdrive_upload_small` (validação MIME/ext/tamanho) [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  
- `msdrive_create_upload_session` (upload grande resumível) [11](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/blob/main/api-reference/beta/resources/driveitem.md)  
- `msdrive_delete_item` (destructive + auditoria)

### 6.4 Microsoft Fabric tools
- `fabric_list_items`
- `fabric_get_item`
- `fabric_create_notebook` / `fabric_update_item` / `fabric_delete_item` [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)  
- `fabric_get_definition` / `fabric_update_definition` [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)  
- `fabric_run_item_job` / `fabric_get_job_instance` / `fabric_cancel_job_instance` [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)  
- `fabric_list_sql_endpoints` (continuationToken/paginação) [13](https://learn.microsoft.com/en-us/rest/api/fabric/articles/)  

### 6.5 Supabase tools
- `supabase_list_tables`
- `supabase_query_table` (filtros PostgREST: eq/gt/gte/ilike/in/is etc.) [15](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=65a20906-8203-4702-9285-6268d424c3bb&cid=ca00acb247e603aa)  
- `supabase_insert_row`, `supabase_update_row`, `supabase_delete_row`
- Observação: Supabase REST API é gerada do schema e usa PostgREST; segurança via RLS/roles/grants. [14](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=31e70c09-bfcf-4bf8-b115-552dceb11b3a&cid=ca00acb247e603aa)  

---

## 7) Segurança (NFRs e guardrails)
### 7.1 Princípios
- Least privilege (escopos mínimos).
- Sem vazamento de segredos em logs/erros.
- Auditoria para ações destrutivas.
- Proteção contra payloads enormes (limites e paginação). [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)[2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  

### 7.2 Streamable HTTP (se usado)
- Validar Origin header (DNS rebinding), bind localhost no modo local e autenticação em todas conexões. [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)  

### 7.3 Observação interna (opcional)
Existe no ambiente um `openapi.json` de uma “AgentEIA Fabric API” (pode inspirar uma integração futura ou gateway). [19](https://www.linkedin.com/pulse/mastering-structured-output-langgraph-raj-yadav-hvsmc)  

---

## 8) Testes, Qualidade e Evals
### 8.1 Qualidade
- Lint/format/typecheck.
- Testes unitários para schemas e validações.
- Testes de integração com mocks das APIs externas.

### 8.2 Evals MCP
Criar 10 perguntas read-only, complexas e verificáveis, focadas em:
- paginação
- busca/listagem
- resolução de IDs
- erros e remediação
- consistência de schema

---

## 9) Entregáveis
- Server MCP Python (stdio default; streamable-http opcional).
- 5 integrações implementadas em `tools/*`.
- Schemas Pydantic completos em `schemas/*`.
- Prompts separados em `prompts/*`.
- Docs: `PRD`, `CHECKLIST`, `SECURITY`, `INTEGRATIONS`, `ADRs`.

