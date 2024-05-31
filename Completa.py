import random

resultado = random.randint(1, 9)

num_usuario = int(input("Dime un número del 1 al 9: "))

while num_usuario != resultado:

    if num_usuario < resultado:

        print("Lo siento, tu número es menor")

    else:

        print("Lo siento, tu número es mayor")

    num_usuario = int(input("Sigue intentándolo, dime otro número: "))

print("¡Correcto!")
