# Integração — Google Drive

## Endpoints relevantes (referência)
- files.list suporta `pageToken`/`nextPageToken` e a recomendação de `fields` (field mask) para reduzir payload. [7](https://atalupadhyay.wordpress.com/2025/02/15/a-step-by-step-guide-with-pydantic-ai-and-langgraph-to-build-ai-agents/)[8](https://github.com/Tanujkumar24/LANGGRAPH-STRUCTURED-OUTPUT-AGENT)

## Tools MCP
- gdrive_list_files (q + paginação + fields_mask opcional)
- gdrive_get_file_metadata
- gdrive_download_file (max_bytes)
- gdrive_upload_file (validação MIME/ext/tamanho) [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)
- gdrive_delete_file (destructive)