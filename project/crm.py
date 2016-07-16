'CRM'

# Сторонние библиотеки
import traceback

# Мои модули
from User import Customer, Admin
from Products import Product
from Errors import QuantityError, AccountError

from printer import *
import fs

# Функции - помощники
def all_products():
    'Возвращает список всех продуктов из products.json'
    _ = fs.read_json('products.json')
    return list(map(lambda i: Product(i['name'], i['cost'], i.get('quantity', 1)), _))

def print_quit(user):
    printGreen('Good bye {}\n'.format(user.name))
    return None

### Функции для работы с админом
def add_product(admin):
    """
        Спрашивает у пользователя наименование и стоимость продукта и добавляет
        в список продуктов
    """
    while True:
        product_name = inputBlue('Name = ... ')
        product_cost = int(inputBlue('Cost = ... ') or 0)
        product_qty = int(inputBlue('Quantity = ... ') or 1)

        try:
            admin.add(product_name, product_cost, product_qty)
        except:
            traceback.print_exc()
            printRed('Can\'t add product {}'.format(product_name))
            continue
        else:
            printGreen('Product: {} was succesfully added'.format(product_name))
            return None

def add_customer(admin):
    """
        Спрашивает у пользователя имя и возвраст клиента и добавляет
        клиента в список клиентов
    """
    while True:
        customer_name = inputBlue('Name = ... ')
        customer_age = int(inputBlue('Age = ... '))
        customer_account = int(inputBlue('Account = ... '))
        customer_to_add = Customer(customer_name, customer_age, [], customer_account)
        try:
            admin.add_customer(customer_to_add)
            customers.append(customer_to_add)
        except:
            printRed('Can\'t add customer {}'.format(customer_name))
            continue
        else:
            printGreen('Customer: {} was succesfully added'.format(customer_name))
            return None

admin_commands = {
    'add': {
        'description': 'Adds new product',
        'fn': add_product
    },
    'customer': {
        'description': 'Adds new customers',
        'fn': add_customer
    },
    'list-products': {
        'description': 'List all products',
        'fn': lambda l: list_all(all_products())(l)
    },
    'list-customers': {
        'description': 'List all customers',
        'fn': lambda l: list_all(customers)(l)
    },
    'list-admins': {
        'description': 'List all admins',
        'fn': lambda l: list_all(admins)(l)
    }
}

def admin_line():
    """
        Интерактивные комманды для роли админа
        Если админ разлогинивается, то возвращает False
    """
    while True:
        commands = list(admin_commands.keys())
        printCommands(admin_commands)

        cmd = inputBlue('Your command: ... ')

        if cmd not in commands + ['quit']:
            printRed('Wrong command {}\n'.format(cmd))
            continue

        if cmd == 'quit':
            return False

        admin_commands.get(cmd).get('fn')(user)

### Функции для работы с клиентом
def buy_product(customer):
    """
        Интерактивный обработчик покупки продукта
        @private
        @param {User.Customer} customer
        @return None
    """
    while True:
        product_name = inputBlue('Product name = ... ')
        product_qty = int(inputBlue('Product quantity = ... (1 by default) ') or 1)

        try:
            customer.buy(product_name, product_qty)
        except QuantityError:
            printRed('Can\'t buy product {}. Not enough products.'.format(product_name))
        except AccountError as err:
            printRed('Can\'t buy product {0}. Not enough money. Need: {1}'.format(
                product_name,
                err.required))
        except Exception as err:
            printRed('Can\'t buy product {}'.format(product_name))
            traceback.print_exc()
        else:
            printGreen('\nProduct: {0} was succesfully bought by {1}'.format(
                product_name,
                customer.name))
            return None


customer_commands = {
    'buy': {
        'description': 'Buy product',
        'fn': buy_product,
    },
    'list-products': {
        'description': 'List all products',
        'fn': lambda l: list_all(all_products())(l)
    },
    'products' : {
        'description': 'List all my products',
        'fn': lambda l: list_all(user.products or [])(l)
    },
    'info': {
        'description': 'Show info',
        'fn': print
    }
}

def customer_line():
    """
        Интерактивные комманды для роли клиента
        Если клиент разлогинивается, то возвращает False
    """
    while True:
        commands = list(customer_commands.keys())
        printCommands(customer_commands)

        cmd = inputBlue('Your command: ... ')

        if cmd not in commands + ['quit']:
            printRed('Wrong command {}\n'.format(cmd))
            continue

        if cmd == 'quit':
            return False

        customer_commands.get(cmd).get('fn')(user)

def create_customer(c):
    """
        @public
        @param {dict} c
        @return {User.Customer}
    """
    return Customer(c.get('name'), c.get('age'), c.get('products'), c.get('account'))

def create_admin(a):
    """
        @public
        @param {dict} a
        @return {User.Admin}
    """
    return Admin(a.get('name'), a.get('age'))

# Чтение сырых данных
users = fs.read_json('users.json')

admins = users.get('admins', [])
customers = users.get('customers', [])

# Инициализация
user = None
admins = list(map(create_admin, admins))
customers = list(map(create_customer, customers))

def main():
    """
        Главная функция
    """
    global user
    global admins
    global customers

    # Главный цикл
    while True:
        user_name = inputGreen('Your name: ... ')
        result = None

        i = 0
        while i < len(admins):
            if admins[i].name == user_name:
                printGreen('\nHello, Admin: {}'.format(user_name))
                kind = 'admin'
                user = admins[i]
                break
            i += 1


        if user and user.kind == 'admin':
            result = admin_line()
            if not result:
                user = print_quit(user)
                continue

        i = 0
        while i < len(customers):
            if customers[i].name == user_name:
                print('Hello, Customer: {}'.format(user_name))
                user = customers[i]
                break
            i += 1

        if user and user.kind == 'customer':
            result = customer_line()
            if not result:
                user = print_quit(user)
                continue

        printRed('Invalid name\n')

if __name__ == '__main__':
    main()
