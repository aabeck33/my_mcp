---
trigger: model_decision
description: When creating AI Agents or MCP related stuff
---

Agentes DEVEM ser implementados com LangGraph (state machine com nós e transições)
Cada nó do grafo DEVE ter responsabilidade única e saída tipada
Respostas do agente DEVEM usar Structured Output (Pydantic models) — nunca texto livre para dados estruturados
Tools do agente DEVEM ter error handling individual — falha de uma tool não deve derrubar o grafo
Prompts do agente DEVEM ficar em arquivos separados, nunca hardcoded dentro da lógica