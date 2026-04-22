# Uma lo so che questa è la tua parte, però volevo portarmi un po' avanti e ho creato queste
# funzioni finte che mi restituiscono dei valori standard, in modo che possa lavorare
# alla mia parte senza doverti aspettare per forza
#
# Quando vorrai lavorare elimina pure queste funzioni
#
### IMPORTANTE ###
# Tutta la fase di ingaggiamento dell'equipaggio, acquisto merci e acquisto provviste devono essere dentro una funzione a testa
# e alla fine deve restituire un dizionario, proprio come vedi nelle mie funzioni mock

def ingaggia_equipaggio_mock():
    return {
        "marinaio": 4,
        "meccanico": 3,
        "medico": 2,
        "cuoco": 2,
        "navigatore": 2
    }

def acquista_provviste_mock():
    return {
        "verdura": 52,
        "frutta": 104,
        "carne": 104,
        "acqua": 52
    }

def acquista_merci_mock():
    return {
        "medicinale": 10,
        "armi": 10,
        "sale": 10,
        "stoffa": 10,
        "coltelli": 10,
        "diamanti": 10
    }