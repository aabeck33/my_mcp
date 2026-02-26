---
trigger: model_decision
description: When creating login forms/screens
---

Autenticação entre frontend e backend SEMPRE via iron-session (cookie httpOnly, secure, sameSite=lax)
SESSION_SECRET com 32+ caracteres, armazenado exclusivamente em variável de ambiente
Frontend NUNCA se comunica diretamente com o backend — todo request passa pelo proxy autenticado (Next.js API Routes)
O proxy decripta o cookie, extrai o user_id e repassa via header X-User-Id para o backend
Backend valida o header X-User-Id em TODAS as rotas protegidas via dependency injection
Tokens, session IDs e refresh tokens NUNCA são expostos no frontend (nem em localStorage, nem em sessionStorage, nem em cookies acessíveis por JS)