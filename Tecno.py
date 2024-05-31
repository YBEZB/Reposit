n1 = float(input("Ingresa la velocidad en rpm de la polea motriz (n1): "))

n2 = float(input("Ingresa la velocidad en rpm de la polea conducida (n2): "))

i = n2 / n1
i = round(i, 2)

print(f"La relación de transmisión del sistema es: {i}")   

if i > 1:
    print("El sistema es un amplificador de velocidad.")
elif i < 1:
    print("El sistema es un reductor de velocidad.")
else:
    print("El sistema no cambia la velocidad.")
