registrat = False
intents = 3
nom = ""
contrasenya = ""

while not registrat:
    
    print("1º Pas: Registra't per a la loteria")
    nom = input("Introdueix el teu nom: ")
    confirma_nom = input("Confirma el teu nom: ")
    
    if confirma_nom == nom:
        contrasenya = input("2º Pas: Crea una contrasenya:")
        contrasenya = contrasenya + "_" + nom + contrasenya
        print("Registre exitós. La teva nova contrasenya és:", contrasenya)
        registrat = True
        
    else:
        print("El nom de confirmació no coincideix amb el nom introduït. Torna-ho a intentar.")

while intents > 0:
    password = input("Introdueix la teva contrasenya per accedir: ")
    if password == contrasenya:
        print("Accés")
        break
    else:
        print("Contrasenya incorrecta. Et queden", intents - 1, "intents.")
        intents -= 1
        if intents == 0:
            print("Has excedit el nombre d'intents. Torna a intentar més tard.")
            break

import random

def jugar_solo():
    palabras = [
        {'palabra': 'random', 'pistas': ['Tiene relación con la aleatoriedad', 'Algo impredecible', 'Sin un patrón específico']},
        {'palabra': 'casio', 'pistas': ['Marca reconocida de relojes', 'También es reconocida por las calculadoras', 'Si has tenido que utilizar tu última oportunidad estás muy desculturizado']},
        {'palabra': 'didac', 'pistas': ['Una máquina en todo', 'Famoso por la palabra. Rarillo', 'Según el día es de un equipo o otro']},
        {'palabra': 'lenovo', 'pistas': ['Marca conocida de ordenadores', 'Puede que lo estés utilizando', 'Puede tener pantalla táctil']},
        {'palabra': 'toyota', 'pistas': ['Marca de automóviles', 'Japonesa', 'Conocida por su fiabilidad']}
    ]

    palabra_secreta = random.choice(palabras)
    palabra = palabra_secreta['palabra']
    pistas = palabra_secreta['pistas']
    palabra_oculta = "_" * len(palabra)
    intentos = 0
    letras_adivinadas = []
    pista_actual = 0

    while intentos < 6:
        print("Si quieres una pista, escribe (pista). Si no te es suficiente, escribe (otra).")
        print("===============================")
        entrada = input("Ingresa una letra: ")

        if entrada.lower() == 'pista':
            if pista_actual < len(pistas):
                print("Pista:", pistas[pista_actual])
                pista_actual += 1
            else:
                print("No hay más pistas disponibles. Inténtalo adivinando la palabra.")
        elif entrada.lower() == 'otra':
            if pista_actual < len(pistas) - 1:
                print("===============================")
                print("Siguiente pista:", pistas[pista_actual])
                print("===============================")
                pista_actual += 1
            else:
                print("No hay más pistas disponibles. Inténtalo adivinando la palabra.")
        else:
            if entrada in letras_adivinadas:
                print("¡Ya adivinaste esa letra! Intenta otra.")
            elif entrada in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == entrada:
                        palabra_oculta = palabra_oculta[:i] + entrada + palabra_oculta[i+1:]

                print("¡Bien hecho! La palabra es:", palabra_oculta)

                if "_" not in palabra_oculta:
                    print("¡Felicidades, adivinaste la palabra!")
                    break
            else:
                intentos += 1
                print("Letra incorrecta, te quedan", 6 - intentos, "intentos.")
                letras_adivinadas.append(entrada)

                if intentos == 1:
                    print("=========")
                    print("    0")
                    print("=========")
                elif intentos == 2:
                    print("=========")
                    print("    0")
                    print("    │")
                    print("=========")
                elif intentos == 3:
                    print("=========")
                    print("    0")
                    print("   /│")
                    print("=========")
                elif intentos == 4:
                    print("=========")
                    print("    0")
                    print("   /│\\")
                    print("=========")
                elif intentos == 5:
                    print("=========")
                    print("    0")
                    print("   /│\\")
                    print("   /")
                    print("=========")

def jugar_en_pareja():
    palabra_jugador1 = input("Jugador 1, ingresa una palabra para que el Jugador 2 la adivine: ")
    pista_jugador1 = input("Jugador 1, ingresa una pista para la palabra ingresada: ")

    palabra_oculta = "_" * len(palabra_jugador1)
    intentos = 0
    letras_adivinadas = []
    pista_revelada = False

    while intentos < 6:
        print("===============================")
        entrada = input("Jugador 2, ingresa una letra: ")

        if entrada.lower() == 'pista' and not pista_revelada:
            print("Pista:", pista_jugador1)
            pista_revelada = True
        elif entrada in letras_adivinadas:
            print("¡Ya adivinaste esa letra! Intenta otra.")
        elif entrada in palabra_jugador1:
            for i in range(len(palabra_jugador1)):
                if palabra_jugador1[i] == entrada:
                    palabra_oculta = palabra_oculta[:i] + entrada + palabra_oculta[i+1:]

            print("¡Bien hecho! La palabra es:", palabra_oculta)

            if "_" not in palabra_oculta:
                print("¡Felicidades, Jugador 2, adivinaste la palabra!")
                break
        else:
            intentos += 1
            print("Letra incorrecta, te quedan", 6 - intentos, "intentos.")
            letras_adivinadas.append(entrada)

            if intentos == 1:
                print("=========")
                print("    0")
                print("=========")
            elif intentos == 2:
                print("=========")
                print("    0")
                print("    │")
                print("=========")
            elif intentos == 3:
                print("=========")
                print("    0")
                print("   /│")
                print("=========")
            elif intentos == 4:
                print("=========")
                print("    0")
                print("   /│\\")
                print("=========")
            elif intentos == 5:
                print("=========")
                print("    0")
                print("   /│\\")
                print("   /")
                print("=========")

modo_juego = input("¿Quieres jugar solo o en pareja? (solo/en pareja): ")

if modo_juego.lower() == 'solo':
    jugar_solo()
elif modo_juego.lower() == 'en pareja':
    jugar_en_pareja()
else:
    print("Modo de juego no válido. Por favor, elige entre 'solo' o 'en pareja'.")
