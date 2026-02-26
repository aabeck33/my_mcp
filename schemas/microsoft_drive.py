from typing import List, Optional, Literal
from pydantic import BaseModel, Field, conint, constr
from .common import PaginationIn, PaginationOut

class MSDrive(BaseModel):
    id: str
    drive_type: Optional[str] = None
    owner: Optional[str] = None

class MSDriveItem(BaseModel):
    id: str
    drive_id: Optional[str] = None
    name: str
    size_bytes: Optional[int] = None
    is_folder: bool = False
    web_url: Optional[str] = None
    download_url: Optional[str] = None

class MSListDrivesIn(BaseModel):
    pass

class MSListDrivesOut(BaseModel):
    drives: List[MSDrive] = Field(default_factory=list)

class MSListChildrenIn(PaginationIn):
    drive_id: str
    parent_item_id: Optional[str] = None
    select_fields: Optional[str] = None

class MSListChildrenOut(BaseModel):
    items: List[MSDriveItem] = Field(default_factory=list)
    pagination: PaginationOut = Field(default_factory=PaginationOut)

class MSGetItemIn(BaseModel):
    drive_id: str
    item_id: str

class MSGetItemOut(BaseModel):
    item: MSDriveItem

class MSDownloadItemIn(BaseModel):
    drive_id: str
    item_id: str
    max_bytes: conint(ge=1, le=50_000_000) = 10_000_000

class MSDownloadItemOut(BaseModel):
    item_id: str
    content_base64: Optional[str] = None
    download_url: Optional[str] = None

class MSUploadSmallIn(BaseModel):
    drive_id: str
    parent_item_id: str
    file_name: constr(min_length=1, max_length=255)
    mime_type: Optional[str] = None
    content_base64: str
    size_bytes: conint(ge=1, le=4_000_000)

class MSUploadSmallOut(BaseModel):
    item: MSDriveItem

class MSCreateUploadSessionIn(BaseModel):
    drive_id: str
    parent_item_id: str
    file_name: constr(min_length=1, max_length=255)
    conflict_behavior: Optional[Literal["fail", "replace", "rename"]] = "rename"

class MSCreateUploadSessionOut(BaseModel):
    upload_url: str
    expiration_datetime: Optional[str] = None

class MSDeleteItemIn(BaseModel):
    drive_id: str
    item_id: str
    reason: str

class MSDeleteItemOut(BaseModel):
    deleted: bool = True