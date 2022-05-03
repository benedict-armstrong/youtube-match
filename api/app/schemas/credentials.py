from typing import List, Optional
from pydantic import BaseModel


class Credentials(BaseModel):
    token: str
    refresh_token: Optional[str] = None
    token_uri: str
    client_id: str
    client_secret: str
    scopes: List[str]
