---
trigger: always_on
---

Usar exceptions em vez de return codes — manter lógica limpa
NUNCA retornar None/null para indicar erro — levantar exception com mensagem clara
NUNCA passar None/null como argumento padrão mutável
Try/except DEVE ser específico: capturar ValueError, HTTPException — NUNCA except Exception genérico (exceto em catch-all de último nível)
Erros de domínio DEVEM usar exceptions customizadas: SubscriptionExpiredError, QuotaExceededError