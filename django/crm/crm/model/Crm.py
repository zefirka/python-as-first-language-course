from crm.model.Emitter import Emitter
from functools import reduce

def uniq(list):
    def inlist(res, item):
        if (item not in res):
            res.append(item)
        return res

    return reduce(inlist, list, [])

class CRM:
    def __init__(self):
        self.customers=[]
    
    def buy(self, customer, product):
        customer = self.get_customer(customer)
        customer.buy(product)

    def add_customer(self, name):
        customer = Customer(name)
        self.customers.append(customer)
        return customer

    def get_customer(self, name):
        matches = list(filter(lambda customer: customer.name == name, self.customers));
        if (len(matches)):
            return matches[0]
        else:
            return 'Custom {0} not found in CRM'.format(name)

    def get_all_products(self):
        return uniq(list(reduce(lambda res, x: res + x.products, self.customers, [])))


class Customer():
    def __init__(self, name):
        self.products = []
        self.name = name
    
    def buy(self, product):
        self.products.append(product)

    def __str__(self):
        return 'Customer: {name} has products: {products}'.format(
            name=self.name,
            products=list(self.products))

class Product():
    def __init__(self, descriptor={}):
        self.descriptor = descriptor

    def __str__(self):
        return str(self.descriptor)