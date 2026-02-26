---
trigger: manual
---

NUNCA expor IDs internos (user_id, session_id, empresa_id, subscription_id) no console do browser
NUNCA logar dados sensíveis em console.log (tokens, emails, senhas, IDs internos)
NUNCA incluir IDs internos em URLs visíveis do frontend — usar slugs ou UUIDs curtos quando necessário
Variáveis de ambiente sensíveis NUNCA devem ter prefixo NEXT_PUBLIC_
Error messages retornadas ao frontend NUNCA devem expor stack traces, queries SQL ou estrutura interna