# Si scriva un programma in linguaggio C che legga da tastiera i valori
# delle lunghezze dei tre lati di un triangolo (detti A, B e C), e determini:
# • se il triangolo è equilatero
# • se il triangolo è isoscele
# • se il triangolo è scaleno
# • se il triangolo è rettangolo.

print("DETERMINAZIONE TIPO DI TRINAGOLO")
a = input("Inserire il valore del lato A: ")
b = input("Inserire il valore del lato B: ")
c = input("Inserire il valore del lato C: ")

a = int(a)
b = int(b)
c = int(c)

print("")

if (a==b & a==c & b==c):
    print("Il trinagolo è EQUILATERO")
elif(a==b or a==c or b==c):
    print("Il triangolo è ISOSCELE")
elif (a!=b & a!=c & b!=c):
    print("Il trinagolo è SCALENO")

if ( (((a**2)+(b**2))==(c**2)) or (((c**2)+(a**2))==(b**2)) or (((b**2)+(c**2))==(a**2)) ):
    print("Il trinagolo è RETTANGOLO")
