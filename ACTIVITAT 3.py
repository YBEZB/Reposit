matematiques = int(input("Nota de Matemàtiques: "))
catala = int(input("Nota de Català: "))
castella = int(input("Nota de Castellà: "))
angles = int(input("Nota d'Anglès: "))

mitjana = (matematiques + catala + castella + angles) / 4
mitjana = round(mitjana, 2)

print("La mitjana de les notes és:", mitjana)
