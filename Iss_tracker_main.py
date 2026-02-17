import requests,smtplib,time
from datetime import datetime

MY_LAT = 53.544388
MY_LNG = -113.490929

#Your position is within +5 or -5 degrees of the ISS position.

def Iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT -5 <= iss_latitude <= MY_LAT+5) and (MY_LNG -5 <= iss_longitude <= MY_LNG +5):
        return True
    return False

def sendMail():
    my_email = "viraj.practice99@gmail.com"
    password = "qspu aihq wfun vjep"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="virajranderia123@gmail.com",
                            msg="Subject:ISS SATALLITE ABOVE\n\nThe ISS(Internation Space Station) is above you.\nCheck out.")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "tzid": "America/Edmonton",
    "formatted": 0,
}
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.


while True:
    time.sleep(10)
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour
    if (sunrise >= hour_now and hour_now >= sunset) and Iss_above():
        print("Look up")
        #sendMail()
        #print("email sent")







