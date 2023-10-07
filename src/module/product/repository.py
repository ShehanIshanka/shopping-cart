from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.exc import NoResultFound
from src.base.infra.postgres.database import Database
from src.base.infra.postgres.model import ProductModel
from src.module.product.domain.product import Product
from src.module.product.mapper import ProductMapper


class ProductRepository(ABC):
    """Repository interface for Product entity"""

    @abstractmethod
    def create(self, product: Product) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, product_id: str) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def update(self, product: Product) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, product_id: str) -> None:
        raise NotImplementedError


class PostgresProductRepositoryImpl(ProductRepository):
    """ProductRepositoryImpl implements CRUD operations related Product entity using SQLAlchemy."""

    def __init__(self, db: Database) -> None:
        self.db: Database = db

    def create(self, product: Product) -> None:
        with self.db.get_session() as session:
            product_model: ProductModel = ProductMapper.to_persistence(product)
            session.add(product_model)

    def find_by_id(self, product_id: str) -> Optional[Product]:
        try:
            with self.db.get_session() as session:
                product_model: ProductModel = (
                    session.query(ProductModel).filter_by(id=product_id).one()
                )
                return ProductMapper.to_domain(product_model)
        except NoResultFound:
            return None
        except:
            raise

    def update(self, product: Product) -> Optional[Product]:
        raise NotImplementedError

    def delete_by_id(self, product_id: str) -> None:
        with self.db.get_session() as session:
            ProductModel.query.filter_by(id=product_id).delete()
            session.commit()
