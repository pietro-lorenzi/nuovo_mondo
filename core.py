from altreFunzioni import *
import random as rn

# ---------- STRUTTURE DATI ----------

equipaggio = {
    "marinaio": {
        "umore": 100,
        "numero": 0, #con numero intendo quanti individui di quel mestiere abbiamo
        "costo": 10
    },
    "meccanico": {
        "umore": 100,
        "numero": 0,
        "costo": 15
    },
    "medico": {
        "umore": 100,
        "numero": 0,
        "costo": 25
    },
    "navigatore": {
        "umore": 100,
        "numero": 0,
        "costo": 20
    },
    "cuoco": {
        "umore": 100,
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

def uomo_in_mare():
    pass

def verdura_in_mare():
    pass

def frutta_in_mare():
    pass

def carne_in_mare():
    pass

def acqua_in_mare():
    pass

def pesca_miracolosa():
    pass

def tempesta_miracolosa():
    pass

def venti_favorevoli():
    pass

def cattivo_tempo():
    pass

def ondata():
    pass

def infestazione_ratti():
    pass

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
            else:
                stampa("Neanche un colpo è andato a segno, l'alabatro si è allontanato e non avete guadagnato carne.")
    else:
        stampa("Durante la navigazione avvistate un alabatro, ma sfortunatamente non avete armi a bordo per provare a colpirlo")

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
    pass

def danni_al_timone():
    pass

def raffiche_di_vento():
    pass

def avvistamento_isola():
    pass

def nessun_imprevisto():
    pass