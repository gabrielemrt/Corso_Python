risposta = ""

def verifica(a):
    if (a=="Y") or (a=="y") or (a=="S") or (a=="s"):
        return "Y"
    elif (a=="N") or (a=="n"):
        return "N"
    else:
        return "error"
    

print("\n\n")
input(">> COMPONI IL NUMERO DI TELEFONO DELLA PERSONA: ")
print(">> E' IN CASA?")
risposta = input("Rispondi con Y se sì o N se no: ")
conferma = verifica(risposta)
if conferma=="N":
    print(">> LASCIA UN MESSAGGIO")
    print(">> ASPETTA DI ESSERE RICHAMATO")
risposta = input(">> TI VA DI MANGIARE QUALCOSA INSIEME? ")
conferma = verifica(risposta)
if conferma=="Y":
    print(">> MANGIATE QUALCOSA INSIEME")
elif conferma=="N":
    risposta = input(">> E DI BERE QUALCOSA DI CALDO? ")
    conferma = verifica(risposta)
    if conferma=="Y":
        print(">> SCEGLI:")
        print(">> TE', CAFFE' o CIOCCOLATA")
        risposta=input()
        conferma = verifica(risposta)
        if conferma=="TE'": 
            print(">> FATEVI STO ", risposta)
        else:
            print(">> FATEVI STA ", risposta)
    elif conferma=="N":
        n=0
        print(">> ALLORA GIOCHIAMO UN PO'...")
        
        while conferma!="Y":
            print(">> ... COS'ALTRO TI VA DI FARE?")
            risposta=input()
            risposta=input(">> E' UNA COSA CHE VA DI FARE ANCHE A TE? ")
            conferma = verifica(risposta)
            if conferma=="Y":
                print(">> E FACCIAMOLO INSIEME DAI...")
            elif conferma=="N":
                n=n+1
                if n>6:
                    print(">> SCEGLI FRA TUTTE LE OPZIONI QUELLA CHE TI SEMBRA ESSERE LA MENO DISUMANA")
                    print(">> FATTELA PIACEGE")
                    break
        
        print(">> SVAGATEVI UN PO' INSIEME")
                


print("\n>> SIETE DIVENTATI AMICI!")
print(">> ORA HAI UNA PERSONA IN PIU' A CUI POTER ROMPERE LE PALLE IN CASO DI BISOGNO. E VICEVERSA")
print("\n\n")