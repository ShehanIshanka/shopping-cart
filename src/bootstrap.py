import logging
from typing import Dict

from src.base.infra.postgres.database import Database
from src.config import Config
from src.module.product.repository import PostgresProductRepositoryImpl
from src.module.product.service import ProductService


def bootstrap_database() -> Database:
    config: Config = Config()
    return initialize_postgres_db(config.db_url)


def initialize_postgres_db(db_url: str) -> Database:
    try:
        db: Database = Database(db_url=db_url)
        db.create_database()

        return db
    except Exception as e:
        logging.exception("Database initialization failed")
        raise e


def initialize_product_service(db: Database) -> ProductService:
    return ProductService(product_repository=PostgresProductRepositoryImpl(db=db))
