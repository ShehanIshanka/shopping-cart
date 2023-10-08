from datetime import datetime
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from src.base.infra.postgres.database import Base


class ProductModel(Base):
    """Product Model entity."""

    __tablename__ = "product"
    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    amount: Mapped[float] = mapped_column(nullable=False)
    created_time: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
    last_modified_time: Mapped[datetime] = mapped_column(
        nullable=False, onupdate=func.now()
    )
