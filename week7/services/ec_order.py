import random

from course.week7.connection.base_session import SessionConn
from course.week7.models.account import Account
from course.week7.models.cart_product import CartProduct
from course.week7.models.ec_order import ECOrder
from course.week7.models.shopping_cart import ShoppingCart
from course.week7.services.ordered_product import OrderedProductService


class ECOrderService:

    @staticmethod
    def create_order(shopping_cart: ShoppingCart, account: Account):
        sess = SessionConn.get_or_create(account)
        products = sess.query(CartProduct).filter(ShoppingCart._id == shopping_cart._id)
        order = ECOrder(number=f"{account._id}" + "".join(random.choices("QWERTYUIPOPAFDSJKBBVCMXVSADJFKSALNFSXZ", k=10)),
                        status="NEW", account_id=account._id)
        sess.add(order)
        res = OrderedProductService.add_products(sess, order, products)
        sess.commit()
        return order
