# missing_person.py
from models.person import Person  # Assuming `Person` is defined in `models.person`

class MissingPerson(Person):
    def __init__(self, id, first_name, last_name, last_seen="Unknown"):
        super().__init__(id, first_name, last_name)        
        self.last_seen = last_seen

    
