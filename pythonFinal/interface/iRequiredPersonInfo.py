from abc import ABC, abstractmethod

class IRequiredPersonInfo(ABC):
    @property
    @abstractmethod
    def first_name(self, firstName):
        pass

    @property
    @abstractmethod
    def last_name(self, lastName):
        pass

    @property
    @abstractmethod
    def get_full_name(self):
        pass

    @property
    @abstractmethod
    def get_person_role_in_TEC(self):
        pass
    