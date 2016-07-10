class Product:
	'Class for products'

	def __init__(self, name, cost, cur='₽'):
		self.name = name
		self.cost = int(cost)
		self.cur = cur

	def __str__(self):
		return'Product: < name: {0.name}, cost: {0.cost}{0.cur}>'.format(self)

	def value(self):
		return {
			'name': self.name,
			'cost': self.cost
		}