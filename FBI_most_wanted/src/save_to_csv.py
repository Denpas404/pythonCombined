# Create method to list to csv file, but check if file exists first else create it, then write to it. File should be named `missing_persons.csv` and `gang_members.csv` respectively.
# File must stay in data folder

import csv

def save_to_csv(data, data_type):
    
    #check if file exists, else create it
    if data_type == "missing_person":
        file_path = "data/missing_persons.csv"
    
    elif data_type == "gang_member":
        file_path = "data/gang_members.csv"
    
    else:
        return None
    
    # Check if file exists if not create it
    try:
        with open(file_path, 'x') as file:
            pass
    except FileExistsError:
        pass

    # Write data to the CSV file
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            if data_type == "missing_person":
                writer.writerow([item.id, item.first_name, item.last_name, item.details, item.last_seen])
            elif data_type == "gang_member":
                writer.writerow([item.id, item.first_name, item.last_name, item.caution, item.gang_name])
            else:
                return None
            
    return True
        
