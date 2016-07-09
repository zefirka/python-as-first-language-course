from crm.model.Crm import CRM, Customer, Product

crm = CRM()

john = crm.add_customer('John')
jane = crm.add_customer('Jane')

crm.buy('John', 'alpha')
crm.buy('John', 'betta')
crm.buy('John', 'gamma')
crm.buy('Jane', 'delta')

def get_customer(name):
    return wrap(crm.get_customer(name))

def buy(name, product):
    crm.buy(name, product)
    return wrap('Ok')

def all():
    return wrap('<br>'.join([str(customer) for customer in crm.customers]) if len(crm.customers) else 'No customers')

def get_all_products():
    return wrap('<br>'.join(crm.get_all_products()))

def wrap(data, title='CRM'):
    return '<html><head><title>{1}</title></head><body>{0}</body></html>'.format(str(data), title)

def create_customer(name):
    try:
        crm.add_customer(name);
    except:
        raise ValueError('Unexpected customer')

create = {
    'customer': create_customer
}