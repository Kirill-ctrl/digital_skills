from sqlalchemy import insert, select

from course.week7.models.account import Account
from course.week7.connection.base_engine import EngineConn
from course.week7.connection.base_session import SessionConn


class AccountService:

    @staticmethod
    def create_account(account: Account):
        account.create_hash_password()
        sql = insert(Account).values(name=account.name, email=account.email, hash_password=account.hash_password)
        with EngineConn.get_connect() as conn:
            res = conn.execute(sql)
            conn.commit()
        return account

    @staticmethod
    def get_by_account_id(account_id: int):
        sql = select(Account.id, Account.name, Account.email, Account.hash_password).where(Account.id == account_id)
        with SessionConn.get_session() as sess:
            res = sess.execute(sql)
        return res

    @staticmethod
    def get_by_account_email(email: str):
        sql = select(Account.id, Account.name, Account.email).where(Account.email == email)
        with SessionConn.get_session() as sess:
            res = sess.execute(sql)
        return res
