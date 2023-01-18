# Scrivere e testare una funzione sostituisci(lista,valore1,valore2)
# che prende in input una lista e due valori e ritorna una lista in cui tutte le occorrenze del valore1 sono sostituite da valore2

def sostituisci(lista, valore1, valore2):
    nuova_lista = [valore2 if x==valore1 else x for x in lista]
    return nuova_lista

lista = [1, 2, 3, 4, 5, 1, 6, 1]
valore1 = 1
valore2 = 7

print(sostituisci(lista, valore1, valore2))
