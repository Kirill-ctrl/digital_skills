from sqlalchemy import func

from course.week7.connection.base_session import SessionConn
from course.week7.models.category import Category
from course.week7.models.product import Product


class ProductService:

    @staticmethod
    def get_list_product():
        with SessionConn.get_session() as sess:
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
        with SessionConn.get_session() as sess:
            res = sess.query(
                Product._id.label("product_id"),
                Product.title.label("product_title"),
                Product.price.label("product_price"),
                Category._id.label("category_id"),
                Category.title.label("category_title")
            ).join(Product.category).where(Product._id == product_id).first()
        return {
            "id": res.product_id,
            "title": res.product_title,
            "price": res.product_price,
            "category": {
                "id": res.category_id,
                "title": res.category_title
            }
        }

    @staticmethod
    def get_product_with_const_price(price: int):
        with SessionConn.get_session() as sess:
            res = sess.query(
                Product._id.label("product_id"),
                Product.title.label("product_title"),
                Product.price.label("product_price"),
                Category._id.label("category_id"),
                Category.title.label("category_title")
            ).join(Product.category).group_by(Category._id).having(Product.price >= price).all()
            sess.close()
        return [{
            "id": item.product_id,
            "title": item.product_title,
            "price": item.product_price,
            "category": {
                "id": item.category_id,
                "title": item.category_title
            }
        } for item in res
        ]

    @staticmethod
    def get_count_product_by_category(category_id):
        with SessionConn.get_session() as sess:
            res = sess.query(
                func.count(Product._id).label("count_product"),
                Category.title.label("category_title")
            ).filter_by(category_id=category_id).join(Product.category).one()
            sess.close()
        return {
            "count_product": res.count_product,
            "category_title": res.category_title
        }
