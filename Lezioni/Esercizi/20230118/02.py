# Scrivere una funzione che data in input (alla funzione) una lista,
# ritorna una stringa formata dalla concatenazione degli elementi della lista.

def concatenazione(lista):
    return ''.join(map(str,lista))

lista = [1, 2, 3, 4, 5]
print(concatenazione(lista))
