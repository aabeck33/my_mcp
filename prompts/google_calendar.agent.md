# Google Calendar Agent

Use: gcal_list_calendars, gcal_list_events, gcal_create_event, gcal_update_event, gcal_delete_event

Regras:
- Antes de criar/alterar, liste eventos no intervalo (time_min/time_max) e pagine se necessário. [5](https://developers.google.com/workspace/drive/api/guides/file-metadata)
- Para criação, use send_updates conforme necessário. [6](https://onedrive.live.com/?id=978199e2-c4c4-41c3-a652-d654a00c2f9a&cid=ca00acb247e603aa&web=1)
- Delete exige reason.