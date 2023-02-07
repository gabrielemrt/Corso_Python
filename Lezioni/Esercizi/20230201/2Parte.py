# Si vuole creare un programma che riesca a gestire un distributore di merendine usando un dizionario
# Usiamo al posto degli Euro i centesimi. Il distributore contiene:
#	merendine fiesta da 80 centesimi
#	merendine duplo da 90 centesimi
#	succhi di frutta da 45 centesimi
#	oreo da 90 centesimi

print("\n=== DISTRIBUTORE DI MERENDINE ===\n") 

dizionarioDistributore = {"fiesta": 80, "duplo": 90, "succhi di frutta": 45, "oreo": 90}

print("Il distributore contiene: ", dizionarioDistributore.keys())
scelta = str(input("Inserire la scelta della merendina: "))

print("prezzo = ", dizionarioDistributore[scelta], " centesimi\n")


# Scrivere una funzione che mi indichi il più costoso, ricordando che il massimo si può trovare attraverso i comandi:

massima_chiave = max(dizionarioDistributore, key=dizionarioDistributore.get)
print(massima_chiave)


# Scrivere una funzione che stampi la merendina che abbia sia il costo minore di 1 euro sia un numero di lettere pari nel nome.

def merendine_economiche(distributore):
  for nome, costo in distributore.items():
      if len(nome) % 2 == 0 and costo < 100:
          print("La merendina con il costo minore di 1euro e un numero di lettere pari è = ", nome, costo)

merendine_economiche(dizionarioDistributore)


# Scrivere una funzione che stampi la merendina che abbia il costo minore di 50 centesimi oppure un numero di lettere pari.

def merendina_50cent_lettPari(distributore):
    for nome, prezzo in distributore.items():
        if prezzo <= 50 or len(nome) % 2 == 0:
          print("La merendina con il costo minore di 50cent oppure un numero di lettere pari è = ", nome, prezzo)
          
merendina_50cent_lettPari(dizionarioDistributore)