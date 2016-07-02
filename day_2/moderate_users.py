# Подготовительный код
from random import choice, randint

names = ['John', 'Jane', 'Bob', 'Alice', 'Pip', 'Sasha', 'Fonzey']
generate_user = lambda:{'name': choice(names), 'age': randint(12, 100)} 
users = [generate_user() for n in range(50)]

# Задача: написать функцию, которая фильтрует список пользователей
# и возвращет список тех пользователей у которых свойство
# age больше 18

