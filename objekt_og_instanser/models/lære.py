from models.person import Person

class Lære(Person):
    def __init__(self, first_name, last_name, fag=None):
        super().__init__( first_name, last_name)
        self.fag = fag if fag is not None else []


    def __repr__(self):
        return f"first_name={self.first_name}, last_name={self.last_name})"