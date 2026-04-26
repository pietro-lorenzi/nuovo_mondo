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
    eq= {
        "marinaio": 0,
        "meccanico": 0,
        "medico": 0,
        "cuoco": 0,
        "navigatore": 0
    }
    marinario=0
    while marinario<1:
        print("quanti marinai vuoi?")
        marinario=int(input())
        eq["marinaio"]=marinario
    meccanico=0
    while meccanico<1:
        print("quanti meccanici vuoi?")
        meccanico=int(input())
        eq["meccanico"]=meccanico
    medico=0
    while medico<1:
        print("quanti medici vuoi?")
        medico=int(input())
        eq["medico"]=medico
    cuoco=0
    while cuoco<1:
        print("quanti cuochi vuoi?")
        cuoco=int(input())
        eq["cuoco"]=cuoco
    navigatore=0
    while navigatore<1:
        print("quanti navigatori vuoi?")
        navigatore=int(input())
        eq["navigatore"]=navigatore
    return eq

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