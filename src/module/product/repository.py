from abc import ABC, abstractmethod
from typing import List, Optional


from src.base.infra.postgres.database import Database
from src.base.infra.postgres.model import ProductModel
from src.module.product.domain.product import Product
from src.module.product.mapper import ProductMapper


class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> str:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, product_id: str) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def fetch_products(self) -> List[Product]:
        raise NotImplementedError

    @abstractmethod
    def update(self, product: Product) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, product_id: str) -> bool:
        raise NotImplementedError


class PostgresProductRepositoryImpl(ProductRepository):
    def __init__(self, db: Database) -> None:
        self.db: Database = db

    def create(self, product: Product) -> str:
        with self.db.get_session() as session:
            product_model: ProductModel = ProductMapper.to_persistence(product)
            session.add(product_model)

        return product.id.to_str()

    def find_by_id(self, product_id: str) -> Optional[Product]:
        with self.db.get_session() as session:
            product_model = session.query(ProductModel).filter_by(id=product_id).one()
            return ProductMapper.to_domain(product_model)

    def fetch_products(self) -> List[Product]:
        with self.db.get_session() as session:
            product_models: List[ProductModel] = session.query(ProductModel).all()
            return [
                ProductMapper.to_domain(product_model)
                for product_model in product_models
            ]

    def update(self, product: Product) -> Optional[Product]:
        raise NotImplementedError

    def delete_by_id(self, product_id: str) -> bool:
        with self.db.get_session() as session:
            product = session.query(ProductModel).filter_by(id=product_id).first()
            if product:
                session.delete(product)
                session.commit()
                return True

        return False
