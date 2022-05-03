from typing import Optional
from models import LoginSession
from sqlalchemy.orm import Session as DBSession
from schemas.login_session import LoginSessionCreate, LoginSessionInDB, LoginSessionUpdate

from crud.base import CRUDBase

class CRUDSession(CRUDBase[LoginSession, LoginSessionCreate, LoginSessionUpdate]):
    def get_by_uuid(self, db: DBSession, *,  uuid: str) -> Optional[LoginSessionInDB]:
        return db.query(LoginSession).filter(LoginSession.uuid == uuid).first()

session = CRUDSession(LoginSession)
