from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


class EngineConn:

    engine = None

    @classmethod
    def set_engine(cls, database: str) -> None:
        cls.engine = create_engine(f'sqlite:///{database}.db', echo=True)
        return cls.engine

    @classmethod
    def get_engine(cls) -> Engine:
        return cls.engine

    @classmethod
    def get_connect(cls):
        return cls.engine.connect()
