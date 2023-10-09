import csv
from contextlib import contextmanager

from sqlalchemy import create_engine, Engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import text
from src.base.exceptions import DatabaseError, NoResultFoundError
from src.base.infra.postgres.model import Base


class Database:
    def __init__(self, db_url: str) -> None:
        self.db_engine: Engine = create_engine(db_url)

    def create_database(self) -> None:
        Base.metadata.drop_all(self.db_engine)
        Base.metadata.create_all(self.db_engine)

    def load_data(self) -> None:
        with self.get_session() as session:
            for table_name in ["product", "cart", "cart_item"]:
                insert_statement: str = get_insert_table_statement(
                    table_name=table_name
                )
                session.execute(text(insert_statement))

    @contextmanager
    def get_session(self) -> Session:
        session = None
        try:
            sm = sessionmaker(bind=self.db_engine)
            session = sm()
            yield session
            session.commit()
        except NoResultFound as e:
            if session:
                session.rollback()
            raise NoResultFoundError(e)
        except Exception as e:
            if session:
                session.rollback()
            raise DatabaseError(e)
        finally:
            if session:
                session.close()


def get_insert_table_statement(table_name: str) -> str:
    with open(
        f"resources/sample_data/{table_name}.csv", "r", encoding="utf-8"
    ) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        values = []
        for row in csv_reader:
            value: str = "', '".join(row)
            values.append(f"('{value}')")

        insert_statement: str = f"INSERT INTO {table_name} VALUES {','.join(values)};"
        return insert_statement
