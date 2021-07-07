import hashlib

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from course.week7.connection.base_engine import EngineConn
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


class Category(Base):
    __tablename__ = "category"

    def __init__(self,
                 _id: int = None,
                 title: str = None):
        self._id = _id
        self.title = title

    _id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    product = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"Category ({self.title})"


class Product(Base):
    __tablename__ = "product"

    def __init__(self,
                 _id: int = None,
                 title: str = None,
                 description: int = None,
                 price: int = None,
                 photo_link: int = None,
                 category_id: int = None):
        self._id = _id
        self.title = title
        self.description = description
        self.price = price
        self.photo_link = photo_link
        self.category_id = category_id

    _id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    photo_link = Column(String)
    category_id = Column(Integer, ForeignKey("category._id"))

    category = relationship("Category", back_populates="product")
    ordered_product = relationship("OrderedProduct", back_populates="product")
    cart_product = relationship("CartProduct", back_populates='product')


class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    STATUSES_CART = (
        "recruited", "ready"
    )

    def __init__(self,
                 _id: int = None,
                 account_id: int = None,
                 status_cart: str = None):
        self._id = _id
        self.account_id = account_id
        self.status_cart = status_cart

    _id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("account._id"))
    status_cart = Column(String, default=STATUSES_CART[0])

    account = relationship("Account", back_populates="shopping_cart")
    cart_product = relationship("ShoppingCart", back_populates="shopping_cart")


class ECOrder(Base):
    __tablename__ = "ec_order"

    def __init__(self,
                 _id: int = None,
                 number: str = None,
                 account_id: int = None,
                 status: str = None):
        self._id = _id
        self.number = number
        self.account_id = account_id
        self.status = status

    _id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True)
    account_id = Column(Integer, ForeignKey('account._id'))
    status = Column(String, nullable=False)

    account = relationship("Account", back_populates="ec_order")
    ordered_product = relationship("OrderedProduct", back_populates='ec_order')


class CartProduct(Base):
    __tablename__ = "cart_product"

    def __init__(self,
                 _id: int = None,
                 shopping_cart_id: int = None,
                 product_id: int = None,
                 quantity_product: int = None):
        self._id = _id
        self.shopping_cart_id = shopping_cart_id
        self.product_id = product_id
        self.quantity_product = quantity_product

    _id = Column(Integer, primary_key=True)
    shopping_cart_id = Column(Integer, ForeignKey("shopping_cart._id"))
    product_id = Column(Integer, ForeignKey("product._id"))
    quantity_product = Column(Integer, nullable=False)

    shopping_cart = relationship("ShoppingCart", back_populates="cart_product")
    product = relationship("Product", back_populates="cart_product")

    def __repr__(self):
        return f"CartProduct({self.shopping_cart_id} for {self.shopping_cart.account.name}"


class OrderedProduct(Base):
    __tablename__ = "ordered_product"

    def __init__(self,
                 _id: int = None,
                 product_id: int = None,
                 ec_order_id: int = None,
                 quantity: int = None):
        self._id = _id
        self.product_id = product_id
        self.ec_order_id = ec_order_id
        self.quantity = quantity

    _id = Column(Integer, nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey("product._id"))
    ec_order_id = Column(Integer, ForeignKey("ec_order._id"))
    quantity = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="ordered_product")
    ec_order = relationship("ECOrder", back_populates="ordered_product")


Base.metadata.create_all(EngineConn.set_engine('../mydatabase'))
