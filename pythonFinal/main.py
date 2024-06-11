import os
from model.tec import TEC
from model.teacher import Teacher

FILENAME_TECHERS = "data/teachers.csv"
FILENAME_SUBJECTS = "data/subjects.csv"

def display_menu():
    print("\n----------------------------")
    print("[1] Opret lærer")
    print("[2] Opdater lærer")
    print("[3] Vis list af alle lærere")
    print("[4] Save and EXIT")
    return int(input("Vælg 1, 2, 3 eller 4: "))

def load_data():
    tec = TEC()
    tec.load_teachers_from_csv(FILENAME_TECHERS)
    subjects = tec.load_subjects(FILENAME_SUBJECTS)
    return tec, subjects

def save_data(tec, subjects):
    tec.save_teachers_to_csv(FILENAME_TECHERS)
    subjects.save_subjects(FILENAME_SUBJECTS)

def create_teacher(tec, subjects):
    first_name = input("Fornavn: ")
    last_name = input("Efternavn: ")
    print("Angive fag: ")
    for idx, subjects in enumerate(subjects, 1):
        print(f"[{idx}] {subjects}")
    subject_choice = int(input("Vælg fag fra listen: "))

    if 1 <= subject_choice <= len(subjects):
        subject = subjects[subject_choice - 1]
        teacher = Teacher(first_name, last_name, subject)
        tec.add_teacher(teacher)
        print(f"{teacher.get_full_name()} er nu oprettet som lærer med følgende fag: {subject}")
    else:
        print("Fejl i valg. Prøv igen.")



def main():
    tec, subjects = load_data()
    create_teacher(tec, subjects)
    save_data(tec, subjects)

if __name__ == "__main__":
    main()