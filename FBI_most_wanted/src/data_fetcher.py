import requests
import re 
from save_to_csv import save_to_csv
from models.missing_person import MissingPerson
from models.gang_member import Gang_member
from read_from_csv import reading_in_list
from save_to_csv import does_files_exist_else_create_csv_file

def fetch_data():
    
    base_url = "https://api.fbi.gov/wanted/v1/list"

    missing_person_list = []
    gang_member_list = []
    

    does_files_exist_else_create_csv_file()
        

    for page_number in range(1, 6):
        params = {'page': page_number}
        response = requests.get(base_url, params=params)
        if response.status_code == 429:
            print("Too many requests, try again later.")
            break

        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            for item in items:
                uid = item.get('uid') # Extract UID from item
                title = item.get('title', '') # Extract title from item
                aliases = item.get('aliases', []) # Extract aliases from item
                category = item.get('subjects', [])  # Extract subjects from item (Missing Persons or Criminal Enterprise Investigations)
                details = item.get('details', '') # Extract details from item'

                # If details is empty, skip this item
                details = details if details is not None else ""

                try:
                    if 'VICTIM' in title:
                        name_part = title.split('VICTIM')[1].strip()
                        print(title)
                    else:
                        name_part = title.split(' - ')[0].strip()

                    # Splitting on first space to separate first and last name
                    first_name, last_name = name_part.split(" ", 1)

                    # Remove <p> tags from details and caution
                    clean_details = re.sub(r'</?p>', '', details)
                    clean_details = re.sub(r'\r\n', ' ', clean_details)
                    clean_details = re.sub(r'\s+', ' ', clean_details).strip()


                except ValueError:
                    continue                   

                # if "ViCAP Missing Persons" in subjects or "Kidnappings and Missing Persons" in subjects:            
                if any("Missing Persons" in subject for subject in category):
                    if not any(person.id == uid for person in missing_person_list):
                        person_to_save = [category, first_name, last_name, aliases, clean_details]
                        missing_person = MissingPerson(uid, first_name, last_name, aliases, clean_details)                    
                        save_to_csv(person_to_save, "missing_person")

                elif "Criminal Enterprise Investigations" in category:
                    if not any(person.id == uid for person in gang_member_list):
                        person_to_save = [category, first_name, last_name, aliases]
                        gang_member = Gang_member(uid, first_name, last_name, aliases)                    
                        save_to_csv(person_to_save, "gang_member")
        
        
    #missing_person_list, gang_member_list = reading_in_list()

    return missing_person_list, gang_member_list