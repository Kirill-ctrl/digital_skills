from course.week7.models.product import Product
from course.week7.router import RouterRequest

if __name__ == '__main__':
    work = RouterRequest()

    account = work.create_account(name='Kirill', email='email', password='password')

    account_kirill = work.get_account_by_id(account_id=account._id)
    print(account_kirill._id)

    categories = work.get_list_category()
    print(categories)

    category = work.get_category_by_id(category_id=categories[0]['id'])
    print(category)

    products = work.get_list_product()
    print(products)

    product = work.get_product_by_id(product_id=products[0]['id'])
    print(product)
    product_m = Product(_id=product['id'],
                        title=product['title'],
                        price=product['price'],
                        category_id=product['category']['id'])

    shopping_cart = work.add_to_cart(product=product_m, account=account_kirill, quantity=2)
    print(shopping_cart)

    account_with_new_email = work.update_account(account_id=account_kirill._id, new_email='k@mail.ru')
    print(account_with_new_email)

    account_with_new_email_1 = work.delete_account(account_id=account_kirill._id)
    print(account_with_new_email_1)

    product_list = work.get_product_with_const_price(price=2000)
    print(product_list)

    price_by_category = work.get_count_product_by_category(category_id=categories[1]['id'])
    print(price_by_category)
