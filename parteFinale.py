import json
#la nave si avvicina alle coste 

#RichiestaFuoco
def RichiestaFuoco(merci):
    errore = True
    if merci["armi"]["numero"] > 0: 
        while errore:
            try:
                richiestaFuoco = input("Vuoi fare fuoco contro gli indigeni? (s/n)>> ")

                match richiestaFuoco:
                    case "s":
                        return True
                    case "n":
                        return False
                    case _:
                        print("Devi inserire una delle 2 opzioni precedenti!")
            except:
                print("Devi inserire una delle 2 opzioni precedenti!")

    else:
        return False        
    

#Baratto
def Baratto(merci):
    merci["perle"] = {"prezzo" : 2, "numero" : 0}
    merci["manufatti"] = {"prezzo" : 2, "numero" : 0}
    merci["spezie"] = {"prezzo" : 1, "numero" : 0}
    PmoneteGuadagnate = 0
    print("Puoi barattare solo sale, stoffa, coltelli e diamanti.")
    for risorsa in merci.keys():
        match risorsa:

            case "sale":
                if  merci["sale"]["numero"] > 0:
                        errore = True
                        print(f"""è ora di barattare il sale, le opzioni che ti offre il capo tribù sono queste:
1) 1 perla = 0.5 sacchi di sale --> {2*merci["sale"]["numero"]};
2) 1 manufatto = 0.5 sacchi di sale --> {2*merci["sale"]["numero"]};
3) 1 barattolo di spezie = 1 sacco di sale --> {1*merci["sale"]["numero"]}.

Oggetti che possiedi:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]};
- Possibili  monete guadagnate (al rientro con gli scambi) --> {PmoneteGuadagnate}.

Valore degli oggetti (che possiedi):
- 1 perla = 2 monete d'oro --> {merci["perle"]["numero"]*2};
- 1 manufatto = 2 monete d'oro --> {merci["manufatti"]["numero"]*2};
- 1 barattolo di spezie = 1 moneta d'oro --> {merci["spezie"]["numero"]*1}.""")
                        while errore:
                            try:
                                scelta = int(input("Che cosa vorresti scambiare?>> "))

                                match scelta:
                                    case 1:
                                        print("Hai appena concluso lo scambio del sale.")
                                        merci["perle"]["numero"] += (merci["sale"]["numero"]*2)
                                        merci["sale"]["numero"] -= merci["sale"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False
                                    case 2:
                                        print("Hai appena concluso lo scambio del sale.")
                                        merci["manufatti"]["numero"] += (merci["sale"]["numero"]*2)
                                        merci["sale"]["numero"] -= merci["sale"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False 
                                    case 3:
                                        print("Hai appena concluso lo scambio del sale.")
                                        merci["spezie"]["numero"] += (merci["sale"]["numero"]*1)
                                        merci["sale"]["numero"] -= merci["sale"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False
                                    case _:
                                        raise
                            except:
                                print("Devi inserire un opzione valida!")

            case "stoffa":
                if  merci["stoffa"]["numero"] > 0:
                    errore = True
                    print(f"""è ora di barattare la stoffa, le opzioni che ti offre il capo tribù sono queste:
1) 1 perla = 5 teli di stoffa --> {0.2*merci["stoffa"]["numero"]};
2) 1 manufatto = 7 teli di stoffa --> {0.1*merci["stoffa"]["numero"]};
3) 1 barattolo di spezie = 3 teli di stoffa --> {0.3*merci["stoffa"]["numero"]}.

Oggetti che possiedi:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]};
- Possibili  monete guadagnate (al rientro con gli scambi) --> {PmoneteGuadagnate}.

Valore degli oggetti (che possiedi):
- 1 perla = 2 monete d'oro --> {merci["perle"]["numero"]*2};
- 1 manufatto = 2 monete d'oro --> {merci["manufatti"]["numero"]*2};
- 1 barattolo di spezie = 1 moneta d'oro --> {merci["spezie"]["numero"]*1}.""")
                    while errore:
                            try:
                                scelta = int(input("Che cosa vorresti scambiare?>> "))

                                match scelta:
                                    case 1:
                                        print("Hai appena concluso lo scambio della stoffa.")
                                        merci["perle"]["numero"] += (merci["sale"]["numero"]*2)
                                        merci["sale"]["numero"] -= merci["sale"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False
                                    case 2:
                                        print("Hai appena concluso lo scambio del stoffa.")
                                        merci["manufatti"]["numero"] += (0.2*merci["stoffa"]["numero"])
                                        merci["stoffa"]["numero"] -= merci["stoffa"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False 
                                    case 3:
                                        print("Hai appena concluso lo scambio del stoffa.")
                                        merci["spezie"]["numero"] += (0.3*merci["stoffa"]["numero"])
                                        merci["stoffa"]["numero"] -= merci["stoffa"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False
                                    case _:
                                        raise
                            except:
                                print("Devi inserire un opzione valida!")
                

            case "coltelli":
                if  merci["coltelli"]["numero"] > 0:
                    errore = True
                    print(f"""è ora di barattare i coltelli, le opzioni che ti offre il capo tribù sono queste:
1) 1 perla = 1 coltello --> {1*merci["coltelli"]["numero"]};
2) 1 manufatto = 3 coltelli --> {0.3*merci["coltelli"]["numero"]};
3) 1 barattolo di spezie = 6 coltelli --> {0.2*merci["coltelli"]["numero"]}.

Oggetti che possiedi:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]};
- Possibili  monete guadagnate (al rientro con gli scambi) --> {PmoneteGuadagnate}.

Valore degli oggetti (che possiedi):
- 1 perla = 2 monete d'oro --> {merci["perle"]["numero"]*2};
- 1 manufatto = 2 monete d'oro --> {merci["manufatti"]["numero"]*2};
- 1 barattolo di spezie = 1 moneta d'oro --> {merci["spezie"]["numero"]*1}.""")
                    while errore:
                            try:
                                scelta = int(input("Che cosa vorresti scambiare?>> "))

                                match scelta:
                                    case 1:
                                        print("Hai appena concluso lo scambio dei coltelli.")
                                        merci["perle"]["numero"] += (1*merci["coltelli"]["numero"])
                                        merci["coltelli"]["numero"] -= merci["coltelli"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False
                                    case 2:
                                        print("Hai appena concluso lo scambio dei coltelli.")
                                        merci["manufatti"]["numero"] += (0.3*merci["coltelli"]["numero"])
                                        merci["coltelli"]["numero"] -= merci["coltelli"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False 
                                    case 3:
                                        print("Hai appena concluso lo scambio dei coltelli.")
                                        merci["spezie"]["numero"] += (0.2*merci["coltelli"]["numero"])
                                        merci["coltelli"]["numero"] -= merci["coltelli"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False
                                    case _:
                                        raise
                            except:
                                print("Devi inserire un opzione valida!")

            case "diamanti":
                if  merci["diamanti"]["numero"] > 0:
                    errore = True
                    print(f"""è ora di barattare i diamanti, le opzioni che ti offre il capo tribù sono queste:
1) 1 perla = 2 diamanti --> {0.5*merci["diamanti"]["numero"]};
2) 1 manufatto = 4 diamanti --> {0.2*merci["diamanti"]["numero"]};
3) 1 barattolo di spezie = 4 diamanti --> {0.2*merci["diamanti"]["numero"]}.

Oggetti che possiedi:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]};
- Possibili  monete guadagnate (al rientro con gli scambi) --> {PmoneteGuadagnate}.

Valore degli oggetti (che possiedi):
- 1 perla = 2 monete d'oro --> {merci["perle"]["numero"]*2};
- 1 manufatto = 2 monete d'oro --> {merci["manufatti"]["numero"]*2};
- 1 barattolo di spezie = 1 moneta d'oro --> {merci["spezie"]["numero"]*1}.""")
                    while errore:
                            try:
                                scelta = int(input("Che cosa vorresti scambiare?>> "))

                                match scelta:
                                    case 1:
                                        print("Hai appena concluso lo scambio dei diamanti.")
                                        merci["perle"]["numero"] += (0.5*merci["diamanti"]["numero"])
                                        merci["coltelli"]["numero"] -= merci["coltelli"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False
                                    case 2:
                                        print("Hai appena concluso lo scambio dei diamanti.")
                                        merci["manufatti"]["numero"] += (0.2*merci["diamanti"]["numero"])
                                        merci["coltelli"]["numero"] -= merci["coltelli"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False 
                                    case 3:
                                        print("Hai appena concluso lo scambio dei diamanti.")
                                        merci["spezie"]["numero"] += (0.2*merci["diamanti"]["numero"])
                                        merci["coltelli"]["numero"] -= merci["coltelli"]["numero"]
                                        PmoneteGuadagnate = sum((merci["perle"]["numero"]*2), (merci["manufatti"]["numero"]*2), (merci["spezie"]["numero"]*1))
                                        errore = False
                                    case _:
                                        raise
                            except:
                                print("Devi inserire un opzione valida!")

        print(f"""
Oggetti che possiedi,  dopo lo scambio:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]};
- Possibili  monete guadagnate (al rientro con gli scambi) --> {PmoneteGuadagnate}.
""")
    if merci["sale"]["numero"] == 0 and merci["stoffa"]["numero"] == 0 and merci["coltelli"]["numero"] == 0 and merci["diamanti"]["numero"] == 0:
        print("Non hai risore scambiabili in questo momento, quindi non puoi barattare!")
        return merci 

    return merci 