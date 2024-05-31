n1 = float(input("Introdueix la velocitat en rpm de la politge motriu: "))
n2 = float(input("Introdueix la velocitat en rpm de la politge conductora: "))

i = n1 / n2
i = round(i, 2)

if n1 > n2:
    print(f"La relació de transmissió es {i}, llavors és un sistema reductor.")
elif n1 < n2:
    print(f"La relació de transmissió es {i}, llavors és un sistema amplificador.")
else:
    print(f"La relació de transmissió es {i}, llavors la velocitat no canvia.")
