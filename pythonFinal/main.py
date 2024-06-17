import os
from model.tec import TEC
from model.teacher import Teacher

FILENAME = "teachers.csv"
SUBJECTS = ["IoT Embedded", "Python", "BigData 1", "Softwaresikkerhed og test", "Serversideprogrammering"]

def load_data():
    tec = TEC()
    tec.load_from_csv(FILENAME)
    return tec

def save_data(tec):
    tec.save_to_csv(FILENAME)

def display_menu():
    print("\n--- Teacher Registration System ---")
    print("1. Create Teacher")
    print("2. Update Teacher")
    print("3. List All Teachers")
    print("4. Save and Exit")
    return input("Choose an option: ")

def create_teacher(tec):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print("Choose a subject:")
    for idx, subject in enumerate(SUBJECTS, 1):
        print(f"{idx}. {subject}")
    subject_choice = int(input("Subject number: "))
    if 1 <= subject_choice <= len(SUBJECTS):
        subject = SUBJECTS[subject_choice - 1]
        print(subject)
        teacher = Teacher(first_name, last_name, subject)
        tec.add_teacher(teacher)
        print(f"Teacher {teacher.get_full_name()} created with subject {subject}")
    else:
        print("Invalid subject choice")

def update_teacher(tec):
    print("-------List of Teachers-------")
    teachers = tec.list_teachers()
    if not teachers:
        print("No teachers found.")
        return

    for idx, teacher in enumerate(teachers, 1):
        print(f"[{idx}] {teacher.get_full_name()}")
    
    try:
        teacher_choice = int(input("Choose teacher to update: "))
        if 1 <= teacher_choice <= len(teachers):
            teacher = teachers[teacher_choice - 1]
            print("[1] Add subject")
            print("[2] Remove subject")
            update_choice = int(input("Choose an option: "))
            if update_choice == 1:
                print("Choose a subject to add:")
                for idx, subject in enumerate(SUBJECTS, 1):
                    print(f"[{idx}]. {subject}")
                subject_choice = int(input("Subject number: "))
                if 1 <= subject_choice <= len(SUBJECTS):
                    subject = SUBJECTS[subject_choice - 1]
                    teacher.add_subject(subject)
                    print(f"Subject {subject} added to teacher {teacher.get_full_name()}")
                else:
                    print("Invalid subject choice")
            
            elif update_choice == 2:
                print("Choose a subject to remove:")
                for idx, subject in enumerate(teacher.subjects, 1):
                    print(f"[{idx}]. {subject}")
                subject_choice = int(input("Subject number: "))
                if 1 <= subject_choice <= len(teacher.subjects):
                    subject = teacher.subjects[subject_choice - 1]
                    teacher.remove_subject(subject)
                    print(f"Subject {subject} removed from teacher {teacher.get_full_name()}")
                else:
                    print("Invalid subject choice")
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice. Exiting...")

def list_teachers(tec):
    print("\n--- List of Teachers ---")
    for teacher in tec.list_teachers():
        print(teacher)

def main():
    tec = load_data()
    while True:
        choice = display_menu()
        if choice == "1":
            create_teacher(tec)
        elif choice == "2":
            update_teacher(tec)
        elif choice == "3":
            list_teachers(tec)
        elif choice == "4":
            save_data(tec)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()