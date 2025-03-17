from curses.ascii import isdigit


def calculate(a: int, b: int) -> int:

    if (type(a) == str):
        return a

    if (isdigit(a) and isdigit(b)):
        return int(a) + int(b)
    else:
        print('This type is not supported')


    # try:
    #     c = a + b
    #     return c
    # except TypeError:
    #     print('This type is not supported')
    # except ArithmeticError:
    #     print('ArithmeticError')
    return -1

a = 4
b = 5

print(calculate(a, b))