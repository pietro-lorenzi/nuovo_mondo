import json
from random import choice, randint
from  core import avvistamento_alabatro

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
    if "perle" not in merci:
        merci["perle"] = {"prezzo" : 2, "numero" : 0}
    if "manufatti" not in merci:
        merci["manufatti"] = {"prezzo" : 2, "numero" : 0}
    if "spezie" not in merci:
        merci["spezie"] = {"prezzo" : 1, "numero" : 0}
        
    print("Puoi barattare solo sale, stoffa, coltelli e diamanti.")
    for risorsa in merci.keys():
        match risorsa:

            case "sale":
                if  merci["sale"]["numero"] > 0:
                        errore = True
                        print(f"""è ora di barattare il sale, le opzioni che ti offre il capo tribù sono queste:
1) 1 perla = 0.5 sacchi di sale --> max {int(2*merci["sale"]["numero"])} perle ottenibili;
2) 1 manufatto = 0.5 sacchi di sale --> max {int(2*merci["sale"]["numero"])} manufatti ottenibili;
3) 1 barattolo di spezie = 1 sacco di sale --> max {int(1*merci["sale"]["numero"])} spezie ottenibili.

Oggetti che possiedi:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]}.

Valore degli oggetti (che possiedi):
- 1 perla = 2 monete d'oro --> {merci["perle"]["numero"]*2};
- 1 manufatto = 2 monete d'oro --> {merci["manufatti"]["numero"]*2};
- 1 barattolo di spezie = 1 moneta d'oro --> {merci["spezie"]["numero"]*1}.""")
                        while errore:
                            try:
                                scelta = int(input("Che cosa vorresti ottenere (inserisci 1, 2, 3)?>> "))
                                
                                if scelta == 1: 
                                    nome_target = "perle"
                                elif scelta == 2: 
                                    nome_target = "manufatti"
                                elif scelta == 3: 
                                    nome_target = "spezie"
                                else: 
                                    raise ValueError
                                
                                quantita = int(input(f"Quante {nome_target} vuoi ottenere?>> "))
                                
                                if quantita <= 0:
                                    print("Quantità non valida, riprova!")
                                else:
                                    match scelta:
                                        case 1:
                                            costo = quantita * 0.5
                                            if costo % 1 != 0 or costo > merci["sale"]["numero"]:
                                                print(f"Non fattibile! Ti costerebbe {costo} sacchi di sale. Devi scambiare un numero pari di perle e avere abbastanza sale.")
                                            else:
                                                costo = int(costo)
                                                print(f"Hai appena ottenuto {quantita} perle pagando {costo} sale.")
                                                merci["perle"]["numero"] += quantita
                                                merci["sale"]["numero"] -= costo
                                                errore = False
                                        case 2:
                                            costo = quantita * 0.5
                                            if costo % 1 != 0 or costo > merci["sale"]["numero"]:
                                                print(f"Non fattibile! Ti costerebbe {costo} sacchi di sale. Devi scambiare un numero pari di manufatti e avere abbastanza sale.")
                                            else:
                                                costo = int(costo)
                                                print(f"Hai appena ottenuto {quantita} manufatti pagando {costo} sale.")
                                                merci["manufatti"]["numero"] += quantita
                                                merci["sale"]["numero"] -= costo
                                                errore = False 
                                        case 3:
                                            costo = quantita * 1
                                            if costo > merci["sale"]["numero"]:
                                                print(f"Non fattibile! Ti costerebbe {costo} sacchi di sale e non ne hai abbastanza.")
                                            else:
                                                costo = int(costo)
                                                print(f"Hai appena ottenuto {quantita} spezie pagando {costo} sale.")
                                                merci["spezie"]["numero"] += quantita
                                                merci["sale"]["numero"] -= costo
                                                errore = False
                                        case _:
                                            raise ValueError
                            except:
                                print("Devi inserire un'opzione o una quantità valida!")

            case "stoffa":
                if  merci["stoffa"]["numero"] > 0:
                    errore = True
                    print(f"""è ora di barattare la stoffa, le opzioni che ti offre il capo tribù sono queste:
1) 1 perla = 5 teli di stoffa --> max {int(merci["stoffa"]["numero"]//5)} perle ottenibili;
2) 1 manufatto = 7 teli di stoffa --> max {int(merci["stoffa"]["numero"]//7)} manufatti ottenibili;
3) 1 barattolo di spezie = 3 teli di stoffa --> max {int(merci["stoffa"]["numero"]//3)} spezie ottenibili.

Oggetti che possiedi:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]}.

Valore degli oggetti (che possiedi):
- 1 perla = 2 monete d'oro --> {merci["perle"]["numero"]*2};
- 1 manufatto = 2 monete d'oro --> {merci["manufatti"]["numero"]*2};
- 1 barattolo di spezie = 1 moneta d'oro --> {merci["spezie"]["numero"]*1}.""")
                    while errore:
                            try:
                                scelta = int(input("Che cosa vorresti ottenere (inserisci 1, 2, 3)?>> "))
                                
                                if scelta == 1: 
                                    nome_target = "perle"
                                elif scelta == 2: 
                                    nome_target = "manufatti"
                                elif scelta == 3: 
                                    nome_target = "spezie"
                                else: raise ValueError
                                
                                quantita = int(input(f"Quante {nome_target} vuoi ottenere?>> "))
                                
                                if quantita <= 0:
                                    print("Quantità non valida, riprova!")
                                else:
                                    match scelta:
                                        case 1:
                                            costo = quantita * 5
                                            if costo > merci["stoffa"]["numero"]:
                                                print(f"Non hai abbastanza stoffa! Te ne servono {costo}.")
                                            else:
                                                print(f"Hai appena ottenuto {quantita} perle pagando {costo} teli di stoffa.")
                                                merci["perle"]["numero"] += quantita
                                                merci["stoffa"]["numero"] -= costo
                                                errore = False
                                        case 2:
                                            costo = quantita * 7
                                            if costo > merci["stoffa"]["numero"]:
                                                print(f"Non hai abbastanza stoffa! Te ne servono {costo}.")
                                            else:
                                                print(f"Hai appena ottenuto {quantita} manufatti pagando {costo} teli di stoffa.")
                                                merci["manufatti"]["numero"] += quantita
                                                merci["stoffa"]["numero"] -= costo
                                                errore = False 
                                        case 3:
                                            costo = quantita * 3
                                            if costo > merci["stoffa"]["numero"]:
                                                print(f"Non hai abbastanza stoffa! Te ne servono {costo}.")
                                            else:
                                                print(f"Hai appena ottenuto {quantita} spezie pagando {costo} teli di stoffa.")
                                                merci["spezie"]["numero"] += quantita
                                                merci["stoffa"]["numero"] -= costo
                                                errore = False
                                        case _:
                                            raise ValueError
                            except:
                                print("Devi inserire un'opzione o una quantità valida!")
                

            case "coltelli":
                if  merci["coltelli"]["numero"] > 0:
                    errore = True
                    print(f"""è ora di barattare i coltelli, le opzioni che ti offre il capo tribù sono queste:
1) 1 perla = 1 coltello --> max {int(merci["coltelli"]["numero"]//1)} perle ottenibili;
2) 1 manufatto = 3 coltelli --> max {int(merci["coltelli"]["numero"]//3)} manufatti ottenibili;
3) 1 barattolo di spezie = 6 coltelli --> max {int(merci["coltelli"]["numero"]//6)} spezie ottenibili.

Oggetti che possiedi:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]}.

Valore degli oggetti (che possiedi):
- 1 perla = 2 monete d'oro --> {merci["perle"]["numero"]*2};
- 1 manufatto = 2 monete d'oro --> {merci["manufatti"]["numero"]*2};
- 1 barattolo di spezie = 1 moneta d'oro --> {merci["spezie"]["numero"]*1}.""")
                    while errore:
                            try:
                                scelta = int(input("Che cosa vorresti ottenere (inserisci 1, 2, 3)?>> "))
                                
                                if scelta == 1: 
                                    nome_target = "perle"
                                elif scelta == 2: 
                                    nome_target = "manufatti"
                                elif scelta == 3: 
                                    nome_target = "spezie"
                                else: raise ValueError
                                
                                quantita = int(input(f"Quante {nome_target} vuoi ottenere?>> "))
                                
                                if quantita <= 0:
                                    print("Quantità non valida, riprova!")
                                else:
                                    match scelta:
                                        case 1:
                                            costo = quantita * 1
                                            if costo > merci["coltelli"]["numero"]:
                                                print(f"Non hai abbastanza coltelli! Te ne servono {costo}.")
                                            else:
                                                print(f"Hai appena ottenuto {quantita} perle pagando {costo} coltelli.")
                                                merci["perle"]["numero"] += quantita
                                                merci["coltelli"]["numero"] -= costo
                                                errore = False
                                        case 2:
                                            costo = quantita * 3
                                            if costo > merci["coltelli"]["numero"]:
                                                print(f"Non hai abbastanza coltelli! Te ne servono {costo}.")
                                            else:
                                                print(f"Hai appena ottenuto {quantita} manufatti pagando {costo} coltelli.")
                                                merci["manufatti"]["numero"] += quantita
                                                merci["coltelli"]["numero"] -= costo
                                                errore = False 
                                        case 3:
                                            costo = quantita * 6
                                            if costo > merci["coltelli"]["numero"]:
                                                print(f"Non hai abbastanza coltelli! Te ne servono {costo}.")
                                            else:
                                                print(f"Hai appena ottenuto {quantita} spezie pagando {costo} coltelli.")
                                                merci["spezie"]["numero"] += quantita
                                                merci["coltelli"]["numero"] -= costo
                                                errore = False
                                        case _:
                                            raise ValueError
                            except:
                                print("Devi inserire un'opzione o una quantità valida!")

            case "diamanti":
                if  merci["diamanti"]["numero"] > 0:
                    errore = True
                    print(f"""è ora di barattare i diamanti, le opzioni che ti offre il capo tribù sono queste:
1) 1 perla = 2 diamanti --> max {int(merci["diamanti"]["numero"]//2)} perle ottenibili;
2) 1 manufatto = 4 diamanti --> max {int(merci["diamanti"]["numero"]//4)} manufatti ottenibili;
3) 1 barattolo di spezie = 4 diamanti --> max {int(merci["diamanti"]["numero"]//4)} spezie ottenibili.

Oggetti che possiedi:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]}.

Valore degli oggetti (che possiedi):
- 1 perla = 2 monete d'oro --> {merci["perle"]["numero"]*2};
- 1 manufatto = 2 monete d'oro --> {merci["manufatti"]["numero"]*2};
- 1 barattolo di spezie = 1 moneta d'oro --> {merci["spezie"]["numero"]*1}.""")
                    while errore:
                            try:
                                scelta = int(input("Che cosa vorresti ottenere (inserisci 1, 2, 3)?>> "))

                                if scelta == 1: 
                                    nome_target = "perle"
                                elif scelta == 2: 
                                    nome_target = "manufatti"
                                elif scelta == 3: 
                                    nome_target = "spezie"
                                else: raise ValueError
                                
                                quantita = int(input(f"Quante {nome_target} vuoi ottenere?>> "))
                                
                                if quantita <= 0:
                                    print("Quantità non valida, riprova!")
                                else:
                                    match scelta:
                                        case 1:
                                            costo = quantita * 2
                                            if costo > merci["diamanti"]["numero"]:
                                                print(f"Non hai abbastanza diamanti! Te ne servono {costo}.")
                                            else:
                                                print(f"Hai appena ottenuto {quantita} perle pagando {costo} diamanti.")
                                                merci["perle"]["numero"] += quantita
                                                merci["diamanti"]["numero"] -= costo
                                                errore = False
                                        case 2:
                                            costo = quantita * 4
                                            if costo > merci["diamanti"]["numero"]:
                                                print(f"Non hai abbastanza diamanti! Te ne servono {costo}.")
                                            else:
                                                print(f"Hai appena ottenuto {quantita} manufatti pagando {costo} diamanti.")
                                                merci["manufatti"]["numero"] += quantita
                                                merci["diamanti"]["numero"] -= costo
                                                errore = False 
                                        case 3:
                                            costo = quantita * 4
                                            if costo > merci["diamanti"]["numero"]:
                                                print(f"Non hai abbastanza diamanti! Te ne servono {costo}.")
                                            else:
                                                print(f"Hai appena ottenuto {quantita} spezie pagando {costo} diamanti.")
                                                merci["spezie"]["numero"] += quantita
                                                merci["diamanti"]["numero"] -= costo
                                                errore = False
                                        case _:
                                            raise ValueError
                            except:
                                print("Devi inserire un'opzione o una quantità valida!")

    print(f"""
Oggetti che possiedi,  dopo lo scambio:
- Sale --> {merci["sale"]["numero"]};
- Stoffa --> {merci["stoffa"]["numero"]};
- Coltelli --> {merci["coltelli"]["numero"]};
- Diamanti --> {merci["diamanti"]["numero"]};
- Perle --> {merci["perle"]["numero"]};
- Manufatti --> {merci["manufatti"]["numero"]};
- Spezie --> {merci["spezie"]["numero"]}.
""")
    if merci["sale"]["numero"] == 0 and merci["stoffa"]["numero"] == 0 and merci["coltelli"]["numero"] == 0 and merci["diamanti"]["numero"] == 0:
        print("Non hai risorse scambiabili in questo momento, quindi non puoi barattare!")
        return merci 

    return merci



