from interfaces.IRequiredPersonInfo import IRequiredPersonInfo

class Person(IRequiredPersonInfo):
    def __init__(self, first_name, last_name):       
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def __repr__(self):
        return f"Person(first_name={self.first_name}, last_name={self.last_name})"
