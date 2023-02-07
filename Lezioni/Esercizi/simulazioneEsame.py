import subprocess

def create_file(filename):
	# scrivere il comando linux per creare un file il cui nome è passato dentro questa funzione 
	name = "touch " + filename
	subprocess.run(name, shell=True)
    
    
def scrivi_errore_hops(filename, site):
	stampERRORE = 'echo "Numero massimo di hops raggiunto per il sito: " ' + site + '>' + filename
	subprocess.run(stampERRORE, shell=True)

def scrivi_ping_sito(filename, site):
	ping = "ping -c 4 " + site + " > " + filename
	subprocess.run(ping, shell=True)

def traceroute_count(site):
	trac = "traceroute " + site + "| wc -l"
	return subprocess.check_output(trac, shell=True).decode('utf-8')

def main():
	# conta quanti hops vengono fatti fino al sito indicato
	sito = "google.com"
	hops_number = int(traceroute_count(sito))
	# creo un file di Log
	filename = "output.txt"
	create_file(filename)
	if (hops_number == 30):
		#se il numero di hops raggiunge il massimo (30) scrivo in un file di output "Numero massimo di hops raggiunto per il sito: <sito>
		scrivi_errore_hops(filename, sito)
	else:
		#altrimenti eseguo il ping (4 pacchetti) al sito e scrivo tutto il risultato del comando ping dentro il file di output
		scrivi_ping_sito(filename, sito)


if __name__ == '__main__':
	main()