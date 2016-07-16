"""
    Модуль для работы с функциями и списками
"""

def some(predicate, list):
    """
        возвращает True если хотя-бы один элементы list 
        соответствуют выражению predicate(item)
    """
    for item in list:
        if predicate(item):
           return True    
    return False

def every(predicate, list):
    """
        возвращает True если все элементы list 
        соответствуют выражению predicate(item)
    """
    for item in list:
        if not predicate(item):
           return False    
    return True

def is_valid_product(product_name):
    return product_name.isalpha()

def propEq(p, v):
    return lambda obj: obj[p] == v

def prop(p):
    return lambda obj: obj[p]

def is_name_in_list(name, list):
    return some(propEq('name', name), list)

def find_by_name(name, lst):
    res = list(filter(propEq('name', name), lst))
    if len(res):
        return res[0]
    return False