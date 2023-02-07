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
distributore={"fiesta": 800, "duplo": 90, "succhi": 45, "oreo": 90}

def distributore_merendine(distributore):
    print("\n\n\tDISTRIBUTORE MERENDINE")
    print(distributore.keys())
    scelta=str(input("Scegliere la merendina: "))    
    
    ##while (scelta != distributore.keys()):
    ##    print("aa")
    
    print("\nPrezzo = ", distributore[scelta], "centesimi")
'''
distributore_merendine(distributore)
'''

    
# Scrivere una funzione che mi indichi il più costoso, ricordando che il massimo si può trovare attraverso i comandi:
def distributore_costoso():
    distributoreMAX = max(distributore, key=distributore.get)
    print("\nLa merendia più costosa è: ", distributoreMAX)
'''
distributore_costoso()
'''


# Scrivere una funzione che stampi la merendina che abbia sia il costo minore di 1 euro sia un numero di lettere pari nel nome.
def distributore_min1_e_lettPari(distrib):
    print("\nLe merendine con un costo minore di 1euro e il numero di lettere pari sono:")
    for nome, prezzo in distrib.items():
        if (prezzo < 100) and (len(nome) % 2 == 0):
            print(nome)
'''
distributore_min1_e_lettPari(distributore)
'''


# Scrivere una funzione che stampi la merendina che abbia il costo minore di 50 centesimi oppure un numero di lettere pari.
def distributore_min50cent_o_letterePari(distr):
    print("\nLe merendine con un costo minore di 50cent o il numero di lettere pari sono:")
    for nome, prezzo in distr.items():
        if (prezzo < 50) or (len(nome) %2 == 0):
            print(nome)
'''
distributore_min50cent_o_letterePari(distributore)
'''


################################################################################################################################################################
################################################################################################################################################################
#####                                                              SIMULAZIONE ESAME                                                                       #####
################################################################################################################################################################
################################################################################################################################################################
import subprocess

def create_file(filename):
	# scrivere il comando linux per creare un file il cui nome è passato dentro questa funzione 
    file=("touch " + filename)
    subprocess.run(file, shell=True)

def scrivi_errore_hops(filename, site):
    stampa = (" echo 'Numero massimo di hops raggiunto per il sito: ' " + site + " > " + filename)
    subprocess.run(stampa, shell=True)

def scrivi_ping_sito(filename, site):
    ping = ("ping -c 4 " + site + " > " + filename)
    subprocess.run(ping, shell=True)

def traceroute_count(site):
    traceroute=("traceroute " + site + "| wc -l")
    return subprocess.check_output(traceroute, shell=True).decode('utf-8')


def main():
    # conta quanti hops vengono fatti fino al sito indicato
    sito = "google.com"
    hops_number = int(traceroute_count(sito))
    # creo un file di Log
    filename = "output.txt"
    create_file(filename)
    if (hops_number == 30):
        #se il numero di hops raggiunge il massimo (30) scrivo in un file di output "Numero massimo di hops raggiunto per il sito: <sito>"
        scrivi_errore_hops(filename, sito)
    else:
        #altrimenti eseguo il ping (4 pacchetti) al sito e scrivo tutto il risultato del comando ping dentro il file di output
        scrivi_ping_sito(filename, sito)

if __name__ == '__main__':
	main()