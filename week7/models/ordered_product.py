from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from course.week7.models.base import Base


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

    product = relationship("Product")
    ec_order = relationship("ECOrder", back_populates="ordered_product")
