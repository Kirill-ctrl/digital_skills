from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from course.week7.models.base import Base


class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    STATUSES_CART = (
        "recruited", "ready"
    )

    account_id = Column(Integer, ForeignKey("account.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity_product = Column(Integer, nullable=False)
    status_cart = Column(String, default=STATUSES_CART[0])

    account = relationship("Account", back_populates="shopping_cart")
    product = relationship("Product", back_populates="shopping_cart")
