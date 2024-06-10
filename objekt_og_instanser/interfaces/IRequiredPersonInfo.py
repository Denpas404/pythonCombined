from abc import ABC, abstractmethod

class IRequiredPersonInfo(ABC):   

    @property
    @abstractmethod
    def first_name(self):
        pass

    @property
    @abstractmethod
    def last_name(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass