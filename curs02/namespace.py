# def functie():
#     global mesaj
#     mesaj = "Buna seara"
#     print(mesaj)


# functie()
# print(mesaj)


def functie():
    def functie2():
        print(f"A doua functie: {msg}")

    global msg
    msg = "Buna seara"
    functie2()
    print(f"functie: {msg}")


# msg = "Buna ziua"
functie()
msg = "Buna ziua"
print(msg)
