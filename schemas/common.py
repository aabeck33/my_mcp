from __future__ import annotations
from typing import Any, Dict, Generic, Optional, TypeVar
from pydantic import BaseModel, Field, conint, constr

T = TypeVar("T")

class MCPError(BaseModel):
    code: constr(min_length=3, max_length=64) = Field(...)
    message: constr(min_length=1, max_length=500) = Field(...)
    retryable: bool = Field(False)
    remediation: Optional[str] = Field(None)
    details: Optional[Dict[str, Any]] = Field(None)

class PaginationIn(BaseModel):
    page_size: conint(ge=1, le=250) = Field(50)
    page_token: Optional[str] = Field(None)

class PaginationOut(BaseModel):
    next_page_token: Optional[str] = Field(None)
    continuation_token: Optional[str] = Field(None)
    total_estimate: Optional[int] = Field(None)

class ToolResult(BaseModel, Generic[T]):
    ok: bool
    data: Optional[T] = None
    error: Optional[MCPError] = None