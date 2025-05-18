# Challenge Exercise

# ONLY ATTEMPT IF YOU HAVE COMFORTABLY COMPLETED THE OTHER EXERCISES!

# Given a list of product dictionaries,
# use map, filter, reduce, and lambda functions to:
# 1. Get a list of names of all products that are in stock (stock > 0).
# 2. Calculate the total value of all 'Electronics' products currently in stock
# 3. (Challenge): Get a list of strings, where each string is "Product Name - $Price"
#       for all products in the 'Apparel' category.
# 4. (Extra Challenge): Refactor #3 to use a list comprehension.

products = [
    {'name': 'Laptop', 'price': 1200.00, 'stock': 10, 'category': 'Electronics'},
    {'name': 'T-Shirt', 'price': 20.00, 'stock': 50, 'category': 'Apparel'},
    {'name': 'Keyboard', 'price': 75.00, 'stock': 0, 'category': 'Electronics'},
    {'name': 'Mug', 'price': 15.00, 'stock': 100, 'category': 'Homeware'},
    {'name': 'Jeans', 'price': 60.00, 'stock': 0, 'category': 'Apparel'},
    {'name': 'Monitor', 'price': 300.00, 'stock': 5, 'category': 'Electronics'}
]

# 1. Get a list of names of all products that are in stock (stock > 0).

in_stock = list(filter(lambda p: p['stock'] > 0, products))
product_names = list(map(lambda p: p['name'], in_stock))
print (product_names)

# 2. Calculate the total value of all 'Electronics' products currently in stock
from functools import reduce
electronics_in_stock = list(filter(lambda p: p['category'] == 'Electronics', in_stock))
print(electronics_in_stock)
value_stock = list(map(lambda p: p['price'] * p['stock'], electronics_in_stock))
print(value_stock)
total_value_eletronics = reduce(lambda acc, current: acc + current, value_stock)
print(f'${total_value_eletronics}')

# 3. (Challenge): Get a list of strings, where each string is "Product Name - $Price"
#       for all products in the 'Apparel' category.
apparel_products = list(filter(lambda p: p['category'] == 'Apparel', products))
print(apparel_products)
apparel_list = list(map(lambda ap: f'{ap['name']} - ${ap['price']}', apparel_products))
print(apparel_list)

# 4. (Extra Challenge): Refactor #3 to use a list comprehension.
apparel_products = [print(f'{ap['name']} - ${ap['price']}') for ap in products if ap['category'] == 'Apparel']
