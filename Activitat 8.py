diccionari = {
    
  "Ordinador": input("Que es un ordinador?:"),
  "Musica": input("Que es la musica?:"),
  "Estofado": input("Que es un guisat?:"),
  "Bolograf": input("Que es un boligraf?:"),
}

while True:
    resposta = input("Escull una opció: Ordinador, Musica, Estofado, Bolograf: ")

    if resposta in diccionari:
        print(diccionari[resposta])
        break
    else:
        print("La recerca introduïda no existeix en el diccionari. Torna a provar.")


