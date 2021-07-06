import hashlib
import os

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from course.week7.models.base import Base


class Account(Base):
    __tablename__ = "account"

    def __init__(self,
                 name: str = None,
                 email: str = None,
                 password: str = None,
                 hash_password: str = None):
        self.name = name
        self.email = email
        self.password = password
        self.hash_password = hash_password

    _id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hash_password = Column(String, nullable=False)

    ec_order = relationship("ECOrder", back_populates="account")
    shopping_cart = relationship("ShoppingCart", back_populates='account')

    def __repr__(self):
        return F"Account({self.name}, {self.email})"

    def create_hash_password(self):
        salt_for_password = b''
        key = hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=self.password.encode('utf-8'),
            salt=salt_for_password,
            iterations=100000
        )
        self.hash_password = key

    def check_password(self, value: str):
        key = self.hash_password
        new_key = hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=value.encode('utf-8'),
            salt=self.salt_for_password,
            iterations=100000
        )
        if new_key != key:
            return False
        return True
