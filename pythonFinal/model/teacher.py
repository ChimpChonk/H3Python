from model.person import Person

class Teacher(Person):
    def __init__(self, first_name, last_name, subject):
        super().__init__(first_name, last_name)
        self.subject = [subject]
    
    def add_subject(self, subject):
        if subject not in self.subject:
            self.subject.append(subject)
    
    def remove_subject(self, subject):
        if subject in self.subject:
            self.subject.remove(subject)
    
    def get_person_role_in_TEC(self):
        return "Teacher"
    
    def __str__(self):
        subjects_str = ", ".join(self.subject)
        return f"Teacher: {self.get_full_name()} ({subjects_str})"
    