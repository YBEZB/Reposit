pes_pallas = 112 
pes_nina = 75

num_pallassos = int(input("Nombre de pallassos venuts: "))
num_nines = int(input("Nombre de nines venudes: "))


pes_total = ((num_pallassos * pes_pallas) + (num_nines * pes_nina))


if pes_total >= 1000:
    pes_total_kg = pes_total / 1000
    pes_total_kg = round(pes_total_kg, 2)
    print("El pes total del paquet que serà enviat es de", pes_total_kg, "kg.")
    
    if pes_total_kg >= 50:
        print("Has excedit el pes màxim")

else:
    pes_total = round(pes_total, 2)
    print("El pes total del paquet que serà enviat es de", pes_total, "g.")
