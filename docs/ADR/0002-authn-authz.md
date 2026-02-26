# ADR 0002 — AuthN/AuthZ (quando houver camada HTTP/API)

## Contexto
Regras do projeto: todas as rotas autenticadas (exceto health/públicas explícitas), validação Pydantic em todas as rotas, rate limit por user_id em rotas sensíveis e CORS restritivo. [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)

## Decisão
- Centralizar autenticação em middleware (quando houver HTTP).
- Implementar autorização por escopos/roles.

## Consequências
- Testes de autorização obrigatórios.
- Logging e auditoria sem PII.