#Tradimento
def Tradimento(merci,  equipaggio, albatro_ucciso = avvistamento_alabatro()):
    if merci["armi"]["numero"] > 0:
        errore = True
        print(f"""Duranta la notte un traditore, con intenzioni sospette, si avvicina alla tenda, dove stai  alloggiando, proponendoti uno scambio il quale prevede lo scambio di 30 perle per ogni arma posseduta:
-perle in possesso --> {merci["perle"]["numero"]};
-numero armi in  possesso --> {merci["armi"]["numero"]};
-numero di perle in caso di scambio --> {(merci["armi"]["numero"]*30)+merci["perle"]["numero"]}.""")
        while errore:
            try:
                AccettaOfferta = input("Vuoi accettare l'offerta del traditore? (s/n)>> ")

                match AccettaOfferta:
                    case "s":
                        #caricamento merci scambiate sulla nave
                        merci["perle"]["numero"] += merci["armi"]["numero"]*30
                        merci["armi"]["numero"] = 0

                        #gestione probabilità di fuga
                        if albatro_ucciso:
                            gameOver_now = True
                        elif not albatro_ucciso:
                            gameOver_now = False
                        else:
                            gameOver_now = choice([True, False])

                        if gameOver_now:
                            print("Il capo tribù è venuto a conoscenza dello scambio che hai effettuato con il traditore e ha ucciso l'intero equipaggio.")
                            for membro in equipaggio.keys():
                                equipaggio[membro]["numero"] = 0

                            errore = False
                            return equipaggio, merci #Qui PD ho azzerato tutti i personaggi dell'equipaggio, perché non so come chiudere il gioco, poi vedi tu, perché qui è GAME OVER
                        else:
                            print("Il capo tribù non è venuto a conoscenza dello scambio che hai effettuato con il traditore, quindi la ciurma è salva.")
                            errore = False
                            return equipaggio, merci
                    case "n":
                        if albatro_ucciso:
                            numPerleOfferte = randint(5, 20)
                        else:
                            numPerleOfferte = randint(30, 50)
                        print(f"Il capo tribù è venuto a conoscenza dello scambio che non hai effettuato con il traditore e ti ha offerto {numPerleOfferte} perle.")
                        merci["perle"]["numero"] += numPerleOfferte
                        errore = False
                        return equipaggio, merci
                    case _:
                        print("Devi inserire una delle 2 opzioni precedenti!")
            except:
                print("Devi inserire una delle 2 opzioni precedenti!")
    else:
        return equipaggio, merci
    

#Epilogo
def Epilogo():
    pass