from src.base.infra.mapper import Mapper
from src.base.infra.postgres.model import ProductModel
from src.module.product.domain.product import Product


class ProductMapper(Mapper):
    @staticmethod
    def to_domain(product_model: ProductModel) -> Product:
        return Product.create(
            product_id=product_model.id,
            name=product_model.name,
            description=product_model.description,
            amount=product_model.amount,
            created_time=product_model.created_time,
            last_modified_time=product_model.last_modified_time,
        )

    @staticmethod
    def to_persistence(product: Product) -> ProductModel:
        return ProductModel(
            product_id=product.id,
            name=product.name,
            description=product.description,
            amount=product.amount.value,
            created_time=product.created_time,
            last_modified_time=product.last_modified_time,
        )
