# Stampare i numeri pari da 1 a 100, poi stampare i numeri dispari da 1 a 40 (utilizzando il ciclo for con la funzione range)
def numeri_pari():
    print("\nStampare i numeri pari da 1 a 100")
    for i in range(2, 102, 2):
        print(i)

def numeri_dispari():
    print("\nStampare i numeri dispari da 1 a 40")
    for i in range(1, 40, 2):
        print(i)
'''     
numeri_pari()
numeri_dispari()
'''

# Generare una lista lunga 20 di numeri casuali compresi tra n ed m inseriti da utente, a questo punto stampare
# la lista e successivamente stamparla capovolta (dall’ultimo elemento al primo) e raddoppiando ogni numero 
import random
lista = []

def cicloLista():
    n=int(input("Inserire il primo numero  : "))
    m=int(input("Inserire il secondo numero: "))
    for i in range(20):
        lista.append(random.randint(n,m))
    print("\nLista origniale   = ", lista)
    lista.reverse()
    print("Lista capovolta   = ", lista)
    for molt in range(20):
        lista[molt] *= 2
    print("Lista raddoppaita = ", lista)
'''
cicloLista()
'''


# Scrivere un programma che individui il valore massimo e minimo all’interno di una lista lunga n (inserito da utente) 
# di numeri generati casualmente da -8 a 15.
listaMinMax= []

def lt_Max_Min():
    l=int(input("Inserire la lunghezza dalla lista: "))
    for i in range(l):
        listaMinMax.append(random.randint(-8, 15))
    print("\nLista origniale = ", listaMinMax)
    print("Valore lista massimo = ", max(listaMinMax))
    print("Valore lista minimo  = ", min(listaMinMax))
'''
lt_Max_Min()
'''

# Si vuole creare un programma che riesca a gestire un distributore di merendine usando un dizionario
# Usiamo al posto degli Euro i centesimi. Il distributore contiene:
#	merendine fiesta da 80 centesimi
#	merendine duplo da 90 centesimi
#	succhi di frutta da 45 centesimi
#	oreo da 90 centesimi

# Scrivere una funzione che mi indichi il più costoso, ricordando che il massimo si può trovare attraverso i comandi:

# Scrivere una funzione che stampi la merendina che abbia sia il costo minore di 1 euro sia un numero di lettere pari nel nome.

# Scrivere una funzione che stampi la merendina che abbia il costo minore di 50 centesimi oppure un numero di lettere pari.
