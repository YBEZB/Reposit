import random

registrat = False
nom = ""
contrasenya = ""
nombre_preferit = ""
sobrenom = ""

def registra():
    global registrat, nom, contrasenya, nombre_preferit, sobrenom
    while not registrat:
        print("1º Pas: Registra't per poder jugar")
        print("----------------------------------")
        nom = input("Introdueix el teu nom: ")
        print("----------------------------------")
        print("2º Pas: Posa el teu sobrenom:")
        sobrenom = input("------------->")
        print("3º Pas: Introdueix el teu numero preferit amb una lletre:")
        print("---------------------------------------------------------")
        numero_preferit = input("")
        contrasenya = sobrenom + nom + numero_preferit
        print("Registre exitós. La teva contrasenya és:", contrasenya)
        print("-------------------------------------------------")
        registrat = True
        while True:
            password = input("Introdueix la teva contrasenya per accedir: ")
            if password == contrasenya:
                print("Accés")
                break
            else:
                print("Error")

def jugar_piedra_papel_tijera():
    registra()
    while True:
        print("A quin joc vols jugar? " + sobrenom)
        print("===================================")
        print("1) Pedre, paper o tisores")
        print("2) Tres en ratlla")
        opcion_juego = input("Escull un joc (1,2): ")
        
        if opcion_juego == '1':
            jugar_piedra_paper_tijera()
        elif opcion_juego == '2':
            jugar_tres_en_ratlla()
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1,2)")

def jugar_piedra_paper_tijera():
    while True:
        aleatorio = random.randrange(0, 3)
        opciones = ["pedra", "paper", "tisores"]
        escoll_BOT = opciones[aleatorio]
        
        print("1) Pedra")
        print("2) Paper")
        print("3) Tisores")
        opcio = int(input("¿Qué escoges: "))
        
        if opcio == 1:
            escoll_USUARI = "pedra"
        elif opcio == 2:
            escoll_USUARI = "paper"
        elif opcio == 3:
            escoll_USUARI = "tisores"
        
        print("Tú escoges:", escoll_USUARI)
        print("BOT escoge:", escoll_BOT)
        print(".....")
        
        if escoll_BOT == escoll_USUARI:
            print("Empate")
            break
        elif (escoll_BOT == "paper" and escoll_USUARI == "tisores") or (escoll_BOT == "tisores" and escoll_USUARI == "pedra") or (escoll_BOT == "pedra" and escoll_USUARI == "paper"):
            print("Guanyas tú")
            break
        else:
            print("Guanya el BOT")
            break
            

def jugar_tres_en_ratlla():
    print("¡Tres en Raya!")
    tablero = [' ' for _ in range(9)]
    
    def mostrar_tablero():
        print("__________")
        print(tablero[0] + ' | ' + tablero[1] + ' | ' + tablero[2])
        print('--+---+--')
        print(tablero[3] + ' | ' + tablero[4] + ' | ' + tablero[5])
        print('--+---+--')
        print(tablero[6] + ' | ' + tablero[7] + ' | ' + tablero[8])
        print("__________")

    def verificar_guanyador(simbolo):
        for i in range(0, 9, 3):
            if tablero[i] == tablero[i + 1] == tablero[i + 2] == simbolo:
                return True 
        for i in range(3):
            if tablero[i] == tablero[i + 3] == tablero[i + 6] == simbolo:
                return True
        if tablero[0] == tablero[4] == tablero[8] == simbolo or tablero[2] == tablero[4] == tablero[6] == simbolo: 
            return True
        return False

    def turno_bot():
        movimientos_disponibles = [i for i, casilla in enumerate(tablero) if casilla == ' ']
        if movimientos_disponibles:
            simbolo = random.choice(movimientos_disponibles)
            tablero[simbolo] = 'O'
            mostrar_tablero()
            if verificar_guanyador('O'):
                print("¡El bot ha ganado!")
                return True
        return False

    while True:
        mostrar_tablero()
        if turno_bot():
            break
        
        movimiento = int(input("Elige un número del 0 al 8 para poner tu ficha: "))
        if tablero[movimiento] == ' ':
            tablero[movimiento] = 'X'
            if verificar_guanyador('X'):
                mostrar_tablero()
                print("¡Has ganado!")
                break
            if ' ' not in tablero:
                mostrar_tablero()
                print("¡Empate!")
                break
        else:
            print("Esta casilla ya está ocupada. Elige otra.")

jugar_piedra_papel_tijera()