import csv
from models.lære import Lære

class tec:
    def __init__(self, ):
        self.lære_liste = self.hent_lære_fra_csv()
        self.fag_liste = ['IoT Embedded', 'Python', 'BigData 1', 'SoftwareSikkerhed og test', 'ServersideProgrammering']
        self.file_path = 'objekt_og_instanser/data/lære.csv'
        
        

    def registere_lære(self, Lære):
        lære_liste = self.hent_lære_fra_csv()
        lære_liste.append(Lære)
        return lære_liste


    def gem_lære(self, liste):
        # Write lære_liste to file lære.csv
        

        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(['first_name', 'last_name', 'fag'])

            for lære in liste:
                fag_str = '-'.join(lære.fag) if lære.fag else ''
                writer.writerow([lære.first_name, lære.last_name, fag_str])
        

    def hent_lære_fra_csv(self):
        # Define the path to the CSV file
        file_path = 'objekt_og_instanser/data/lære.csv'
        
        lære_liste = []

        # Open the file in read mode
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skips reader
            
            # Read each row and create a Lære object
            for row in reader:
                first_name, last_name, fag_str = row
                # if fag_str.strip():  
                #     fag = [f.strip() for f in fag_str.split(' ') if f.strip()]
                # else:
                #     fag = []
                fag = fag_str.split('-')
                lære_liste.append(Lære(first_name, last_name, fag))  # Use 0 for id since it's not in the CSV

        return lære_liste

    def opdatere_lære_csv(self, row_index, lære):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            rows[row_index] = [lære.first_name, lære.last_name, lære.fag]
        
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def print_fag_ud(self, *args):
        lære_list = []
        if len(args) == 3:
            fornavn, efternavn, liste = args
        else:
            ny_lære, liste = args
        
        print(f"\nVælg et fag til {fornavn} {efternavn}")
        for index, fag in enumerate(liste, start=1):
            print(f"{index}: {fag}")

            while True:
                valgt_fag = input("Vælg et fag fra listen: (0 for at afbryde)")
                if valgt_fag.isdigit():
                    valgt_fag = int(valgt_fag)

                    if valgt_fag == 0:
                        print("\nGoing back to main menu.")
                        break  # Går ud af loop og tilbage til forrige menu

                    elif 1 <= valgt_fag <= len(liste):
                        ny_lære.fag = [liste[valgt_fag-1]]
                        print(f"{ny_lære.first_name} {ny_lære.last_name} er nu opetter med følgende fag:")
                        print(f"\t-{ny_lære.fag}")
                        lære_list.append(ny_lære)
                        break

                else:              
                    print("Forkert indtastning, prøv igen:")
                    
        return lære_list

