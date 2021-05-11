import requests
from datetime import datetime
# import os


APP_KEY="158909c5469ec587d5a15522197c6789"

sheety_API="https://api.sheety.co/a47ee9e7727d8061c5ef9fde9733d70e/workoutTracking/workouts"

APP_ID = "2fb3f1e6"
exercise_text=input("Tell us which exercises you did:")
headers = {
     "x-app-id": APP_ID,
     "x-app-key": APP_KEY,

}

user_params={
     "query": exercise_text,
     "gender": "male",
     "weight_kg": 80,
     "height_cm": 180,
     "age": 50,
}

response = requests.post(url="https://trackapi.nutritionix.com//v2/natural/exercise", json=user_params, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# bearer_headers = {
#     "Authorization": f"Bearer {os.environ['jklwjkunjljhr&5$(']}"
# }

for excercise in result["exercises"]:
     sheet_inputs = {
          "workout":{
               "date": today_date,
               "time": now_time,
               "exercise": excercise['name'],
               "duration": excercise['duration_min'],
               "calories": excercise['nf_calories']
          }
     }

Username= "michaelfan0310"

Password= "jklwjkunjljhr&5$("


response_sheet=requests.post(sheety_API, json=sheet_inputs)