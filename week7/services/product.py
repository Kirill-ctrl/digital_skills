from sqlalchemy import select

from course.week7.connection.base_session import SessionConn
from course.week7.models.category import Category
from course.week7.models.product import Product


class ProductService:

    @staticmethod
    def get_list_product():
        sess = SessionConn.get_session()
        res = sess.query(
            Product._id.label("product_id"),
            Product.title.label("product_title"),
            Product.price.label("product_price"),
            Category._id.label("category_id"),
            Category.title.label("category_title")
        ).join(Product.category).all()
        return [
            {
                "id": item.product_id,
                "title": item.product_title,
                "price": item.product_price,
                "category": {
                    "id": item.category_id,
                    "title": item.category_title
                }
            }
            for item in res
        ]

    @staticmethod
    def get_product_by_id(product_id: int):
        sess = SessionConn.get_session()
        res = sess.query(
            Product._id.label("product_id"),
            Product.title.label("product_title"),
            Product.price.label("product_price"),
            Category._id.label("category_id"),
            Category.title.label("category_title")
        ).join(Product.category).where(Product._id == product_id).first()
        print(isinstance(res, Product))
        return {
            "id": res.product_id,
            "title": res.product_title,
            "price": res.product_price,
            "category": {
                "id": res.category_id,
                "title": res.category_title
            }
        }
