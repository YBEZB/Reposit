file = open("datos.txt","a")

nom=input("Nom:")

cognom=input("Cognom:")

data_de_neixement=input("data:")

file.write("\n" + nom + "\n" + cognom + "\n" + data_de_neixement)

file.close()

