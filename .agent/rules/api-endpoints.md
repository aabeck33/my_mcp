---
trigger: model_decision
description: When creating APIs or any sort of endpoint
---

TODAS as rotas de API DEVEM ser autenticadas (exceto health check e rotas públicas explícitas)
Input validation obrigatória em TODAS as rotas via Pydantic models
Rate limiting por user_id em rotas sensíveis (auth, geração de conteúdo, billing)
CORS restritivo: aceitar requests APENAS dos domínios do frontend
Stripe webhooks DEVEM validar assinatura antes de processar
File upload: validar tipo MIME, extensão e tamanho máximo antes de aceitar