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
                AbstractModel.metadata.create_all(cls.engine)  # type: ignore

                session.add(user)
    
    @classmethod
    def get_user_by_id(cls, id: int):
        with Session(cls.engine) as session:
            return session.query(UserModel).filter(UserModel.id == id).first()
