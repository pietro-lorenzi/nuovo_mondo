from termcolor import cprint
from pyfiglet import figlet_format
import os
from altreFunzioni import *
 
def ingaggia_eq():
    eq = {
        "marinaio": 0,
        "meccanico": 0,
        "medico": 0,
        "cuoco": 0,
        "navigatore": 0
    }
 
    cprint("Ogni spedizione ha bisogno di uomini disposti a seguirti oltre l'orizzonte.", "cyan")
    cprint("Marinai, medici, navigatori, meccanici e cuochi : scegli con attenzione chi farà parte della tua spedizione.", "cyan")
    cprint("Ogni membro della ciurma richiederà una paga proporzionata alle proprie capacità.", "cyan")
    cprint("Ricorda: avere più uomini non significa avere uomini migliori.", "cyan")
    print()
 
    massimo=False

    while not massimo:

        marinaio=0
        while marinaio<1:
            try:
                cprint("Quanti marinai vuoi portare con te, capitano?", "blue")
                cprint("I marinai sono uomini comuni senza capacità speciali, ma a volte un braccio in più non fa male.", "blue")
                cprint("Costo: 10 monete a settimana", "blue")
                marinaio=int(input())
            except:
                cprint("Inserire un numero valido", "red")

        meccanico=0
        while meccanico<1:
            try:
                cprint("Quanti meccanici vuoi portare con te, capitano?", "blue")
                cprint("I meccanici non hanno esperienza con le onde, ma lasciarli a riva potrebbe far finire voi sott'acqua.", "blue")
                cprint("Costo: 15 monete a settimana", "blue")
                meccanico=int(input())
            except:
                cprint("Inserire un numero valido" , "red")

        medico=0
        while medico<1:
            try:
                cprint("Quanti medici vuoi portare con te, capitano?", "blue")
                cprint("I medici sono costosi ma indispensabili: quando qualcuno cade, sono l'unico ponte tra la vita e il mare.", "blue")
                cprint("Costo: 25 monete a settimana", "blue")
                medico=int(input())
            except:
                cprint("Inserire un numero valido", "red")

        cuoco=0
        while cuoco<1:
            try:
                cprint("Quanti cuochi vuoi portare, capitano?", "blue")
                cprint("I cuochi trasformano scorte misere in qualcosa che tiene l'equipaggio in piedi… e a volte di buon umore.", "blue")
                cprint("Costo: 15 monete a settimana", "blue")
                cuoco=int(input())
            except:
                cprint(("Inserire un numero valido", "red"))     

        navigatore=0
        while navigatore<1:
            try:
                cprint("Quanti navigatori vuoi portare con te, capitano?", "blue")
                cprint("I navigatori conoscono le rotte e le stelle, senza dubbio potrebbero evitare che il viaggio si allunghi inutilmente.", "blue")
                cprint("Costo: 20 monete a settimana", "blue")
                navigatore=int(input())
            except:
                cprint(("Inserire un numero valido", "red"))   

        tot=marinaio+meccanico+medico+cuoco+navigatore
 
        if tot > 16:
            cprint("La nave non può reggere così tante anime, capitano. Sedici è il limite. Ricominciamo con l'ingaggio.", "red")
        else:
            eq["marinaio"] = marinaio       
            eq["cuoco"] = cuoco
            eq["meccanico"] = meccanico
            eq["medico"] = medico
            eq["navigatore"] = navigatore
            os.system("cls")

            massimo=True
    return eq
 
def provviste_eq(numero):
    provviste= {
        "verdura": 0,
        "frutta": 0,
        "carne": 0,
        "acqua": 0,
    }
 
    spesa=False
    while not spesa:
        monete=2000

        cprint("Ora è il momento di comprare le provviste, ma non ti preoccupare, ti consiglierò io la quantità necessaria per le 8 settimane di viaggio.","cyan")
        cprint("Ricorda, però, che il capitano sei tu, e sta a te decidere se essere previdenti e acquistarne di più o se rischiare per soldi e prenderne di meno.", "cyan")
        print()

        verdura = None 
        while verdura == None:
            try:
                cprint(f"Quanta verdura carichi sulla nave, capitano? (Ideale: {numero*0.5*8}kg)", "blue")
                cprint(f"Costo: 0.5 monete al kilo.", "blue")

                verdura=int(input())
                if verdura < 0:
                    raise Exception
            except:
                print(("Inserire un numero valido", "red"))   

        frutta = None
        while frutta == None:
            try:
                cprint(f"E la frutta? Le vitamine sono importanti, capitano. (Ideale: {numero*1*8}kg)", "blue")
                cprint(f"Costo: 1 moneta al kilo.", "blue")

                frutta=int(input())
                if frutta < 0:
                    raise Exception
            except:
                print(("Inserire un numero valido", "red"))

        carne = None
        while carne == None:
            try:
                cprint(f"Quanta carne porti con te? Gli uomini hanno fame, capitano. (Ideale: {numero*1*8}kg)", "blue")
                cprint(f"Costo: 2 monete al kilo.", "blue")

                carne=int(input())
                if carne < 0:
                    raise Exception
            except:
                print(("Inserire un numero valido", "red"))

        acqua = None
        while acqua == None:
            try:
                cprint(f"E quanti barili d'acqua? Senza, morirete prima ancora di arrivare, capitano. (Ideale: {numero*0.5*8} barili)", "blue")
                cprint(f"Costo: 0.5 monete al kilo.", "blue")

                acqua=int(input())
                if acqua < 0:
                    raise Exception
            except:
                print(("Inserire un numero valido", "red"))   

        costo_verdura=verdura*0.5
        monete=monete-costo_verdura
        
        costo_frutta=frutta*1
        monete=monete-costo_frutta
        
        costo_carne=carne*2
        monete=monete-costo_carne
        
        costo_acqua=acqua*0.5
        monete=monete-costo_acqua

        if monete < 0:
            print("Hai speso troppo, capitano. Riprova", "red")
        else:
            provviste["acqua"] = acqua      
            provviste["carne"] = carne
            provviste["frutta"] = frutta
            provviste["verdura"] = verdura
            os.system("cls")

            spesa=True
    return provviste
 
