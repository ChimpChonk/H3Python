from interface.iRequiredPersonInfo import IRequiredPersonInfo
from abc import ABC, abstractmethod

class Person(IRequiredPersonInfo):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def first_name(self):
        return self.first_name
    
    @property
    def last_name(self):
        return self.last_name
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @abstractmethod
    def get_person_role_in_TEC(self):
        pass