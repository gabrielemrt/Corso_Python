# Data l’equazione "ax + b = 0" con a e b inseriti da tastiera,
# scrivere un programma in linguaggio C per determinare il
# valore di x, se esiste, che risolve l’equazione

print("CALCOLO EQUAZIONE ax + b = 0")

a = input("Inserire il valore di A: ")
b = input("Inserire il valore di B: ")

x = -(int(b)/int(a))

print("Il risultati di X è = ", x)
