from Emitter import Emitter

class CRM:
    customers=[]
    
    def add_customer(self, name):
        customers.append(Customer(name))    


class Product(Emitter):
    def __init__(self, descriptor={}):
        self.descriptor = descriptor
        self.subscribe('buy', lambda customer: print('Customer: {0} bought product: {1}'.format(customer, self.descriptor)))

class Customer(Emitter):
    products = []

    def __init__(self, name):
        self.name = name
    
    def buy(self, product):
        self.products.append(product)
        self.emit('buy', product)
        product.emit('but', self.name)


crm = CRM()

crm.addCustomer('John')

