# ADR 0001 — Transport MCP (stdio default; streamable-http opcional)

## Contexto
O MCP define `stdio` e `Streamable HTTP` como transports padrão. [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)

## Decisão
- Default: `stdio` para execução local e compatibilidade.
- Opcional: `streamable-http` quando necessário.

## Consequências / Requisitos
Se habilitar `streamable-http`:
- Validar `Origin` para prevenir DNS rebinding. [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)
- Bind em localhost no modo local. [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)
- Autenticação em todas conexões. [4](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0)