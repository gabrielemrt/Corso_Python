'''
CREARE UN PROGRAMMA CHE CALCOLI LA MEDIA DI 10 NUMERI INSERITI DA TASTIERA
'''
'''
n=0
sum=0
med=0

for x in range(10):
    n = int(input("Inserisci un numero: "))
    sum = sum + n    
    med = sum/10
print("Il rusultato è: ", med)
'''

''' CALCOLATRICE '''
n1 = int(input("Inserire il primo numero: "))
op = input("Inserire l'operazione logica: ")
n2 = int(input("Inserire il secondo numero: "))

def calcolatrice(a,b,c):
    if c=="+":
        ris=a+b
    elif c=="-":
        ris=a-b
    elif c=="*":
        ris=a*b
    elif c=="/":
        ris=a/b
    print("Il risultato è = ", ris)

calcolatrice(n1,n2,op)
