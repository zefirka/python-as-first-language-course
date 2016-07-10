from User import Customer, Admin
import utils
import fs

users = fs.read_json('users.json')

admins = users.get('admins', [])
customers = users.get('customers', [])

i = 0
while i < len(admins):
	admin_data = admins[i]
	admins[i] = Admin(admin_data['name'], admin_data['age'])
	i += 1

i = 0
while i < len(customers):
	customer_data = customers[i]
	customers[i] = Customer(customer_data['name'], customer_data['age'])
	i += 1

kind = None
user = None


def admin_line():
	while True:
		print('print "add" to add product')
		print('print "customer" to add customer')
		print('print "quit" to sign out\n')

		cmd = input('Your command: ... ')

		if cmd not in ['add', 'customer', 'quit']:
			print('Wrong command {}\n'.format(cmd))
			continue

		if cmd == 'quit':
			return False

		admin_commands[cmd](user)

def add_product(user):
	while True:
		product_name = input('Name = ... ')
		product_cost = int(input('Cost = ... '))

		try:
			user.add(product_name, product_cost)
			return None
		except:
			print('Can\'t add product {}'.format(product_name))
			continue

def add_customer(user):
	while True:
		customer_name = input('Name = ... ')
		customer_age = int(input('Age = ... '))

		try:
			customers.append(Customer(customer_name, customer_age))
			return None
		except:
			print('Can\'t add customer {}'.format(product_name))
			continue

admin_commands = {
	'add': add_product,
	'customer': add_customer
}

while True:
	user_name = input('Your name: ... ')
	result = None
	
	i = 0
	while i < len(admins):
		if admins[i].name == user_name:
			print('Hello, Admin: {}'.format(user_name))
			kind = 'admin'
			user = admins[i]
			break
		i += 1

	if kind:
		if kind == 'admin':
			result = admin_line()
			if not result:
				kind = None
				user = None
				continue

	i = 0
	while i < len(customers):
		if customers[i].name == user_name:
			print('Hello, Customer: {}'.format(user_name))
			kind = 'customer'
			user = customers[i]
			break
		i += 1

	if kind:
		if kind == 'admin':
			admin_line()

	print('Invalid name')
