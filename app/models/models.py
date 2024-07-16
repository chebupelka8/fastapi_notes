from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


# @as_declarative()
class AbstractModel(DeclarativeBase):
    ...


class UserModel(AbstractModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)

