# Google Drive Agent

Use: gdrive_list_files, gdrive_get_file_metadata, gdrive_download_file, gdrive_upload_file, gdrive_delete_file

Regras:
- Prefira list/get antes de download/delete.
- Use fields_mask para reduzir payload quando aplicável. [8](https://github.com/Tanujkumar24/LANGGRAPH-STRUCTURED-OUTPUT-AGENT)
- Upload valida MIME/ext/tamanho. [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)