import sys
import time

def stampa(testo, delay=0.03): #funzione per stampare il testo lentamente, in modo più figo
    for i in testo:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    print()