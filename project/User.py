from Products import Product
import fs
import utils

class User:
	rights = ['read']
	kind = 'User'

	def __init__(self, name, age):
		self.name = name
		self.age = int(age)

	def __str__(self):
		return '{obj.kind}: <name: {obj.name}, age: {obj.age}>'.format(obj=self)


class Customer(User):
	rights = ['read', 'buy']
	kind = 'Customer'

	def __init__(self, name, age, products=[]):
		super().__init__(name, age)
		self.products = products

	def buy(self, product_name, product_cost=0):
		products = fs.read_json('products.json')

		if not utils.is_name_in_list(product_name, products):
			raise Exception('Product: {} not in list'.format(product_name))

		product = Product(product_name, product_cost)
		self.products.append(product)


class Admin(User):
	rights = ['read', 'add']
	kind = 'Admin'

	def add(self, product_name, product_cost):
		product = Product(product_name, product_cost)
		products = fs.read_json('products.json')

		if utils.is_name_in_list(product_name, products):
			raise Exception('Product: {} already in products.json'.format(product_name))

		fs.update_json_list('products.json', product.value())

