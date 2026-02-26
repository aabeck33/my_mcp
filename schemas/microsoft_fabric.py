from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field, constr
from .common import PaginationIn, PaginationOut

class FabricItem(BaseModel):
    id: str
    display_name: str
    type: str
    workspace_id: str

class FabricListItemsIn(PaginationIn):
    workspace_id: str

class FabricListItemsOut(BaseModel):
    items: List[FabricItem] = Field(default_factory=list)
    pagination: PaginationOut = Field(default_factory=PaginationOut)

class FabricGetItemIn(BaseModel):
    workspace_id: str
    item_id: str

class FabricGetItemOut(BaseModel):
    item: FabricItem

class FabricCreateNotebookIn(BaseModel):
    workspace_id: str
    display_name: constr(min_length=1, max_length=200)
    definition_format: Literal["ipynb", "fabricGitSource"] = "ipynb"
    parts: List[Dict[str, Any]]

class FabricCreateNotebookOut(BaseModel):
    item: FabricItem

class FabricUpdateItemIn(BaseModel):
    workspace_id: str
    item_id: str
    display_name: Optional[constr(min_length=1, max_length=200)] = None

class FabricUpdateItemOut(BaseModel):
    updated: bool = True

class FabricGetDefinitionIn(BaseModel):
    workspace_id: str
    item_id: str

class FabricGetDefinitionOut(BaseModel):
    definition: Dict[str, Any]

class FabricUpdateDefinitionIn(BaseModel):
    workspace_id: str
    item_id: str
    definition_format: Literal["ipynb", "fabricGitSource"] = "ipynb"
    parts: List[Dict[str, Any]]

class FabricUpdateDefinitionOut(BaseModel):
    updated: bool = True

class FabricDeleteItemIn(BaseModel):
    workspace_id: str
    item_id: str
    reason: str

class FabricDeleteItemOut(BaseModel):
    deleted: bool = True

class FabricRunNotebookIn(BaseModel):
    workspace_id: str
    item_id: str
    job_type: str
    parameters: Optional[Dict[str, Any]] = None

class FabricRunNotebookOut(BaseModel):
    job_instance_id: str

class FabricGetJobInstanceIn(BaseModel):
    workspace_id: str
    item_id: str
    job_instance_id: str

class FabricGetJobInstanceOut(BaseModel):
    status: Dict[str, Any]

class FabricCancelJobInstanceIn(BaseModel):
    workspace_id: str
    item_id: str
    job_instance_id: str
    reason: str

class FabricCancelJobInstanceOut(BaseModel):
    canceled: bool = True

class FabricSqlEndpoint(BaseModel):
    id: str
    display_name: str
    type: str
    workspace_id: str
    description: Optional[str] = None

class FabricListSqlEndpointsIn(BaseModel):
    workspace_id: str
    continuation_token: Optional[str] = None
    recursive: Optional[bool] = None
    root_folder_id: Optional[str] = None

class FabricListSqlEndpointsOut(BaseModel):
    endpoints: List[FabricSqlEndpoint] = Field(default_factory=list)
    pagination: PaginationOut = Field(default_factory=PaginationOut)