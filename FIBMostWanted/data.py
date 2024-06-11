import csv
import os

class ReadData:
    def read_csv(filename):
        existing_data = []
        if os.path.exists("data/" + filename): 
            with open("data/" + filename, mode='r') as csvfile:
                reader = csv.DictReader(csvfile)
                id = 1
                for row in reader:
                    filtered_row = {
                        "Id": id,
                        "Uid": row.get("Id"),
                        "First Name": row.get("First Name"),
                        "Last Name": row.get("Last Name")
                    }
                    
                    # Add 'last_seen' or 'gang' based on filename
                    if "missing_persons" in filename:
                        filtered_row["Last Seen"] = row.get("Last Seen")
                    elif "gang_members" in filename:
                        filtered_row["Gang Name"] = row.get("Gang Name")

                    id += 1
                    existing_data.append(filtered_row)
        return existing_data

    # Gem data i CSV-filer
class WriteData:
    def save_to_csv(data, filename):
        if os.path.exists("data/" + filename):
            existing_ids = ReadData.read_csv(filename)
            new_entries = [item for item in data if item.id not in [d['Uid'] for d in existing_ids]]
            if new_entries:
                with open("data/" + filename, mode='a', newline='') as csvfile:
                    writer = csv.writer(csvfile)    
                    for item in new_entries:
                        writer.writerows([[item.id, item.first_name, item.last_name, item.aliases, item.details, "Unkown"]])
        else:
            with open("data/" + filename, 'w', newline='') as file:
                writer = csv.writer(file)
                if data:
                    if(filename == "missing_persons.csv"):
                        writer.writerow(["Id", "First Name", "Last Name", "Aliases", "Details","Last Seen"])
                        for item in data:
                            writer.writerow([item.id, item.first_name, item.last_name, item.aliases, item.details,"Unkown"])
                    elif(filename == "gang_members.csv"):
                        writer.writerow(["Id", "First Name", "Last Name", "Aliases", "Details", "Gang Name"])
                        for item in data:
                            writer.writerow([item.id, item.first_name, item.last_name, item.aliases, item.details,"Unkown"])
                else:
                    print(f"No data to write to {filename}")

class UpdateData:
    def update_person(index, location, updated_data):
        with open("data/" + location, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        data[index][5] = updated_data

        with open("data/" + location, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)