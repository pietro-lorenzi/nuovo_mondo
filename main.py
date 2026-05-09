from altreFunzioni import *
from core import *
from parteIniziale import *
from parteFinale import *
from termcolor import colored

def ingaggio_completato():
    #diz = ingaggia_eq()
    equipaggio["marinaio"]["numero"] = 2 #diz["marinaio"]
    equipaggio["cuoco"]["numero"] = 2 #diz["cuoco"]
    equipaggio["meccanico"]["numero"] = 2 #diz["meccanico"]
    equipaggio["medico"]["numero"] = 2 #diz["medico"]
    equipaggio["navigatore"]["numero"] = 2 #diz["navigatore"]

def provviste_completate():
    #diz = provviste_eq(calcola_ciurma(equipaggio))
    provviste["verdura"]["numero"] = 60#diz["verdura"]
    provviste["frutta"]["numero"] = 100#diz["frutta"]
    provviste["carne"]["numero"] = 100#diz["carne"]
    provviste["acqua"]["numero"] = 60#diz["acqua"]
    monete = 2000
    for i in provviste:
        monete -= provviste[i]["numero"] + provviste[i]["costo"]
    stampa(f"Apri il borsellino e conti {monete} monete")
    return monete

def merci_completate(monete):
    #diz = merci_eq(monete)
    merci["medicinale"]["numero"] = 10#diz["medicinale"]
    merci["armi"]["numero"] = 8#diz["armi"]
    merci["sale"]["numero"] = 50#diz["sale"]
    merci["stoffa"]["numero"] = 60#diz["stoffa"]
    merci["coltelli"]["numero"] = 70#diz["coltelli"]
    merci["diamanti"]["numero"] = 80#diz["diamanti"]
    for i in merci:
        monete -= merci[i]["numero"] * merci[i]["prezzo"]
    stampa(f"Apri il borsellino e conti {monete} monete")
    return monete

def messaggio_settimanale():
    print(f"---------- SETTIMANA {viaggio["settimana attuale"]} ----------")
    print()

menu()
azione = scelta()
if azione == 1:
    introduzione()
    ingaggio_completato()
    monete = provviste_completate()
    monete = merci_completate(monete)
    costo_equipaggio = calcola_costo_equipaggio()
    aggiunta_morale()


pool_eventi = [
    uomo_in_mare, verdura_in_mare, frutta_in_mare, carne_in_mare, acqua_in_mare, pesca_miracolosa, 
    tempesta_miracolosa, venti_favorevoli, cattivo_tempo, ondata, infestazione_ratti, 
    avvistamento_alabatro, avvistamento_scialuppa, epidemia, attacco_pirata, danni_al_timone, 
    raffiche_di_vento, lambda: avvistamento_isola(viaggio["alabatro_ucciso"]), nessun_imprevisto
]


morte = False

os.system("cls")
# --------------------- CICLO PRINCIPALE ---------------------

while viaggio["settimana attuale"] <= viaggio["settimane totali"] and not morte:
    messaggio_settimanale()

# ---------- EVENTO ----------
    nuovo = False
    while not nuovo:
        evento = rn.choice(pool_eventi)
        if evento not in viaggio["eventi accaduti"]:
            if evento == avvistamento_alabatro and viaggio["conta alabatro"] < 3:
                if evento():
                    viaggio["alabatro_ucciso"] = True
            else:
                evento()
                if evento != nessun_imprevisto:
                    viaggio["eventi accaduti"].append(evento)
            nuovo = True
    spazio()

# ---------- SCORTE ----------
    calcolo_scorte_viaggio()
    rimuovi_scorte()
    spazio()

# ---------- MORALE ----------
    aggiornamento_morale()

# ---------- RIEPILOGO ----------
    riepilogo()
    spazio()

# ---------- AMMUTINAMENTO ----------
    punti = punti_ammutinamento(viaggio["alabatro avvistato"], viaggio["alabatro ucciso"])
    morte = ammutinamento(punti)
    spazio()

# ---------- RICALCOLO ----------
    ricalcolato = ricalcolo()
    if ricalcolato:
        spazio()

    viaggio["settimana attuale"] += 1

# ------------ MORTE ------------
if morte:
    messaggio_morte()

if viaggio["conta alabatro"] > 0:
    viaggio["alabatro_avvistato"] = True

