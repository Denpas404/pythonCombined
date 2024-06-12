from tec import Tec
from models.lære import Lære

import os

def main():
    tec = Tec()    

    while True:
        print("\n-----------------------------")
        print("Welcome to the teacher register\n")
        print("[1] Register teacher")
        print("[2] Update teacher")
        print("[3] Show list of all teachers")
        print("[4] Save and exit")
        print("[0] Exit without saving")
        choice = input("Choose 1, 2, 3, 4 or 0 for exit: ")


        if choice == '1':
            os.system('cls')
            print("Registrer teacher:")
            tec.create_teacher(tec) 

        elif choice == '2': 
            os.system('cls')
            tec.update_teacher(tec)
            

        elif choice == '3':        
            os.system("cls")
            print("\nList of teachers: \n")
            tec.show_teachers(tec)

        elif choice == '4':        
            os.system("cls")
            print("\nSave and exit program.")
            tec.save_teacher(tec)
            print("Farvel!")
            break

        elif choice == '0':
            exit()

        else:
            print("Invalid input, try again.")



if __name__ == "__main__":
    main()