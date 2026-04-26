from altreFunzioni import *
import random as rn
from time import sleep

#TODO termcolor

# ---------- STRUTTURE DATI ----------

equipaggio = {
    "marinaio": {
        "numero": 0, #con numero intendo quanti individui di quel mestiere abbiamo
        "costo": 10
    },
    "meccanico": {
        "numero": 0,
        "costo": 15
    },
    "medico": {
        "numero": 0,
        "costo": 25
    },
    "navigatore": {
        "numero": 0,
        "costo": 20
    },
    "cuoco": {
        "numero": 0,
        "costo": 15
    }
}

provviste = {
    "verdura":{
        "costo": 0.5,     #monete al kilo
        "consumo": 0.5,   #comsumo settimanale per membro
        "numero": 0       #quanta ne abbiamo
    },
    "frutta":{
        "costo": 1,   
        "consumo": 1, 
        "numero": 0   
    },
    "carne":{
        "costo": 2,   
        "consumo": 1, 
        "numero": 0   
    },
    "acqua":{
        "costo": 0.5,   
        "consumo": 0.5, 
        "numero": 0   
    }
}

merci = {
    "medicinale":{
        "prezzo": 1,
        "numero": 0
    },
    "armi":{
        "prezzo": 5,
        "numero": 0
    },
    "sale":{
        "prezzo": 0.5,
        "numero": 0
    },
    "stoffa":{
        "prezzo": 2,
        "numero": 0
    },
    "coltelli":{
        "prezzo": 0.5,
        "numero": 0
    },
    "diamanti":{
        "prezzo": 1,
        "numero": 0
    },
}

viaggio = {
    "settimana attuale": 0,
    "settimane totali": 8,
    "morale": 100
}

# ---------- FUNZIONI CALCOLO ----------

def calcola_costo_equipaggio(): #TODO sistemare
    costo_totale = 0
    for ruolo in equipaggio:
        costo_totale += equipaggio[ruolo]["numero"] * equipaggio[ruolo]["costo"]
    return costo_totale


# --------------- EVENTI ---------------

def uomo_in_mare():
    acc = ciurma_accettabile(equipaggio)
    morto = rn.choice(acc)
    stampa("Lentamente, dall'orizzonte, un navigatore scorge un onda anomala.")
    stampa("Prima che chiunque possa reagire, l'onda si abbatte violentemente sulla nave.", 0.05)
    stampa(f"Un {morto} cade tra le fauci dell'oceano.")
    sleep(2)
    stampa("Nessuno ha più il coraggio di guardare indietro...", 0.1)

def verdura_in_mare():
    denom = rn.choice([2,3,4,5])
    perdita = provviste["verdura"]["numero"] // denom
    provviste["verdura"]["numero"] -= perdita
    stampa("In pochi minuti, il cielo si oscura.")
    stampa("Rombi e tuoni rieccheggiano in lontananza.")
    stampa(f"Le onde divorano {perdita} unità di verdura cadere in mare.")
    stampa("La fame vi attende, ", 0.05, False)
    sleep(0.5)
    stampa("inesorabilmente", 0.2)

def frutta_in_mare():
    denom = rn.choice([2,3,4,5])
    perdita = provviste["frutta"]["numero"] // denom
    provviste["frutta"]["numero"] -= perdita
    stampa("La furia del mare non conosce pietà.")
    stampa("Potente come un colpo di cannone, un onda si abbatte sullo scafo.")
    stampa(f"Dalla nave scivolano {perdita} unità di frutta.")
    stampa("Anche oggi il mare si è divorato qualcosa di tuo...")
    stampa("E il prossimo potresti", capo=False)
    stampa(" essere tu.", 0.2)

def carne_in_mare():
    denom = rn.choice([2,3,4,5])
    perdita = provviste["carne"]["numero"] // denom
    provviste["carne"]["numero"] -= perdita
    stampa("Avverti l'arrivo di una tempesta in lontananza.")
    stampa("In pochi minuti, ti ritrovi in balia delle onde.")
    stampa(f"Lentamente, {perdita} unità di carne scivolano giù dalla nave.")
    stampa("I predatori del mare ricevono un banchetto gratis.")
    stampa("E tu rimarrai a guardare.")

def acqua_in_mare():
    stampa("La furia del mare non conosce pietà.")
    denom = rn.choice([2,3,4,5])
    perdita = provviste["acqua"]["numero"] // denom
    provviste["acqua"]["numero"] -= perdita
    stampa(f"L'urto con uno scoglio non danneggia la nave, ma rovescia in mare {perdita} barili d'acqua.")
    stampa("Gli sguardi dell'equipaggio si fanno più cupi.")
    stampa("Sanno cosa significa razionare l'acqua.")
    stampa("Sanno cosa gli uomini disperati sono capaci di fare.")

