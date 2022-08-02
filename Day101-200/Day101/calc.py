from operator import truediv, mul, add, sub


def calc(operator, x, y):

    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv
    }
    method = operators.get(operator, lambda x, y: None)
    if method:
        return method(x, y)

    return None
