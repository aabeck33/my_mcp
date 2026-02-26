from datetime import datetime
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, constr
from .common import PaginationIn, PaginationOut

class GCalCalendar(BaseModel):
    id: str
    summary: str
    time_zone: Optional[str] = None
    primary: bool = False

class GCalListCalendarsIn(BaseModel):
    pass

class GCalListCalendarsOut(BaseModel):
    calendars: List[GCalCalendar] = Field(default_factory=list)

class GCalEvent(BaseModel):
    id: str
    calendar_id: str
    summary: Optional[str] = None
    description: Optional[str] = None
    start: datetime
    end: datetime
    status: Optional[Literal["confirmed", "tentative", "cancelled"]] = None
    html_link: Optional[str] = None

class GCalListEventsIn(PaginationIn):
    calendar_id: str
    time_min: datetime
    time_max: datetime
    q: Optional[str] = None

class GCalListEventsOut(BaseModel):
    events: List[GCalEvent] = Field(default_factory=list)
    pagination: PaginationOut = Field(default_factory=PaginationOut)

class GCalCreateEventIn(BaseModel):
    calendar_id: str
    summary: constr(min_length=1, max_length=200)
    description: Optional[constr(max_length=5000)] = None
    start: datetime
    end: datetime
    attendees_emails: Optional[List[str]] = None
    send_updates: Optional[Literal["all", "externalOnly", "none"]] = "none"
    idempotency_key: Optional[str] = None

class GCalCreateEventOut(BaseModel):
    event_id: str
    html_link: Optional[str] = None

class GCalUpdateEventIn(BaseModel):
    calendar_id: str
    event_id: str
    summary: Optional[constr(min_length=1, max_length=200)] = None
    description: Optional[constr(max_length=5000)] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class GCalUpdateEventOut(BaseModel):
    updated: bool = True
    html_link: Optional[str] = None

class GCalDeleteEventIn(BaseModel):
    calendar_id: str
    event_id: str
    reason: str

class GCalDeleteEventOut(BaseModel):
    deleted: bool = True