def merci_eq(dobloni):
    merci = {
        "medicinale": 0,
        "armi": 0,
        "sale": 0,
        "stoffa": 0,
        "coltelli": 0,
        "diamanti": 0,
    }
 
    cprint("Le merci saranno la tua principale fonte di guadagno durante il viaggio.", "cyan")
    cprint("Investire bene prima della partenza potrebbe fare la differenza al ritorno.", "cyan")
    print()
 
    spesa = False
    while not spesa:
            monete=dobloni 
            medicinali = None
            while medicinali == None:
                try:
                    cprint("Quante bottiglie di medicinale carichi? La malattia non avvisa, capitano. ", "blue")
                    cprint("Costo: 1 moneta a bottiglia.", "blue")

                    medicinali=int(input())
                    if medicinali < 0: 
                        raise Exception
                except:
                    print(("Inserire un numero valido", "red"))   

            armi = None
            while armi == None:
                try:
                    cprint("Quante armi porti? Il mare non è l'unico pericolo, capitano. ", "blue")
                    cprint("Costo: 5 monete a fucile.", "blue")

                    armi=int(input())
                    if armi < 0:
                        raise Exception
                except:
                    print(("Inserire un numero valido", "red"))   

            sale = None
            while sale == None:
                try:
                    cprint("Quanto sale vuoi? I piatti non conditi non piacciono a nessuno, capitano. ", "blue")
                    cprint("Costo: 0.5 monete per busta.", "blue")

                    sale=int(input())
                    if sale < 0:
                        raise Exception
                except:
                    print(("Inserire un numero valido", "red"))   

            stoffa = None
            while stoffa == None:
                try:
                    cprint("Quanti teli di stoffa? Gli indigeni ne vanno matti, capitano. ", "blue")
                    cprint("Costo: 2 monete a telo.", "blue")

                    stoffa=int(input())

                    if stoffa < 0:
                        raise Exception
                except:
                    print(("Inserire un numero valido", "red"))   

            coltelli = None
            while coltelli == None:
                try:
                    cprint("I coltelli sono ottimi per barattare. Quanti ne porti, capitano? ", "blue")
                    cprint("Costo: 0.5 monete a coltello.", "blue")

                    coltelli=int(input())
                    if coltelli < 0:
                        raise Exception
                except:
                    print(("Inserire un numero valido", "red"))   

            diamanti = None
            while diamanti == None:
                try:
                    cprint("E i diamanti? Sappiamo entrambi che il loro sbrilluccichio piace a qualsiasi popolazione, capitano. ", "blue")
                    cprint("Costo: 1 moneta a diamante.", "blue")

                    diamanti=int(input())
                    if diamanti < 0:
                        raise Exception
                except:
                    print(("Inserire un numero valido", "red"))   
 
            costo_med=medicinali*1
            monete=monete-costo_med
     
            costo_armi=armi*5
            monete=monete-costo_armi
       
            costo_sale=sale*0.5
            monete=monete-costo_sale
     
            costo_stoffa=stoffa*2
            monete=monete-costo_stoffa
     
            costo_coltelli=coltelli*0.5
            monete=monete-costo_coltelli
    
            costo_diamanti=diamanti*1
            monete=monete-costo_diamanti

            if monete < 0:
                print("Hai speso troppo, capitano. Riprova", "red")
            else:
                merci["armi"] = armi
                merci["coltelli"] = coltelli
                merci["diamanti"] = diamanti
                merci["medicinale"] = medicinali
                merci["sale"] = sale
                merci["stoffa"] = stoffa
                os.system("cls")
                spesa = True
    return merci
 
def introduzione():
    stampa("Nessuno sa davvero cosa spinga gli uomini verso l'orizzonte.")
    stampa("L'oro, forse.")
    stampa("La gloria.")
    stampa("O magari quella strana sensazione che esista qualcosa oltre ciò che conosciamo.")
    stampa("Il mare separa i codardi dagli esploratori… e spesso seppellisce entrambi nello stesso modo.")
    stampa("Ora una nave attende i tuoi ordini.")
    stampa("E oltre le onde ti aspetta un mondo che non sa ancora il tuo nome.")
    spazio()
 
def menu():
    cprint(figlet_format("NUOVO MONDO"), "blue")
    cprint("1 - INIZIA UN NUOVO VIAGGIO", "cyan")
    cprint("2 - RICORDA UNA VECCHIA AVVENTURA", "cyan")
    cprint("3 - CALA L'ANCORA", "cyan")
 
def scelta():

    errore = True
    while errore:
        try:
            azione = int(input())
            if azione < 0 or azione > 3:
                raise Exception
            else:
                errore = False
        except:

            cprint("ROTTA SCONOSCIUTA", "red")
 
    os.system("cls")
    return azione
 
