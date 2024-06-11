from models.person import Person

class Gang_member(Person):
    def __init__(self, id, first_name, last_name, aliases, gang_name = "Unknown"):
        super().__init__(id, first_name, last_name)
        self.aliases = aliases
        self.gang_name = gang_name

    def __repr__(self):
        return f"Gang_member({self.id}, {self.first_name}, {self.last_name}, {self.aliases}, {self.gang_name})"