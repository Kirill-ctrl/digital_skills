import logging

import sqlalchemy.exc
from sqlalchemy import insert, select, update

from course.week7.models.account import Account
from course.week7.connection.base_session import SessionConn


class AccountService:

    @staticmethod
    def create_account(account: Account):
        account.create_hash_password()
        with SessionConn.get_session() as sess:
            try:
                sess.add(account)
                sess.commit()
                account_id = sess.query(Account._id.label("account_id")).filter_by(email=account.email).one()
                account._id = account_id[0]
            except sqlalchemy.exc.IntegrityError as exc:
                logging.warning(exc._message())
                return None
        return account

    @staticmethod
    def get_by_account_id(account_id: int):
        with SessionConn.get_session() as sess:
            res = sess.query(Account).filter(Account._id == account_id).first()
        return res

    @staticmethod
    def get_by_account_email(email: str):
        with SessionConn.get_session() as sess:
            res = sess.query(Account).filter(Account.email == email).first()
        return res

    @staticmethod
    def update_account_email(account_id: int, new_email: str):
        with SessionConn.get_session() as sess:
            res = sess.query(Account).filter(Account._id == account_id).update({"email": new_email}, synchronize_session="fetch")
            sess.commit()
        return res

    @staticmethod
    def delete_account(account_id: int):
        with SessionConn.get_session() as sess:
            res = sess.query(Account).filter(Account._id == account_id).delete(synchronize_session="fetch")
            sess.commit()
        return res
