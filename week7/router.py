from course.week7.connection.base_engine import EngineConn
from course.week7.models.account import Account
from course.week7.services.account import AccountService
from course.week7.services.category import CategoryService
from course.week7.services.ec_order import ECOrderService
from course.week7.services.product import ProductService
from course.week7.services.shopping_cart import ShoppingCartService


class RouterRequest:

    def __init__(self):
        EngineConn.set_engine('mydatabase')

    @staticmethod
    def create_account(**kwargs):
        return AccountService.create_account(Account(name=kwargs.get('name'), email=kwargs.get('email'), password=kwargs.get('password')))

    @staticmethod
    def update_account(**kwargs):
        return AccountService.update_account_email(account_id=kwargs.get("account_id"), new_email=kwargs.get('new_email'))

    @staticmethod
    def get_account_by_id(**kwargs):
        return AccountService.get_by_account_id(account_id=kwargs.get('account_id'))

    @staticmethod
    def delete_account(**kwargs):
        return AccountService.delete_account(account_id=kwargs.get('account_id'))

    @staticmethod
    def get_list_category():
        return CategoryService.get_list_category()

    @staticmethod
    def get_category_by_id(**kwargs):
        return CategoryService.get_category_by_id(category_id=kwargs.get('category_id'))

    @staticmethod
    def create_order(**kwargs):
        return ECOrderService.create_order(shopping_cart=kwargs.get('shopping_cart'), account=kwargs.get('account'))

    @staticmethod
    def get_list_product():
        return ProductService.get_list_product()

    @staticmethod
    def get_product_by_id(**kwargs):
        return ProductService.get_product_by_id(product_id=kwargs.get('product_id'))

    @staticmethod
    def get_product_with_const_price(**kwargs):
        return ProductService.get_product_with_const_price(price=kwargs.get('price'))

    @staticmethod
    def get_count_product_by_category(**kwargs):
        return ProductService.get_count_product_by_category(category_id=kwargs.get('category_id'))

    @staticmethod
    def add_to_cart(**kwargs):
        return ShoppingCartService().add_to_cart(account=kwargs.get('account'), product=kwargs.get('product'), quantity=kwargs.get('quantity'))
