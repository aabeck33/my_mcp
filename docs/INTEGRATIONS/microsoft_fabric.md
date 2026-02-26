# Integração — Microsoft Fabric

## Notebooks (CRUD + Jobs)
A API pública de notebooks suporta criação/atualização/remoção e ações de job scheduler (run/cancel/status). [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)

## SQL Endpoints
- List SQL endpoints: GET /v1/workspaces/{workspaceId}/sqlEndpoints
- Suporta paginação via continuationToken. [13](https://learn.microsoft.com/en-us/rest/api/fabric/articles/)
- Escopos delegados (Workspace.Read.*) e a doc indica que service principal não é suportado para este endpoint específico. [13](https://learn.microsoft.com/en-us/rest/api/fabric/articles/)

## Tools MCP
- fabric_list_items, fabric_get_item
- fabric_create_notebook, fabric_update_item, fabric_delete_item [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)
- fabric_get_definition, fabric_update_definition [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)
- fabric_run_item_job, fabric_get_job_instance, fabric_cancel_job_instance [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)
- fabric_list_sql_endpoints (continuationToken) [13](https://learn.microsoft.com/en-us/rest/api/fabric/articles/)