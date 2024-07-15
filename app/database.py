from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import DATABASE_URL

from models import UserModel, AbstractModel

from typing import Optional


class Database:
    engine = create_engine(DATABASE_URL, echo=True)  # type: ignore

    @classmethod
    def add_user(cls, user: UserModel) -> None:
        with Session(cls.engine) as session:
            with session.begin():
                session.add(user)
                # AbstractModel.metadata.create_all(cls.engine)  # type: ignore

    @classmethod
    def delete_user_by_id(cls, id: int) -> Optional[UserModel]:
        if (user := cls.get_user_by_id(id)) is None:
            return

        with Session(cls.engine) as session:
            with session.begin():
                session.delete(user)
        
        return user
    
    @classmethod
    def get_user_by_id(cls, id: int) -> Optional[UserModel]:
        with Session(cls.engine) as session:
            return session.query(UserModel).filter(UserModel.id == id).first()
