import json
from random import choice, randint, shuffle
from core import avvistamento_alabatro
from altreFunzioni import *
from time import sleep
from termcolor import colored

#RichiestaFuoco
def RichiestaFuoco(merci):
    stampa("Improvvisamente, dalla cima dell'albero maestro, uno dei tuoi uomini urla 'ECCOLO! IL NUOVO MONDO! LO VEDO!'")
    stampa("Avvicinandovi, però, scorgete un particolare.")
    stampa("Ad aspettarvi non ci sono ricchezze e tesori, ma bensì un grande gruppo di indigeni, che vi scrutano con dubbio.")
    stampa("L'attenzione passa in un attimo dagli indigeni a te. I tuoi uomini aspettano indicazioni. Alcuni sono già corsi ad armarsi. Altri predicano dialogo e pace. Ma, in fondo, sanno che la decisione finale spetta al capitano. Apri il fuoco?")
    errore = True
    if merci["armi"]["numero"] > 0: 
        while errore:
            try:
                richiestaFuoco = input("").strip().lower()

                match richiestaFuoco:
                    case "s":
                        stampa("Tutta questa strada, tutte queste intemperie, per decidere di erigere il proprio impero sul sangue...")
                        stampa("Ma la decisione è stata presa.")
                        stampa("Il primo fucile caricato. Il primo grilletto premuto. E gli indigeni sentono per la prima volta il ruomore dell'Europa.")
                        stampa("Un attimo di silenzio.")
                        stampa("Poi la risposta.")
                        stampa("Le frecce arrivano prima ancora che tu possa capire cosa hai fatto.")
                        stampa("La nave non è pronta.")
                        stampa("Non lo è mai stata.")
                        stampa("Il legno si spezza.")
                        stampa("Il fuoco si spegne.")
                        stampa("E il mare osserva, immobile.")
                        stampa("Non era un incontro.")
                        stampa("Era un errore.")
                        stampa("Il Nuovo Mondo non ha accettato il vostro saluto.")
                        sleep(2)
                        stampa(colored("GAME OVER", "red"),0.1)
                        stampa("Hai scelto il sangue alle parole.")
                        stampa("Il mare non ti ha ucciso questa volta.")
                        stampa("Ci sei riuscito da solo.")
                        return True
                    case "n":
                        stampa("Resti immobile.")
                        stampa("Il dito si allontana dal grilletto.")
                        stampa("E il mare smette di sembrare un confine.")
                        stampa("SCELTA SAGGIA")
                        stampa("Non tutte le scoperte richiedono sangue.")
                        return False
                    case _:
                        stampa("Devi inserire una delle 2 opzioni precedenti!")
            except:
                stampa("Devi inserire una delle 2 opzioni precedenti!")
    else:
        return False        
    

