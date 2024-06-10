import csv
import os
from models.missing_person import MissingPerson
from models.gang_member import Gang_member

def reading_in_list():

    missing_person_path = "FBI_most_wanted/data/missing_persons.csv"
    gang_member_path = "FBI_most_wanted/data/gang_members.csv"

    missing_person_list = []
    gang_member_list = []

    # Read data from csv file
    with open (missing_person_path, "r") as file:
        reader = csv.reader(file)
        next(reader) # Skip header
        for row in reader:            
            if len(row) >= 4:  # Ensure the row has at least 4 elements
                missing_person = MissingPerson(row[0], row[1], row[2], row[3])
                missing_person_list.append(missing_person)

    # Read data from csv file
    with open (gang_member_path, "r") as file:
        reader = csv.reader(file)
        next(reader) # Skip header
        for row in reader:            
            if len(row) >= 4:
                gang_member = Gang_member(row[0], row[1], row[2], row[3])
                gang_member_list.append(gang_member)

    return missing_person_list, gang_member_list