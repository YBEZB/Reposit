diccionari = {
    
  "Ordinador": "L'estas Utilitant",
  "Musica": "Tipo de entreteniment",
  "Estofado": "Et pot agrada.",
  "Bolograf": "El boligraf es un estri que sirveix para a escriure.",
}

while True:
    resposta = input("Escull una opció: Ordinador, Musica, Estofado, Bolograf: ")

    if resposta in diccionari:
        print(diccionari[resposta])
        break
    else:
        print("La recerca introduïda no existeix en el diccionari. Torna a provar.")

