from math import sqrt
import sys

# чтобы вычислить квадратный корень из n используйте sqrt(n)

def hypot(a, b):
    "Hypot: Number -> Number -> String"

    try:
        a = float(a)
        b = float(b)
    except:
        return 'Unexpected values at a and b'
    else:
        if a <= 0 or b <= 0:
            return 'Some value less or equal than zero'

        return sqrt(a**2 + b**2)


a = sys.argv[1]
b = sys.argv[2]

print(hypot(a, b))