import logging

import sqlalchemy.exc
from sqlalchemy import insert, select

from course.week7.models.account import Account
from course.week7.connection.base_session import SessionConn


class AccountService:

    @staticmethod
    def create_account(account: Account):
        sess = SessionConn.get_or_create(account)
        account.create_hash_password()
        try:
            res = sess.add(account)
            sess.commit()
        except sqlalchemy.exc.IntegrityError as exc:
            logging.warning(exc._message())
            return None
        print(res)
        return res

    @staticmethod
    def get_by_account_id(account_id: int):
        sess = SessionConn.get_session()
        res = sess.query(Account).filter(Account._id == account_id).first()
        sess.close()
        return res

    @staticmethod
    def get_by_account_email(email: str):
        sess = SessionConn.get_session()
        res = sess.query(Account).filter(Account.email == email).first()
        sess.close()
        return res
