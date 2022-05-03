from typing import List

from sqlalchemy import text
from models import Subscription
from schemas.subscription import SubscriptionCreate, SubscriptionInDB, SubscriptionUpdate
from sqlalchemy.orm import Session

from crud.base import CRUDBase

class CRUDSubscription(CRUDBase[Subscription, SubscriptionCreate, SubscriptionUpdate]):
    def get_shared_subscriptions(self, db: Session, user_ids: List[int]) -> List[str]:
        params = {}
        params["user_ids"] = tuple(user_ids)
        statement = text("""
        
        SELECT distinct channel_name from (
            Select * from subscriptions where user_id in :user_ids
        ) sub
        Group by channel_name
        Having COUNT(channel_name) > 1
        
        """)
        return db.execute(statement, params).fetchall()

    # q = db_session.query(Device, ParentDevice)\
    # .outerjoin(
    #               (ParentDevice, Device.parent_device_id==ParentDevice.device_id)
    #           )


subscription = CRUDSubscription(Subscription)
