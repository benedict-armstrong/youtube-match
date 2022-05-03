import sys
from typing import Any
import google_auth_oauthlib
import google_auth_oauthlib.flow
from oauth2client import client
import json

from sqlalchemy.orm import Session as DBSession
from core.config import settings
import crud
from schemas import LoginSession, Credentials
from schemas.user import User, UserUpdate


def create_credentials(credentials):
  return Credentials(
    token=credentials.token,
    refresh_token=credentials.refresh_token,
    token_uri=credentials.token_uri,
    client_id=credentials.client_id,
    client_secret=credentials.client_secret,
    scopes=credentials.scopes
  )

def save_auth(db: DBSession, state: str, code: str) -> User:

  # TODO: Remove
  import os 
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  user = crud.user.get_by_state(db=db, state=state)

  flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    settings.CLIENT_SECRETS_FILE, scopes=settings.SCOPES, state=state)

  flow.redirect_uri = settings.REDIRECT_URL

  # Use the authorization server's response to fetch the OAuth 2.0 tokens.
  flow.fetch_token(code=code)

  # Store credentials in the session.
  # ACTION ITEM: In a production app, you likely want to save these
  #              credentials in a persistent database instead.
  credentials = flow.credentials

  try:
    user = crud.user.update(db=db, db_obj=user, obj_in=UserUpdate(credentials=create_credentials(credentials)))
  except Exception as e:
    crud.user.remove(db=db, db_obj=user)
    print(e)

  return user