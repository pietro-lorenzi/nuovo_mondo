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

from altreFunzioni import *
from core import *
from parteIniziale import *
from time import sleep

def ingaggio_completato():
    equipaggio["marinaio"]["numero"] = ingaggia_equipaggio_mock()["marinaio"]
    equipaggio["cuoco"]["numero"] = ingaggia_equipaggio_mock()["cuoco"]
    equipaggio["meccanico"]["numero"] = ingaggia_equipaggio_mock()["meccanico"]
    equipaggio["medico"]["numero"] = ingaggia_equipaggio_mock()["medico"]
    equipaggio["navigatore"]["numero"] = ingaggia_equipaggio_mock()["navigatore"]

def provviste_completate():
    provviste["verdura"]["numero"] = acquista_provviste_mock()["verdura"]
    provviste["frutta"]["numero"] = acquista_provviste_mock()["frutta"]
    provviste["carne"]["numero"] = acquista_provviste_mock()["carne"]
    provviste["acqua"]["numero"] = acquista_provviste_mock()["acqua"]

def merci_completate():
    merci["medicinale"]["numero"] = acquista_merci_mock()["medicinale"]
    merci["armi"]["numero"] = acquista_merci_mock()["armi"]
    merci["sale"]["numero"] = acquista_merci_mock()["sale"]
    merci["stoffa"]["numero"] = acquista_merci_mock()["stoffa"]
    merci["coltelli"]["numero"] = acquista_merci_mock()["coltelli"]
    merci["diamanti"]["numero"] = acquista_merci_mock()["diamanti"]

ingaggio_completato()
provviste_completate()
merci_completate()
costo_equipaggio = calcola_costo_equipaggio()