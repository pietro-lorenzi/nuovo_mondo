# Ho sistemato alcune cose perché mi serviva urgentemente andare avanti visto che domani non riesco a lavorare
# La tua parte è praticamente finita, vedi tu se vuoi ritoccare qualcosina

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
                marinaio=int(input("\033[93m" + "quanti marinai vuoi?" + "\033[0m"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        meccanico=0
        while meccanico<1:
            try:
                meccanico=int(input("quanti meccanici vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        medico=0
        while medico<1:
            try:
                medico=int(input("quanti medici vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        cuoco=0
        while cuoco<1:
            try:
                cuoco=int(input("quanti cuochi vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))     
        
        navigatore=0
        while navigatore<1:
            try:
                navigatore=int(input("quanti navigatori vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
        
        tot=marinaio+meccanico+medico+cuoco+navigatore

        if tot > 16:
            print("\033[91m" + "hai superato il numero massimo di equipaggio" + "\033[0m")
        else:
            eq["marinaio"] = marinaio       # Ho aggiunto questa parte perché sennò il dizionario che mi restituivi era sempre vuoto
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

        verdura = None # Ho messo sta roba del None perché sennò se inserisci un valore sbagliato (esempio: 2.3) ti dice che il valore non va bene ma non te lo richiede, va avanti lo stesso. così invece continua a richiedertelo finché non lo metti giusto
        while verdura == None:
            try:
                verdura=int(input("quanta verdura vuoi?"))
                if verdura < 0:
                    raise Exception # Ho messo che se il valore che inserisci è negativo e quindi minore di 0, il programma lancia l'eccezione, dà il messaggio di errore e rifà la domanda
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
        
        frutta = None
        while frutta == None:
            try:
                frutta=int(input("quanta frutta vuoi?"))
                if frutta < 0:
                    raise Exception
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        carne = None
        while carne == None:
            try:
                carne=int(input("quanta carne vuoi?"))
                if carne < 0:
                    raise Exception
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        
        acqua = None
        while acqua == None:
            try:
                acqua=int(input("quanti barili di acqua vuoi?"))
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
            print("\033[91m" + "sei andato in bancarotta" + "\033[0m")
        
        else:
            provviste["acqua"] = acqua      # Stesso discorso di prima
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
            monete=dobloni # Monete non può essere ancora uguale a 2000 perché prima hai già comprato provviste, quindi lo mettiamo come argomento
   
            medicinali = None # Stesso discorso di provviste
            while medicinali == None:
                try:
                    medicinali=int(input("quanti medicinali vuoi?"))
                    if medicinali < 0: # Uguale a provviste
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
                
            armi = None
            while armi == None:
                try:
                    armi=int(input("quante armi vuoi?"))
                    if armi < 0:
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
                
            sale = None
            while sale == None:
                try:
                    sale=int(input("quanto sale vuoi?"))
                    if sale < 0:
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            stoffa = None
            while stoffa == None:
                try:
                    stoffa=int(input("quanta stoffa vuoi?"))
                    if stoffa < 0:
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
                
            coltelli = None
            while coltelli == None:
                try:
                    coltelli=int(input("quanti coltelli vuoi?"))
                    if coltelli < 0:
                        raise Exception
                except:
                    print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
                
            diamanti = None
            while diamanti == None:
                try:
                    diamanti=int(input("quanti diamanti vuoi?"))
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
            
            if monete < 0:
                print("\033[91m" + "sei andato in bancarotta" + "\033[0m")
            else:
                merci["armi"] = armi
                merci["coltelli"] = coltelli
                merci["diamanti"] = diamanti
                merci["medicinale"] = medicinali
                merci["sale"] = sale
                merci["stoffa"] = stoffa
                spesa = True

    return merci, monete