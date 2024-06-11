# missing_person.py
from models.person import Person  # Assuming `Person` is defined in `models.person`

class MissingPerson(Person):
    def __init__(self, id, first_name, last_name, aliases, details, last_seen="Unknown"):
        super().__init__(id, first_name, last_name)
        self.aliases = aliases
        self.details = details
        self.last_seen = last_seen

    def __repr__(self):
        return f"MissingPerson({self.id}, {self.first_name}, {self.last_name}, {self.aliases}, {self.details}, {self.last_seen})"        
