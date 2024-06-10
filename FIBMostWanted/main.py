from data import WriteData, ReadData
from fbi_list import FBIList


def main():

    missing_persons, gang_members = FBIList.fetch_data()
    WriteData.save_to_csv(missing_persons, "missing_persons.csv")
    WriteData.save_to_csv(gang_members, "gang_members.csv")

    while True:
        display_menu()
        menu_choice = int(input("Enter your choice: "))

        match menu_choice:
            case 1:
                choice_one()
            case 2:
                choice_two()
            case 3:
                break

def display_menu():
    print("[1] Show missing people")
    print("[2] Show gang members")
    print("[3] Exit")

def choice_one():
    data = ReadData.read_csv("missing_persons.csv")

    print("Missing People:")
    print("------------------------------------------")
    print("|ID | First Name | Last Name | Last Seen |")
    print("------------------------------------------")

    for item in data:
        for key, value in item.items():
            print(f"{value} | ", end="")
        print()
    print("------------------------------------------")

    while True:
        sub_menu()
        menu_choice = int(input("Enter your choice: "))

        match menu_choice:
            case 1:
                sub_menu("missing_persons.csv")
            case 2:
                break


def choice_two():
    data = ReadData.read_csv("gang_members.csv")

    print("Gang Members:")
    print("------------------------------------------")
    print("|ID | First Name | Last Name | Gang Name |")
    print("------------------------------------------")

    for item in data:
        for key, value in item.items():
            print(f"{value} | ", end="")
        print()
    print("------------------------------------------")

def sub_menu(location):
    while True:
        print("[1] Update person")
        print("[2] exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            if location == "missing_persons.csv":
                update_stat = input("Enter update Last Seen: ")
                update_person(name, location, update_stat)
            elif location == "gang_members.csv":
                update_stat = input("Enter update Gang Name: ")
                update_person(name, location, update_stat)
        elif choice == 2:
            break


def update_person(name, location, updated_data):
    if location == "missing_persons.csv":
        WriteData.save_to_csv(name, "missing_persons.csv")
    elif location == "gang_members.csv":
        WriteData.save_to_csv(name, "gang_members.csv")

if __name__ == "__main__":
    main()