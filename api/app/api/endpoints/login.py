import re
from typing import Any, Dict, Optional
from fastapi import APIRouter, Depends, Request
from requests import session
from sqlalchemy.orm import Session as DBSession
import api.deps as deps
from auth.get_auth_url import get_auth_url
from auth.google_auth import save_auth
from schemas.login_session import LoginSession
import google.oauth2.credentials
import googleapiclient.discovery
import crud
from core.config import settings
from schemas.subscription import SubscriptionCreate
from service.youtube import fetch_channels

router = APIRouter()


@router.get("/url", response_model=Dict[str, Any])
def get_url(
    uuid: Optional[str] = None,
    db: DBSession = Depends(deps.get_db),
) -> Any:
    url, uuid = get_auth_url(db=db, uuid=uuid)
    return {"url": url, "uuid": uuid}


@router.get('/oauth2callback', response_model=Any)
async def oauth2callback(
    state: str,
    code: str,
    db: DBSession = Depends(deps.get_db)
) -> Any:
    user = save_auth(db=db, state=state, code=code)

    credentials = google.oauth2.credentials.Credentials(**user.credentials)
    yt = googleapiclient.discovery.build(settings.API_SERVICE_NAME, settings.GOOGLE_API_VERSION, credentials=credentials)
    channels = fetch_channels(yt)
    for channel in channels:
        matches = re.search(r"(?P<channel_name>.*) \((?P<channel_id>.*)\)", channel)
        channel_name, channel_id = matches.group('channel_name'), matches.group('channel_id')
        crud.subscription.create(db=db, obj_in=SubscriptionCreate(
            channel_name=channel_name,
            channel_id=channel_id,
            user_id=user.id,
        ))

    session = crud.session.get(db=db, id=user.login_session_id)

    return {"uuid": session.uuid}