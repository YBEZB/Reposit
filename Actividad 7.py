print("Inserte los Datos")

file = open("Date-base.txt", "a")

date = input("Data:")

date_2 = input("Hora:")

date_3 = input("Adreça:")

date_4 = input("Codi Postal:")

file.write("\n" + date + "\n" + date_2 + "\n" + date_3 + "\n" + date_4)

file.close()

print("Gracias por proporcionar los datos")
