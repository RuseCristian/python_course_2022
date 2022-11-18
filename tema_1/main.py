lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

li_ordonata = lista.copy()
li_ordonata.sort()
print("Lista ordonata ascendent", li_ordonata)
print("Lista ordonata descendent", li_ordonata[::-1])

numere_pare = f"{li_ordonata[1:2]}, {li_ordonata[3:4]}, {li_ordonata[5:6]}, {li_ordonata[7:8]}, {li_ordonata[9:10]}"
print("Afisarea numerelor pare", numere_pare)

numere_impare = f"{li_ordonata[0:1]}, {li_ordonata[2:3]}, {li_ordonata[4:5]}, {li_ordonata[6:7]}, {li_ordonata[8:9]}"
print("Afisarea numerelor impare", numere_impare)

"""
Nu este specific in cerinta, dar am presupus ca doriti sa folosim slice-uri si pentru
acest exercitiu, dar o alta varianta ar fi fost cu un list comprehension.

multiplii_3 = [x for x in li_ordonata if x % 3 == 0]

"""

multiplii_3 = f"{li_ordonata[2:3]}, {li_ordonata[5:6]}, {li_ordonata[8:9]}"
print("Afisarea multiplilor de 3 ", multiplii_3)

