import csv
import os

def determine_file_path(data_type):
    # Bestem filstien baseret på datatype
    if data_type == "missing_person":
        return "FBI_most_wanted/data/missing_persons.csv"        
    elif data_type == "gang_member":
        return "FBI_most_wanted/data/gang_members.csv"    


def does_files_exist_else_create_csv_file():
    missing_persons_path = "FBI_most_wanted/data/missing_persons.csv"
    gang_members_path = "FBI_most_wanted/data/gang_members.csv"
    
    # Check and create missing_persons.csv if it doesn't exist
    if not os.path.exists(missing_persons_path):
        with open(missing_persons_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Name", "Aliases", "Details"])


        # Check and create gang_members.csv if it doesn't exist
    if not os.path.exists(gang_members_path):
        with open(gang_members_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Name", "Aliases", "Gang Name"])
    


def save_to_csv(data, data_type):
    file_path = determine_file_path(data_type)
    if file_path is None:
        return False

    # Skriv data til CSV-filen og tilføjer eksisterende indhold
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)

        # Skriv data række
        if data_type == "missing_person":
            writer.writerow([data[0], f"{data[1]} {data[2]}", data[3], data[4]])
        elif data_type == "gang_member":
            writer.writerow([data[0], f"{data[1]} {data[2]}", data[3]])

    return True

def update_csv_row(data, data_type, row_index):
    # Bestem filstien baseret på datatype
    file_path = determine_file_path(data_type)
    if file_path is None:
        return False
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if data_type == "missing_person":
        rows[row_index] = [data.id, data.first_name, data.last_name, data.aliases, data.details, data.last_seen]
    elif data_type == "gang_member":
        rows[row_index] = [data.id, data.first_name, data.last_name, data.aliases, data.gang_name]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
