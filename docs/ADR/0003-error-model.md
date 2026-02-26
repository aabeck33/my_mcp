# ADR 0003 — Modelo de erro estruturado (MCPError)

## Contexto
Boas práticas MCP pedem erros acionáveis e orientados à solução. [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)
Regras do projeto exigem Structured Output com Pydantic. [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)

## Decisão
- Padronizar erro como `MCPError { code, message, retryable, remediation, details }`.
- Nunca vazar segredos/PII.

## Consequências
- Todas tools devem mapear erros upstream para esse formato.