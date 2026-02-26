# Integração — Microsoft Drive (OneDrive/SharePoint via Microsoft Graph)

## Conceitos do Graph
- Microsoft Graph expõe `Drive` e `DriveItem` para trabalhar com arquivos e bibliotecas. [9](https://deepwiki.com/modelcontextprotocol/java-sdk/5.3-streamable-http-transport)[10](https://mcpindotnet.github.io/docs/concepts/architecture-overview/layers/transport-layer/streamable-http/)
- Upload grande/resumível via `driveItem: createUploadSession`. [11](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/blob/main/api-reference/beta/resources/driveitem.md)

## Tools MCP
- msdrive_list_drives
- msdrive_list_children
- msdrive_get_item
- msdrive_download_item (max_bytes)
- msdrive_upload_small (validação upload) [2](https://www.bilibili.com/video/BV15z411B7Dq/?uid=425631357A34313142374471)
- msdrive_create_upload_session (upload grande) [11](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/blob/main/api-reference/beta/resources/driveitem.md)
- msdrive_delete_item (destructive + reason)

## Observações
- Preferir operações de metadata/list antes de baixar conteúdo.