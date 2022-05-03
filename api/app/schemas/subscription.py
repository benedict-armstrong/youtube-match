from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel

class SubscriptionBase(BaseModel):
    channel_name: Optional[str] = None
    channel_id: Optional[str] = None
    

# Properties to receive via API on creation
class SubscriptionCreate(SubscriptionBase):
    channel_name: str
    channel_id: str
    user_id: int


# Properties to receive via API on update
class SubscriptionUpdate(SubscriptionBase):
    pass

class SubscriptionInDBBase(SubscriptionBase):
    id: int
    channel_name: str
    channel_id: str
    user_id: str

    class Config:
        orm_mode = True


# Additional properties to return via API
class Subscription(SubscriptionInDBBase):
    pass


# Additional properties stored in DB
class SubscriptionInDB(SubscriptionInDBBase):
    pass
