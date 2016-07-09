from time import time

def speed(n):
   import math;
   result = []
   i = 1
   while i <= n:
       x = 3
       b = int(math.sqrt(i))
       c = 0
       while x <= b:
           if i % x == 0:
               c = 1
           x +=2
       if c == 0:
           result.append(i)
       i +=2
   return result

def fantastic_four(n):

    a = list(range(n+1))
    a[1] = 0
    lst = []

    i = 3
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in list(range(i, n+1, i)):
                a[j] = 0
        i += 2

    return lst

def defnum(a):
    if a == 2:
        return a
    elif a == 0:
        return None
    else:
        result=[2]
        for i in range(2,a):
            if (i>10 and i%5==0) or i%2==0:
                continue
            is_prime = True
            for j in range(2,i//2):
                    if i%j==0:
                        is_prime = False
                        break
            if is_prime:
                result.append(i)
        return result

def prime_number(a):
    if a == 2:
        return 2;
    elif a<2:
        return None;
    else:
        numbers = [2]
        i = 3
        while i <= a:
            check = 0
            for num in numbers:
                if not i % num:
                    check = 1
                    break
            if not check:
                numbers.append(i)
            i += 2
    return numbers


def test(fn, v):
    print(fn.__name__)
    start = time()
    fn(v)
    print(time() - start)


small = int(input('Small = '))
middle = int(input('Middle = '))
big = int(input('Big = '))

test(speed, small)
test(speed, middle)
# test(speed, big)

test(fantastic_four, small)
test(fantastic_four, middle)
test(fantastic_four, big)

test(prime_number, small)
test(prime_number, middle)
test(prime_number, big)
