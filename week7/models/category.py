from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from course.week7.models.base import Base


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
