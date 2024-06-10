import requests
from model.person import MissingPerson, GangMember
import requests

class FBIList:
    def fetch_data():
        FBI_URL = "https://api.fbi.gov/wanted/v1/list"
        missing_person_category = "Missing Persons"
        gang_member_category = "Criminal Enterprise Investigations"

        response = requests.get(FBI_URL)
        data = response.json()["items"]
        transformed_misssing_person_data = []
        transformed_gang_data = []

        for item in data:
            categories = item.get("subjects", [])
            name_parts = item.get("title").split(' ', 1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ""

            if categories[0].find(missing_person_category) != -1:
                missing_person = MissingPerson(item['uid'], first_name, last_name)
                transformed_misssing_person_data.append(missing_person)

            elif categories[0].find(gang_member_category) != -1:
                gang_member = GangMember(item['uid'], first_name, last_name)
                transformed_gang_data.append(gang_member)

        return transformed_misssing_person_data, transformed_gang_data