#Baratto
def Baratto(merci):
    stampa("La nave entra nella baia senza resistenza.")
    stampa("Nessun suono. Nessun avvertimento.")
    stampa("Solo sguardi.")
    stampa("E per la prima volta… non sono sguardi ostili.")
    stampa("La gente del villaggio si raduna sulla riva.")
    stampa("Non si avvicina troppo.")
    stampa("Non si allontana.")
    stampa("Ti studiano come hai studiato loro.")
    stampa("Un uomo avanza.")
    stampa("Non ha armi visibili.")
    stampa("Non ha paura evidente.")
    stampa("Si ferma a distanza di voce.")
    stampa("Poi guarda la nave.")
    stampa("Poi guarda te.")
    stampa("Nessuna parola comprensibile.")
    stampa("Ma il significato è chiaro.")
    stampa("Non siete invasori.")
    stampa("Non siete ospiti.")
    stampa("Siete… qualcosa da definire.")
    stampa("L'uomo apre le mani.")
    stampa("Mostra oggetti. Perle, manufatti, spezie.")
    stampa("Poi aspetta.")
    stampa("Si sta fidando di te.")
    stampa("Ti dà fiducia.")
    stampa("Come te ne hai data a loro rimuovendo il dito dal grilletto.")
    stampa("E ora sta a te scegliere con cosa scambiare le merci proposte.")

    for risorsa in merci.keys():
        match risorsa:

            case "sale":
                if  merci["sale"]["numero"] > 0:
                        errore = True
                        stampa(f"""è ora di barattare il sale, le opzioni che ti offre il capo tribù sono queste:
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
                                    stampa("Quantità non valida, riprova!")
                                else:
                                    match scelta:
                                        case 1:
                                            costo = quantita * 0.5
                                            if costo % 1 != 0 or costo > merci["sale"]["numero"]:
                                                stampa(f"Non fattibile! Ti costerebbe {costo} sacchi di sale. Devi scambiare un numero pari di perle e avere abbastanza sale.")
                                            else:
                                                costo = int(costo)
                                                stampa(f"Hai appena ottenuto {quantita} perle pagando {costo} sale.")
                                                merci["perle"]["numero"] += quantita
                                                merci["sale"]["numero"] -= costo
                                                errore = False
                                        case 2:
                                            costo = quantita * 0.5
                                            if costo % 1 != 0 or costo > merci["sale"]["numero"]:
                                                stampa(f"Non fattibile! Ti costerebbe {costo} sacchi di sale. Devi scambiare un numero pari di manufatti e avere abbastanza sale.")
                                            else:
                                                costo = int(costo)
                                                stampa(f"Hai appena ottenuto {quantita} manufatti pagando {costo} sale.")
                                                merci["manufatti"]["numero"] += quantita
                                                merci["sale"]["numero"] -= costo
                                                errore = False 
                                        case 3:
                                            costo = quantita * 1
                                            if costo > merci["sale"]["numero"]:
                                                stampa(f"Non fattibile! Ti costerebbe {costo} sacchi di sale e non ne hai abbastanza.")
                                            else:
                                                costo = int(costo)
                                                stampa(f"Hai appena ottenuto {quantita} spezie pagando {costo} sale.")
                                                merci["spezie"]["numero"] += quantita
                                                merci["sale"]["numero"] -= costo
                                                errore = False
                                        case _:
                                            raise ValueError
                            except:
                                stampa("Devi inserire un'opzione o una quantità valida!")

            case "stoffa":
                if  merci["stoffa"]["numero"] > 0:
                    errore = True
                    stampa(f"""è ora di barattare la stoffa, le opzioni che ti offre il capo tribù sono queste:
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
                                    stampa("Quantità non valida, riprova!")
                                else:
                                    match scelta:
                                        case 1:
                                            costo = quantita * 5
                                            if costo > merci["stoffa"]["numero"]:
                                                stampa(f"Non hai abbastanza stoffa! Te ne servono {costo}.")
                                            else:
                                                stampa(f"Hai appena ottenuto {quantita} perle pagando {costo} teli di stoffa.")
                                                merci["perle"]["numero"] += quantita
                                                merci["stoffa"]["numero"] -= costo
                                                errore = False
                                        case 2:
                                            costo = quantita * 7
                                            if costo > merci["stoffa"]["numero"]:
                                                stampa(f"Non hai abbastanza stoffa! Te ne servono {costo}.")
                                            else:
                                                stampa(f"Hai appena ottenuto {quantita} manufatti pagando {costo} teli di stoffa.")
                                                merci["manufatti"]["numero"] += quantita
                                                merci["stoffa"]["numero"] -= costo
                                                errore = False 
                                        case 3:
                                            costo = quantita * 3
                                            if costo > merci["stoffa"]["numero"]:
                                                stampa(f"Non hai abbastanza stoffa! Te ne servono {costo}.")
                                            else:
                                                stampa(f"Hai appena ottenuto {quantita} spezie pagando {costo} teli di stoffa.")
                                                merci["spezie"]["numero"] += quantita
                                                merci["stoffa"]["numero"] -= costo
                                                errore = False
                                        case _:
                                            raise ValueError
                            except:
                                stampa("Devi inserire un'opzione o una quantità valida!")
                

            case "coltelli":
                if  merci["coltelli"]["numero"] > 0:
                    errore = True
                    stampa(f"""è ora di barattare i coltelli, le opzioni che ti offre il capo tribù sono queste:
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
                                    stampa("Quantità non valida, riprova!")
                                else:
                                    match scelta:
                                        case 1:
                                            costo = quantita * 1
                                            if costo > merci["coltelli"]["numero"]:
                                                stampa(f"Non hai abbastanza coltelli! Te ne servono {costo}.")
                                            else:
                                                stampa(f"Hai appena ottenuto {quantita} perle pagando {costo} coltelli.")
                                                merci["perle"]["numero"] += quantita
                                                merci["coltelli"]["numero"] -= costo
                                                errore = False
                                        case 2:
                                            costo = quantita * 3
                                            if costo > merci["coltelli"]["numero"]:
                                                stampa(f"Non hai abbastanza coltelli! Te ne servono {costo}.")
                                            else:
                                                stampa(f"Hai appena ottenuto {quantita} manufatti pagando {costo} coltelli.")
                                                merci["manufatti"]["numero"] += quantita
                                                merci["coltelli"]["numero"] -= costo
                                                errore = False 
                                        case 3:
                                            costo = quantita * 6
                                            if costo > merci["coltelli"]["numero"]:
                                                stampa(f"Non hai abbastanza coltelli! Te ne servono {costo}.")
                                            else:
                                                stampa(f"Hai appena ottenuto {quantita} spezie pagando {costo} coltelli.")
                                                merci["spezie"]["numero"] += quantita
                                                merci["coltelli"]["numero"] -= costo
                                                errore = False
                                        case _:
                                            raise ValueError
                            except:
                                stampa("Devi inserire un'opzione o una quantità valida!")

            case "diamanti":
                if  merci["diamanti"]["numero"] > 0:
                    errore = True
                    stampa(f"""è ora di barattare i diamanti, le opzioni che ti offre il capo tribù sono queste:
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
                                    stampa("Quantità non valida, riprova!")
                                else:
                                    match scelta:
                                        case 1:
                                            costo = quantita * 2
                                            if costo > merci["diamanti"]["numero"]:
                                                stampa(f"Non hai abbastanza diamanti! Te ne servono {costo}.")
                                            else:
                                                stampa(f"Hai appena ottenuto {quantita} perle pagando {costo} diamanti.")
                                                merci["perle"]["numero"] += quantita
                                                merci["diamanti"]["numero"] -= costo
                                                errore = False
                                        case 2:
                                            costo = quantita * 4
                                            if costo > merci["diamanti"]["numero"]:
                                                stampa(f"Non hai abbastanza diamanti! Te ne servono {costo}.")
                                            else:
                                                stampa(f"Hai appena ottenuto {quantita} manufatti pagando {costo} diamanti.")
                                                merci["manufatti"]["numero"] += quantita
                                                merci["diamanti"]["numero"] -= costo
                                                errore = False 
                                        case 3:
                                            costo = quantita * 4
                                            if costo > merci["diamanti"]["numero"]:
                                                stampa(f"Non hai abbastanza diamanti! Te ne servono {costo}.")
                                            else:
                                                stampa(f"Hai appena ottenuto {quantita} spezie pagando {costo} diamanti.")
                                                merci["spezie"]["numero"] += quantita
                                                merci["diamanti"]["numero"] -= costo
                                                errore = False
                                        case _:
                                            raise ValueError
                            except:
                                stampa("Devi inserire un'opzione o una quantità valida!")

    stampa(f"""
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
        stampa("Non hai risorse scambiabili in questo momento, quindi non puoi barattare!")
        return merci 

    return merci



#Tradimento
def tradimento(merci,  equipaggio, albatro_avvistato, albatro_ucciso):
    if merci["armi"]["numero"] > 0:
        errore = True
        stampa("La notte è diversa qui.")
        stampa("Non è come in mare.")
        stampa("Non è vuota.")
        stampa("È piena di presenze che non si vedono.")
        stampa("La nave è ferma nella baia.")
        stampa("Il villaggio dorme… o finge di dormire.")
        stampa("Solo le torce sulla riva restano accese.")
        stampa("Come occhi che non si chiudono mai del tutto.")
        stampa("Quando pensi che tutto sia finito, arriva una barca.")
        stampa("Senza rumore.")
        stampa("Senza luce.")
        stampa("Si ferma sotto il fianco della nave.")
        stampa("Un uomo sale a bordo.")
        stampa("Non è del villaggio con cui hai trattato oggi.")
        stampa("È diverso.")
        stampa("Più freddo. Più diretto.")
        stampa("Non perde tempo.")
        stampa("Mostra le perle.")
        stampa("Poi guarda le tue armi.")
        stampa("E parla poco, ma abbastanza:")
        stampa("“30 perle per ogni arma.”")
        stampa("Silenzio.")
        stampa("Nessuna spiegazione.")
        stampa("Nessuna garanzia.")
        stampa("Solo uno scambio che non dovrebbe esistere.")
        stampa("Lo sguardo dell'uomo non cambia mai.")
        stampa("Non sembra mentire.")
        stampa("Ma nemmeno dire tutta la verità.")
        stampa(f"""
        -perle in possesso --> {merci["perle"]["numero"]};
        -numero armi in  possesso --> {merci["armi"]["numero"]};
        -numero di perle in caso di scambio --> {(merci["armi"]["numero"]*30)+merci["perle"]["numero"]}.""")
        while errore:
            try:
                AccettaOfferta = input("Vuoi accettare l'offerta? (s/n)>> ")
                match AccettaOfferta:
                    case "s":
                        merci["perle"]["numero"] += merci["armi"]["numero"]*30
                        merci["armi"]["numero"] = 0
                        if albatro_avvistato and albatro_ucciso:
                            gameOver_now = True
                        elif albatro_avvistato and not albatro_ucciso:
                            gameOver_now = False
                        else:
                            gameOver_now = choice([True, False])
                        if gameOver_now:
                            stampa("Le perle pesano più di quanto dovrebbero.")
                            stampa("Ma le prendi lo stesso.")
                            stampa("L'uomo non sorride.")
                            stampa("Non serve.")
                            stampa("Si limita ad annuire… e sparisce nella notte.")
                            stampa("Il mare resta calmo.")
                            stampa("Troppo calmo.")
                            stampa("Quando il sole sorge, capisci l'errore senza bisogno di parole.")
                            stampa("Le prime urla non vengono dal mare.")
                            stampa("Vengono dalla tua nave.")
                            stampa("Non importa chi ha deciso cosa.")
                            stampa("Ora nessuno fa più domande.")
                            stampa("La tribù locale ha scoperto il tradimento.")
                            stampa("E si è vendicata sui tuoi uomini.")
                            stampa("GAME OVER")
                            stampa("Sopravvissuto grazie all'intelligenza, morto per avidità.")
                            errore = False
                            return True
                        else:
                            stampa("Il villaggio non si muove.")
                            stampa("Nessuna allerta.")
                            stampa("Nessun segnale.")
                            stampa("Il mare resta calmo.")
                            stampa("Non indifferente…")
                            stampa("solo silenzioso.")
                            stampa("Le ore passano.")
                            stampa("Nessuno viene a reclamare nulla.")
                            stampa("E per una volta…")
                            stampa("il mondo non ti chiede il prezzo di ciò che hai fatto.")
                            errore = False
                            return merci
                    case "n":
                        stampa("Il capo tribù ti osserva.")
                        stampa("Sul suo volto non passa neanche un emozione.")
                        stampa("Non è sorpreso.")
                        stampa("Non è deluso.")
                        stampa("Non prova neanche a convincerti.")
                        stampa("Ti osserva dritto negli occhi per qualche secondo, per poi voltarsi lentamente e sparire nelle ombre da cui è comparso.")
                        stampa("Sapevi di non poter tradire la tribù del baratto al villaggio.")
                        stampa("Loro si sono fidati di te.")
                        stampa("E tu hai scelto la loro fiducia sopra a qualsiasi moneta.")
                        if albatro_avvistato and albatro_ucciso:
                            numPerleOfferte = randint(5, 20)
                        else:
                            numPerleOfferte = randint(30, 50)
                        stampa("Il giorno dopo, poco prima della partenza, il capo della tribù con la quale avevi barattato si presenta e, a gesti, fa capire che è venuto a conoscenza dello scambio, e che è felice del fatto che tu non abbia accettato.")
                        stampa(f"Per sdebitarsi, ti offre {numPerleOfferte} perle.")
                        merci["perle"]["numero"] += numPerleOfferte
                        errore = False
                        return merci
                    case _:
                        stampa("Devi inserire una delle 2 opzioni precedenti!")
            except:
                stampa("Devi inserire una delle 2 opzioni precedenti!")
    else:
        return merci
    

#Epilogo
def epilogo(equipaggio, provviste, merci, viaggio, albatro_avvistato, albatro_ucciso, costo_equipaggio_iniziale, costo_merci_iniziali, costo_provviste_iniziali):
    stampa("""Prima di ripartire il capo tribù rifornisce il giocatore di scorte che bastano a coprire 3 settimane di 
viaggio.
Il ritorno non è in patria, ma verso l'isola civilizzata più vicina, nella quale si 
potranno rivendere le merci acquistate nel nuovo mondo. 
""")

    membri_TOT = 0  
    for membro in equipaggio.keys():
        membri_TOT += equipaggio[membro]["numero"]

    for cibo in provviste.keys():
        provviste[cibo]["numero"] += (provviste[cibo]["consumo"]*3)*membri_TOT

    #calcolo tempo di durata viaggio ritorno
    if equipaggio["navigatore"]["numero"] > 0:
        if albatro_avvistato and albatro_ucciso:
            stampa("Il viaggio di ritorno durerà 2 settimane.")
            viaggio["settimane totali"] += 2
        else:
            stampa("Il viaggio di ritorno durerà solo 1 settimana.")
            viaggio["settimane totali"] += 1
    elif equipaggio["navigatore"]["numero"] < 1:
        if albatro_avvistato and albatro_ucciso:
            stampa("Il viaggio di ritorno durerà 3 settimane.")
            viaggio["settimane totali"] += 3
        else:
            stampa("Il viaggio di ritorno durerà 2 settimana.")
            viaggio["settimane totali"] += 2


    #valori delle merci prima e ora
    monete_iniziali = 2000
    moltiplicatore = choice([0.5, 1, 2])
    merci["perle"]["prezzo"] *= moltiplicatore
    merci["manufatti"]["prezzo"] *= moltiplicatore
    merci["spezie"]["prezzo"] *= moltiplicatore
    stampa(f"""Finalmente arrivati, c'è la possibilità di fare degli scambi delle merci ma prima vediamo il nuovo valore delle merci con le variazioni del tempo (1/2, 1, 2):
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

    stampa(f"""Ecco qualche rapido calcolo eseguito dal contabile del villaggio:
    -profitto --> {profitto};
    -monete iniziali dopo l'acquisto delle provviste e delle merci --> {monete_iniziali};
    -monete residue --> {monete_residue}
    -monete che si devono ai membri dell'equipaggio dopo il viaggio --> {costo_equipaggio_finale}.""")

    if monete_residue > costo_equipaggio_finale:
        return 1

    stampa("Le tue monete non sono abbastanza per pagare l'equipaggio! Puoi accettare però di mettere all'asta la tua nave, così da provare a salvarti!")
    scelta = input("Vuoi accettare? (s/n)>> ").strip().lower()
    errore = True
    while errore:
        if scelta == "n":
            return 0
        elif scelta == "s":
            errore = False
        else:
            stampa("devi inserire un valore valido")

    
    lista_offerte = [50, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 1200]
    infiniti = [50, 300, 400, 450]
    estratti = []

    contatore = 1
    accetta = False
    while not accetta:
        corretto = False
        while not corretto:
            offerta = choice(lista_offerte)
            if estratti.count(offerta) < 2 or offerta in infiniti:
                corretto = True
            else:
                lista_offerte.remove(offerta)
        
        estratti.append(offerta)
        stampa(f"L'offerta numero {contatore} è {offerta}! L'accetti?")
        errore = True
        while errore:
            scelta = input("(s/n) >> ").strip().lower()
            if scelta == "s":
                if offerta + monete_residue > costo_equipaggio_finale:
                    return 2
                elif offerta + monete_residue == costo_equipaggio_finale:
                    return 3
                else:
                    return 4
            elif scelta == "n":
                stampa("Hai rifiutato l'offerta. Passiamo a quella successiva.")
                contatore += 1
                errore = False
            else:
                stampa("Devi scegliere una delle 2 opzioni!")



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