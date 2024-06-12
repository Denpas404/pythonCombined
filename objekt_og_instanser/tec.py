import csv
import os
from models.teacher import Teacher

class Tec:
    def __init__(self, ):
        self.teacher_list = self.load_teacher()
        self.subject_list = ['IoT Embedded', 'Python', 'BigData 1', 'SoftwareSikkerhed og test', 'ServersideProgrammering']

    def create_teacher(self, tec):
        first_name = input("Enter teacher's first name: ")
        last_name = input("Enter teacher's last name: ")
        
        for index, subject in enumerate(self.subject_list, start=1):
            print(f"[{index}]: {subject}")
            
        while True:
            user_input =input("Choose a subject to add to the teacher, (press 0 to cancel): ")
            if user_input.isdigit():
                user_input = int(user_input)

                if user_input == 0:
                    print("Returning to previous menu")
                    break
                elif 1 <= user_input <= len(self.subject_list):
                    new_subject = self.subject_list[user_input-1]
                    print(f"{first_name} {last_name} er nu opetter med følgende fag:")
                    print(f"\t-{new_subject}")
                    self.teacher_list.append(Teacher(first_name,last_name, [subject]))
                    break
                else:
                    print("Invalid input, try again")
            
            else:
                print("Invalid input, try again")
        
        new_teacher = Teacher(first_name, last_name, [subject])
        self.teacher_list.append(new_teacher)
        
        return new_teacher

    def update_teacher(self, tec):
        if len(tec.teacher_list) <=0:
            print("\nThere are no teachers to update")           
            return
        else:
            print("\n\tList of all teachers:")
            for i, teacher in enumerate(tec.teacher_list, 1):
                print(f"[{i}] {teacher.first_name} {teacher.last_name}")
            
            while True:
                teacher_number = input("Choose a teacher from the list: ")
                if teacher_number.isdigit():
                    teacher_number = int(teacher_number)

                    if teacher_number == 0:
                        print("Returning to previous menu")
                        break
                    if 1 <= teacher_number <= len(tec.teacher_list):
                        selected_teacher = tec.teacher_list[teacher_number-1]                        

                        edit_choice = 999
                        os.system('cls')    
                        while True:                
                            try:
                                print(f"what do you want to do with {selected_teacher.first_name} {selected_teacher.last_name}:")
                                edit_choice = int(input("[1] Add a subject\n[2] Remove a subject\n[0] Return to previous menu: "))
                            except:
                                print("Invalid input, try again")

                            if edit_choice == 0:
                                break

                            elif edit_choice == 1:
                                os.system('cls')
                                print("Add a subject\n")                                
                                self.print_all_subjects(selected_teacher, tec.subject_list)
                                
                                
                                break
                                
                            elif edit_choice == 2:
                                print("Remove a subject")
                                self.print_all_subjects(selected_teacher)
                                break
                            else:
                                print("Invalid input, try again")
                        break
                        
                    else:
                        print("Invalid input, try again")

    def show_teachers(self, tec):
        if len(self.teacher_list) <= 0:
            print("\nThere are no teachers in the list")
        else:
            for teacher in tec.teacher_list:  
                print(f"\n{teacher.first_name} {teacher.last_name}:")
                for subject in teacher.subject:
                    print(f"\t-{subject}")      

    def save_teacher(self, tec):
        file_path = 'objekt_og_instanser/lære.csv'
        with open(file_path, 'w', newline='') as file:
            # writer = csv.DictWriter(file, fieldnames=["first_name","last_name","fag"])

            # writer.writeheader
            write = csv.writer(file)

            write.writerow(["first_name","last_name","fag"])
            
            for teacher in self.teacher_list:
                subject_string = ""
                for subject in teacher.subject:
                    subject_string += subject+"-"
                
                subject_string = subject_string[:-1]
                write.writerow([teacher.first_name, teacher.last_name, subject_string] )


    def load_teacher(self, ):
        # Define the path to the CSV file
        file_path = 'objekt_og_instanser/lære.csv' 
        new_teacher_list = []
        # Open the file in read mode
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skips reader
            
            # Read each row and create a Lære object
            for row in reader:
                first_name, last_name, fag_str = row
                fag = fag_str.split('-')
                
                new_teacher = Teacher(first_name, last_name, fag)
                new_teacher_list.append(new_teacher)

            return new_teacher_list
    
    def print_all_subjects(self, *args):
        if len(args) == 2:
            teacher, subject_list = args
            new_subject_list = []
            
            
            print(f"{teacher.first_name} {teacher.last_name} has following subjects:")
            for subject in teacher.subject:                
                    print(f"\t-{subject}")
            for subjects in subject_list:
                if subjects not in teacher.subject:
                    new_subject_list.append(subjects)
                    
            print(f"\nWhich other subject would you add to {teacher.first_name} {teacher.last_name}: ")
            for index, subjects in enumerate(new_subject_list, start=1):
                print(f"{index} {subjects}")

            choice = 0
            while True:                
                try:
                    choice = int(input(f"select a subject to add - Press[0] to return to previous menu: "))
                except:
                    print("Invalid input, try again")

                if choice == 0:
                    break
                    
                elif 1 <= choice <= len(new_subject_list):
                    new_subject = new_subject_list[choice-1]
                    print(f" {new_subject} has been added to {teacher.first_name} {teacher.last_name}'s subjects")
                    print(f"\t-{new_subject}")

                    teacher.add_subject(new_subject)
                    break

            
        else:
            teacher = args[0]
            for index, subject in enumerate(teacher.subject, start=1):
                print(f"[{index}]: {subject}")

            choice = 0 
            while True:
                try:
                    choice = int(input("Choose a subject to remove from: (Press 0 to cancel)"))
                except:
                    print("Invalid input, try again")

                if choice == 0:
                    break

                elif 1 <= choice <= len(teacher.subject):
                    teacher.subject.pop(choice-1)
                    break
                
                else:
                    print("Invalid input, try again")

