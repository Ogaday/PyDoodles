from math import sqrt

def prime():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n +=1

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for n in range(3, int(sqrt(number) + 1), 2):
            if number % n == 0:
                return False
        return True
    return False

def fib():
    result = 0
    base = 1
    while True:
        yield result
        n = result + base
        result = base
        base = n
