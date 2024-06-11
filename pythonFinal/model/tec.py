import os
import csv
from teacher import Teacher
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
    
    def load_teachers_from_csv(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    first_name, last_name, subjects = row
                    subjects_list = subjects.split(';')
                    teacher = Teacher(first_name, last_name, subjects_list[0])
                    teacher.subject = subjects_list
                    self.add_teacher(teacher)
    
    def save_teachers_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for teacher in self.teachers:
                writer.writerow([teacher.first_name, teacher.last_name, ';'.join(teacher.subject)])

    def load_subjects(filename):
        subjects = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    subjects.append(row[0])
        return subjects
    
    def save_subjects(filename, subjects):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for subject in subjects:
                writer.writerow([subject])