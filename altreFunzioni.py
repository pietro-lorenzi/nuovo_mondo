import sys
import time

def stampa(testo, delay=0.04, capo=True): #funzione per stampare il testo lentamente, in modo più figo
    for i in testo:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    if capo:
        print()

def ciurma_accettabile(diz): #funzione per definire quali membri della ciurma sono effettivamente presenti
    ciurma = ["marinaio", "cuoco", "meccanico", "medico", "navigatore"]
    acc = []
    for i in ciurma:
        if diz[i]["numero"] > 0:
            acc.append(i)
    return acc