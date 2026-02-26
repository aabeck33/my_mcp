# Integração — Google Calendar

## Endpoints relevantes (referência)
- events.list retorna eventos com filtros e paginação (pageToken/nextPageToken). [5](https://developers.google.com/workspace/drive/api/guides/file-metadata)
- events.insert cria evento e suporta `sendUpdates`. [6](https://onedrive.live.com/?id=978199e2-c4c4-41c3-a652-d654a00c2f9a&cid=ca00acb247e603aa&web=1)

## Tools MCP
- gcal_list_calendars
- gcal_list_events (time_min/time_max + paginação)
- gcal_create_event (send_updates)
- gcal_update_event
- gcal_delete_event (destructive)

## Regras
- Sempre usar intervalo (time_min/time_max) para minimizar retorno. [5](https://developers.google.com/workspace/drive/api/guides/file-metadata)
- Delete exige reason e auditoria (política interna do projeto).