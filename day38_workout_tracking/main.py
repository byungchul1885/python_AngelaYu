import requests
from datetime import datetime

APP_ID = "8cc317c8"
API_KEY = "ffe8346652cfc97caf8abf24e8a081a3"

exercise_endpoint = \
    "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_config = {
    "query": input("Tell me which exercise you did"),
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",    
}

response = requests.post(
    url=exercise_endpoint, 
    json=exercise_config, 
    headers=headers)
print(response.text)

data_list = response.json()["exercises"]

sheety_endpoint = \
    "https://api.sheety.co/fd81df72098a976484ecf693894c0fc3/myWorkouts/workouts"
headers = {
    "Authorization": "Basic YmNjaG86YmNjaG8=",
}
    
for wo in data_list:
    sheety_config = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": wo["name"].title(),
            "duration": wo["duration_min"],
            "calories": wo["nf_calories"],
        }
    }

    response = requests.post(
        url=sheety_endpoint, 
        json=sheety_config,
        headers=headers)
    print(response.text)