from models.tec import tec
from models.lære import Lære

import os

def main():
    global tec_instance
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

            lære_list= print_fag_ud(forNavn, efterNavn, lære_list, fag_list)   
        

        elif valg == '2': # Opdatere en lære
            os.system('cls')
            print("\n Vælg en lære og opdater: ")
            for index, lære in enumerate(lære_list, start=1): # Udskriver lære fra lære_list
                print(f"[{index}] {lære.first_name} {lære.last_name}")
            
            valgt_lære = input("Valg: ")
            while True:
                if valgt_lære.isdigit():
                    valgt_lære = int(valgt_lære)

                    if valgt_lære == 0:
                        print("Opdatering annulleret!")
                        break
                    elif 1 <= valgt_lære <= len(lære_list):                    
                        lære = lære_list[valgt_lære-1]

                        while True:
                            valgt_opdatering = input("\n[1] Tilføj fag\n[2] slet fag\n[0] Tilbage\nVælg: ")
                            if valgt_opdatering.isdigit():
                                valgt_opdatering = int(valgt_opdatering)

                                if valgt_opdatering == 0:
                                    print("\nGoing back to main menu.")
                                    opdatering_fuldført = True
                                    break  # Går ud af loop og tilbage til forrige menu
                            
                                elif valgt_opdatering == 1:                                   
                                    lære_list = print_fag_ud(lære, lære_list, fag_list)
                                    opdatering_fuldført = True
                                    break

                                elif valgt_opdatering == 2:
                                    print("Slet fag fra lære: ")
                                    lære_list = print_fag_ud(lære, lære_list, fag_list, "slet", "slet")
                                    opdatering_fuldført = True
                                    break
                                
                                else:
                                    print("Ugyldigt valg. Prøv igen.")


                if opdatering_fuldført:
                    break


        elif valg == '3':        
            os.system("cls")
            print("\nList af lære: \n")
            if len(lære_list) < 1:
                print("Der er ingen lære oprettet!!")
            else:
                for lære in lære_list:
                    print(f"{lære.first_name} {lære.last_name}")
                    for fag in lære.fag:
                        print(f"\t-{fag}")
                    print()

            
        elif valg == '4':
            tec_instance.gem_lære(lære_list)
            exit()
        else:
            print("Ugyldigt valg. Prøv igen.")



def print_fag_ud(*args):
    global tec_instance
    

    # Hvis metoden's parameter = 4 (for og efternan, lære_liste, liste(fag))
    if len(args) == 4:
        forNavn, efterNavn, lære_list,  liste = args
        
        ny_lære = Lære(forNavn, efterNavn)   

        print_list(liste)

        while True:
            valgt_fag = input("Vælg et fag fra listen: (0 for at afbryde)")
            if valgt_fag.isdigit():
                valgt_fag = int(valgt_fag)

                if valgt_fag == 0:
                    print("\nReturner til hovedmenu.")
                    break  # Går ud af loop og tilbage til forrige menu

                elif 1 <= valgt_fag <= len(liste):
                    ny_lære.fag = liste[valgt_fag-1]
                    print(f"{ny_lære.first_name} {ny_lære.last_name} er nu opetter med følgende fag:")
                    print(f"\t-{ny_lære.fag}")
                    lære_list.append(ny_lære)

                    return lære_list

            else:              
                print("Forkert indtastning, prøv igen:")

    # Hvis metodens parameter er = 3 (lære, lære_liste,  liste(fag))
    elif len(args) == 3:
        lære_der_opdateres, lære_list, liste = args            

        # print(f"\nVælg et fag til {lære_der_opdateres.first_name} {lære_der_opdateres.last_name}")        
        liste = print_list(lære_der_opdateres, liste)

        while True:
            nyt_fag = input("Vælg et fag fra listen: (0 for at afbryde)")
            if nyt_fag.isdigit():
                nyt_fag = int(nyt_fag)

                if nyt_fag == 0:
                    print("\nReturner til hovedmenu.")
                    break # Går ud af loop og tilbage til forrige menu

                elif 1 <= nyt_fag <= len(liste):                    
                    nyt_valg_fag = liste[nyt_fag-1]
                    
                    print(f"{lære_der_opdateres.first_name} {lære_der_opdateres.last_name} er nu tilmeld følgende fag:")
                    for lære in lære_list:
                        if lære.first_name == lære_der_opdateres.first_name and lære.last_name == lære_der_opdateres.last_name:
                            lære.fag.append(nyt_valg_fag)
                            lære_der_opdateres = lære
                    for fag in lære_der_opdateres.fag:
                        print(fag)
                    
                    return lære_list
    
    elif len(args) == 5:
        lære_der_opdateres, lære_list, liste, ignor1, ignor2 = args 

        liste = print_list(lære_der_opdateres, liste, ignor1)

        while True:
            index_der_slettes = input("Vælg et fag fra listen (0 for at afbryde): ")
            if index_der_slettes.isdigit():
                index_der_slettes = int(index_der_slettes)



                if index_der_slettes == 0:
                    print("\nReturner til hovedmenu.")
                    break # Går ud af loop og tilbage til forrige menu

                elif 1 <= index_der_slettes <= len(liste):
                    print(f"\n{lære_der_opdateres.first_name} {lære_der_opdateres.last_name} er nu frameldt: -{liste[index_der_slettes-1]}:")
                    slette = liste[index_der_slettes-1]
                    
                    for lære in lære_list:
                        if lære.first_name == lære_der_opdateres.first_name and lære.last_name == lære_der_opdateres.last_name:
                            lære.fag.remove(liste[index_der_slettes-1])
                            lære_der_opdateres = lære                    
                    return lære_list





                    return lære_list



        
        return lære_list


def print_list(*args):
        
    if len(args) == 2:
        læren, liste = args
        ny_fag_liste =[]
        print(f"\n{læren.first_name} {læren.last_name} har følgende fag: ")
        for fag in læren.fag:
            print(f"\t- {fag}")
        print("\nHvilket fag vil du tilføje ", læren.first_name, læren.last_name)
        for index, fag_i_fagListe in enumerate(liste, start=1):
            if fag_i_fagListe not in læren.fag:
                ny_fag_liste.append(fag_i_fagListe)

        for index, fag in enumerate(ny_fag_liste, start=1):
            print(f"{index}: {fag}")       
            
        return ny_fag_liste
    
    elif len(args) == 3:
        læren, liste, ignor = args
        ny_fag_liste =[]
        
        print("\nHvilket fag vil du slette fra", læren.first_name, læren.last_name)
        for index, fag_i_fagListe in enumerate(liste, start=1):
            if fag_i_fagListe in læren.fag:
                ny_fag_liste.append(fag_i_fagListe)

        for index, fag in enumerate(ny_fag_liste, start=1):
            print(f"{index}: {fag}")       
            
        return ny_fag_liste
    
    else:
        for index, fag in enumerate(args, start=1):
            print(f"{index}: {fag}")    




if __name__ == "__main__":
    main()