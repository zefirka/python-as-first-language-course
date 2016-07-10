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

while True:
	user_name = input('Your name: ... ')

	i = 0
	while i < len(admins):
		if admins[i].name == user_name:
			print('Hello, Admin: {}'.format(user_name))
			kind = 'admin'
			break
		i += 1

	if kind:
		break

	i = 0
	while i < len(customers):
		if customers[i].name == user_name:
			print('Hello, Customer: {}'.format(user_name))
			kind = 'customer'
			break
		i += 1

	if kind:
		break

	print('Invalid name')

