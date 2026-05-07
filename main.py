from altreFunzioni import *
from core import *
from parteIniziale import *
from parteFinale import *

def ingaggio_completato():
    diz = ingaggia_eq()
    equipaggio["marinaio"]["numero"] = diz["marinaio"]
    equipaggio["cuoco"]["numero"] = diz["cuoco"]
    equipaggio["meccanico"]["numero"] = diz["meccanico"]
    equipaggio["medico"]["numero"] = diz["medico"]
    equipaggio["navigatore"]["numero"] = diz["navigatore"]

def provviste_completate():
    diz = provviste_eq()
    provviste["verdura"]["numero"] = diz["verdura"]
    provviste["frutta"]["numero"] = diz["frutta"]
    provviste["carne"]["numero"] = diz["carne"]
    provviste["acqua"]["numero"] = diz["acqua"]
    monete = 2000
    for i in provviste:
        monete -= provviste[i]["numero"] + provviste[i]["costo"]
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
    return monete


def messaggio_settimanale():
    print(f"---------- SETTIMANA {viaggio["settimana attuale"]} ----------")
    print()

ingaggio_completato()
monete = provviste_completate()
monete = merci_completate(monete)
costo_equipaggio = calcola_costo_equipaggio()

alabatro_risparmiato = False
pool_eventi = [
    uomo_in_mare, verdura_in_mare, frutta_in_mare, carne_in_mare, acqua_in_mare, pesca_miracolosa, 
    tempesta_miracolosa, venti_favorevoli, cattivo_tempo, ondata, infestazione_ratti, 
    avvistamento_alabatro, avvistamento_scialuppa, epidemia, attacco_pirata, danni_al_timone, 
    raffiche_di_vento, lambda: avvistamento_isola(alabatro_risparmiato), nessun_imprevisto
]

aggiunta_morale()
morte = False

os.system("cls")
# --------------------- CICLO PRINCIPALE ---------------------

while viaggio["settimana attuale"] <= viaggio["settimane totali"] or morte == True:
    messaggio_settimanale()

# ---------- EVENTO ----------
    nuovo = False
    while not nuovo:
        evento = rn.choice(pool_eventi)
        if evento not in viaggio["eventi accaduti"]:
            if evento == avvistamento_alabatro and viaggio["conta albatro"] < 3:
                viaggio["conta albatro"] += 1
            elif (evento == avvistamento_alabatro and viaggio["conta alabatro"] >= 3) or evento != nessun_imprevisto:
                evento()
                viaggio["eventi accaduti"].append(evento)
            else:
                evento
            nuovo = True
    spazio()

# ---------- SCORTE ----------
    rimuovi_scorte()
    calcolo_scorte_viaggio()
    spazio()

# ---------- MORALE ----------
    aggiornamento_morale()
    spazio()

# ---------- RIEPILOGO ----------
    riepilogo()
    spazio()

# ---------- AMMUTINAMENTO ----------
    punti = punti_ammutinamento()
    morte = ammutinamento(punti)
    spazio()

# ---------- RICALCOLO ----------
    ricalcolato = ricalcolo()
    if ricalcolato:
        spazio()

    viaggio["settimana attuale"] += 1