# ---------- ARRIVO NEL NUOVO MONDO ----------
RichiestaFuoco(merci)
merci = Baratto(merci)

x = tradimento(merci, equipaggio, viaggio["alabatro avvistato"], viaggio["alabatro ucciso"])
if x == True:
    messaggio_morte()
else:
    merci = x

esito, monete = epilogo()
if esito == 0:
    stampa("Tutto, ma non la nave.")
    stampa("Ti rendi conto che questa è una mancanza di rispetto.")
    stampa("Verso i tuoi uomini, che vogliono essere pagati.")
    stampa("Verso i creditori, che si sono fidati di te.")
    stampa("Verso di te, che non hai saputo mantenere la parola.")
    stampa("Ma la decisione è stata presa.")
    stampa("La nave, compagna di mesi di avventure, non verrà messa all'asta.")
    stampa("Probabilmente dovrai lavorare anni per ripagare  debiti.")
    stampa("Ma sai che, quando vorrai, potrai tentare una nuova avventura verso il nuovo mondo.")
    stampa("-----------------------------------")
    stampa(f"Hai terminato il viaggio con un debito di {monete} monete.")
elif esito == 1:
    stampa("Il porto si avvicina lentamente, come in un sogno che non osi interrompere.")
    stampa("Le monete tintinnano nelle casse. ")
    stampa("L'equipaggio ride, per la prima volta da settimane.")
    stampa("Paghi tutti. Fino all'ultimo uomo. Fino all'ultimo centesimo dovuto.")
    stampa("E quando la folla sul molo si apre per lasciarti passare, capisci che non stai solo tornando a casa.")
    stampa("Stai tornando vincitore.")
    stampa("Il mare ti ha messo alla prova.")
    stampa("E tu hai vinto.")
    stampa("-----------------------------------")
    stampa(f"Hai terminato il viaggio con un credito di {monete} monete.")
elif esito == 2:
    stampa("Non è andata come avevi pianificato. Non va mai come si pianifica, in mare.")
    stampa("La barca se n'è andata. L'hai guardata allontanarsi dal molo con un nodo in gola che non riesci a spiegare.")
    stampa("Ma i tuoi uomini sono stati pagati. Tutti. Fino all'ultimo.")
    stampa("E quando l'ultimo di loro ti stringe la mano prima di andarsene, capisci che alcune cose valgono più di una nave.")
    stampa("Hai perso qualcosa.")
    stampa("Ma hai mantenuto la tua parola.")
    stampa("E in questo mondo, non è poco.")
    stampa("-----------------------------------")
    stampa(f"Hai terminato il viaggio vendendo la nave, con un credito di {monete} monete.")
elif esito == 3:
    stampa("Le monete sono esatte. Né una in più, né una in meno.")
    stampa("Hai venduto la nave per pagare gli uomini. Hai attraversato l'oceano per tornare con le mani vuote.")
    stampa("Mesi di viaggio, tempeste, morti, paure.")
    stampa("E il saldo finale è zero.")
    stampa("Eppure, mentre guardi i tuoi uomini allontanarsi con la loro paga in tasca, ti chiedi se il profitto fosse davvero quello che stavi cercando.")
    stampa("Il mare non ti ha reso ricco.")
    stampa("Ma forse ti ha reso qualcos'altro.")
    stampa("Decidilo tu.")
    stampa("-----------------------------------")
    stampa(f"Hai terminato il viaggio senza aver guadagnato né perso neanche una moneta.")
elif esito == 4:
    stampa("Hai venduto tutto. La nave, la dignità, le speranze.")
    stampa("E non è bastato.")
    stampa("I tuoi uomini ti guardano con occhi che non accusano, il che è peggio.")
    stampa("Non c'è rabbia nei loro volti. Solo stanchezza.")
    stampa("Hai attraversato il mondo conosciuto, hai sfidato il mare, hai perso compagni lungo la strada.")
    stampa("E alla fine non hai nemmeno abbastanza per guardare negli occhi chi è sopravvissuto con te.")
    stampa("Alcune storie non hanno un lieto fine.")
    stampa("La tua è una di queste.")
    stampa("-----------------------------------")
    stampa(f"Hai terminato il viaggio vendendo la nave, ma mantendendo lo stesso un debito di {monete} monete")