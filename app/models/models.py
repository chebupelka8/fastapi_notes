from sqlalchemy.orm import mapped_column, Mapped, as_declarative


@as_declarative()
class AbstractModel:
    ...


class UserModel(AbstractModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)

