from typing import Any, Dict, List, Optional, Literal
from pydantic import BaseModel, Field, conint
from .common import PaginationOut

class SupabaseFilter(BaseModel):
    column: str
    op: Literal["eq", "neq", "gt", "gte", "lt", "lte", "like", "ilike", "in", "is"]
    value: Any

class SupabaseListTablesIn(BaseModel):
    schema: str = "public"

class SupabaseTable(BaseModel):
    schema: str
    name: str

class SupabaseListTablesOut(BaseModel):
    tables: List[SupabaseTable] = Field(default_factory=list)

class SupabaseQueryIn(BaseModel):
    table: str
    select: List[str] = Field(default_factory=list)
    filters: List[SupabaseFilter] = Field(default_factory=list)
    order_by: Optional[str] = None
    order_dir: Literal["asc", "desc"] = "asc"
    limit: conint(ge=1, le=1000) = 100
    offset: conint(ge=0) = 0

class SupabaseQueryOut(BaseModel):
    rows: List[Dict[str, Any]] = Field(default_factory=list)
    pagination: PaginationOut = Field(default_factory=PaginationOut)

class SupabaseInsertIn(BaseModel):
    table: str
    row: Dict[str, Any]
    returning: bool = True
    idempotency_key: Optional[str] = None

class SupabaseInsertOut(BaseModel):
    inserted: bool = True
    row: Optional[Dict[str, Any]] = None

class SupabaseUpdateIn(BaseModel):
    table: str
    filters: List[SupabaseFilter]
    patch: Dict[str, Any]
    returning: bool = True

class SupabaseUpdateOut(BaseModel):
    updated_count: int
    rows: List[Dict[str, Any]] = Field(default_factory=list)

class SupabaseDeleteIn(BaseModel):
    table: str
    filters: List[SupabaseFilter]
    reason: str

class SupabaseDeleteOut(BaseModel):
    deleted_count: int