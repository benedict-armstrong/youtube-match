import re
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession
import api.deps as deps
from core.config import settings
import crud
import google.oauth2.credentials
import googleapiclient.discovery
from schemas.subscription import Subscription, SubscriptionCreate

from service.youtube import fetch_channels

router = APIRouter()


# @router.get("/{uuid}", response_model=Any)
# async def get_subscriptions(
#     uuid: str,
#     db: DBSession = Depends(deps.get_db),
# ) -> Any:
#     session = crud.session.get_by_uuid(db=db, uuid=uuid)
#     if session is None:
#         raise HTTPException(
#             status_code=404, detail="Not found")

#     for user in session.users:
#         credentials = google.oauth2.credentials.Credentials(**user.credentials)
#         yt = googleapiclient.discovery.build(settings.API_SERVICE_NAME, settings.GOOGLE_API_VERSION, credentials=credentials)
#         channels = fetch_channels(yt)
#         for channel in channels:
#             matches = re.search(r"(?P<channel_name>.*)\((?P<channel_id>.*)\)", channel)
#             channel_name, channel_id = matches.group('channel_name'), matches.group('channel_id')
#             crud.subscription.create(db=db, obj_in=SubscriptionCreate(
#                 channel_name=channel_name,
#                 channel_id=channel_id,
#                 user_id=user.id,
#             ))

#     return "OK"

@router.get("/{uuid}" , response_model=Any)
def get_subscriptions(
    uuid: str,
    db: DBSession = Depends(deps.get_db),
) -> Any:
    session = crud.session.get_by_uuid(db=db, uuid=uuid)
    if session is None:
        raise HTTPException(
            status_code=404, detail="Not found")
    
    user_ids = []
    for user in session.users:
        user_ids.append(user.id)

    subs = crud.subscription.get_shared_subscriptions(db=db, user_ids=user_ids)

    return [sub["channel_name"] for sub in subs]
