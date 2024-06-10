from models.tec import tec
from models.lære import Lære

import os

tec_instance = tec()
lære_list = tec_instance.hent_lære_fra_csv()



while True:
    print("\n-----------------------------")
    print("Velkommen til lærerregisteret\n")
    print("[1] Registrer lærer")
    print("[2] Opdater lærer")
    print("[3] Vis liste af alle lærere")
    print("[4] Gem og afslut")
    valg = input("Vælg 1, 2, 3 eller 4: ")

    if valg == '1':
        os.system('cls')
        print("Reistrer lærer:")
        forNavn = input("Navn: ")
        efterNavn = input("Efternavn: ")
        

        print(f"\nVælg et fag til {forNavn} {efterNavn}")
        for subject in tec_instance.fag_liste:
           print(f"{subject.index}" + subject)



        # lære_list.append(Lære(forNavn, efterNavn))        
        # tec_instance.gem_lære()
          
    elif valg == '2':
        pass
        
    elif valg == '3':
        print("valg 3")
    elif valg == '4':
        print("valg 4")
        exit()
    else:
        print("Ugyldigt valg. Prøv igen.")