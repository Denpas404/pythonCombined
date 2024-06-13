import requests
import re
import csv
import os
from models.missing_person import MissingPerson
from models.gang_member import Gang_member
from save_to_csv import does_files_exist_else_create_csv_file


def main_fetch_data():
    print("\nFetching data from FBI API...")
    
    missing_person_list = []
    gang_member_list = []

    missing_person_list, gang_member_list = extract_from_api()

    return  missing_person_list, gang_member_list # returns missing_person_list, gang_member_list to main()



def extract_from_api():
    base_url = "https://api.fbi.gov/wanted/v1/list"

    extracted_data = []    
    
    missing_person_list = []    
    gang_member_list = []
    

    for page_number in range(1, 3):
        params = {'page': page_number}
        response = requests.get(base_url, params=params)

        if response.status_code == 429:
            print("Too many requests, try again later.")
            break

        if response.status_code == 200:
            print("Data fetched successfully.")
            data = response.json()
            items = data.get('items', [])           

    missing_person_list, gang_member_list = transform_data(items)

    return  missing_person_list, gang_member_list # returns missing_person_list, gang_member_list to main_fetch_data()


def transform_data(items):
    print("\nTransforming data...")

    transformed_data = []

    for item in items:
        uid = item.get('uid')
        title = item.get('title', '')
        aliases = item.get('aliases', [])
        category = item.get('subjects', [])
        details = item.get('details', '')

        # If details is empty, use an empty string
        details = details if details is not None else ""

        try:
            if 'VICTIM' in title:
                name_part = title.split('VICTIM')[1].strip()
            else:
                name_part = title.split(' - ')[0].strip()

            # Splitting on first space to separate first and last name
            first_name, last_name = name_part.split(" ", 1)

        except ValueError:
            continue

        # Remove <p> tags from details and caution
        clean_details = re.sub(r'</?p>', '', details)  # Remove <p> tags
        clean_details = re.sub(r'\r\n', ' ', clean_details)  # Remove newlines
        clean_details = re.sub(r'\s+', ' ', clean_details).strip()  # Remove extra spaces

        for item in category:            
            if "Missing Persons" in item:
                new_category = "Missing Persons"
                transformed_data.append([uid, new_category, first_name, last_name, aliases, clean_details])
            elif "Criminal Enterprise Investigations" in item:
                new_category = "Criminal Enterprise Investigations"
                transformed_data.append([uid, new_category, first_name, last_name, aliases, clean_details])

    
    print("Data transformed successfully.")
    
    missing_person_list, gang_member_list = load_data_(transformed_data)    

    return missing_person_list, gang_member_list # returns missing_person_list, gang_member_list to main_fetch_data()

def load_existing_data(file_path, key_index, cls):
    existing_data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if cls == MissingPerson:
                    existing_data.append(cls(row[key_index.start], row[key_index.start + 1], row[key_index.start + 2], row[key_index.start + 3]))
                elif cls == Gang_member:
                    existing_data.append(cls(row[key_index.start], row[key_index.start + 1], row[key_index.start + 2], row[key_index.start + 3]))
                else:
                    existing_data.append(row[key_index])
    return existing_data

def load_data_(extracted_data):
    print("\nLoading data...")
    does_files_exist_else_create_csv_file() # checks if files exists, if not creates them, with headers
    # missing person header:    id,first_name,last_name,last_seen
    # gang member header:       id,first_name,last_name,gang_name    
    # missing etl header:       category,fullname,aliases,details
    # gang etl header:          category,fullname,aliases

    # Load existing data to check for duplicates
    existing_missing_persons = load_existing_data("FBI_most_wanted/data/missing_persons.csv", slice(0, 4), MissingPerson)
    existing_missing_etl = load_existing_data("FBI_most_wanted/data/missing_etl.csv", slice(0, 2), tuple)
    existing_gang_members = load_existing_data("FBI_most_wanted/data/gang_members.csv", slice(0, 4), Gang_member)
    existing_gang_etl = load_existing_data("FBI_most_wanted/data/gang_etl.csv", slice(0, 3,), tuple)




    with open("FBI_most_wanted/data/missing_persons.csv", "a", newline="") as missing_persons_file, \
        open("FBI_most_wanted/data/missing_etl.csv", "a", newline="") as missing_etl_file, \
        open("FBI_most_wanted/data/gang_members.csv", "a", newline="") as gang_members_file, \
        open("FBI_most_wanted/data/gang_etl.csv", "a", newline="") as gang_etl_file:

        missing_person_writer = csv.writer(missing_persons_file)
        missing_etl_writer = csv.writer(missing_etl_file)
        gang_members_writer = csv.writer(gang_members_file)
        gang_etl_writer = csv.writer(gang_etl_file)
        
        

        for data in extracted_data:
            uid, category, first_name, last_name, aliases, details = data
            if "Missing Persons" in category:
                missing_person = MissingPerson(uid, first_name, last_name,)
                if (missing_person.id, missing_person.first_name, missing_person.last_name) not in [(mp.id, mp.first_name, mp.last_name) for mp in existing_missing_persons]:
                    missing_person_writer.writerow([missing_person.id, missing_person.first_name, missing_person.last_name, missing_person.last_seen])
                    existing_missing_persons.append(missing_person)
                    
                    full_name = f"{first_name} {last_name}"                
                    missing_etl_writer.writerow([category, full_name, aliases, details])                    
                    existing_missing_etl.append((category, full_name, aliases, details))
                    

            elif "Criminal Enterprise Investigations" in category:
                gang_member = Gang_member(uid, first_name, last_name)
                if (gang_member.id, gang_member.first_name, gang_member.last_name) not in [(gm.id, gm.first_name, gm.last_name) for gm in existing_gang_members]:
                    gang_members_writer.writerow([gang_member.id, gang_member.first_name, gang_member.last_name, gang_member.gang_name])
                    existing_gang_members.append(gang_member)                    
                    full_name = f"{first_name} {last_name}"
                    gang_etl_writer.writerow([category, full_name, aliases])
                    existing_gang_etl.append((category, full_name, aliases))

    print("Data loaded successfully.")
    return existing_missing_persons, existing_gang_members # returns missing_persons_file, gang_members_file to transform_data()