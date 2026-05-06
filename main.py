"""
-*-*-*- ORGANIZZAZIONE DEL LAVORO -*-*-*-

- Questo è il main, quindi qua ci andrà solo il corpo del programma
- Il progetto l'ho diviso in tre parti, forse non sono eque ma non mi interessa, l'importante è che alla fine esca un lavoro
fatto bene perché il tempo ce l'abbiamo
- Chi fa tutto all'ultimo verrà pestato di botte

PD ---> CORE DEL GIOCO
- Progettazione delle strutture dati principali (stato del gioco, equipaggio, scorte, merci)
- Implementazione del ciclo principale del viaggio settimanale
- Sviluppo del sistema di eventi
- Gestione del morale dell'equipaggio e delle condizioni di morte
- Calcolo e gestione dell'ammutinamento
- Controllo delle condizioni di terminazione del gioco

UMA ---> FASI INIZIALI E INTERAZIONI CON L'UTENTE
- Implementazione della fase di ingaggio dell'equipaggio
- Gestione dell'acquisto di provviste e merci
- Controllo e validazione degli input utente
- Gestione dell'interfaccia testuale (falla un minimo colorata con cprint o con quello che vuoi)
- Documentazione tecnica (ovviamente dovrai farla alla fine di tutto)

LEMMY ---> FASI FINALI E SISTEMA DI SALVATAGGIO
- Implementazione dell'arrivo nel nuovo mondo
- Sviluppo del sistema di baratto
- Gestione dell'evento di tradimento
- Calcolo del profitto finale
- Implementazione del sistema di salvataggio e caricamento su file


Il workflow funziona così:

BRANCH
    - Esistono due branch, che si chiamano main e dev
    - Nel branch main NON CI DEVE LAVORARE NESSUNO
    - Tutti lavoriamo nel branch dev, quando abbiamo implementato una nuova feature e FUNZIONA facciamo il merge con il main
    - Il main deve essere SEMPRE FUNZIONANTE AL 100%
    - Se non vi offendete (e lo so che non vi offendete 🤗) i merge li faccio SOLO IO così controllo bene che tutto funzioni prima di unire

FILE
    - Oltre al main ci sono altri 4 file, ognuno di quelli (come si capisce dal nome) ha una funzione specifica
    - core.py è la mia parte
    - parteIniziale.py è la parte di Uma
    - parteFinale.py è la parte di Lemmy
    - altreFunzioni.py è un altro file in cui se ci servono funzioni generiche le buttiamo dentro lì per mantenere un minimo di ordine


🌈 Have fun 🌈
"""

#TODO sys clear terminal

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

def merci_completate():
    diz = merci_eq()
    merci["medicinale"]["numero"] = diz["medicinale"]
    merci["armi"]["numero"] = diz["armi"]
    merci["sale"]["numero"] = diz["sale"]
    merci["stoffa"]["numero"] = diz["stoffa"]
    merci["coltelli"]["numero"] = diz["coltelli"]
    merci["diamanti"]["numero"] = diz["diamanti"]

ingaggio_completato()
provviste_completate()
merci_completate()
costo_equipaggio = calcola_costo_equipaggio()

alabatro_risparmiato = False
pool_eventi = [
    uomo_in_mare, verdura_in_mare, frutta_in_mare, carne_in_mare, acqua_in_mare, pesca_miracolosa, 
    tempesta_miracolosa, venti_favorevoli, cattivo_tempo, ondata, infestazione_ratti, 
    avvistamento_alabatro, avvistamento_scialuppa, epidemia, attacco_pirata, danni_al_timone, 
    raffiche_di_vento, lambda: avvistamento_isola(alabatro_risparmiato), nessun_imprevisto
    ]

print(equipaggio, provviste, merci)

while viaggio["settimana attuale"] <= viaggio["settimane totali"]:
    pass