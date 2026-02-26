# Guardrails Compartilhados (MCP + Agente)

1) Prefira tools read-only antes de write/destructive.
2) Nunca exponha segredos, tokens, chaves ou PII em outputs.
3) Use paginação e limites; evite respostas gigantes. [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)
4) Para destructive (delete/cancel), exija "reason" e registre auditoria.
5) Em caso de erro, siga remediation do erro estruturado e tente alternativa segura. [3](https://onedrive.live.com/?id=fe7e3145-e18f-4a8b-ae5a-ea75b205bc2e&cid=ca00acb247e603aa&web=1)
6) Dados estruturados devem seguir schema Pydantic (Structured Output). [1](https://onedrive.live.com/?id=c5fc793d-4074-4363-a282-68159ca0f808&cid=ca00acb247e603aa&web=1)