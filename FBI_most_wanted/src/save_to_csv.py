import csv
import os

def save_to_csv(data, data_type):
    # Bestem filstien baseret på datatype
    if data_type == "missing_person":
        file_path = "data/missing_persons.csv"
    elif data_type == "gang_member":
        file_path = "data/gang_members.csv"
    else:
        return None
    
    # Sørg for, at data-mappen eksisterer
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Skriv data til CSV-filen og overskriv eksisterende indhold
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)

        # Skriv header baseret på datatype
        if data_type == "missing_person":
            writer.writerow(["ID", "First Name", "Last Name", "Details", "Last Seen"])
        elif data_type == "gang_member":
            writer.writerow(["ID", "First Name", "Last Name", "Caution", "Gang Name"])

        # Skriv data rækker
        for item in data:
            if data_type == "missing_person":
                writer.writerow([item.id, item.first_name, item.last_name, item.details, item.last_seen])
            elif data_type == "gang_member":
                writer.writerow([item.id, item.first_name, item.last_name, item.caution, item.gang_name])

    return True
