# CHECKLIST — MCP Server (Python)

**Projeto:** <nome>  
**Owner:** <time>  
**Versão:** <semver>  
**Transport:** stdio | streamable-http  
**Última atualização:** <YYYY-MM-DD>

---

## 0) PR GATE (obrigatório para merge)
- [ ] Segurança (Seção 1) 100% PASS
- [ ] MCP Compliance (Seção 2) 100% PASS
- [ ] LangGraph & Prompts (Seção 3) 100% PASS
- [ ] Observabilidade mínima (Seção 4) 100% PASS
- [ ] Testes & Qualidade (Seção 5) 100% PASS

Evidências:
- CI: <link>
- pytest/coverage: <link>
- logs sample (redacted): <link>
- evals.xml: <link>

---

## 1) Segurança (obrigatório)
### 1.1 Controles gerais
- [ ] Structured Output via Pydantic (PASS/FAIL) [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  Evidência: ___
- [ ] Error handling isolado por tool (PASS/FAIL) [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  Evidência: ___
- [ ] Prompts em arquivos separados (PASS/FAIL) [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  Evidência: ___
- [ ] Paginação/limites para reduzir contexto (PASS/FAIL) [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)  Evidência: ___

### 1.2 Se houver HTTP endpoints
- [ ] Rotas autenticadas exceto health/públicas explícitas (PASS/FAIL) [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  Evidência: ___
- [ ] Validação Pydantic em todas as rotas (PASS/FAIL) [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  Evidência: ___
- [ ] Rate limit por user_id em rotas sensíveis (PASS/FAIL) [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  Evidência: ___
- [ ] CORS restritivo (PASS/FAIL) [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  Evidência: ___
- [ ] Upload valida MIME/ext/tamanho (PASS/FAIL) [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  Evidência: ___

### 1.3 Streamable HTTP (se habilitado)
- [ ] Validar Origin header (anti DNS rebinding) (PASS/FAIL) [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)  Evidência: ___
- [ ] Bind localhost no modo local (PASS/FAIL) [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)  Evidência: ___
- [ ] Autenticação nas conexões (PASS/FAIL) [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)  Evidência: ___

### 1.4 Auditoria e logs
- [ ] Redaction de secrets/PII (PASS/FAIL) Evidência: ___
- [ ] destructive exige reason + auditoria (PASS/FAIL) Evidência: ___

---

## 2) MCP Compliance (obrigatório)
- [ ] Naming consistente (prefixo+verbo+objeto) (PASS/FAIL) [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)  Evidência: ___
- [ ] Tools com schemas (input/output) (PASS/FAIL) [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)[3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)  Evidência: ___
- [ ] Paginação/filtros onde aplicável (PASS/FAIL) [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)  Evidência: ___
- [ ] Erros acionáveis com remediation (PASS/FAIL) [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)  Evidência: ___

---

## 3) LangGraph & Prompts (obrigatório)
- [ ] LangGraph usado (PASS/FAIL) [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  Evidência: ___
- [ ] Nós com responsabilidade única + saída tipada (PASS/FAIL) [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  Evidência: ___
- [ ] Tool failure não derruba grafo (PASS/FAIL) [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  Evidência: ___
- [ ] Prompts externos (PASS/FAIL) [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  Evidência: ___

---

## 4) Observabilidade (mínimo)
- [ ] Logs estruturados + correlation_id (PASS/FAIL) Evidência: ___
- [ ] Métricas por tool (latência/erros) (PASS/FAIL) Evidência: ___
- [ ] Healthcheck (PASS/FAIL) Evidência: ___

---

## 5) Testes & Qualidade
- [ ] Unit tests schemas/validações (PASS/FAIL) Evidência: ___
- [ ] Integration tests com mocks (PASS/FAIL) Evidência: ___
- [ ] Lint/format/typecheck (PASS/FAIL) Evidência: ___
- [ ] SAST (PASS/FAIL) Evidência: ___

---

## 6) Requisitos mínimos por integração (PASS/FAIL)
### Google Calendar
- [ ] list events usa time_min/time_max e paginação [5](https://developers.google.com/workspace/drive/api/guides/file-metadata) Evidência: ___
- [ ] insert suporta send_updates conforme API [6](https://onedrive.live.com/?id=978199e2-c4c4-41c3-a652-d654a00c2f9a&cid=ca00acb247e603aa&web=1) Evidência: ___

### Google Drive
- [ ] list files paginação + fields_mask quando aplicável [7](https://atalupadhyay.wordpress.com/2025/02/15/a-step-by-step-guide-with-pydantic-ai-and-langgraph-to-build-ai-agents/)[8](https://github.com/Tanujkumar24/LANGGRAPH-STRUCTURED-OUTPUT-AGENT) Evidência: ___

### Microsoft Drive
- [ ] driveItem/Drive mapeados [9](https://deepwiki.com/modelcontextprotocol/java-sdk/5.3-streamable-http-transport)[10](https://mcpindotnet.github.io/docs/concepts/architecture-overview/layers/transport-layer/streamable-http/) Evidência: ___
- [ ] upload grande via createUploadSession [11](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/blob/main/api-reference/beta/resources/driveitem.md) Evidência: ___

### Microsoft Fabric
- [ ] notebooks CRUD + jobs [12](https://www.youtube.com/watch?v=bDgMUS9zyVg) Evidência: ___
- [ ] sqlEndpoints list com continuationToken [13](https://learn.microsoft.com/en-us/rest/api/fabric/articles/) Evidência: ___

### Supabase
- [ ] REST PostgREST + RLS respeitado [14](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=31e70c09-bfcf-4bf8-b115-552dceb11b3a&cid=ca00acb247e603aa) Evidência: ___
- [ ] filtros PostgREST suportados [15](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=65a20906-8203-4702-9285-6268d424c3bb&cid=ca00acb247e603aa) Evidência: ___