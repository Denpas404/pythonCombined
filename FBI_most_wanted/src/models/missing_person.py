# missing_person.py
from models.person import Person  # Assuming `Person` is defined in `models.person`

class MissingPerson(Person):
    def __init__(self, id, first_name, last_name, details, last_seen="Unknown"):
        super().__init__(id, first_name, last_name)
        self.details = details
        self.last_seen = last_seen

    def __repr__(self):
        return f"MissingPerson(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, details={self.details}, last_seen={self.last_seen})"        
