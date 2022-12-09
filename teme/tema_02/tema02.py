def your_function(*args: int or float, **kwargs):
    sum = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i

    return sum


def gauss_recursiv(n, tip_de_suma):
    """
    :param n: primele n numere
    :param tip_de_suma: tipul de suma, 0 = gauss normal, 1 = gauss pare, 2 = gauss impare
    :return: suma pt suma gauss respectiva
    """
    if tip_de_suma == 0:
        if n <= 1:
            return n
        return n + gauss_recursiv(n - 1, 0)

    elif tip_de_suma == 1:
        if n <= 2:
            return n
        if n % 2 == 0:
            return n + gauss_recursiv(n - 1, 1)
        else:
            return gauss_recursiv(n - 1, 1)

    elif tip_de_suma == 2:
        if n <= 1:
            return n
        if n % 2 != 0:
            return n + gauss_recursiv(n - 1, 2)
        else:
            return gauss_recursiv(n - 1, 2)


def functie_input():
    x = input("Please input somehting: ")
    try:
        return int(x)
    except ValueError:
        return 0


# returns 3
print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))

# returns 0
print(your_function())

# returns 6
print(your_function(2, 4, 'abc', param_1=2))

# gauss simplu  55
print(gauss_recursiv(10, 0))
# gauss pare    30
print(gauss_recursiv(10, 1))
# gauss impare  20
print(gauss_recursiv(10, 2))

print(functie_input())
