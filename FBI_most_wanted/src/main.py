from data_fetcher import fetch_data
from save_to_csv import save_to_csv, update_csv_row

def main():
    while True:
        missing_person_list, gang_member_list = fetch_data()
        
        print("\nPress 1 to show missing persons")
        print("Press 2 to show gang members")
        print("Press 3 to exit")
    
        choice = input("Enter your choice: ")

        
        if choice == '1':            
            missing_person_list = edit_person(missing_person_list, "missing_person")

        elif choice == '2':            
            gang_member_list = edit_person(gang_member_list, "gang_member")

            
        elif choice == '3':
            print("Exiting program.")
            exit()
        else:
            print("Invalid choice. Please try again.")


def edit_person(person_list, data_type):
    print(f"\n{data_type.capitalize()}:")

    if data_type == "missing_person":
        for index, person in enumerate(person_list, start=1):
            print(f'[{index}], Name: {person.first_name} {person.last_name}, Last Seen: {person.last_seen}\n')
            if index > 9:
                break
    elif data_type == "gang_member":
        for index, person in enumerate(person_list, start=1):
            print(f'[{index}], Name: {person.first_name} {person.last_name}, Gang Name: {person.gang_name}\n')
            if index > 9:
                break
            
    while True:
        person_to_edit = input("Enter the number of the person you want to edit or press 0 to go back: ")
        if person_to_edit.isdigit():
            person_to_edit = int(person_to_edit)

            if person_to_edit == 0:
                print("\nGoing back to main menu.")
                break  # Exit the loop and go back to the main menu

            elif 1 <= person_to_edit <= len(person_list):

                if data_type == "missing_person":
                    print("Editing person: ", person_list[person_to_edit - 1].first_name, person_list[person_to_edit - 1].last_name)
                    new_last_seen = input("Enter new last seen date: ")
                    # Update the person in the list
                    person_list[person_to_edit - 1].last_seen = new_last_seen
                    updated_person = person_list[person_to_edit - 1]                    
                    update_csv_row(updated_person, "missing_person", person_to_edit)

                elif data_type == "gang_member":
                    print("Editing person: ", person_list[person_to_edit - 1].first_name, person_list[person_to_edit - 1].last_name)
                    new_gang_name = input("Enter new gang name: ")
                    # Update the person in the list
                    person_list[person_to_edit - 1].gang_name = new_gang_name
                    updated_person = person_list[person_to_edit - 1]
                    update_csv_row(updated_person, "gang_member", person_to_edit)

                break  # Exit the loop and go back to the main menu

            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__": 
    main()




# if choice == '1':
        #     missing_person_list = fetch_data("missing_person")
        #     print("\nMissing Persons:")

        #     # Printing the list with index
        #     for index, missing_person in enumerate(missing_person_list, start=1):
        #         print(f'[{index}], Name: {missing_person.first_name} {missing_person.last_name}, Last Seen: {missing_person.last_seen}\n')

        #     person_to_edit = input("Enter the number of the person you want to edit or press 0 to go back: ")
        #     if person_to_edit.isdigit():
        #         person_to_edit = int(person_to_edit)
        #         if person_to_edit == 0:
        #             print("\nGoing back to main menu.")
        #             continue  # Go back to the last menu
        #         if person_to_edit < 1 or person_to_edit > len(missing_person_list):
        #             print("Invalid input. Going back to main menu.")
        #             continue
        #         else:
        #             print("Editing person: ", missing_person_list[person_to_edit - 1].first_name, missing_person_list[person_to_edit - 1].last_name)
        #             new_last_seen = input("Enter new last seen date: ")
        #             # update the person in the list
        #             missing_person_list[person_to_edit - 1].last_seen = new_last_seen
        #             updated_person = missing_person_list[person_to_edit - 1]
        #             update_csv_row(updated_person, "missing_person", person_to_edit)

        # elif choice == '2':
        #     gang_member_list = fetch_data("gang_member")
        #     print("\nGang Members:")