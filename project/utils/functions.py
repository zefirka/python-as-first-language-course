"""
    functions - модуль для работы с функциями и списками
"""

def some(predicate, list):
    for item in list:
        if predicate(item):
           return True
    return False

def every(predicate, list):
    for item in list:
        if not predicate(item):
           return False    
    return True

def is_valid_product(product_name):
    return product_name.isalpha()