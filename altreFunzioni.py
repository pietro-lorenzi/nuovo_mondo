import sys
import time
import os
from termcolor import colored, cprint

def stampa(testo, delay=0.04, capo=True):
    for i in testo:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    if capo:
        print()

def ciurma_accettabile(diz):
    ciurma = ["marinaio", "cuoco", "meccanico", "medico", "navigatore"]
    acc = []
    for i in ciurma:
        if diz[i]["numero"] > 0:
            acc.append(i)
    return acc

def calcola_ciurma(diz):
    ciurma = diz["marinaio"]["numero"] + diz["meccanico"]["numero"] + diz["medico"]["numero"] + diz["navigatore"]["numero"] + diz["cuoco"]["numero"]
    return ciurma

def invio():
    print("Premi INVIO per continuare...")
    input()
    os.system("cls")

def messaggio_morte():
    stampa(colored("GAME OVER", "red"), 0.3)
    stampa("Nessuno saprà mai quanto lontano siete arrivati...", 0.08)
    invio()

def sceltaSiNo():
    errore = True
    while errore:
        azione = input("").strip().lower()
        if azione in ["si", "yes", "y", "s"]:
            azione = "s"
            errore = False
        elif azione in ["no", "n"]:
            azione = "n"
            errore = False
        else:
            cprint("Scelta non accettabile", "red")
    return azione