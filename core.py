from altreFunzioni import *
import random as rn

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


# ---------- FUNZIONI CALCOLO ----------

def calcola_costo_equipaggio(): #TODO sistemare
    costo_totale = 0
    for ruolo in equipaggio:
        costo_totale += equipaggio[ruolo]["numero"] * equipaggio[ruolo]["costo"]
    return costo_totale


# ---------- EVENTI ----------

#TODO controllare che nelle selezioni casuali di morti della ciurma siano presenti effettivamente membri di quella classe

def uomo_in_mare():
    ciurma = ["marinaio", "cuoco", "meccanico", "medico", "navigatore"]
    acc = []
    for i in ciurma:
        if equipaggio[i]["numero"] > 0:
            acc.append(i)
    morto = rn.choice(acc)
    stampa("Oh no! Un onda anomala si è scagliata sulla nave!")
    stampa(f"Un {morto} è caduto in mare ed è affogato!")
    stampa("Pace all'anima sua.")

def verdura_in_mare():
    stampa("Una violenta tempesta si abbatte sulla nave!")
    denom = rn.choice([2,3,4,5])
    perdita = provviste["verdura"]["numero"] // denom
    provviste["verdura"]["numero"] -= perdita
    stampa(f"Sfortunatamente {perdita} unità di verdura cadono in mare!")

def frutta_in_mare():
    stampa("Una violenta tempesta si abbatte sulla nave!")
    denom = rn.choice([2,3,4,5])
    perdita = provviste["frutta"]["numero"] // denom
    provviste["frutta"]["numero"] -= perdita
    stampa(f"Sfortunatamente {perdita} unità di frutta cadono in mare!")

def carne_in_mare():
    stampa("Una violenta tempesta si abbatte sulla nave!")
    denom = rn.choice([2,3,4,5])
    perdita = provviste["carne"]["numero"] // denom
    provviste["carne"]["numero"] -= perdita
    stampa(f"Sfortunatamente {perdita} unità di carne cadono in mare!")

def acqua_in_mare():
    stampa("Una violenta tempesta si abbatte sulla nave!")
    denom = rn.choice([2,3,4,5])
    perdita = provviste["acqua"]["numero"] // denom
    provviste["acqua"]["numero"] -= perdita
    stampa(f"Sfortunatamente {perdita} unità di acqua cadono in mare!")

def pesca_miracolosa():
    stampa("Settimana tranquilla, l'equipaggio decide di approfittarne per pescare.")
    pesca = rn.int(11,20)
    provviste["carne"]["numero"] += pesca
    stampa(f"Il tuo equipaggio è riuscito a pescare {pesca} kili di carne!")

def tempesta_miracolosa():
    stampa("Una tempesta irrompe, ma il tuo equipaggio si fa trovare pronto e posiziona strategicamente i barili per raccogliere l'acqua piovana")
    acqua = rn.int(11,20)
    provviste["acqua"]["numero"] += acqua
    stampa(f"Il tuo equipaggio è riuscito a pescare {acqua} litri di acqua!")

def venti_favorevoli():
    stampa("Venti favorevoli permettono alla nave di navigare più velocemente!")
    stampa("Il viaggio si accorcia di una settimana, e il tuo equipaggio sembra esserne felice")
    #TODO gestire morale e settimane

def cattivo_tempo():
    stampa("Settimana influenzata dal cattivo tempo!")
    denom = rn.choice([2,3,4,5])
    perdita = merci["medicinale"]["numero"] // denom
    merci["medicinale"]["numero"] -= perdita
    stampa(f"Sfortunatamente {perdita} bottiglie di medicinale vengono rovesciate per terra!")

def ondata():
    stampa("Avvistata un'onda anomala!")
    denom = rn.choice([2,3,4,5])
    perdita = merci["armi"]["numero"] // denom
    merci["armi"]["numero"] -= perdita
    stampa(f"Sfortunatamente {perdita} armi vengono gettate in mare dall'onda!")

def infestazione_ratti():
    stampa("I marinai ti hanno avvisato di un infestazione di ratti!")
    denom = rn.choice([2,3,4,5])
    perdita = merci["stoffa"]["numero"] // denom
    merci["stoffa"]["numero"] -= perdita
    stampa(f"Sfortunatamente {perdita} stoffe vengono rosicchiate dai topi!")

def avvistamento_alabatro():
    if merci["armi"] > 0:
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
                merci["carne"]["numero"] += carne_guadagnata
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
        else:
            stampa("Decidete di non salvare i 4 uomini e proseguite la navigazione, chissà cosa c'era nella cassa...")
            errore = False

def epidemia():
    stampa("Durante la navigazione scoppia una terribile epidemia a bordo!")
    medicine = merci["medicinale"]["numero"]
    if medicine > 0:
        stampa(f"Fortunatamente hai a disposizione {medicine} medicinali, e hai curato altrettanti membri del tuo equipaggio")
        ammalati = []
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
    numero_difensori = min(equipaggio, merci["armi"]["numero"])
    uomini_persi = min(numero_pirati-numero_difensori, ciurma)
    if uomini_persi <= 0:
        stampa(f"I pirati erano ben {numero_pirati}, ma grazie a un equipaggio corposo e a un buon numero di armi siete riusciti a difendervi!")
    else:
        stampa(f"Sfortunatamente siete stati colti impreparati, avete perso {uomini_persi} membri!")
        stampa("I morti sono:")
        for i in range(uomini_persi):
            morto = rn.choice("marinaio", "meccanico", "medico", "cuoco", "navigatore")
            equipaggio[morto]["numero"] -= 1
            stampa(morto)

def danni_al_timone():
    pass

def raffiche_di_vento():
    pass

def avvistamento_isola(alabatro):
    stampa("TERRAAAAAAAAAAAAAAAAAAA!!!!!!!!")
    stampa("E' stata avvistata un isola all'orizzonte, chissà se è abitata...")
    stampa("Vuoi esplorarla? (esplorare un isola potrebbe allungare il viaggio di qualche settimana...)")
    errore = True
    while errore:
        scelta = input(">> ").lower().strip()
        if scelta in ["si", "s", "y"]:
            errore = False
            abitata = rn.choice(True, False)
            if abitata:
                ostili = rn.choice(True, False)
                if ostili:
                    stampa("L'isola era abitata da dei locali ostili, meglio darsela a gambe!")
                else:
                    stampa("Che fortuna! L'isola era abitata da locali pacifici!")
                    stampa("Gli siete sembrati simpatici e hannod eciso di regalarvi le seguenti risorse:")
                    if alabatro:
                        for i in ["medicinale", "armi", "sale", "stoffa", "diamanti", "coltelli"]:
                            x = rn.int(5,20)
                            merci[i]["numero"] += x
                            stampa(f"{i} - {x} unità")
                    else:
                        for i in ["medicinale", "armi", "sale", "stoffa", "diamanti", "coltelli"]:
                            x = rn.int(20,40)
                            merci[i]["numero"] += x
                            stampa(f"{i} - {x} unità")
            else:
                stampa("L'isola non era abitata, l'esplorazione si è rivelata vana.")
            return True
        elif scelta in ["no", "n"]:
            stampa("Hai deciso di non esplorare l'isola.")
            stampa("Non ti piace perdere tempo, ma chissà cosa avresti potuto trovarci...")
            return False

def nessun_imprevisto():
    pass