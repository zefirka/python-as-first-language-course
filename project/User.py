from Products import Product
from Errors import QuantityError, AccountError

import fs
import utils

class User:
    """
        User: общий класс пользователей
    """
    kind = 'user'

    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def __str__(self):
        return '{kind}: <name: {obj.name}, age: {obj.age}>'.format(
            kind=self.kind.title(),
            obj=self)

    def value(self):
        return {
            'name': self.name,
            'age': self.age
        }

class Customer(User):
    """
        Customer: класс пользователей с правами админа
    """

    kind = 'customer'

    def __init__(self, name, age, products=[], account=0):
        super().__init__(name, age)
        self.account = account
        self.products = list(map(lambda p: Product(p['name'], p['cost'], p.get('quantity')), products))

    def __add(self, product):
        """
            Добавляет {product} в список {@.products}
            @private
            @param {Product} product
        """
        i = 0
        while i < len(self.products):
            p = self.products[i]
            if p.name == product.name:
                self.products[i].quantity += product.quantity
                return None
            i += 1
        self.products.append(product)


    def buy(self, name, qty=1):
        """
            Совершает покупку продукта пользователем

            @public
            @param {str} name - имя продукта
            @param {int} qty - количество
        """
        products = fs.read_json('products.json')

        product = utils.find_by_name(name, products)
        required_money = product.get('cost') * qty

        if not product:
            raise Exception('Product: {} not in list'.format(name))

        if product.get('quantity', 1) < qty:
            raise QuantityError('Not enough products')

        if required_money > self.account:
            raise AccountError('Not enough money', required_money)
        
        product = Product(name, product.get('cost'), qty)
        
        self.__add(product)
        self.account -= required_money
        
        fs.update_product(product)
        fs.update_customer(self.value())

    def value(self):
        res = super().value()
        res['account'] = self.account
        res['products'] = list(map(lambda p: p.value(), self.products))
        return res

    def __str__(self):
        return 'Customer <name: {0.name}, age: {0.age}, account: {0.account}>'.format(self)

class Admin(User):
    """
        Admin: класс пользователей с правами админа
    """

    kind = 'admin'

    def add_customer(self, customer):
        """
            Записывает в файл users.json нового клиента
            
            @public
            @param {User.Customer} customer
        """
        try:
            fs.add_user(customer)
        except:
            print('Customer: {} was not added'.format(customer.name))
        else:
            print('Customer: {} was added to list'.format(customer.name))

    def add(self, name, cost=None, qty=1):
        """
            Добавляет новый продукт в products.json

            @public
            @param {str} name - имя продукта
            @param {int} cost - стоимость
            @param {int} qty - количество
        """
        product = Product(name, cost, qty)
        fs.update_product(product, True)
