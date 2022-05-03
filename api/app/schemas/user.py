from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, EmailStr

from schemas.credentials import Credentials
from schemas.subscription import Subscription

class UserBase(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    credentials: Optional[Credentials] = None
    state: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    name: Optional[str]
    email: Optional[EmailStr]
    login_session_id: int
    state: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    credentials: Optional[Credentials]
    name: Optional[str]
    email: Optional[EmailStr]


class UserInDBBase(UserBase):
    id: int
    created_at:datetime
    uuid: str
    subscriptions: List[Subscription]

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    pass
