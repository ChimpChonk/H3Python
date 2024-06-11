from data import WriteData, ReadData, UpdateData
from fbi_list import FBIList
import threading
import time

def background_thread():
    while True:
        url = "https://api.fbi.gov/wanted/v1/list"
        if FBIList.fetch_data(url):
            print("Api call Success")
        else:
            print("Api call Failed")
        time.sleep(60*60*24)


def main():
    
    while True:
        time.sleep(3)
        display_menu()
        menu_choice = int(input("Enter your choice: "))
        match menu_choice:
            case 1:
                choice("missing_persons.csv")
            case 2:
                choice("gang_members.csv")
            case 3:
                exit("Shutting down...")

def display_menu():
    print("[1] Show missing people")
    print("[2] Show gang members")
    print("[3] Exit")

def choice(location):
    data = ReadData.read_csv(location)
    for item in data:
        for key, value in item.items():
            print(f"{key}: {value} ", end="")
        print()

    if location == "missing_persons.csv":
        sub_menu("missing_persons.csv")
    elif location == "gang_members.csv":
        sub_menu("gang_members.csv")

def sub_menu(location):
    while True:
        print("[1] Update person")
        print("[2] exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            id = int(input("Enter id: "))
            if location == "missing_persons.csv":
                update_stat = input("Enter update Last Seen: ")
                update_person(id, location, update_stat)
            elif location == "gang_members.csv":
                update_stat = input("Enter update Gang Name: ")
                update_person(id, location, update_stat)
        elif choice == 2:
            break


def update_person(id, location, updated_data):
    if location == "missing_persons.csv":
        UpdateData.update_person(id, "missing_persons.csv", updated_data)
    elif location == "gang_members.csv":
        UpdateData.update_person(id, "gang_members.csv", updated_data)

if __name__ == "__main__":
    background_thread = threading.Thread(target=background_thread)
    background_thread.deamon = True
    background_thread.start()
    main()