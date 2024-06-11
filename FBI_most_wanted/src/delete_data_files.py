import os

def delete_data_files(confirm):
    
    file_paths = ["FBI_most_wanted/data/missing_persons.csv", "FBI_most_wanted/data/gang_members.csv"]

    while True:
        if confirm.lower() == "yes":
            for file_path in file_paths:
                if os.path.exists(file_path):
                    os.remove(file_path)            
            return "yes"

        elif confirm.lower() == "no":
            return "no"            

        else:
            return "Invalid input. Type 'yes' to confirm deletion\nType 'no' to cancel\n"




