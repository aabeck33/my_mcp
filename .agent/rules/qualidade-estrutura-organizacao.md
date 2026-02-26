---
trigger: always_on
---

Lei de Demeter: NUNCA encadear acessos a.get_b().get_c().do_something() — criar método direto
Um arquivo, uma responsabilidade: não misturar routes + service + schemas no mesmo arquivo
Imports organizados: stdlib → third-party → local (Python) / react → libs → components → utils (TypeScript)
Código morto (funções não usadas, imports não usados, variáveis comentadas) DEVE ser removido, não comentado