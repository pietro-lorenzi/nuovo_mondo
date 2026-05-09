from altreFunzioni import *
import random as rn
from time import sleep
from termcolor import colored, cprint

#TODO termcolor

# ---------- STRUTTURE DATI ----------

equipaggio = {
    "marinaio": {
        "numero": 0,
        "costo": 10,
        "morale": []
    },
    "meccanico": {
        "numero": 0,
        "costo": 15,
        "morale": []
    },
    "medico": {
        "numero": 0,
        "costo": 25,
        "morale": []
    },
    "navigatore": {
        "numero": 0,
        "costo": 20,
        "morale": []
    },
    "cuoco": {
        "numero": 0,
        "costo": 15,
        "morale": []
    },
}

provviste = {
    "verdura":{
        "costo": 0.5,     
        "consumo": 0.5,
        "numero": 0,      
    },
    "frutta":{
        "costo": 1,   
        "consumo": 1, 
        "numero": 0,
    },
    "carne":{
        "costo": 2,   
        "consumo": 1, 
        "numero": 0,
    },
    "acqua":{
        "costo": 0.5,   
        "consumo": 0.5, 
        "numero": 0, 
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
    "perle":{
        "prezzo": 2,
        "numero": 0
    },
    "manufatti":{
        "prezzo": 2,
        "numero": 0
    },
    "spezie":{
        "prezzo": 1,
        "numero": 0
    },
}

viaggio = {
    "settimana attuale": 1,
    "settimane totali": 8,
    "delta_morale": 0,
    "scorta dimezzata": False,
    "conta alabatro": 0,
    "eventi accaduti": [],
    "alabatro avvistato": False,
    "alabatro ucciso": False
}

# ---------- CALCOLO COSTO ----------

def calcola_costo_equipaggio():
    costo_totale = 0
    for ruolo in equipaggio:
        costo_totale += equipaggio[ruolo]["numero"] * equipaggio[ruolo]["costo"]
    return costo_totale

# --------------- EVENTI ---------------

def uomo_in_mare():
    acc = ciurma_accettabile(equipaggio)
    morto = rn.choice(acc)
    equipaggio[morto]["numero"] -= 1
    morale = rn.choice(equipaggio[morto]["morale"])
    equipaggio[morto]["morale"].remove(morale)
    stampa("Lentamente, dall'orizzonte, un navigatore scorge un onda anomala.")
    stampa("Prima che chiunque possa reagire, l'onda si abbatte violentemente sulla nave.", 0.05)
    stampa(f"Un {morto} cade tra le fauci dell'oceano.")
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
    stampa("Una tempesta viene avvistata in lontananza, ma questa volta è diverso.")
    acqua = rn.randint(11,20)
    provviste["acqua"]["numero"] += acqua
    stampa("Non c'è vento a precederla. Non c'è rabbia nell'aria.")
    stampa("Poi inizia a piovere, gocce grosse, rumorose, costanti.")
    stampa(f"Ordini all'equipaggio di posizionare i barili, e raccogliete {acqua} litri di acqua.")
    stampa("Sembra quasi che il mare abbia deciso di risparmiarvi questa volta, eppure esiste un detto tra voi uomini di mare...")
    stampa("Se sopravvivi alla tempesta, non ringraziare, perché significa che ", capo=False)
    stampa("non è finita.", 0.2)

def venti_favorevoli(): #TODO SISTEMARE NARRATORE
    stampa("In una fredda mattina ti accorgi che dei venti favorevoli stanno spingendo la nave più velocemente.")
    stampa("L'equipaggio ne è felice, festeggia perché arriverai prima a destinazione.")
    viaggio["settimane totali"] -= 1
    for ruolo in equipaggio:
        for i in range(equipaggio[ruolo]["numero"]):
            equipaggio[ruolo]["morale"][i] += rn.randint(5,15)
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
        stampa("Un'ombra bianca solca il cielo nuvoloso.")
        stampa("Uccidere un alabatro si sa, porta sfortuna.")
        stampa("Ma la fame non conosce superstizioni.", 0.05)
        ciurma = calcola_ciurma(equipaggio)
        tentativi = min(merci["armi"]["numero"], ciurma)
        colpito = False
        for i in range(tentativi):
            if rn.choice([True, False]):
                colpito = True
        
        if colpito:
            carne_guadagnata = rn.randint(10, 15)
            provviste["carne"]["numero"] += carne_guadagnata
            stampa("Lo sparo echeggia nell'aria, e il corpo morto del pennuto precipita a prua.")
            stampa(f"Recuperate {carne_guadagnata} unità di carne.")
            stampa("Alcuni marinai si fanno il segno della croce.")
            stampa("Chissà se il mare rivendicherà questa morte.")
            stampa("Ma almeno stasera non morirete di fame.")
            return True
        else:
            stampa("Innumerevoli spari squarciano l'aria.")
            stampa("Ma tu hai assunto uomini di mare, non tiratori scelti.")
            stampa("L'uccello danza tra i proiettili, come a sfidare i tuoi uomini a fare di meglio, per poi allontanarsi, beffardo.")
            stampa("Alcuni sono sollevati, almeno non verrete bersagliati dalla sfortuna.")
            stampa("Vero?", 0.1)
            return False
    else:
        stampa("Un alabatro sorvola la nave.")
        stampa("Maestoso. Irraggiungibile.")
        stampa("L'equipaggio lo osserva, affamato e impotente.")
        stampa("Senza armi, siete solo spettatori.")
        stampa("Come lui, voi navigate verso l'ignoto.")
        stampa("Ma a differenza sua, voi potreste non tornare.")
        return False

def avvistamento_scialuppa():
    stampa("Durante un pomeriggio tranquillo, in lontananza avvistate una scialuppa.")
    stampa("Il legno è marcio. Sono in mare da molto più di voi.")
    stampa("A bordo intravedi 4 uomini dalla pancia scavata dalla fame e gli occhi gonfi di paura.")
    stampa("Uno di loro appoggia la testa su una cassa, chissà cosa contiene.")
    stampa("Vuoi salvarli?")
    errore = True
    while errore:
        scelta = input(">> ").lower().strip()
        if scelta == "si":
            for i in range(4):
                membro = rn.choice(list(equipaggio.keys()))
                equipaggio[membro]["numero"] += 1
                morale = rn.randint(25,75)
                equipaggio[membro]["morale"].append(morale)
            stampa("Con riluttanza decidi di calare le scialuppe per farli salire a bordo.")
            stampa("Non sembrano contenti. Non sembrano grati. Sembrano solo provati dal mare.")
            stampa("Decidete di aprire la cassa, e all'interno di essa trovate alcune merci utili per il vostro viaggio.")
            for i in merci:
                caso = rn.randint(10,20)
                merci[i]["numero"] += caso
                stampa(f"{i} + {caso}")
            errore = False
        elif scelta == "no":
            stampa("Salvare altre vite non è una vostra priorità e decidete di proseguire oltre.")
            stampa("Guardando indietro vi sembra quasi che uno degli uomini vi stia fissando sorridendo.")
            stampa("La decisione è ormai presa.")
            errore = False

def epidemia():
    stampa("Improvvisamente un brivido ti percorre il collo. Un presagio.")
    stampa("Uno dei tuoi uomini tossice improvvisamente. Poi un altro. E un altro ancora.")
    stampa("L'aria inizia a farsi pesante, irrespirabile.")
    medicine = merci["medicinale"]["numero"]
    ammalati = []
    if medicine > 0:
        stampa(f"Dalla stiva riesci a recuperare {medicine} medicine. Chissà se basteranno per tutti...")
        for i in equipaggio:
            for x in range(equipaggio[i]["numero"]):
                ammalati.append(i)

        stampa("Li osservi uno ad uno. Sudano freddo. Tossiscono secco. Gli occhi sono già quasi spenti. Non c'è tempo di scegliere chi salvare.")
        for i in ammalati[:]:
            if rn.randint(1,10) > 7:
                ammalati.remove(i)

        for i in range(medicine):
            if ammalati:
                fortunato = rn.choice(ammalati)
                ammalati.remove(fortunato)
                medicine -= 1

        for i in ammalati:
            equipaggio[i]["numero"] -= 1
            morale = rn.choice(equipaggio[i]["morale"])
            equipaggio[i]["morale"].remove(morale)

        merci["medicinale"]["numero"] = medicine
    
    if ammalati:
        stampa(f"Il medico ci ha provato in tutti i modi, ma {len(ammalati)} morti sono stati inevitabili. Questa epidemia non può essere un caso.")
        stampa("I morti corrispondono a:")
        for i in ammalati:
            stampa(i.upper())
    else:
        stampa("Il medico è riuscito a curare tutti, ma sai che il mare non perdonerà queste vite che già sentiva proprie.")
    
    stampa(f"Restano {medicine} bottiglie di medicinale. Poche per sentirsi al sicuro.")

def attacco_pirata():
    stampa("In lontananza la vedete. La bandiera nera con teschio bianco, che sventola fiera nel cielo azzurro.")
    stampa("Morire qua renderebbe tutto inutile.")
    numero_pirati = rn.randint(3,10)
    ciurma = calcola_ciurma(equipaggio)
    numero_difensori = min(ciurma, merci["armi"]["numero"])
    uomini_persi = min(numero_pirati-numero_difensori, ciurma)
    if uomini_persi <= 0:
        stampa(f"{numero_pirati} pirati si abbattono sulla nave.")
        stampa("Il ponte si tinge di rosso.")
        stampa("Ma non è il vostro sangue.")
        stampa("Questa volta.")
        stampa("I cadaveri dei pirati scivolano in mare.")
        stampa("L'oceano accoglie tutti, prima o poi.")
    else:
        stampa("E chi avrebbe mai pensato che nel momento dell'ingaggio sarebbero potuti servire anche guerrieri?")
        stampa("Il sangue si sparge. I corpi cadono. Difficile distinguere se sono tuoi compagni o nemici.")
        stampa(f"{uomini_persi} dei tuoi uomini hanno già visto la loro ultima alba, senza saperlo.")
        stampa("I loro corpi vengono gettati in mare. Senza preghiere o cerimonie. Senza dignità.")
        stampa("I morti sono:")
        for i in range(uomini_persi):
            acc = ciurma_accettabile(equipaggio)
            morto = rn.choice(acc)
            equipaggio[morto]["numero"] -= 1
            morale = rn.choice(equipaggio[morto]["morale"])
            equipaggio[morto]["morale"].remove(morale)
            stampa(morto)

def danni_al_timone():
    stampa("Improvvisamente un pezzo di legno del timone ti si conficca nella mano.")
    stampa("Inizialmente pensi sia una scheggia. Solo dopo ti accorgi che il timone cade a pezzi.")
    stampa("Il viaggio è a rischio. E lo sai.")
    if equipaggio["meccanico"]["numero"] > 0:
        viaggio["settimane totali"] += 1
        stampa("Nel tuo equipaggio è presente un meccanico, che riesce a riparare il danno senza troppi problemi.")
        stampa("Tuttavia l'incidente non è superificiale, e il viaggio si allunga di una settimana.")
    else:
        aumento = rn.randint(2,4)
        viaggio["settimane totali"] += aumento
        stampa("Nessuno dei tuoi uomini è un meccanico, e nessuno è in grado di riparare il timone a dovere.")
        stampa("Tentativi maldestri. Riparazioni improvvisate.")
        stampa(f"Il viaggio si allunga di {aumento} settimane.")
        stampa("E nel mentre le provviste diminuiscono.")

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
                            x = rn.randint(20,40)
                            merci[i]["numero"] += x
                            stampa(f"{i} - {x} unità")
                    else:
                        for i in ["medicinale", "armi", "sale", "stoffa", "diamanti", "coltelli"]:
                            x = rn.randint(5,20)
                            merci[i]["numero"] += x
                            stampa(f"{i} - {x} unità")
            else:
                stampa("L'isola non era abitata, l'esplorazione si è rivelata vana.")
            viaggio["settimane totali"] += 2
        elif scelta in ["no", "n"]:
            stampa("Hai deciso di non esplorare l'isola.")
            stampa("Non ti piace perdere tempo, ma chissà cosa avresti potuto trovarci...")
            errore = False

def nessun_imprevisto():
    stampa("Durante questa settimana di navigazione non si è verificato nessun imprevisto.")
    stampa("La calma prima della tempesta?", 0.1)


# ---------- CONTROLLO SCORTE ----------

def rimuovi_scorte():
    ciurma = calcola_ciurma(equipaggio)
    for i in provviste:
        provviste[i]["numero"] -= provviste[i]["consumo"]*ciurma

def calcolo_scorte_viaggio():
    ciurma = calcola_ciurma(equipaggio)
    viaggio["scorta dimezzata"] = False
    for i in provviste:
        if provviste[i]["numero"] <= 0:
            stampa(f"Hai esaurito le razioni di {i}, la tua ciurma non ne sarà felice...", 0.02)
            viaggio["delta_morale"] -= 10
        
        elif provviste[i]["numero"] < provviste[i]["consumo"]*ciurma*(viaggio["settimane totali"] - viaggio["settimana attuale"]):
            stampa(f"Per completare il viaggio avresti bisogno di {provviste[i]["consumo"]*ciurma*(viaggio["settimane totali"] - viaggio["settimana attuale"])} unità di {i}, ma tu ne possiedi solo {provviste[i]["numero"]}", 0.02)
            stampa(f"Intendi dimezzarle?", 0.02)
            errore = True
            while errore:
                scelta = input(">> ").strip().lower()
                if scelta in ["si", "s", "y"]:
                    provviste[i]["consumo"] /= 2
                    viaggio["scorta dimezzata"] = True
                    errore = False
                elif scelta in ["no", "n"]:
                    errore = False
                else:
                    stampa("Scelta non accettabile", 0.02)
        
        elif provviste[i]["numero"] > provviste[i]["consumo"]*ciurma*(viaggio["settimane totali"] - viaggio["settimana attuale"]):
            stampa(f"Per completare il viaggio avresti bisogno di {provviste[i]["consumo"]*ciurma*(viaggio["settimane totali"] - viaggio["settimana attuale"])} unità di {i}, mentre tu ne hai {provviste[i]["numero"]} unità", 0.02)
            stampa("Intendi raddoppiare le razioni?", 0.02)
            errore = True
            while errore:
                scelta = input(">> ").strip().lower()
                if scelta in ["si", "s", "y"]:
                    provviste[i]["consumo"] *= 2
                    errore = False
                elif scelta in ["no", "n"]:
                    errore = False
                else:
                    stampa("Scelta non accettabile", 0.02)

# --------------- MORALE ---------------

def aggiornamento_morale():
    for ruolo in equipaggio:
        for i in range(equipaggio[ruolo]["numero"]):
            equipaggio[ruolo]["morale"][i] += viaggio["delta_morale"]
    
    for ruolo in equipaggio:
        for i in range(equipaggio[ruolo]["numero"]):
            if equipaggio[ruolo]["morale"][i] <= 0:
                equipaggio[ruolo]["numero"] -= 1
                equipaggio[ruolo]["morale"].remove(0)
                stampa(f"La fame, la stanchezza, la paura. Un {ruolo} ha deciso che erano abbastanza.")
                stampa(f"Un {ruolo} è morto suicida.")

def aggiunta_morale():
    for ruolo in equipaggio:
        for membro in range(equipaggio[ruolo]["numero"]):
            equipaggio[ruolo]["morale"].append(100)

# -------------- RIEPILOGO -------------

def riepilogo():
    stampa(colored("La ciurma ancora in vita è composta da:", "cyan"))
    conta = 1
    for ruolo in equipaggio:
        for i in range(equipaggio[ruolo]["numero"]):
            stampa(f"{conta} - {ruolo.capitalize()} - Morale: {equipaggio[ruolo]["morale"][i]}", 0.02)
            conta += 1
    print()

    stampa(colored("Le scorte di cibo residue sono composte da:", "cyan"))
    for scorta in provviste:
        stampa(f"{scorta.capitalize()} - {provviste[scorta]["numero"]:.0f} unità", 0.02)
    print()

    stampa(colored("Le merci di scambio rimanenti sono:", "cyan"))
    for merce in merci:
        stampa(f"{merce.capitalize()} - {merci[merce]["numero"]:.0f} unità", 0.02)

# ------------ AMMUTINAMENTO -----------

def punti_ammutinamento(alabatro_visto, alabatro_ucciso):
    punti = 0
    cprint("AMMUTINAMENTO", "red")
    if viaggio["scorta dimezzata"]:
        punti += 30
        print("Razioni ridotte: L'equipaggio ha ricevuto meno cibo del previsto, la fame aumenta tensione e malcontento.")
    if equipaggio["cuoco"]["numero"] == 0:
        punti += 30
        print("Mancanza del cuoco: Senza nessuno a valorizzare il cibo, la qualità dei pasti peggiora e il morale cala.")
    if alabatro_visto and not alabatro_ucciso:
        punti += 30
        print("Albatro ucciso: Un presagio negativo: averlo abbattuto viene visto come un segno di sfortuna.")
    if alabatro_ucciso:
        punti -= 20
        print("Albatro avvistato ma non ucciso: Il segno viene interpretato con ottimismo e rispetto, riducendo la tensione a bordo.")
    if calcola_ciurma(equipaggio) > 12:
        punti += 30
        print("Troppi uomini a bordo: La nave è sovraffollata, aumentano conflitti, disordine e instabilità.")
    if viaggio["settimana attuale"] > 8:
        x = viaggio["settimana attuale"] - 8
        punti += 10*x
        print("Viaggio più lungo del previsto: La permanenza in mare logora la disciplina e aumenta la stanchezza dell’equipaggio.")
    elif viaggio["settimane totali"] < 8:
        x = 8 - viaggio["settimane totali"]
        punti -= 10*x
        print("Viaggio più corto del previsto: Meno tempo in mare riduce lo stress generale e mantiene più stabile il morale.")

    return punti

def ammutinamento(punti):
    msg_rischio = [
            "Senti gli sguardi pesarti addosso. Qualcosa sta per spezzarsi.",
            "I tuoi uomini parlano sottovoce quando ti avvicini. Non è un buon segno.",
            "Di notte senti voci nella stiva. Smettono appena scendi a controllare.",
            "Qualcuno ha scritto qualcosa sul bordo della tua cabina. È stato cancellato, ma ne restano le tracce.",
            "I tuoi ordini vengono eseguiti. Ma con un secondo di ritardo di troppo."
        ]
    msg_ammutinamento = [
        "Non c'è più niente da fare. I tuoi uomini ti guardano come si guarda un nemico.",
        "Le catene che li tenevano legati alla tua autorità si sono spezzate. Uno ad uno abbandonano i loro posti.",
        "Nessun grido, nessuna rissa. Solo il rumore dei loro passi che si allontanano. Questo è peggio.",
        "Ti hanno già giudicato. La sentenza è silenziosa e definitiva.",
        "La nave è ancora tua. Ma non c'è più nessuno disposto a farla andare avanti."
    ]
    if punti > 1 and punti < 99:
       stampa(rn.choice(msg_rischio))
       stampa("Il rischio di ammutinamento è palpabile.")
       return False
    elif punti > 100:
        stampa(rn.choice(msg_ammutinamento))
        stampa("La tua ciurma si ammutina. Il viaggio termina qua.")
        return True
    else:
        stampa("I tuoi uomini sono soddisfatti del loro capitano, non rischi l'ammutinamento")
        return False

# ---------- RICALCOLO VIAGGIO ----------

def ricalcolo():
    scontenti = 0
    mezza_ciurma = calcola_ciurma(equipaggio) / 2
    for ruolo in equipaggio:
        for i in equipaggio[ruolo]["morale"]:
            if i < 30:
                scontenti += 1

    if scontenti > mezza_ciurma:
        viaggio["settimane totali"] += 1
        msg_allungo = [
            "I tuoi uomini si muovono come fantasmi. Lenti, svuotati. La nave avanza, ma non abbastanza.",
            "La rassegnazione è contagiosa quanto la peste. I remi pesano il doppio quando nessuno ci crede più.",
            "Nessuno corre più agli ordini. Il viaggio si allunga, e tutti fingono di non sapere perché."
        ]
        stampa(rn.choice(msg_allungo))
        stampa("La settimana si allunga di una settimana in quanto il morale di più della metà dei tuoi uomini è basso.")
        return True
    return False