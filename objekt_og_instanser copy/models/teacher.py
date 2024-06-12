from models.person import Person

class Lære(Person):
    def __init__(self, first_name, last_name, subject=None):
        super().__init__( first_name, last_name)
        self.subject = subject if subject is not None else []

        def add_subject(self, new_subject):
            if new_subject not in self.subject:
                self.subject.append(new_subject)


        def remove_subject(self, new_subject):
            if new_subject in self.subject:
                self.subject.remove(new_subject)