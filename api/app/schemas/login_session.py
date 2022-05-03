from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel

from schemas.user import User

class LoginSessionBase(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime]
    uuid: Optional[str] = None

# Properties to receive via API on creation
class LoginSessionCreate(LoginSessionBase):
    pass


# Properties to receive via API on update
class LoginSessionUpdate(LoginSessionBase):
    pass

class LoginSessionInDBBase(LoginSessionBase):
    id: int
    created_at:datetime
    uuid: str
    users: List[User]

    class Config:
        orm_mode = True


# Additional properties to return via API
class LoginSession(LoginSessionInDBBase):
    pass


# Additional properties stored in DB
class LoginSessionInDB(LoginSessionInDBBase):
    pass
