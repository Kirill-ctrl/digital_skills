from typing import List

from sqlalchemy import insert

from course.week7.models.cart_product import CartProduct
from course.week7.models.ec_order import ECOrder
from course.week7.models.ordered_product import OrderedProduct


class OrderedProductService:

    @staticmethod
    def add_products(sess, order: ECOrder, products: List[CartProduct]):
        sql = insert(OrderedProduct).values(
            [
                {
                    "product_id": item.CartProduct.product_id,
                    "ec_order_id": order._id,
                    "quantity": item.CartProduct.quantity_product
                 }
            for item in products
            ]
        )
        result = sess.execute(sql)
        return result
