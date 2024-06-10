import requests
from save_to_csv import save_to_csv
from models.missing_person import MissingPerson
from models.gang_member import Gang_member
from read_from_csv import reading_in_list
from save_to_csv import does_files_exist_else_create_csv_file

def fetch_data():
    
    
    base_url = "https://api.fbi.gov/wanted/v1/list?page="
    page_count = 4  # Set the number of pages to fetch

    missing_person_list = []
    gang_member_list = []
    
    counter = 0

    if does_files_exist_else_create_csv_file():
        missing_person_list, gang_member_list = reading_in_list()

    for page_number in range(1, page_count + 1):
        url = base_url + str(page_number)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            for item in items:
                uid = item.get('uid') # Extract UID from item
                title = item.get('title', '') # Extract title from item
                subjects = item.get('subjects', [])  # Extract subjects from item (Missing Persons or Criminal Enterprise Investigations)        

                # Extract first and last name from title - removing ' - ' and splitting on first space
                name_part = title.split(' - ')[0]

                # Splitting on first space to separate first and last name
                first_name, last_name = name_part.split(" ", 1)

                # if "ViCAP Missing Persons" in subjects or "Kidnappings and Missing Persons" in subjects:            
                if any("Missing Persons" in subject for subject in subjects):
                    if not any(person.id == uid for person in missing_person_list):
                        missing_person = MissingPerson(uid, first_name, last_name)                    
                        save_to_csv(missing_person, "missing_person")

                elif "Criminal Enterprise Investigations" in subjects:
                    if not any(person.id == uid for person in gang_member_list):
                        gang_member = Gang_member(uid, first_name, last_name)                    
                        save_to_csv(gang_member, "gang_member")

        else:
            return None
        
    missing_person_list, gang_member_list = reading_in_list()

    return missing_person_list, gang_member_list