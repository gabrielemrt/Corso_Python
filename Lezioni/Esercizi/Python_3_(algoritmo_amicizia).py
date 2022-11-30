risposta = ""

print("\n\n")
input("COMPONI IL NUMERO DI TELEFONO DELLA PERSONA: ")
print("E' IN CASA?")
risposta = input("Rispondi con Y se sì o N se no: ")
if risposta=="N":
    print("LASCIA UN MESSAGGIO")
    print("ASPETTA DI ESSERE RICHAMATO")
risposta = input("TI VA DI MANGIARE QUALCOSA INSIEME? ")
if risposta=="Y":
    print("MANGIATE QUALCOSA INSIEME")
elif risposta=="N":
    risposta = input("E DI BERE QUALCOSA DI CALDO? ")
    if risposta=="Y":
        print("SCEGLI:")
        print("TE', CAFFE' o CIOCCOLATA")
        risposta=input()
        if risposta=="TE'": 
            print("FATEVI STO ", risposta)
        else:
            print("FATEVI STA ", risposta)
    elif risposta=="N":
        print("")        


print("SIETE DIVENTATI AMICI!")
print("ORA HAI UNA PERSONA IN PIU' A CUI POTER ROMPERE LE PALLE IN CASO DI BISOGNO. E VICEVERSA")
