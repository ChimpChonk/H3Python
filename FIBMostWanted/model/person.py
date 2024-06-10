class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
class MissingPerson(Person):
    def __inif__(self, id, first_name, last_name, last_seen="Unkown"):
        super().__init__(id, first_name, last_name, last_seen)
        self.last_seen = last_seen
    
class GangMember(Person):
    def __inif__(self, id, first_name, last_name, gang="Unkown"):
        super().__init__(id, first_name, last_name, gang)
        self.gang = gang