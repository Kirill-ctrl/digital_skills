from sqlalchemy import ForeignKey, Integer, Column
from sqlalchemy.orm import relationship

from course.week7.models.base import Base


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

    shopping_cart = relationship("ShoppingCart", foreign_keys=[shopping_cart_id])
    product = relationship("Product", foreign_keys=[product_id])

    def __repr__(self):
        return f"CartProduct({self.shopping_cart_id} for {self.shopping_cart.account.name}"
