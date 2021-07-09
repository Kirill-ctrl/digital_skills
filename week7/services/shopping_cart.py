from course.week7.connection.base_session import SessionConn
from course.week7.models.account import Account
from course.week7.models.cart_product import CartProduct
from course.week7.models.product import Product
from course.week7.models.shopping_cart import ShoppingCart


class ShoppingCartService:

    def add_to_cart(self, account: Account, product: Product, quantity: int):
        with SessionConn.get_session() as sess:
            shopping_cart = self.get_or_create(sess, account)
            added_product = CartProduct(shopping_cart_id=shopping_cart._id, product_id=product._id, quantity_product=quantity)
            sess.add(added_product)
            sess.commit()
        return shopping_cart

    @staticmethod
    def get_or_create(sess, account: Account):
        shopping_cart = sess.query(ShoppingCart).join("account").where(Account._id == account._id).first()
        if not shopping_cart:
            shopping_cart = ShoppingCart(account_id=account._id, status_cart="NEW")
            sess.add(shopping_cart)
            sess.commit()
        return shopping_cart
