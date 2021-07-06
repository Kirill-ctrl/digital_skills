from sqlalchemy.orm import sessionmaker

from course.week7.connection.base_engine import EngineConn


class SessionConn:

    session = None

    @staticmethod
    def create_session():
        return sessionmaker(bind=EngineConn.get_engine())

    @classmethod
    def get_session(cls):
        if not cls.session:
            sess = cls.create_session()
            cls.session = sess()
        return cls.session
