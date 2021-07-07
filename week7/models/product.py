from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from course.week7.models.base import Base


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
    # ordered_product = relationship("OrderedProduct", back_populates="product")
    # cart_product = relationship("CartProduct", back_populates='product')

    def __repr__(self):
        return f"Product: {self.title}: {self.price}"