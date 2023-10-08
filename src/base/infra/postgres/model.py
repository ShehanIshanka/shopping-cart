import uuid
from datetime import datetime
from typing import Dict, List

from sqlalchemy import ForeignKey, func, JSON, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.base.infra.postgres.database import Base


class ProductModel(Base):
    """Product Model entity."""

    __tablename__ = "product"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        autoincrement=False,
    )
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    amount: Mapped[float] = mapped_column(nullable=False)
    created_time: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
    last_modified_time: Mapped[datetime] = mapped_column(
        nullable=False, onupdate=func.now()
    )


class CartModel(Base):
    """Cart Model entity."""

    __tablename__ = "cart"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        autoincrement=False,
    )
    amount: Mapped[int] = mapped_column(nullable=False, default=func.now())
    created_time: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
    last_modified_time: Mapped[datetime] = mapped_column(
        nullable=False, default=func.now()
    )

    cart_items: Mapped[List["CartItemModel"]] = relationship(
        uselist=True,  # for one-to-Many relationship,
        lazy=False,
        primaryjoin="CartModel.id == CartItemModel.cart_id",
    )


class CartItemModel(Base):
    """Cart Items Model entity."""

    __tablename__ = "cart_item"
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    cart_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("cart.id", ondelete="restrict"),
        type_=UUID,
        autoincrement=False,
    )
    item_id: Mapped[str] = mapped_column(
        ForeignKey("product.id", ondelete="restrict"), type_=UUID, nullable=False
    )
    created_time: Mapped[datetime] = mapped_column(nullable=False, default=func.now())

    product: Mapped["ProductModel"] = relationship(
        uselist=False,  # for one-to-one relationship
        lazy=False,
        primaryjoin="CartItemModel.item_id == ProductModel.id",
    )


class OrderModel(Base):
    """Order Model entity."""

    __tablename__ = "order"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, autoincrement=False)
    basket: Mapped[Dict] = mapped_column(type_=JSON, nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False, default=func.now())
    delivery_time: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
    created_time: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
