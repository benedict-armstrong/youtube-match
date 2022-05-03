from typing import Optional
from models import User
from sqlalchemy.orm import Session 
from schemas.user import UserCreate, UserInDB, UserUpdate

from crud.base import CRUDBase

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_state(self, db: Session, *,  state: str) -> Optional[UserInDB]:
        return db.query(User).filter(User.state == state).first()
    

user = CRUDUser(User)
