from sqlalchemy import select

from course.week7.connection.base_session import SessionConn
from course.week7.models.product import Product


class ProductService:

    @staticmethod
    def get_list_product():
        sql = select(Product._id, Product.title, Product.price, Product.category._id, Product.category.title).join(Product.category)
        with SessionConn.get_session() as sess:
            res = sess.execute(sql)
        return [
            {
                "id": item.Product._id,
                "title": item.Product.title,
                "price": item.Product.price,
                "category": {
                    "id": item.Category._id,
                    "title": item.Category.title
                }
            }
            for item in res
        ]

    @staticmethod
    def get_product_by_id(product_id: int):
        sql = select(Product._id, Product.title, Product.price, Product.category._id, Product.category.title).join(Product.category).where(Product.id == product_id)
        with SessionConn.get_session() as sess:
            res = sess.execute(sql)
        return {
            "id": res.Product._id,
            "title": res.Product.title,
            "price": res.Product.price,
            "category": {
                "id": res.Category._id,
                "title": res.Category.title
            }
        }
