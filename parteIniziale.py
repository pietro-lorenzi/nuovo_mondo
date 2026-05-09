def ingaggia_eq():
    eq = {
        "marinaio": 0,
        "meccanico": 0,
        "medico": 0,
        "cuoco": 0,
        "navigatore": 0
    }

    massimo=False
    while not massimo:
        marinaio=0
        while marinaio<1:
            try:
                marinaio=int(input("Quanti marinai vuoi portare con te, capitano?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        meccanico=0
        while meccanico<1:
            try:
                meccanico=int(input("Quanti meccanici vuoi portare con te, capitano?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        medico=0
        while medico<1:
            try:
                medico=int(input("Quanti medici vuoi prtare con te, capitano?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        cuoco=0
        while cuoco<1:
            try:
                cuoco=int(input("Quanti cuochi vuoi prtare, capitano?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))     
        
        navigatore=0
        while navigatore<1:
            try:
                navigatore=int(input("Quanti navigatori vuoi portare con te, capitano?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
        
        tot=marinaio+meccanico+medico+cuoco+navigatore

        if tot > 16:
            print("\033[91m" + "La nave non può reggere così tante anime, capitano. Sedici è il limite. Riprova" + "\033[0m")
        else:
            eq["marinaio"] = marinaio       
            eq["cuoco"] = cuoco
            eq["meccanico"] = meccanico
            eq["medico"] = medico
            eq["navigatore"] = navigatore
            massimo=True
    return eq

def provviste_eq():
    provviste= {
        "verdura": 0,
        "frutta": 0,
        "carne": 0,
        "acqua": 0,
    }

    spesa=False
    while not spesa:
        monete=2000

        verdura = None 
        while verdura == None:
            try:
                verdura=int(input("Quanta verdura carichi sulla nave, capitano?"))
                if verdura < 0:
                    raise Exception # Ho messo che se il valore che inserisci è negativo e quindi minore di 0, il programma lancia l'eccezione, dà il messaggio di errore e rifà la domanda
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
        
        frutta = None
        while frutta == None:
            try:
                frutta=int(input("E la frutta? Senza, lo scorbuto vi attende. "))
                if frutta < 0:
                    raise Exception
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        carne = None
        while carne == None:
            try:
                carne=int(input("Quanta carne porti con te? Gli uomini hanno fame. "))
                if carne < 0:
                    raise Exception
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        acqua = None
        while acqua == None:
            try:
                acqua=int(input("E l'acqua? Senza, morirete prima ancora di arrivare. "))
                if acqua < 0:
                    raise Exception
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
        
        costo_verdura=verdura*0.5
        monete=monete-costo_verdura
        costo_frutta=frutta*1
        monete=monete-costo_frutta
        costo_carne=carne*2
        monete=monete-costo_carne
        costo_acqua=acqua*0.5
        monete=monete-costo_acqua
        
        if monete < 0:
            print("\033[91m" + "Hai speso troppo, capitano. Riprova" + "\033[0m")
        
        else:
            provviste["acqua"] = acqua      
            provviste["carne"] = carne
            provviste["frutta"] = frutta
            provviste["verdura"] = verdura
            spesa=True
    return provviste, monete


def merci_eq(dobloni):
    merci = {
        "medicinale": 0,
        "armi": 0,
        "sale": 0,
        "stoffa": 0,
        "coltelli": 0,
        "diamanti": 0,
    }

    spesa = False
    while not spesa:
            
            monete=dobloni 
   
            medicinali = None
            while medicinali == None:
                try:
                    medicinali=int(input("Quante bottiglie di medicinale carichi? La malattia non avvisa. "))
                    if medicinali < 0: 
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
                
            armi = None
            while armi == None:
                try:
                    armi=int(input("Quante armi porti? Il mare non è l'unico pericolo. "))
                    if armi < 0:
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
                
            sale = None
            while sale == None:
                try:
                    sale=int(input("Quanto sale vuoi?"))
                    if sale < 0:
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            stoffa = None
            while stoffa == None:
                try:
                    stoffa=int(input("Quanti teli di stoffa? Gli indigeni ne vanno matti. "))
                    if stoffa < 0:
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
                
            coltelli = None
            while coltelli == None:
                try:
                    coltelli=int(input("I coltelli sono ottimi per barattare. Quanti ne porti?"))
                    if coltelli < 0:
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
                
            diamanti = None
            while diamanti == None:
                try:
                    diamanti=int(input("E i diamanti? Brillano quanto le opportunità che ti aspettano. "))
                    if diamanti < 0:
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   

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
            
            if monete<0:
             print("\033[91m" + "Hai speso troppo, capitano. Riprova" + "\033[0m")

            else:
                merci["armi"] = armi
                merci["coltelli"] = coltelli
                merci["diamanti"] = diamanti
                merci["medicinale"] = medicinali
                merci["sale"] = sale
                merci["stoffa"] = stoffa
                spesa = True
    return merci, monete

def introduzione():
   print("\033[94m" + "Per secoli, l'oceano a occidente e' rimasto una distesa sconosciuta." + "\033[0m")
   print("\033[94m" + "Le mappe finiscono molto prima di quelle acque, come se il mondo stesso avesse paura di cio' che si trova oltre." + "\033[0m")
   print("\033[94m" + "Ora, con il vento che soffia verso l'Atlantico occidentale, una nuova spedizione e' pronta a salpare." + "\033[0m")
   print("\033[94m" + "E il mare, silenzioso come sempre, aspetta." + "\033[0m")




introduzione()
eq=ingaggia_eq()
provviste, monete_rimaste=provviste_eq()
merci, monete_rimaste=merci_eq(monete_rimaste)
