from typing import Tuple
import google_auth_oauthlib.flow

import crud
from models.models import LoginSession
from schemas.login_session import LoginSessionInDB, LoginSessionCreate
from sqlalchemy.orm import Session as DBSession

from core.config import settings
from schemas.user import UserCreate


def get_auth_url(db: DBSession, uuid: str = None) -> Tuple[str, str]:
    # Use the client_secret.json file to identify the application requesting
    # authorization. The client ID (from that file) and access scopes are required.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(settings.CLIENT_SECRETS_FILE, scopes=settings.SCOPES)

    # Indicate where the API server will redirect the user after the user completes
    # the authorization flow. The redirect URI is required. The value must exactly
    # match one of the authorized redirect URIs for the OAuth 2.0 client, which you
    # configured in the API Console. If this value doesn't match an authorized URI,
    # you will get a 'redirect_uri_mismatch' error.

    print(uuid)

    if uuid is None:
        session: LoginSessionInDB = crud.session.create(db=db, obj_in = LoginSessionCreate())
    else:
        session: LoginSessionInDB = crud.session.get_by_uuid(db=db, uuid=uuid)



    flow.redirect_uri = settings.REDIRECT_URL

    # Generate URL for request to Google's OAuth 2.0 server.
    # Use kwargs to set optional request parameters.
    authorization_url, state = flow.authorization_url()
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        #access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        #include_granted_scopes='true')


    user = crud.user.create(db=db, obj_in = UserCreate(
        state=state,
        login_session_id=session.id
    ))

    return authorization_url, session.uuid