# Задача: написать функцию primes

from time import time

def primes(n):
    """
        primes: int -> list[int]
        Возвращает список всех простых чисел меньщих или равных n
    """
    pass

def test_fn(fn):
    start = time()
    fn()
    print(time() - start)