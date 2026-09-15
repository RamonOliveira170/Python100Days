import requests
from datetime import datetime

MY_LATITUDE = 38.736946
MY_LONGITUDE = 9.142685

'''response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)
'''

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
sun_data = sun_response.json()

sunrise = sun_data["results"]["sunrise"].split("T")[1].split("+")[0]
sunset = sun_data["results"]["sunset"].split("T")[1].split("+")[0]

print(sunset)
print(sunrise)

time_now = datetime.now()
print(time_now)
