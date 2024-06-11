import requests
from model.person import MissingPerson, GangMember
from data import WriteData, ReadData
import re

class FBIList:
    def fetch_data(FBI_URL):
        FILENAME_GANG_MEMBERS = "gang_members.csv"
        FILENAME_MISSING_PERSONS = "missing_persons.csv"
        missing_person_category = "Missing Persons"
        gang_member_category = "Criminal Enterprise Investigations"

        response = requests.get(FBI_URL)

        if response.status_code == 200:
            data = response.json()["items"]
            transformed_misssing_person_data = []
            transformed_gang_data = []

            for item in data:
                categories = item.get("subjects", [])
                title = item.get("title", "")
                aliases = item.get("aliases", [])
                details = item.get("details", "") 
                details = details if details is not None else ""

                try:
                    if 'VICTIM' in title:
                        name_part = title.split('VICTIM')[1].strip()
                    else:
                        name_part = title.split(' - ')[0].strip()

                    # Splitting on first space to separate first and last name
                    first_name, last_name = name_part.split(" ", 1)

                    # Remove <p> tags from details and clean up
                    clean_details = re.sub(r'</?p>', '', details)
                    clean_details = re.sub(r'\r\n', ' ', clean_details)
                    clean_details = re.sub(r'\s+', ' ', clean_details).strip()

                    if categories and categories[0].find(missing_person_category) != -1:
                        missing_person = MissingPerson(item['uid'], first_name, last_name, aliases, clean_details)
                        transformed_misssing_person_data.append(missing_person)
                    elif categories and categories[0].find(gang_member_category) != -1:
                        gang_member = GangMember(item['uid'], first_name, last_name, aliases, clean_details)
                        transformed_gang_data.append(gang_member)

                except ValueError:
                    # Handle the case where name_part.split(" ", 1) does not return two parts
                    print(f"Unable to split the name for title: {title}")
                    continue
                
            WriteData.save_to_csv(transformed_misssing_person_data, FILENAME_MISSING_PERSONS)
            WriteData.save_to_csv(transformed_gang_data, FILENAME_GANG_MEMBERS)

            return True

        else:
            print("Error fetching data from the API. Status code:", response.status_code)
            return False