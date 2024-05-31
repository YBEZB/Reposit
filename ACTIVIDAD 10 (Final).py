print ("----------------------------------------------------------------------------------------")
print("Introdueix les dades per veure quin equip té més probabilitats de guanyar el partit")
print ("----------------------------------------------------------------------------------------")

def validar_equip(equip):
    if equip.isalpha():  
        return equip
    else:
        print(f"ERROR")
        return input("Introduïu el nom del primer equip: ")

def validar_nivell_joc(nivell_joc):
    opcions_valides = ["alt", "mitjà", "baix"]
    if nivell_joc.lower() in opcions_valides:
        return nivell_joc
    else:
        print(f"ERROR")
        return input("Nivell de joc (alt, mitjà, baix): ")

def validar_sn(resposta):
    opcions_valides = ["sí", "no"]
    if resposta.lower() in opcions_valides:
        return resposta
    else:
        print(f"ERROR")
        return input("¿Juga a casa? (sí/no): ")
    
def validar_enter(valor):
    try:
        return int(valor)
    except ValueError:
        print(f"ERROR")
        return new_func()

def new_func():
    return int(input("Nombre de partits guanyats: "))

equip1 = validar_equip(input("Introduïu el nom del primer equip: "))
print ("------------------------------------")
nivell_joc_equip1 = validar_nivell_joc(input("Nivell de joc (alt, mitjà, baix): "))
print ("------------------------------------")
partits_guanyats_equip1 = validar_enter(input("Nombre de partits guanyats: "))
print ("------------------------------------")
partits_perduts_equip1 = validar_enter(input("Nombre de partits perduts: "))
print ("------------------------------------")
partits_empatats_equip1 = validar_enter(input("Nombre de partits empatats: "))
print ("------------------------------------")
a_casa_equip1 = validar_sn(input("¿Juga a casa? (sí/no): "))
print ("------------------------------------")
gols_a_favor_equip1 = validar_enter(input("Gols a favor: "))
print ("------------------------------------")
gols_en_contra_equip1 = validar_enter(input("Gols en contra: "))
print ("------------------------------------")
jugadors_lesionats_equip1 = validar_enter(input("Nombre de jugadors lesionats: "))
print ("=================================================================")
print ("=================================================================")
equip2 = validar_equip(input("Introduïu el nom del segon equip: "))
print ("------------------------------------")
nivell_joc_equip2 = validar_nivell_joc(input("Nivell de joc (alt, mitjà, baix): "))
print ("------------------------------------")
partits_guanyats_equip2 = validar_enter(input("Nombre de partits guanyats: "))
print ("------------------------------------")
partits_perduts_equip2 = validar_enter(input("Nombre de partits perduts: "))
print ("------------------------------------")
partits_empatats_equip2 = validar_enter(input("Nombre de partits empatats: "))
print ("------------------------------------")
a_casa_equip2 = validar_sn(input("¿Juga a casa? (sí/no): "))
print ("------------------------------------")
gols_a_favor_equip2 = validar_enter(input("Gols a favor: "))
print ("------------------------------------")
gols_en_contra_equip2 = validar_enter(input("Gols en contra: "))
print ("------------------------------------")
jugadors_lesionats_equip2 = validar_enter(input("Nombre de jugadors lesionats: "))
print ("------------------------------------")


def ajust_per_nivell(nivell_joc):
    if nivell_joc.lower() == "alt":
        return 2
    elif nivell_joc.lower() == "mitjà":
        return 1.5
    elif nivell_joc.lower() == "baix":
        return 1.15

def joc_a_casa(a_casa_equip):
    if a_casa_equip == "sí":
        return 2
    elif a_casa_equip == "no":
        return 1.2
    else:
        return 1

nivell_equip1 = ajust_per_nivell(nivell_joc_equip1)
nivell_equip2 = ajust_per_nivell(nivell_joc_equip2)

casa_equip1 = joc_a_casa(a_casa_equip1)
casa_equip2 = joc_a_casa(a_casa_equip2)

probabilitat_equip1 = (partits_guanyats_equip1 + gols_a_favor_equip1 - partits_perduts_equip1 - gols_en_contra_equip1 - jugadors_lesionats_equip1 + partits_empatats_equip1) * nivell_equip1 * casa_equip1
probabilitat_equip2 = (partits_guanyats_equip2 + gols_a_favor_equip2 - partits_perduts_equip2 - gols_en_contra_equip2 - jugadors_lesionats_equip2 + partits_empatats_equip2) * nivell_equip2 * casa_equip2

total_probabilitat = probabilitat_equip1 + probabilitat_equip2
if total_probabilitat > 100:
    factor_ajust = 100 / total_probabilitat
    probabilitat_equip1 = round(probabilitat_equip1 * factor_ajust, 2)
    probabilitat_equip2 = round(probabilitat_equip2 * factor_ajust, 2)
else:
    probabilitat_equip1 = round(probabilitat_equip1, 2)
    probabilitat_equip2 = round(probabilitat_equip2, 2)

empatats_equips = 100 - probabilitat_equip1 - probabilitat_equip2
empatats_equips = round(empatats_equips, 2)

print(f"La probabilitat que guanyi el {equip1} és: {probabilitat_equip1}%")
print(f"La probabilitat que guanyi el {equip2} és: {probabilitat_equip2}%")
print(f"La probabilitat d'empat entre {equip1} i {equip2} és: {empatats_equips}%")

def guardar_dades(probabilitat_equip1, probabilitat_equip2, empatats_equips):
    with open("Dades_dels_equips.txt", "a") as file:
        file.write(f"ACTIVITAT FINAL: -------------------------------------------\n")
        file.write(f"\n")
        file.write(f"Les probabilitats dels equips són apartir de:\n")
        file.write(f"El nivell de jugabilitat del {equip1} es {nivell_joc_equip1}\n")
        file.write(f"El nivell de jugabilitat del {equip2} es {nivell_joc_equip2}\n")
        file.write(f"El partits guanyats per {equip1} són {partits_guanyats_equip1}\n")
        file.write(f"El partits guanyats per {equip2} són {partits_guanyats_equip2}\n")
        file.write(f"El partits perduts per {equip1} són {partits_perduts_equip1}\n")
        file.write(f"El partits perduts per {equip2} són {partits_perduts_equip2}\n")
        file.write(f"El partits empatats per {equip1} són {partits_empatats_equip1}\n")
        file.write(f"El partits empatats per {equip2} són {partits_empatats_equip2}\n")
        file.write(f"El {equip1} {a_casa_equip1} juga en casa\n")
        file.write(f"El {equip2} {a_casa_equip2} juga en casa\n")
        file.write("-------------------------------------------------------------------\n") 
        file.write(f"{equip1}: {probabilitat_equip1}%\n")
        file.write(f"{equip2}: {probabilitat_equip2}%\n")
        file.write(f"Probabilitat d'empat: {empatats_equips}%\n")
        file.write("-------------------------------------------------------------------\n")   
        
guardar_dades(probabilitat_equip1, probabilitat_equip2, empatats_equips)
