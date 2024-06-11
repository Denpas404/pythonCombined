from models.tec import tec
from models.lære import Lære

import os

def main():
    tec_instance = tec()
    fag_list = tec_instance.fag_liste
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
            print("Registrer lærer:")
            forNavn = input("Navn: ")
            efterNavn = input("Efternavn: ")  

            ny_lære = Lære(forNavn, efterNavn)      

            # print(f"\nVælg et fag til {forNavn} {efterNavn}")
            # for index, fag in enumerate(fag_list, start=1):
            #     print(f"{index}: {fag}")

            # while True:
            #     valgt_fag = input("Vælg et fag fra listen: (0 for at afbryde)")
            #     if valgt_fag.isdigit():
            #         valgt_fag = int(valgt_fag)

            #         if valgt_fag == 0:
            #             print("\nGoing back to main menu.")
            #             break  # Går ud af loop og tilbage til forrige menu

            #         elif 1 <= valgt_fag <= len(fag_list):
            #             ny_lære.fag = [fag_list[valgt_fag-1]]
            #             print(f"{ny_lære.first_name} {ny_lære.last_name} er nu opetter med følgende fag:")
            #             print(f"\t-{ny_lære.fag}")
            #             lære_list.append(ny_lære)
            #             break

            #     else:              
            #         print("Forkert indtastning, prøv igen:")

        elif valg == '2':
            valg = input("[1] Tilføj fag\n[2] slet fag\n[0] Tilbage\nVælg: ")
            while True:
                if valg.isdigit():
                    valg = int(valg)

                    if valg == 0:
                            print("\nGoing back to main menu.")
                            break  # Går ud af loop og tilbage til forrige menu
                    
                    elif valg == 1:
                        for fag in fag_list:
                            
                            print()

        elif valg == '3':        
            os.system("cls")
            print("\nList af lære: \n")
            if len(lære_list) < 1:
                print("Der er ingen lære oprettet!!")
            else:
                for lære in lære_list:
                    print(f"{lære.first_name} {lære.last_name}")
                    for fag in lære.fag:
                        print(f"\t{fag}")
                    print()

            
        elif valg == '4':
            tec_instance.gem_lære(lære_list)
            exit()
        else:
            print("Ugyldigt valg. Prøv igen.")

if __name__ == "__main__":
    main()