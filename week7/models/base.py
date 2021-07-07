from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class BaseDeclarative:
#
#     def __init__(self):
#         self.Base = declarative_base()
#         self.account = Account
#         self.category = Category
#         self.product = Product
#         self.ec_order = ECOrder
#         self.shopping_cart = ShoppingCart
#         self.cart_product = CartProduct
#         self.ordered_product = OrderedProduct
#
#     def create(self):
#         print(self.Base.metadata)
#         self.Base.metadata.create_all(EngineConn.set_engine('../mydatabase'))
#         print(self.Base.metadata)
#
#
# BaseDeclarative().create()
