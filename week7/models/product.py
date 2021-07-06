from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from course.week7.models.base import Base


class Product(Base):
    __tablename__ = "product"

    _id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    photo_link = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))

    category = relationship("Category", back_populates="product")
    ordered_product = relationship("OrderedProduct", back_populates="product")
    shopping_cart = relationship("ShoppingCart", back_populates='product')
