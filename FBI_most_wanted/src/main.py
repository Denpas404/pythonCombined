from data_fetcher import main_fetch_data
from save_to_csv import update_csv_row
from delete_data_files import delete_data_files
import threading
import time
import datetime
import os


def main():
    
    while True:

        
        
        missing_person_list, gang_member_list = main_fetch_data()
        
        


        if not missing_person_list and not gang_member_list:
            print("\nNo data was found in the CSV files, and access to the API is currently unavailable.")
            print("\nExiting program.\n")
            os._exit(0)
            
        else:
            print("\nPress 1 to show missing persons")
            print("Press 2 to show gang members")
            print("Press 3 to Delete data files")
            print("Press 4 to exit")
        
            choice = input("Enter your choice: ")

            
            if choice == '1':            
                missing_person_list = edit_person(missing_person_list, "missing_person")

            elif choice == '2':            
                gang_member_list = edit_person(gang_member_list, "gang_member")

            elif choice == '3':
                while True:
                    confirm = input("Are you sure you want to delete the data files?\nType 'yes' to confirm\nType 'no' to cancel\n")
                    result = delete_data_files(confirm)    

                    if result == "yes":                        
                        print("Data files deleted. Exiting program.")
                        print("Creating new data files.")
                        break
                    elif result == "no":
                        print("Deletion cancelled.")
                        break
                    else:
                        print(result)  # This will print the invalid input message


            elif choice == '4':
                print("Exiting program.")
                quit()
            else:
                print("Invalid choice. Please try again.")



def edit_person(person_list, data_type):
    bool_loop = True
    print(f"\n{data_type.capitalize()}:")

    if data_type == "missing_person":
        if len(person_list) == 0:
            print("No missing persons found.")
            bool_loop = False            
        else:
            for index, person in enumerate(person_list, start=1):
                print(f'[{index}], Name: {person.first_name} {person.last_name}, Last Seen: {person.last_seen}\n')
                if index > 9:
                    break
    elif data_type == "gang_member":
        if len(person_list) == 0:
            print("No gang members found, its' a peaceful world now")
        else:
            for index, person in enumerate(person_list, start=1):
                print(f'[{index}], Name: {person.first_name} {person.last_name}, Gang Name: {person.gang_name}\n')
                if index > 9:
                    break
            
    while bool_loop:
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

def schedule_main(initial_event):
    while True:
        now = datetime.datetime.now() # Get the current time
        next_run = now.replace(hour=10, minute=0, second=0, microsecond=0) # Set the next run time to 10:00 AM

        if now >= next_run: # If the current time is past 10:00 AM, set the next run to the next day
            next_run += datetime.timedelta(days=1) # Add one day to the next run time

        time_to_wait = (next_run - now).total_seconds() # Calculate the time to wait in seconds
        print(f"Waiting for {time_to_wait / 60:.2f} minutes until next run at 10:00 AM")

        if initial_event:
            initial_event.set()  # Signal that the initial print is done

        time.sleep(time_to_wait) # Wait until the next run time

        print("Running main() at 10:00 AM")

if __name__ == "__main__":
    initial_event = threading.Event()

    # Run the schedule_main function in a new thread
    schedule_thread = threading.Thread(target=schedule_main, args=(initial_event,), name='ScheduleThread')
    schedule_thread.start()

    # Wait for the initial event before running main
    initial_event.wait()  # Wait for the event to be set by schedule_main

    # Run the main function
    main_thread = threading.Thread(target=main, name='MainThread')
    main_thread.start()

    # Join the main and schedule threads to keep the program running
    main_thread.join()
    schedule_thread.join()