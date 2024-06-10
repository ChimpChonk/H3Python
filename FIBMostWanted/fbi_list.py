import requests
import json
def FBIList():
    FBI_URL = "https://api.fbi.gov/wanted/v1/list"
    missing_person_category = "Missing Persons"
    gang_member_category = "Criminal Enterprise Investigations"

    # Hent data fra FBI API
    response = requests.get(FBI_URL)
    data = response.json()["items"]

    # Transformér data til struktureret format
    transformed_data = []
    id = 0
    for item in data:
        if item["subjects"][0].find(missing_person_category) != -1:
            transformed_item = {
                "id": item["uid"],
                "category": item["subjects"],
                "name": item["title"],
            }
            transformed_data.append(transformed_item)
        elif item["subjects"][0].find(gang_member_category) != -1:
            transformed_item = {
                "id": item["uid"],
                "category": item["subjects"],
                "name": item["title"],
            }
            transformed_data.append(transformed_item)