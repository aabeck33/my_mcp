---
trigger: always_on
---

Python: type hints obrigatórios em todas as funções e variáveis. Sem Any genérico.
TypeScript: strict mode habilitado. Sem any, sem @ts-ignore, sem as unknown as.
Sempre usar bibliotecas e componentes padrão do ecossistema (shadcn/ui, Pydantic, Supabase client) — código customizado somente se o usuário solicitar explicitamente
Organização por domínio: cada módulo com seus routes, service, schemas — nunca misturar domínios
Secrets e chaves de API exclusivamente em .env — NUNCA hardcoded, NUNCA commitados no git
.env.example DEVE existir com todas as variáveis necessárias, sem valores reais