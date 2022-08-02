def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def calc(operator, x, y):

    operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    method = operators.get(operator)
    if method:
        return method(x, y)

    return None
