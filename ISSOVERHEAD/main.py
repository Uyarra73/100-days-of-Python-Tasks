import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 35.689487 # Your latitude
MY_LONG = 139.691711 # Your longitude
MY_EMAIL = "alberto.python.73@gmail.com"
MY_PASSWORD = "kdpiumbxmcdegbgj"

def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude

def visible():
    iss_latitude, iss_longitude =get_iss_position()
    #print(low_margin, high_margin)
    if MY_LAT - 5 <= iss_latitude <= MY_LAT +5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 9
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 9

    sunrise = sunrise % 24
    sunset = sunset % 24

    current_hour = datetime.now().hour
    if current_hour >= sunset or current_hour <= sunrise:
        return True

def send_email():
    if visible() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="roselluyarra@gmail.com",
                                msg=f"Subject: La ISS es visible!\n\nMIRA HACIA ARRIBA!! Ahora puedes ver la ISS sobre Tokio")
    else:
        print("La ISS aun no es visible")

while True:
    send_email()
    time.sleep(10)





