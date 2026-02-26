# SECURITY — MCP Server (Python)

## 1) Escopo de segurança
Este documento define guardrails de segurança para:
- transport MCP (stdio e opcional streamable-http)
- autenticação/autorização (se aplicável)
- validação de inputs (Pydantic)
- proteção de dados (PII/secrets)
- auditoria de ações destrutivas
- práticas específicas por integração

## 2) Controles obrigatórios (derivados das regras do projeto)
- Prompts não podem estar hardcoded; devem estar em arquivos versionados. [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  
- Tools com erro isolado (falha não derruba grafo). [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  
- Structured Output via Pydantic para dados estruturados. [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)  
- Em HTTP: autenticação em rotas, validação Pydantic, rate limit por user_id (sensíveis), CORS restritivo, uploads validados. [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  
- Em streamable-http: validar Origin e bind localhost no modo local. [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)  

## 3) Modelo de ameaça (high-level)
### Ameaças comuns
- Exfiltração de tokens/PII por logs/erros
- SSRF / DNS rebinding contra servidor local (streamable-http)
- Abuso de tools destrutivas (delete/cancel)
- Payload gigante (download/upload), saturação
- Escopos excessivos (permissões amplas)

### Mitigações
- Redaction de segredos em logs; erros estruturados sem conteúdo sensível.
- Rate limiting em rotas sensíveis (quando houver API). [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  
- Paginação, limites de bytes em downloads, validação de uploads. [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  
- Validação `Origin` e bind localhost para evitar DNS rebinding no streamable-http. [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)  
- Auditoria e “reason” obrigatório para destructive.

## 4) Segurança por integração (pontos críticos)
### Google Drive / Microsoft Drive
- Downloads devem ter limite (max_bytes) e evitar retorno de payloads grandes.
- Uploads devem validar MIME/ext/tamanho. [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)  

### Microsoft Graph (upload grande)
- Upload grande deve usar `createUploadSession` (resumível). [11](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/blob/main/api-reference/beta/resources/driveitem.md)  

### Microsoft Fabric
- SQL endpoints list: requer escopos delegados e suporta paginação; observar throttling/429. [13](https://learn.microsoft.com/en-us/rest/api/fabric/articles/)  
- Notebooks CRUD/jobs: APIs públicas, com capacidade de automação. [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)  

### Supabase
- Usar filtros PostgREST e respeitar RLS/roles/grants. [14](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=31e70c09-bfcf-4bf8-b115-552dceb11b3a&cid=ca00acb247e603aa)[15](https://onedrive.live.com/personal/ca00acb247e603aa/_layouts/15/doc.aspx?resid=65a20906-8203-4702-9285-6268d424c3bb&cid=ca00acb247e603aa)  

## 5) Auditoria
- Logar (sem PII) quem acionou: tool, parâmetros não sensíveis, resultado, code.
- Para destructive: reason obrigatório; registrar id do recurso e timestamp.
