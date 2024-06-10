import csv
import os

class ReadData:
    def read_csv(filename):
        existing_data = []
        if os.path.exists("data/" + filename):
            with open("data/" + filename, mode='r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    existing_data.append(row)
        # print(existing_data)
        return existing_data

    # Gem data i CSV-filer
class WriteData:
    def save_to_csv(data, filename):
        existing_ids = ReadData.read_csv(filename)
        new_entries = [item for item in data if item.id not in [d['id'] for d in existing_ids]]

        if new_entries:
            with open("data/" + filename, mode='a', newline='') as csvfile:
                writer = csv.writer(csvfile)    
                for item in new_entries:
                    writer.writerows([[item.id, item.first_name, item.last_name, "Unkown"]])
        else:
            with open("data/" + filename, 'w', newline='') as file:
                writer = csv.writer(file)
                if data:
                    if(filename == "missing_persons.csv"):
                        writer.writerow(["id", "First Name", "Last Name", "Last Seen"])
                        for item in data:
                            writer.writerow([item.id, item.first_name, item.last_name, "Unkown"])
                    elif(filename == "gang_members.csv"):
                        writer.writerow(["id", "First Name", "Last Name", "Gang Name"])
                        for item in data:
                            writer.writerow([item.id, item.first_name, item.last_name, "Unkown"])
                else:
                    print(f"No data to write to {filename}")

class updateData:
    def update_person(name, location, updated_data):
        pass