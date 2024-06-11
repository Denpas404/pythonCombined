from models.person import Person

class Gang_member(Person):
    def __init__(self, id, first_name, last_name, aliases, gang_name = "Unknown"):
        super().__init__(id, first_name, last_name)
        self.aliases = aliases
        self.gang_name = gang_name

    