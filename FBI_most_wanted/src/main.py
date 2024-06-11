from data_fetcher import fetch_data
from save_to_csv import save_to_csv, update_csv_row
import threading
import time
import datetime


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
        if len(person_list) == 0:
            print("No missing persons found.")
            
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

def schedule_main():
    while True:
        now = datetime.datetime.now() # Get the current time
        next_run = now.replace(hour=10, minute=00, second=0, microsecond=0) # Set the next run time to 10:00 AM

        if now >= next_run: # If the current time is past 10:00 AM, set the next run to the next day
            next_run += datetime.timedelta(days=1) # Add one day to the next run time

        time_to_wait = (next_run - now).total_seconds() # Calculate the time to wait in seconds
        print(f"Waiting for {time_to_wait / 60:.2f} minutes until next run at 10:00 AM")

        time.sleep(time_to_wait) # Wait until the next run time

        print("Running main() at 10:00 AM")
        main_thread = threading.Thread(target=main, name='MainThread') # Create a new thread to run main
        main_thread.start() # Start the thread
        main_thread.join() # Wait for the thread to finish

if __name__ == "__main__":
    # Run the main function immediately
    main_thread = threading.Thread(target=main, name='MainThread') # Create a new thread to run main
    main_thread.start() # Start the thread

    # Start the scheduling thread to run main at 5:00 AM daily
    schedule_thread = threading.Thread(target=schedule_main, name='ScheduleThread') # Create a new thread to run the schedule_main
    schedule_thread.start() # Start the thread

    # Join the main thread to keep the program running
    main_thread.join() # Wait for the main thread to finish
    schedule_thread.join() # Wait for the schedule thread to finish



