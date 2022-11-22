# print("")
# input("Alege o litera")


def functie_1(param_1=3, param_2=4, *args, **kwargs):
    print(type(*args))
    suma = 0
    suma = param_1 + param_2
    for i in args:
        suma += i

    for i in kwargs.values():
        suma += i
    return suma


print(functie_1(1, 5, 6, v=3, c=6))