def pesca_miracolosa():
    stampa("Il mare si stende davanti a voi come un grande telo blu.")
    stampa("Il silenzio è assordante, non un onda, non un gabbiano, e neanche la nave osa schricchiolare.")
    stampa("Qualcuno dice che è un buon segno, e decidete di approfittarne per pescare.")
    pesca = rn.randint(11,20)
    provviste["carne"]["numero"] += pesca
    stampa(f"Riuscite a recuperare {pesca} kili di carne. Strano...")
    stampa("Erano ammassati lì sotto...")
    stampa("Come ad aspettarvi", 0.08, capo=False)
    stampa("...", 0.5)

def tempesta_miracolosa():
    stampa("Una tempesta viene avvistata in lontananza, ma sta volta è diverso.")
    acqua = rn.randint(11,20)
    provviste["acqua"]["numero"] += acqua
    stampa("Non c'è vento a precederla. Non c'è rabbia nell'aria.")
    stampa("Poi inizia a piovere, gocce grosse, rumorose, costanti.")
    stampa(f"Ordini all'equipaggio di posizionare i barili, e raccogliete {acqua} litri di acqua.")
    stampa("Sembra quasi che il mare abbia deciso di risparmiarvi questa volta, eppure esiste un detto tra voi uomini di mare...")
    stampa("Se sopravvivi alla tempesta, non ringraziare, perché significa che ", capo=False)
    stampa("non è finita.", 0.2)

def venti_favorevoli():
    stampa("In una fredda mattina ti accorgi che dei venti favorevoli stanno spingendo la nave più velocemente.")
    stampa("L'equipaggio ne è felice, festeggia perché arriverai prima a destinazione.")
    viaggio["settimane totali"] -= 1
    viaggio["morale"] += rn.randint(5,15)
    stampa("Eppure vedi un uomo, seduto rannicchiato cupo in un angolo della cabina.")
    stampa("Gli domandi cosa c'è che non va, e perché non è a festeggiare con gli altri.")
    stampa("E lui ti risponde: ", capo=False)
    stampa("Sta andando esattamente come deve andare...", 0.1)

def cattivo_tempo():
    stampa("La nave questa notte è in balia degli elementi.")
    stampa("Onde e vento non danno pietà.")
    denom = rn.choice([2,3,4,5])
    perdita = merci["medicinale"]["numero"] // denom
    merci["medicinale"]["numero"] -= perdita
    stampa(f"Un onda più alta delle altre scaraventa per terra {perdita} bottiglie di medicinale.")
    stampa("Il medico impallidisce.")
    stampa(f"{perdita}, come le vite che avrebbe potuto salvare.")

def ondata():
    stampa("In una tranquilla serata, improvvisamente un onda si alza come una montagna vivente.")
    denom = rn.choice([2,3,4,5])
    perdita = merci["armi"]["numero"] // denom
    merci["armi"]["numero"] -= perdita
    stampa("La parete d'acqua si abbatte sulla nave.")
    stampa(f"{perdita} armi vengono scaraventate giù dal ponte.")
    stampa("L'equipaggio ora è più vulnerabile.")
    stampa("E il mare lo sa.", 0.08)

def infestazione_ratti():
    stampa("Piccoli occhi rossi risplendono nell'ombra della stiva.")
    denom = rn.choice([2,3,4,5])
    perdita = merci["stoffa"]["numero"] // denom
    merci["stoffa"]["numero"] -= perdita
    stampa(f"Un gruppo di ratti hanno divorato {perdita} rotoli di stoffa.")
    stampa("E ora vi osservano affamati.")
    stampa("I ratti hanno fame.")
    stampa("E la stoffa era l'antipasto.", 0.08)

def avvistamento_alabatro():
    if merci["armi"]["numero"] > 0:
            stampa("Durante la navigazione avvistate un alabatro!")
            stampa("Fortunatamente avete delle armi a bordo, ora potete provare a colpirlo per aumentare le scorte di carne!")
            ciurma = equipaggio["marinaio"]["numero"] + equipaggio["meccanico"]["numero"] + equipaggio["medico"]["numero"] + equipaggio["navigatore"]["numero"] + equipaggio["cuoco"]["numero"]
            tentativi = min(merci["armi"]["numero"], ciurma)
            colpito = False
            for i in range(tentativi):
                if rn.choice([True, False]):
                    colpito = True
            
            if colpito:
                carne_guadagnata = rn.randint(10, 15)
                provviste["carne"]["numero"] += carne_guadagnata
                stampa(f"Complimenti, siete riusciti a colpire l'alabatro e avete guadagnato {carne_guadagnata} unità di carne!")
                return True
            else:
                stampa("Neanche un colpo è andato a segno, l'alabatro si è allontanato e non avete guadagnato carne.")
                return False
    else:
        stampa("Durante la navigazione avvistate un alabatro, ma sfortunatamente non avete armi a bordo per provare a colpirlo")
        return False

