from data_fetcher import fetch_data
from save_to_csv import save_to_csv

while True:
    print("\nPress 1 to show missing persons")
    print("Press 2 to show gang members")
    print("Press 3 to exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        missing_person_list = fetch_data("missing_person")
        print("\nMissing Persons:")

        for missing_person in missing_person_list:
            print("ID: " + missing_person.id)            
            print("Name: " + missing_person.first_name, missing_person.last_name)
            print("Details: " + missing_person.details)
            missing_person.last_seen = input("Enter last seen: ")
            print("Last Seen: " + missing_person.last_seen)
            print("\n")
            # save last seen to csv file
            if save_to_csv(missing_person_list, "missing_person"):
                print("Data saved to missing_persons.csv")
            else:
                print("Error saving data to missing_persons.csv")

    elif choice == '2':
        gang_member_list = fetch_data("gang_member")
        print("\nGang Members:")

        for gang_member in gang_member_list:
            print("Name: " + gang_member.first_name, gang_member.last_name)
            print("Caution: " + gang_member.caution)
            gang_member.gang_name = input("Enter gang name: ")
            print("Gang Name: " + gang_member.gang_name)
            print("\n")
            
            # save gang name to csv file
            if save_to_csv(gang_member_list, "gang_member"):
                print("Data saved to gang_members.csv")
            else:
                print("Error saving data to gang_members.csv")

        
    elif choice == '3':
        print("Exiting program.")
        exit()
    else:
        print("Invalid choice. Please try again.")
