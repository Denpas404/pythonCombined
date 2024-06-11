from abc import ABC, abstractmethod

class IRequiredPersonInfo(ABC):   

    # This is a property
    @property
    @abstractmethod
    def first_name(self):
        pass
    
    # This is a property
    @property
    @abstractmethod
    def last_name(self):
        pass 


