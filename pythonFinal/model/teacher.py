from model.person import Person

class Teacher(Person):
    def __init__(self, first_name, last_name, subjects):
        super().__init__(first_name, last_name)
        self.subjects = [subjects]
    
    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
    
    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
    
    def get_person_role_in_TEC(self):
        return "Teacher"
    
    def __str__(self):
        subjects_str = ", ".join(self.subjects)
        return f"Teacher: {self.get_full_name()} Subjects: {subjects_str}"
    