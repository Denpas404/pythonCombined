from models.person import Person

class Gang_member(Person):
    def __init__(self, id, forNavn, efterNavn, caution, gang_name = "Unknown"):
        super().__init__(id, forNavn, efterNavn)
        self.caution = caution
        self.gang_name = gang_name

    def __repr__(self):
        return f"Gang_member(id={self.id}, forNavn={self.forNavn}, efterNavn={self.efterNavn}, caution={self.caution}, gang_name={self.gang_name})"        