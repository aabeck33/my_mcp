---
trigger: manual
---

TODAS as tabelas do Supabase DEVEM ter RLS habilitado, sem exceção
Toda tabela com dados de usuário DEVE ter coluna user_id com policy de isolamento
Policies obrigatórias por tabela: SELECT, INSERT, UPDATE, DELETE filtrados por auth.uid() = user_id
Tabelas públicas (ex: plans) DEVEM ter policy explícita de somente leitura
Operações de escrita em tabelas públicas SOMENTE via service_role no backend
Testar isolamento: User A NUNCA deve acessar dados do User B