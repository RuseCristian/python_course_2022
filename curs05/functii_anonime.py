# def my_lambda(x, y):
#     return x + y


# my_lambda = lambda x, y: x + y
#
#
# suma = my_lambda(2, 3)
# print(suma)


players = [
    {
        "firt_name": 'Ion',
        "last_name": "Popescu",
        "varsta": 12
    },
    {
        "firt_name": 'Andreea',
        "last_name": "Popa",
        "varsta": 35
    },
    {
        "firt_name": 'Isabela',
        "last_name": "Enache",
        "varsta": 25
    }
]


jucatori_sortate = sorted(players, key=lambda jucator: jucator["last_name"])
print(jucatori_sortate)
