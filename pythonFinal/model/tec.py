import os
import csv
from model.teacher import Teacher
class TEC:
    def __init__(self):
        self.teachers = []
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def find_teacher(self, full_name):
        for teacher in self.teachers:
            if teacher.get_full_name() == full_name:
                return teacher
        return None
    
    def list_teachers(self):
        return self.teachers
    
    def load_from_csv(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    first_name = row['first_name']
                    last_name = row['last_name']
                    subjects = row['subjects']
                    subjects_list = subjects.split('-')
                    teacher = Teacher(first_name, last_name, subjects_list[0])
                    teacher.subjects = subjects_list
                    self.add_teacher(teacher)
    
    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['first_name', 'last_name', 'subjects']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for teacher in self.teachers:
                writer.writerow({
                    'first_name': teacher.first_name,
                    'last_name': teacher.last_name,
                    'subjects': '-'.join(teacher.subjects)
                })