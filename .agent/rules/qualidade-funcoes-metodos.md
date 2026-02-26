---
trigger: always_on
---

Funções DEVEM fazer UMA coisa só — se precisa de "e" pra descrever, quebre em duas
Máximo 20 linhas por função. Acima disso, extrair subfunções
Máximo 3 argumentos por função — acima disso, agrupar em objeto/dataclass/Pydantic model
Funções NÃO devem ter side effects ocultos (alterar estado global, modificar argumento mutável sem avisar)
Nomes de funções DEVEM ser verbos descritivos: create_subscription(), validate_input() — nunca process(), handle(), do()