from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy import ForeignKey


# @as_declarative()
class AbstractModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)


class UserModel(AbstractModel):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(unique=True, autoincrement=True)
    name: Mapped[str]


class NoteModel(AbstractModel):
    __tablename__ = "notes"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    title: Mapped[str]

