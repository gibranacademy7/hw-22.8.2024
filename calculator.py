

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a = int, b = int):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!");
    return a / b

def power (a,b):
    return a**b

def sqrt (a):
    import math
    return math.sqrt(a);

def is_prime (a):
    if a<=1:
        return False
    return not any( a % i == 0 for i in range (2,a));

print(is_prime(1));

def factorial (a):
    while a >= 0:
        result = 1
        for i in range (1, a+1):
            result *= i
        return result
    else:
        raise ValueError ("Factorial not defined for negative values ");

print(factorial(2));


# check all cases
# auto keep functionality working
# make QA life more simple
# keep bug fix working