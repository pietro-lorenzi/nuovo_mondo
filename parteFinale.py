#la nave si avvicina alle coste 

#RichiestaFuoco
def RichiestaFuoco(DictArmi):
    errore = True
    for arma in DictArmi.keys():
        if DictArmi[arma] > 0: #la quantità di quell'arma
            while errore:
                try:
                    richiestaFuoco = input("Vuoi fare fuoco contro gli indigeni? (s/n)>> ")

                    match richiestaFuoco:
                        case "s":
                            return True
                        case "n":
                            return False
                        case _:
                            print("Devi inserire una delle 2 opzioni precedenti!")
                except:
                    print("Devi inserire una delle 2 opzioni precedenti!")

    else:
        return False        
    

#Baratto
def Baratto(DictRisorse):
    print("Puoi barattare solo sale, stoffa, coltelli e diamanti.")
    for risorsa in DictRisorse.keys():
        if DictRisorse[risorsa] > 0:
           match risorsa:
                case "sale": #1 opzione
                   errore = True
                   while errore:
                        try:
                            print("""Le opzioni scambio con il sale cono queste:
1) 1 perla = 0.5 sacchi di sale;
2) 1 manufatto = 0.5 sacchi di sale;
3) 1 barattolo di spezie = 1 sacco di sale.""")
                            
                            opzioneScelta = int(input("Cosa vorresti fare?>> "))
                            
                            match  opzioneScelta:
                                case 1:
                                    pass
                                
                                case 2:
                                    pass

                                case 3:
                                    pass

                                case _:
                                    print("Devi inserire una delle opzioni precedenti!")
                        except:
                            print("Devi inserire una delle opzioni precedenti!")

                case "sale": #2 opzione
                   errore = True
                   while errore:
                        try:
                            print("""Le opzioni scambio con il sale cono queste:
1) 1 perla = 0.5 sacchi di sale;
2) 1 manufatto = 0.5 sacchi di sale;
3) 1 barattolo di spezie = 1 sacco di sale.""")
                            
                            opzioneScelta = int(input("Cosa vorresti fare?>> "))
                            
                            match  opzioneScelta:
                                case 1:
                                    pass
                                
                                case 2:
                                    pass

                                case 3:
                                    pass

                                case _:
                                    print("Devi inserire una delle opzioni precedenti!")
                        except:
                            print("Devi inserire una delle opzioni precedenti!")

                case "sale": #3 opzione
                   errore = True
                   while errore:
                        try:
                            print("""Le opzioni scambio con il sale cono queste:
1) 1 perla = 0.5 sacchi di sale;
2) 1 manufatto = 0.5 sacchi di sale;
3) 1 barattolo di spezie = 1 sacco di sale.""")
                            
                            opzioneScelta = int(input("Cosa vorresti fare?>> "))
                            
                            match  opzioneScelta:
                                case 1:
                                    pass
                                
                                case 2:
                                    pass

                                case 3:
                                    pass

                                case _:
                                    print("Devi inserire una delle opzioni precedenti!")
                        except:
                            print("Devi inserire una delle opzioni precedenti!")

                case "sale": #4 opzione
                   errore = True
                   while errore:
                        try:
                            print("""Le opzioni scambio con il sale cono queste:
1) 1 perla = 0.5 sacchi di sale;
2) 1 manufatto = 0.5 sacchi di sale;
3) 1 barattolo di spezie = 1 sacco di sale.""")
                            
                            opzioneScelta = int(input("Cosa vorresti fare?>> "))
                            
                            match  opzioneScelta:
                                case 1:
                                    pass
                                
                                case 2:
                                    pass

                                case 3:
                                    pass

                                case _:
                                    print("Devi inserire una delle opzioni precedenti!")
                        except:
                            print("Devi inserire una delle opzioni precedenti!")
                            
    else:
        return False
            