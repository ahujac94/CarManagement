from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class Status(str, Enum):
    free: str = "free"
    reserved: str = "reserved"


class Car(BaseModel):
    name: str
    company: str
    model: str
    status: Status
    chassis_no: UUID
