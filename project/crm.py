#  Открыть файлы customers.txt и products.txt и считать оттуда информацияю 
# записав все в списки products и customers

products = []
customers = []
admins = []

def create_product(product_name):
	with open('products.txt', 'r+') as products:
		content = products.read()
		prods = content.split('\n')

		if product_name in prods:
			raise Exception('Product: {0} already exists'.format(product_name))

		products.write('\n{0}'.format(product_name))

def create_customer(name):
	'Создает нового клиента и записывает его имя в файл: customers.txt'
	pass


