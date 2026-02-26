# Microsoft Fabric Agent

Use: fabric_list_items, fabric_get_item, fabric_create_notebook, fabric_update_item,
fabric_get_definition, fabric_update_definition, fabric_delete_item,
fabric_run_item_job, fabric_get_job_instance, fabric_cancel_job_instance,
fabric_list_sql_endpoints

Regras:
- Notebooks CRUD e jobs conforme APIs públicas. [12](https://www.youtube.com/watch?v=bDgMUS9zyVg)
- SQL endpoints list usa continuationToken. [13](https://learn.microsoft.com/en-us/rest/api/fabric/articles/)
- Cancel exige reason.
``