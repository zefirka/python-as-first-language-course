import json
from utils import is_name_in_list, find_by_name

USERFILE = 'users.json'
PRODUCTFILE = 'products.json'

def read_json(filename):
    with open(filename, 'r') as jsonfile:
        content = jsonfile.read()
        return json.loads(content)

def write_json(filename, struct):
    with open(filename, 'w+') as jsonfile:
        content = json.dumps(struct)
        jsonfile.write(content)


def update_json_list(filename, dict):
    struct = read_json(filename)
    
    if type(struct) != list:
        raise Exception('{0} is not a list'.format(filename))

    struct.append(dict)
    write_json(filename, struct)

def add_user(user):
    struct = read_json(USERFILE)
    name_of_list = user.kind + 's'
    list_of_users = struct.get(name_of_list, [])

    if is_name_in_list(user.name, list_of_users):
        raise Exception('User: {0.name} have been already added'.format(customer))

    list_of_users.append(user.value())
    struct[name_of_list] = list_of_users

    write_json(USERFILE, struct)

def update_product(product, add=False):
    products = read_json(PRODUCTFILE)

    if is_name_in_list(product.name, products):
        i = 0
        while i < len(products):
            p = products[i]
            if p['name'] == product.name:
                if add:
                    print(product)
                    new_qty = p.get('quantity', 1) + product.quantity
                else:
                    new_qty = p.get('quantity', 1) - product.quantity           
                updated = products[i]
                updated['quantity'] = new_qty
                products[i] = updated
                break
            i += 1
    else:
        products.append(product.value())

    write_json(PRODUCTFILE, products)


def update_customer(customer):
    users = read_json(USERFILE)
    customers = users.get('customers', [])

    index = 0
    while index < len(customers):
        c = customers[index]
        if c.get('name') == customer.get('name'):
            customers[index] = customer
            break
        index += 1
    users['customers'] = customers

    write_json(USERFILE, users)
