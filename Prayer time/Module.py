import smtplib
import threading
import requests
import time
from _Classes_ import *


class Modul:

    pwd = 'vpjoiwuhhxdtxxre'
    user = '19slsusman@gmail.com'
    usman_mail = 'usmandankama1@gmail.com'

    conn = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    conn.login(user=user, password=pwd)

    user_params = {
        "latitude": PrayerTiming.latitude,
        "longitude": PrayerTiming.longitude,
        "method": 99,
        "month": 10,
        "year": 2022,
    }

    response = requests.get(url=f'https://api.aladhan.com/v1/calendar', params=user_params)




