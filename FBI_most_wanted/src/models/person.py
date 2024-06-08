# person.py
class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Person(id={self.id}, first_name={self.first_name}, last_name={self.last_name})"
