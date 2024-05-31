def asignar_nivel_jugabilidad(nivel):
    if nivel == "alto":
        return 3
    elif nivel == "medio":
        return 2
    elif nivel == "bajo":
        return 1
    else:
        return 1  # Por defecto, asume bajo si la respuesta no coincide con alto o medio

def calcular_probabilidad_victoria():
    equipo_1 = input("Introduce el nombre del equipo 1: ")
    nivel_jugabilidad_1 = input(f"¿Cuál es el nivel de jugabilidad de {equipo_1}? (alto, medio, bajo): ")
    valor_jugabilidad_1 = asignar_nivel_jugabilidad(nivel_jugabilidad_1)
    ganados_equipo_1 = int(input(f"Introduce el número de partidos ganados por {equipo_1}: "))

    equipo_2 = input("Introduce el nombre del equipo 2: ")
    nivel_jugabilidad_2 = input(f"¿Cuál es el nivel de jugabilidad de {equipo_2}? (alto, medio, bajo): ")
    valor_jugabilidad_2 = asignar_nivel_jugabilidad(nivel_jugabilidad_2)
    ganados_equipo_2 = int(input(f"Introduce el número de partidos ganados por {equipo_2}: "))

    probabilidad_equipo_1 = round((ganados_equipo_1 * valor_jugabilidad_1) / ((ganados_equipo_1 * valor_jugabilidad_1) + (ganados_equipo_2 * valor_jugabilidad_2)) * 100, 2)
    probabilidad_equipo_2 = round((ganados_equipo_2 * valor_jugabilidad_2) / ((ganados_equipo_1 * valor_jugabilidad_1) + (ganados_equipo_2 * valor_jugabilidad_2)) * 100, 2)

    print(f"El % de probabilidad de victoria para {equipo_1} es {probabilidad_equipo_1}%")
    print(f"El % de probabilidad de victoria para {equipo_2} es {probabilidad_equipo_2}%")

    with open("Equips.txt", "a") as file:
        file.write(f"Probabilidades de victoria\n")
        file.write(f"{equipo_1}: {probabilidad_equipo_1}%\n")
        file.write(f"{equipo_2}: {probabilidad_equipo_2}%\n")
        file.write("\n")

calcular_probabilidad_victoria()
