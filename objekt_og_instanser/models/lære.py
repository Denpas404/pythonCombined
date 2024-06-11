from models.person import Person

class Lære(Person):
    def __init__(self, first_name, last_name, fag=None):
        super().__init__( first_name, last_name)
        self.fag = fag if fag is not None else []


    
    
    