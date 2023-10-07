from contextlib import contextmanager

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from src.base.exceptions import DatabaseError

Base = declarative_base()


class Database:
    def __init__(self, db_url: str) -> None:
        self.db_engine: Engine = create_engine(db_url)

    def create_database(self) -> None:
        Base.metadata.create_all(self.db_engine)

    @contextmanager
    def get_session(self) -> Session:
        session = None
        try:
            sm = sessionmaker(bind=self.db_engine)
            session = sm()
            yield session
            session.commit()
        except Exception as e:
            if session:
                session.rollback()
            raise DatabaseError(e)
        finally:
            if session:
                session.close()
