import requests
from datetime import datetime
import time

MY_LAT = 49.135452 # Your latitude
MY_LONG = -122.903183 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT +5 >= iss_latitude >= MY_LAT -5 and MY_LONG +5 >= iss_longitude >= MY_LONG -5:
        return True

#Your position is within +5 or -5 degrees of the ISS position.

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = (int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 17) % 24
    sunset = (int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 17) % 24

    time_now = datetime.now()
    hour_now = int(str(time_now).split(' ')[1].split(':')[0])

    if hour_now <= sunrise or hour_now >= sunset:
        return True
    
if is_dark() and is_iss_overhead():
    #send email  USE: smtplib module


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

#whether it is dark or not