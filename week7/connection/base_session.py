from sqlalchemy.orm import sessionmaker

from course.week7.connection.base_engine import EngineConn
from course.week7.models.account import Account


class SessionConn:

    session = {}

    @staticmethod
    def create_session():
        return sessionmaker(bind=EngineConn.get_engine())

    @classmethod
    def get_session(cls):
        sess = cls.create_session()
        sess.configure(bind=EngineConn.get_engine())
        return sess()

    @classmethod
    def get_or_create(cls, account: Account):
        if not cls.session.get(f'{account._id}'):
            sess = cls.create_session()
            sess.configure(bind=EngineConn.get_engine())
            cls.session[f'{account._id}'] = sess()
        return cls.session[f'{account._id}']
