---
trigger: model_decision
description: When creating anything using FastAPI
---

TODAS as routes e services do FastAPI DEVEM ser async
TODAS as chamadas a APIs externas (Supabase, Stripe, LLMs, Fal.ai) DEVEM ser await — nunca bloqueantes
Streaming de respostas de IA via SSE (Server-Sent Events) — nunca aguardar resposta completa para enviar
Conexões com banco e APIs externas DEVEM ter timeout configurado