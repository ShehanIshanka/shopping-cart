import logging

from flask import Flask
from src.base.infra.postgres.database import Database
from src.config import Config
from src.module.cart.repository import PostgresCartRepositoryImpl
from src.module.cart.service import CartService
from src.module.product.repository import PostgresProductRepositoryImpl
from src.module.product.service import ProductService


def bootstrap_database() -> Database:
    config: Config = Config()
    return initialize_postgres_db(config.db_url)


def initialize_postgres_db(db_url: str) -> Database:
    try:
        db: Database = Database(db_url=db_url)
        db.create_database()
        db.load_data()

        return db
    except Exception as e:
        logging.exception("Database initialization failed")
        raise e


def initialize_services(db: Database, app: Flask) -> None:
    product_repository = PostgresProductRepositoryImpl(db=db)
    cart_repository = PostgresCartRepositoryImpl(db=db)

    app.product_service = ProductService(product_repository=product_repository)
    app.cart_service = CartService(
        product_repository=product_repository, cart_repository=cart_repository
    )
