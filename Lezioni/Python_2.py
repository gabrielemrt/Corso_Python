#Scrivere un programma che legga la temperatura in centgradi e mostri un
#messaggio che segua la seguente didascalia:
# T < 0 "clima gelido"
# T 0-10 "clima veramente freddo"
# T 10-20 "clima freddo"
# T 20-30 "temperatura normale"
# T 30-40 "clima caldo"
# T 40 "clima veramente caldo"

temp = int(input("Inserire la temperatura: "))

def switch(temp):
    if temp < 0:
        return "clima gelido"
    elif temp >= 0 and temp < 10:
        return "clima veramente freddo"
    elif temp >= 10 and temp < 20:
        return "clima freddo"
    elif temp >= 20 and temp < 30:
        return "temperatura normale"
    elif temp >= 30 and temp < 40:
        return "clima caldo"
    elif temp > 40:
        return "clima veramente caldo"

print(">>> ", switch(temp), " <<<") 




a=0
while a<10:
    a=a+1
    print(a)




stringa = ""
num = int( input("Inserire un numero: ") )
while (num != 0):
    stringa = stringa+str(num%10)
    num = num/10
    num = int(num)
print("il numero è = " +stringa)
  


x=2
while x<20:
    print(x)
    x=x+2
x=1
for x in range(1, 20, 2):
    print(x)



pss="ciao"
txt=""
while txt!=pss:
    txt=input("Inserisci la password: ")
    if txt != pss:
        print ("Password ERRATA, riprovare.")
    else:
        print ("Password CORRETTA")
