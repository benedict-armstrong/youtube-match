import secrets
from typing import Set
import os

from pydantic import (
    BaseSettings,
)

db_string = 'postgresql://{user}:{password}@{host}/{db}'.format(user=os.getenv(
    'PGUSER'), host=os.getenv("PGHOST"), db=os.getenv("PGDATABASE"), password=os.getenv("PGPASSWORD"))


class Settings(BaseSettings):
    APP_BASE_URL = os.getenv("APP_BASE_URL") or "http://localhost:8000"
    API_VERSION: str = 'v1'
    API_PREFIX: str = f'/api/{API_VERSION}'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 2  # 2 days
    SECRET_KEY: str = 'test'  # secrets.token_urlsafe(32)
    FIRST_SUPERUSER: str = "admin@test.com"
    FIRST_SUPERUSER_PASSWORD: str = "test"
    CLIENT_SECRETS_FILE: str = "secret/client_secret.json"
    API_SERVICE_NAME: str = "youtube"
    GOOGLE_API_VERSION: str = "v3"
    REDIRECT_URL: str = '{}{}/login/oauth2callback'.format(APP_BASE_URL, API_PREFIX)
    
    SCOPES: Set[str] = {
        'https://www.googleapis.com/auth/userinfo.profile',
        'openid',
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/youtube'
    }
    SQLALCHEMY_DATABASE_URI: str = db_string if os.getenv(
        "PGHOST") else "postgresql://postgres:postgres@localhost/ym"


settings = Settings()
