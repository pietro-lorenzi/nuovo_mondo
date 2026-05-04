# Uma lo so che questa è la tua parte, però volevo portarmi un po' avanti e ho creato queste
# funzioni finte che mi restituiscono dei valori standard, in modo che possa lavorare
# alla mia parte senza doverti aspettare per forza
#
# Quando vorrai lavorare elimina pure queste funzioni
#
### IMPORTANTE ###
# Tutta la fase di ingaggiamento dell'equipaggio, acquisto merci e acquisto provviste devono essere dentro una funzione a testa
# e alla fine deve restituire un dizionario, proprio come vedi nelle mie funzioni mock
print("\033[94m" + "-----INGAGGIO EQUIPAGGIO-----" + "\033[0m")
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
            try:
                marinaio=int(input("\033[93m" + "quanti marinai vuoi?" + "\033[0m"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        meccanico=0
        while meccanico<1:
            try:
                meccanico=int(input("quanti meccanici vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        medico=0
        while medico<1:
            try:
                medico=int(input("quanti medici vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))
        cuoco=0
        while cuoco<1:
            try:
                cuoco=int(input("quanti cuochi vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))     
        navigatore=0
        while navigatore<1:
            try:
                navigatore=int(input("quanti navigatori vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
        tot=marinaio+meccanico+medico+cuoco+navigatore

        if tot > 16:
            print("\033[91m" + "hai superato il numero massimo di equipaggio" + "\033[0m")
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
            try:
                verdura=int(input("quanta verdura vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            frutta=0
            try:
                frutta=int(input("quanta frutta vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            carne=0
            try:
                carne=int(input("quanta carne vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            acqua=0
            try:
                acqua=int(input("quanti barili di acqua vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   

            costo_verdura=verdura*0.5
            monete=monete-costo_verdura

            costo_frutta=frutta*1
            monete=monete-costo_frutta

            costo_carne=carne*2
            monete=monete-costo_carne

            costo_acqua=acqua*0.5
            monete=monete-costo_acqua
            
            if monete<0:
             print("\033[91m" + "sei andato in bancarotta" + "\033[0m")
            else:
                spesa=True
    return proviste, monete


def merci_eq():
    merci= {
        "medicinali": 0,
        "armi": 0,
        "sale": 0,
        "stoffa": 0,
        "coltelli":0,
        "diamanti":0,
}
    monete=2000
    spesa=False
    while not spesa:
            medicinali=0
            try:
                medicinali=int(input("quanti medicinali vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            armi=0
            try:
                armi=int(input("quante armi vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            sale=0
            try:
             sale=int(input("quanto sale vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            stoffa=0
            try:
             stoffa=int(input("quanta stoffa vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            coltelli=0
            try:
             coltelli=int(input("quanti coltelli vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   
            
            diamanti=0
            try:
             diamanti=int(input("quanti diamanti vuoi?"))
            except:
                print(("\033[91m" + "inserire un numero valido" + "\033[0m"))   

            costo_med=medicinali*1
            monete=monete-costo_med

            costo_armi=armi*5
            monete=monete-costo_armi

            costo_sale=sale*0.5
            monete=monete-costo_sale

            costo_stoffa=stoffa*2
            monete=monete-costo_stoffa
            
            costo_coltelli=coltelli*0.5
            monete=monete-costo_coltelli

            costo_diamanti=diamanti*1
            monete=monete-costo_diamanti
            
            if monete<0:
             print("\033[91m" + "sei andato in bancarotta" + "\033[0m")
            else:
                spesa=True
    return merci, monete



ingaggia_equipaggio_mock()
proviste_eq()
merci_eq()

