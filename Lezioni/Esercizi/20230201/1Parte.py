# Stampare i numeri pari da 1 a 100, poi stampare i numeri dispari da 1 a 40 (utilizzando il ciclo for con la funzione range)
'''
print("Stampare i numeri pari da 1 a 100")
for a in range(2, 102, 2):
    print(f"\t{a}")

print("Stampare i numeri dispari da 1 a 40")
for b in range(1, 41, 2):
    print(f"\t{b}")
''' 

# Generare una lista lunga 20 di numeri casuali compresi tra n ed m inseriti da utente, a questo punto stampare
# la lista e successivamente stamparla capovolta (dall’ultimo elemento al primo) e raddoppiando ogni numero 
'''
import random

lista = []
n = int(input("Inserire il primo parametro per la lista:   "))
m = int(input("Inserire il secondo parametro per la lista: "))

for l in range(20):
    lista.append(random.randint(n,m))

print("lista originale = ", lista)
lista.reverse()
print("lista invertita = ", lista)
'''

# Scrivere un programma che individui il valore massimo e minimo all’interno di una lista lunga n (inserito da utente) 
# di numeri generati casualmente da -8 a 15.

import random

lista = []
n = int(input("Inserire la lunghezza della lista: "))

for l in range(n):
    lista.append(random.randint(-8,15))

print(lista)

print("Valore massimo della lista = ", max(lista))
print("Valore minimo della lista  = ", min(lista))
