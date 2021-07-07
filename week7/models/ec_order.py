from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from course.week7.models.base import Base


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
    account_id = Column(Integer, ForeignKey('account.id'))
    status = Column(String, nullable=False)

    account = relationship("Account", back_populates="ec_order")
    ordered_product = relationship("OrderedProduct", back_populates='ec_order')

    def __repr__(self):
        return f"ECOrder ({self.number} for {self.account.name}"
