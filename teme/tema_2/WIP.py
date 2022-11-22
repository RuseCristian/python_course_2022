def your_function(*args):
    sum = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i

    return sum


def gauss_recursiv(n):
    if n <= 1:
        return n
    else:
        return n + gauss_recursiv(n-1)


def functie_input():
    x = input("Please input somehting: ")
    if type(x) == int:
        return x
    return 0
