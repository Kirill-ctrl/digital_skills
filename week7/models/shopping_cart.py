from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from course.week7.models.base import Base


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

    account = relationship("Account", foreign_keys=[account_id])
    # cart_product = relationship("ShoppingCart")
