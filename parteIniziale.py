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
    massimo=False
    while not massimo:
        marinaio=0
        while marinaio<1:
            print("quanti marinai vuoi?")
            marinaio=int(input())
            eq["marinaio"]=marinaio
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
        tot=marinaio+meccanico+medico+cuoco+navigatore

        if tot > 16:
            print("hai superato il numero massimo di equipaggio")
        else:
            massimo=True
    return eq

def proviste_eq():
    proviste= {
        "verdura": 0,
        "frutta": 0,
        "carne": 0,
        "acqua": 0,
}
    monete=2000
    spesa=False
    while not spesa:
            verdura=0
            print("quanta verdura vuoi?")
            verdura=int(input())
            proviste["verdura"]=verdura
            
            frutta=0
            print("quanta frutta vuoi?")
            frutta=int(input())
            proviste["frutta"]=frutta
            
            carne=0
            print("quanta carne vuoi?")
            carne=int(input())
            proviste["carne"]=carne
            
            acqua=0
            print("quanti barili di acqua vuoi?")
            acqua=int(input())
            proviste["acqua"]=acqua

            costo_verdura=verdura*0.5
            monete=monete-costo_verdura

            costo_frutta=frutta*1
            monete=monete-costo_frutta

            costo_carne=carne*2
            monete=monete-costo_carne

            costo_acqua=acqua*0.5
            monete=monete-costo_acqua
            
            if monete<0:
             print("sei andato in bancarotta")
            else:
                spesa=True
    return proviste, monete





ingaggia_equipaggio_mock()
proviste_eq()

