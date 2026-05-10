from altreFunzioni import *
from core import *
from parteIniziale import *
from parteFinale import *
from termcolor import colored
import sys

def ingaggio_completato():
    diz = ingaggia_eq()
    equipaggio["marinaio"]["numero"] = diz["marinaio"]
    equipaggio["cuoco"]["numero"] = diz["cuoco"]
    equipaggio["meccanico"]["numero"] = diz["meccanico"]
    equipaggio["medico"]["numero"] = diz["medico"]
    equipaggio["navigatore"]["numero"] = diz["navigatore"]

def provviste_completate():
    monete = 2000
    diz = provviste_eq(calcola_ciurma(equipaggio))
    provviste["verdura"]["numero"] = diz["verdura"]
    provviste["frutta"]["numero"] = diz["frutta"]
    provviste["carne"]["numero"] = diz["carne"]
    provviste["acqua"]["numero"] = diz["acqua"]
    for i in provviste:
        monete -= provviste[i]["numero"] * provviste[i]["costo"]
    stampa(f"Apri il borsellino e conti {monete:.0f} monete")
    invio()
    return monete

def merci_completate(monete):
    diz = merci_eq(monete)
    merci["medicinale"]["numero"] = diz["medicinale"]
    merci["armi"]["numero"] = diz["armi"]
    merci["sale"]["numero"] = diz["sale"]
    merci["stoffa"]["numero"] = diz["stoffa"]
    merci["coltelli"]["numero"] = diz["coltelli"]
    merci["diamanti"]["numero"] = diz["diamanti"]
    for i in merci:
        monete -= merci[i]["numero"] * merci[i]["prezzo"]
    stampa(f"Apri il borsellino e conti {monete:.0f} monete")
    invio()
    return monete

def messaggio_settimanale():
    print(f"---------- SETTIMANA {viaggio["settimana attuale"]} ----------")
    print()

menu()
azione = scelta()

if azione == 2:
    dati = Carica()
    if dati == False:
        azione = 1
        stampa("La pagina del diario è vuota. Ma ciò non significa che lo resterà a lungo.")
        invio()
    else:
        for ruolo in dati["equipaggio"]:
            equipaggio[ruolo].update(dati["equipaggio"][ruolo])
        for provvista in dati["provviste"]:
            provviste[provvista].update(dati["provviste"][provvista])
        for merce in dati["merci"]:
            merci[merce].update(dati["merci"][merce])
        for i in viaggio:
            viaggio[i] = dati["viaggio"][i]
        msg_ripresa = [
            "Il diario di bordo viene riaperto.",
            "Il mare vi stava aspettando.",
            "La spedizione riprende il suo corso.",
            "Le onde ricordano ancora il vostro nome.",
            "La nave torna lentamente a muoversi.",
            "L'oceano non ha dimenticato la vostra rotta.",
            "Il capitano è tornato al timone.",
            "Le pagine del diario riprendono a scriversi.",
            "Il silenzio del mare viene spezzato ancora una volta.",
            "L'equipaggio torna ai propri posti.",
            "Le onde riprendono a raccontare la vostra storia.",
        ]
        print(rn.choice(msg_ripresa))
        invio()

if azione == 1:
    introduzione()
    ingaggio_completato()
    monete = provviste_completate()
    viaggio["monete"] = merci_completate(monete)
    aggiunta_morale()

if azione == 3:
    cprint("Il capitano abbandona i suoi uomini.", "red")
    invio()
    sys.exit()

def evento_isola():
    return avvistamento_isola(viaggio["alabatro ucciso"])

pool_eventi = [
    uomo_in_mare, verdura_in_mare, frutta_in_mare, carne_in_mare, acqua_in_mare, pesca_miracolosa, 
    tempesta_miracolosa, venti_favorevoli, cattivo_tempo, ondata, infestazione_ratti, 
    avvistamento_alabatro, avvistamento_scialuppa, epidemia, attacco_pirata, danni_al_timone, 
    raffiche_di_vento, evento_isola, nessun_imprevisto
]

morte = False

os.system("cls")
# --------------------- CICLO PRINCIPALE ---------------------

while viaggio["settimana attuale"] <= viaggio["settimane totali"] and not morte and calcola_ciurma(equipaggio) > 0:
    messaggio_settimanale()

# ---------- EVENTO ----------
    nuovo = False
    while not nuovo:
        evento = rn.choice(pool_eventi)
        if evento.__name__ not in viaggio["eventi accaduti"]:
            if evento == avvistamento_alabatro and viaggio["conta alabatro"] < 3:
                if evento():
                    viaggio["alabatro ucciso"] = True
                viaggio["conta alabatro"] += 1
            else:
                evento()
                if evento != nessun_imprevisto:
                    viaggio["eventi accaduti"].append(evento.__name__)
            nuovo = True
    invio()

# ---------- SCORTE ----------
    calcolo_scorte_viaggio(provviste, equipaggio, viaggio)
    rimuovi_scorte(provviste, equipaggio)
    invio()

# ---------- MORALE ----------
    aggiornamento_morale(equipaggio, viaggio)

# ---------- RIEPILOGO ----------
    riepilogo(equipaggio, provviste, merci)
    invio()

# ---------- AMMUTINAMENTO ----------
    punti = punti_ammutinamento(viaggio["alabatro avvistato"], viaggio["alabatro ucciso"], equipaggio, viaggio)
    morte = ammutinamento(punti)
    invio()

# ---------- RICALCOLO ----------
    ricalcolato = ricalcolo(equipaggio, viaggio)
    if ricalcolato:
        invio()

    viaggio["settimana attuale"] += 1
# ---------- SALVATAGGIO ----------
    cprint("SALVATAGGIO", "yellow")
    stampa("Prima di continuare con il viaggio, vuoi annotare i progressi della spedizione nel diario di bordo?", 0.03)
    ris = sceltaSiNo()
    if ris == "s":
        Salva(equipaggio, provviste, merci, viaggio)
        stampa("Salvataggio completato!", 0.03)
        invio()
    else:
        os.system("cls")

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
    os.system("cls")
    esito, monete = epilogo(equipaggio, provviste, merci, viaggio, viaggio["alabatro avvistato"], viaggio["alabatro ucciso"], viaggio["monete"])
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