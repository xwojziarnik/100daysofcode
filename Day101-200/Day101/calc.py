def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def calc(operator, x, y):
    if operator == "+":
        return add(x, y)

    elif operator == "-":
        return subtract(x, y)

    elif operator == "*":
        return multiply(x, y)

    elif operator == "/":
        return divide(x, y)

    else:
        return None