def avvistamento_scialuppa():
    stampa("Durante la navigazione avvistate una scialuppa alla deriva!")
    stampa("A bordo ci sono 4 uomini e una cassa, ma chissà cosa potrebbe mai contenere")
    stampa("Vuoi salvare i 4 uomini?")
    errore = True
    while errore:
        scelta = input(">> ").lower().strip()
        if scelta == "si":
            for i in range(4):
                membro = rn.choice(list(equipaggio.keys()))
                equipaggio[membro]["numero"] += 1
            stampa("Decidete di salvare i 4 uomini e li accogliete a bordo, ora avete un equipaggio più numeroso!")
            for i in merci:
                merci[i]["numero"] += rn.randint(10,20)
            stampa("Inoltre, all'interno della cassa trovate delle merci preziose che aumentano le vostre scorte!")
            errore = False
        elif scelta == "no":
            stampa("Decidete di non salvare i 4 uomini e proseguite la navigazione, chissà cosa c'era nella cassa...")
            errore = False

def epidemia():
    stampa("Durante la navigazione scoppia una terribile epidemia a bordo!")
    medicine = merci["medicinale"]["numero"]
    ammalati = []
    if medicine > 0:
        stampa(f"Fortunatamente hai a disposizione {medicine} medicinali, e hai curato altrettanti membri del tuo equipaggio")
        for i in equipaggio:
            ripetizioni = equipaggio[i]["numero"]
            for x in range(ripetizioni):
                ammalati.append(i)

        for i in ammalati:
            if rn.randint(1,10) > 7:
                ammalati.remove(i)

        for i in range(medicine):
            if ammalati:
                fortunato = rn.choice(ammalati)
                ammalati.remove(fortunato)
                medicine -= 1

        for i in ammalati:
            equipaggio[i]["numero"] -= 1

        merci["medicinale"]["numero"] = medicine
    
    if ammalati:
        stampa(f"Ci sono stati {len(ammalati)} morti, che corrispondono a:")
        for i in ammalati:
            stampa(i.upper())
    else:
        stampa("Incredibile! Il medico è riuscito a curare tutti!")
    
    stampa(f"Restano {medicine} bottiglie di medicinale")

def attacco_pirata():
    stampa("Durante la navigazione siete stati attaccati dai pirati!")
    numero_pirati = rn.randint(3,10)
    ciurma = equipaggio["marinaio"]["numero"] + equipaggio["meccanico"]["numero"] + equipaggio["medico"]["numero"] + equipaggio["navigatore"]["numero"] + equipaggio["cuoco"]["numero"]
    numero_difensori = min(ciurma, merci["armi"]["numero"])
    uomini_persi = min(numero_pirati-numero_difensori, ciurma)
    if uomini_persi <= 0:
        stampa(f"I pirati erano ben {numero_pirati}, ma grazie a un equipaggio corposo e a un buon numero di armi siete riusciti a difendervi!")
    else:
        stampa(f"Sfortunatamente siete stati colti impreparati, avete perso {uomini_persi} membri!")
        stampa("I morti sono:")
        for i in range(uomini_persi):
            acc = ciurma_accettabile(equipaggio)
            morto = rn.choice(acc)
            equipaggio[morto]["numero"] -= 1
            stampa(morto)

def danni_al_timone():
    stampa("Durante la navigazione si sono verificati dei danni al timone!")
    if equipaggio["meccanico"]["numero"] > 0:
        viaggio["settimane totali"] += 1
        stampa("Fortunatamente nel tuo equipaggio è presente un meccanico, che riesce a riparare in fretta.")
        stampa("Il viaggio si allunga di una sola settimana")
    else:
        aumento = rn.randint(2,4)
        viaggio["settimane totali"] += aumento
        stampa("Nel tuo equipaggio non è presente neanche un meccanico, è quindi compito del resto della ciurma aggiustare il timone alla bell'e meglio")
        stampa(f"Il viaggio si allunga di {aumento} settimane")

