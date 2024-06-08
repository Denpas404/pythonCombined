import requests
import re 
from models.missing_person import MissingPerson
from models.gang_member import Gang_member


def fetch_data(data_type):
    
    url = "https://api.fbi.gov/wanted/v1/list"
    params = {
        "pageSize": 100  # Limiting results to 8
    }

    missing_person_list = []
    gang_member_list = []

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])
        

        for item in items:
            uid = item.get('uid')
            title = item.get('title', '')
            details = item.get('details', '')
            caution = item.get('caution', '')

            # If details is empty, skip this item
            details = details if details is not None else ""
            caution = caution if caution is not None else ""
            
            # Extract first and last name from title - removing ' - ' and splitting on first space
            name_part = title.split(' - ')[0]

            # Splitting on first space to separate first and last name
            first_name, last_name = name_part.split(" ", 1)

            # Remove <p> tags from details and caution
            clean_details = re.sub(r'</?p>', '', details)
            clean_details = re.sub(r'\r\n', ' ', clean_details)
            clean_details = re.sub(r'\s+', ' ', clean_details).strip()

            clean_caution = re.sub(r'</?p>', '', caution)
            clean_caution = re.sub(r'\s+', ' ', clean_caution).strip()
            clean_caution = re.sub(r'\r\n', ' ', clean_caution)


            # Extract subjects from item (Missing Persons or Criminal Enterprise Investigations)        
            subjects = item.get('subjects', [])  
            
            if "ViCAP Missing Persons" in subjects and len(missing_person_list) < 4:            
                # Create a missing person object
                missing_person = MissingPerson(uid, first_name, last_name, clean_details)                
                missing_person_list.append(missing_person)

                
            if "Criminal Enterprise Investigations" in subjects and len(gang_member_list) < 4:
                # Create a gang member object
                gang_member = Gang_member(uid, first_name, last_name, clean_caution)
                gang_member_list.append(gang_member)
            
                
    else:
        return None
    
    if data_type == "missing_person":
        return missing_person_list
    elif data_type == "gang_member":
        return gang_member_list
    else:
        return None