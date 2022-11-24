variabila = input("Adauga un nr: ")
# variabila = int(variabila)s
lista = [1, 2, 3]
try:
    if variabila.isdigit():
        raise ValueError
    print(lista[3])
    a = None
    #print(a)  # NameError - nu e variabila def
    variabila = int(variabila)

except ValueError:   # ValueError apartine in Exception
    print("exceptie")
    if variabila.isdigit():
        variabila = int(variabila)
except NameError:
    print('variabila nedef')
    a = None
except Exception:   # clasa cu toate exceptiile din py
    print('clasa default')
except IndexError:
    print("eroare de index")
    print(lista[3:4])
else:
    print("nu exista nicio exceptie")
finally:
    print("se ruleaza oricum")

print(variabila, 'variabla')
print(a, 'a')
