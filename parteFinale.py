import json
from random import choice, randint, shuffle
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
def Tradimento(merci,  equipaggio, albatro_avvistato, albatro_ucciso):
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
                        if albatro_avvistato and albatro_ucciso:
                            gameOver_now = True
                        elif albatro_avvistato and not albatro_ucciso:
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
                        if albatro_avvistato and albatro_ucciso:
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
def Epilogo(equipaggio, provviste, merci, viaggio, albatro_avvistato, albatro_ucciso, costo_equipaggio_iniziale, costo_merci_iniziali, costo_provviste_iniziali):
    print("""Prima di ripartire il capo tribù rifornisce il giocatore di scorte che bastano a coprire 3 settimane di 
viaggio.
Il ritorno non è in patria, ma verso l’isola civilizzata più vicina, nella quale si 
potranno rivendere le merci acquistate nel nuovo mondo. 
""")
    #aggiunta provviste *3 settimane di viaggio per membro
    membri_TOT = 0  
    for membro in equipaggio.keys():
        membri_TOT += equipaggio[membro]["numero"]

    for cibo in provviste.keys():
        provviste[cibo]["numero"] += (provviste[cibo]["consumo"]*3)*membri_TOT

    #calcolo tempo di durata viaggio ritorno
    if equipaggio["navigatore"]["numero"] > 0:
        if albatro_avvistato and albatro_ucciso:
            print("Il viaggio di ritorno durerà 2 settimane invece che 1 perché hai ucciso un albatro.")
            viaggio["settimane totali"] += 2
        else:
            print("Il viaggio di ritorno durerà 1 settimana.")
            viaggio["settimane totali"] += 1
    elif equipaggio["navigatore"]["numero"] < 1:
        if albatro_avvistato and albatro_ucciso:
            print("Il viaggio di ritorno durerà 3 settimane invece che 1 perché hai ucciso un albatro e non hai più navigatori sulla nave.")
            viaggio["settimane totali"] += 3
        else:
            print("Il viaggio di ritorno durerà 2 settimana invece che 1 perché non hai navigatori sulla nave.")
            viaggio["settimane totali"] += 2


    #valori delle merci prima e ora
    monete_iniziali = 2000
    merci["perle"]["prezzo"] *= choice([0.5, 1, 2])
    merci["manufatti"]["prezzo"] *= choice([0.5, 1, 2])
    merci["spezie"]["prezzo"] *= choice([0.5, 1, 2]) 
    print(f"""Finalmente arrivati, c'è la possibilità di fare degli scambi delle merci ma prima vediamo il nuovo valore delle merci con le variazioni del tempo (1/2, 1, 2):
valori di prima:
-perle --> 2 monete d'oro;
-manufatti --> 2 monete d'oro;
-spezie --> 1 moneta d'oro.

valori di ora:
-perle --> {merci["perle"]["prezzo"]} monete d'oro;
-manufatti --> {merci["manufatti"]["prezzo"]} monete d'oro;
-spezie --> {merci["spezie"]["prezzo"]} monete d'oro.""")
    
    # calcolo dei profitti
    profitto = (
        merci["perle"]["numero"] * merci["perle"]["prezzo"] +
        merci["manufatti"]["numero"] * merci["manufatti"]["prezzo"] +
        merci["spezie"]["numero"] * merci["spezie"]["prezzo"]
    )
    monete_iniziali -= costo_merci_iniziali + costo_provviste_iniziali
    monete_residue = profitto + monete_iniziali
    costo_equipaggio_finale = costo_equipaggio_iniziale * viaggio["settimane totali"]

    print(f"""ora ti diamo il valore di tutto quello che hai:
-profitto --> {profitto};
-monete iniziali dopo l'acquisto delle provviste e delle merci --> {monete_iniziali};
-monete residue --> {monete_residue}
-monete che si devono ai membri dell'equipaggio dopo il viaggio --> {costo_equipaggio_finale}.""")

    if monete_residue > costo_equipaggio_finale:
        print("Le tue monete sono abbastanza per pagare l'equipaggio!")
        print("Il viaggio da ora e finito")
        return False #PD QUI SAREBBE GAME OVER POI VEDI TU

    print("Le tue monete non sono abbastanza per pagare l'equipaggio! Però puoi accettare di mettere all'asta la tua nave, così da provare a salvarti!")
    scelta = input("Vuoi accettare? (s/n)>> ").strip().lower()
    errore = True
    while errore:
        if scelta == "n":
            print("Hai rifiutato l'asta. Non puoi pagare l'equipaggio. Il gioco finisce in negativo.")
            return False
        elif scelta == "s":
            errore = False
        else:
            print("devi inserire un valore valido")

    lista_offerte1 = [50, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 1200]
    shuffle(lista_offerte1)
    lista_offerte2 = [50, 300, 400, 450]
    shuffle(lista_offerte2)

    indice = 0
    errore = True
    while errore:
        if indice < 2:
            if indice < len(lista_offerte1):
                offerta = lista_offerte1[indice]
            else:
                offerta = lista_offerte2[indice - 2]
        else:
            offerta = lista_offerte2[(indice - 2) % len(lista_offerte2)]

        print(f"Questo è il valore offerto per la nave: {offerta} monete")
        scelta2 = input("Vuoi accettare? (s/n)>> ").strip().lower()

        if scelta2 == "s":
            if offerta > costo_equipaggio_finale:
                avanzo = offerta - costo_equipaggio_finale
                print(f"Positivo: sei riuscito a pagare l'equipaggio e ti restano {avanzo} monete.")
                esito = "positivo"
            elif offerta == costo_equipaggio_finale:
                print("Nullo: sei riuscito a pagare l'equipaggio ma non ti resta nulla.")
                esito = "nullo"
            else:
                print("Negativo: l'offerta non è sufficiente a pagare l'equipaggio.")
                esito = "negativo"
            return {
                "profitto": profitto,
                "monete_finali": offerta,
                "costo_equipaggio": costo_equipaggio_finale,
                "esito": esito,
                "asta": True,
                "offerta": offerta
            }

        if scelta2 == "n":
            print("Hai rifiutato l'offerta. Passiamo a quella successiva.")
        else:
            print("Devi scegliere una delle 2 opzioni")

        indice = indice + 1



#carica e salva
def Salva(equipaggio, provviste, merci, viaggio):
    dati_da_salvare = {
        "equipaggio": equipaggio,
        "provviste": provviste,
        "merci": merci,
        "viaggio": viaggio
    }
    with open("Salvataggi.txt", "w", encoding="utf-8") as file:
        json.dump(dati_da_salvare, file)
    return True


def Carica():
    with open("Salvataggi.txt", "r", encoding="utf-8") as file:
        dati = json.load(file)
    return dati["equipaggio"], dati["provviste"], dati["merci"], dati["viaggio"]