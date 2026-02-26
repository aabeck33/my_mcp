from typing import List, Optional
from pydantic import BaseModel, Field, conint, constr
from .common import PaginationIn, PaginationOut

class GDriveFile(BaseModel):
    id: str
    name: str
    mime_type: Optional[str] = None
    size_bytes: Optional[int] = None
    modified_time: Optional[str] = None
    web_view_link: Optional[str] = None

class GDriveListFilesIn(PaginationIn):
    q: Optional[str] = None
    folder_id: Optional[str] = None
    include_trashed: bool = False
    fields_mask: Optional[str] = Field(None, description="Drive fields mask (opcional).")

class GDriveListFilesOut(BaseModel):
    files: List[GDriveFile]
    pagination: PaginationOut = Field(default_factory=PaginationOut)

class GDriveGetMetadataIn(BaseModel):
    file_id: str

class GDriveGetMetadataOut(BaseModel):
    file: GDriveFile

class GDriveDownloadIn(BaseModel):
    file_id: str
    max_bytes: conint(ge=1, le=50_000_000) = 10_000_000

class GDriveDownloadOut(BaseModel):
    file_id: str
    mime_type: Optional[str] = None
    content_base64: Optional[str] = None
    download_url: Optional[str] = None

class GDriveUploadIn(BaseModel):
    folder_id: Optional[str] = None
    name: constr(min_length=1, max_length=255)
    mime_type: constr(min_length=3, max_length=200)
    content_base64: str
    size_bytes: conint(ge=1, le=50_000_000)

class GDriveUploadOut(BaseModel):
    file_id: str
    web_view_link: Optional[str] = None

class GDriveDeleteIn(BaseModel):
    file_id: str
    reason: str

class GDriveDeleteOut(BaseModel):
    deleted: bool = True