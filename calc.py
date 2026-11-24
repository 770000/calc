def add (a, b):
    return a + b

def diff (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    if b == 0:
        raise ValueError ('Нельзя делить на ноль')
    return a / b

def mod (a, b):
    return a % b