def raffiche_di_vento():
    stampa("Durante la navigazione si sono verificate delle forti raffiche di vento!")
    if equipaggio["navigatore"]["numero"] > 0:
        viaggio["settimane totali"] += 1
        stampa("Fortunatamente nel tuo equipaggio è presente un navigatore, che riesce a rimettere nella giusta rotta la nave!")
        stampa("Il viaggio si allunga di una sola settimana")
    else:
        aumento = rn.randint(2,4)
        viaggio["settimane totali"] += aumento
        stampa("Nel tuo equipaggio non è presente neanche un navigatore, e di conseguenza il resto della ciurma prova a tornare in rotta, senza però girare un po' a vuoto")
        stampa(f"Il viaggio si allunga di {aumento} settimane")

def avvistamento_isola(alabatro):
    stampa("TERRAAAAAAAAAAAAAAAAAAA!!!!!!!!")
    stampa("E' stata avvistata un isola all'orizzonte, chissà se è abitata...")
    stampa("Vuoi esplorarla? (esplorare un isola potrebbe allungare il viaggio di qualche settimana...)")
    errore = True
    while errore:
        scelta = input(">> ").lower().strip()
        if scelta in ["si", "s", "y"]:
            errore = False
            abitata = rn.choice([True, False])
            if abitata:
                ostili = rn.choice([True, False])
                if ostili:
                    stampa("L'isola era abitata da dei locali ostili, meglio darsela a gambe!")
                else:
                    stampa("Che fortuna! L'isola era abitata da locali pacifici!")
                    stampa("Gli siete sembrati simpatici e hanno deciso di regalarvi le seguenti risorse:")
                    if alabatro:
                        for i in ["medicinale", "armi", "sale", "stoffa", "diamanti", "coltelli"]:
                            x = rn.randint(5,20)
                            merci[i]["numero"] += x
                            stampa(f"{i} - {x} unità")
                    else:
                        for i in ["medicinale", "armi", "sale", "stoffa", "diamanti", "coltelli"]:
                            x = rn.randint(20,40)
                            merci[i]["numero"] += x
                            stampa(f"{i} - {x} unità")
            else:
                stampa("L'isola non era abitata, l'esplorazione si è rivelata vana.")
            errore = False
            return True
        elif scelta in ["no", "n"]:
            stampa("Hai deciso di non esplorare l'isola.")
            stampa("Non ti piace perdere tempo, ma chissà cosa avresti potuto trovarci...")
            errore = False
            return False

def nessun_imprevisto():
    stampa("Durante questa settimana di navigazione non si è verificato nessun imprevisto.")
    stampa("La calma prima della tempesta?", 0.1)


# ---------- CONTROLLO SCORTE ----------

def rimuovi_scorte():
    ciurma = equipaggio["marinaio"]["numero"] + equipaggio["meccanico"]["numero"] + equipaggio["medico"]["numero"] + equipaggio["navigatore"]["numero"] + equipaggio["cuoco"]["numero"]
    for i in provviste:
        provviste[i]["numero"] -= provviste[i]["consumo"]*ciurma

def calcolo_scorte_viaggio():
    ciurma = equipaggio["marinaio"]["numero"] + equipaggio["meccanico"]["numero"] + equipaggio["medico"]["numero"] + equipaggio["navigatore"]["numero"] + equipaggio["cuoco"]["numero"]
    for i in provviste:
        if provviste[i]["numero"] <= 0:
            stampa(f"Hai esaurito le razioni di {i}, la tua ciurma non ne sarà felice...")
            #TODO morale
        
        if provviste[i]["numero"] < provviste[i]["consumo"]*ciurma:
            stampa(f"Le scorte attuali di {i} non sono sufficienti a coprire tutta la durata del viaggio.")
            stampa(f"Intendi dimezzarle?")
            errore = True
            while errore:
                scelta = input(">> ").strip().lower()
                if scelta in ["si", "s", "y"]:
                    provviste[i]["consumo"] /= 2
                    #TODO Gestione morale (-5 punti a settimana)
                    errore = False
                elif scelta in ["no", "n"]:
                    errore = False
                else:
                    stampa("Scelta non accettabile")
        
        elif provviste[i]["numero"] > provviste[i]["consumo"]*ciurma*2:
            stampa(f"Le scorte attuali di {i} sono abbondanti, intendi raddoppiare le razioni?")
            errore = True
            while errore:
                scelta = input(">> ").strip().lower()
                if scelta in ["si", "s", "y"]:
                    provviste[i]["consumo"] *= 2
                    #TODO Gestione morale (+5 punti a settimana)
                    errore = False
                elif scelta in ["no", "n"]:
                    errore = False
                else:
                    stampa("Scelta non accettabile")


# --------------- MORALE ---------------

def aggiornamento_morale():
    pass