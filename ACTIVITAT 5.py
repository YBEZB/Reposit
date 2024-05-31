from decimal import Decimal

def suma_num():
    primer_numero = Decimal(input("Ingresa el primer número: "))
    segundo_numero = Decimal(input("Ingresa el segundo número: "))
    tercer_numero = Decimal(input("Ingresa el tercer número: "))

    resultado = primer_numero + segundo_numero + tercer_numero
    print("Resultado:", resultado)

suma_num()
