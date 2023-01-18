# Scrivere una funzione che prende in input una lista,
# la controlla e se contiene almeno un valore che non sia
# un intero ritorna un errore. Altrimenti la funzione ritorna
# una lista che in prima posizione contiene il valore
# minimo dell’input, in seconda posizione la media e in
# terza posizione contiene il valore massimo.

def statistiche(lista):
    if any(not isinstance(i, int) for i in lista):
        raise ValueError("La lista contiene elementi che non sono interi.")
    else:
        min_val = min(lista)
        max_val = max(lista)
        avg_val = sum(lista) / len(lista)
        return [min_val, avg_val, max_val]

lista = [1, 2, 3, 4, 5]
print(statistiche(lista))
