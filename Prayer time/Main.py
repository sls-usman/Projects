from email.message import EmailMessage
from Module import *
import _ctime_
import random
import imghdr


class App:
    # App attributes
    all_current_data = None
    current_time = _ctime_.response.json()['data']

    # Prayer Variables
    time_ = Modul.response.json()['data'][0]['timings']
    fajr = time_['Fajr'][0:5]
    dhuhr = time_['Dhuhr'][0:5]
    asr = time_['Asr'][0:5]
    maghrib = time_['Maghrib'][0:5]
    isha = time_['Isha'][0:5]

    # Email Variables
    my_email = Modul.user
    my_pwd = Modul.pwd

    msg = EmailMessage()
    msg['From'] = my_email
    msg['Subject'] = "IT'S PRAYER TIME DUDE"
    msg['body'] = "sls_python~~"

    msg.set_content('Click to view')
    image_files = None

    def __int__(self):
        pass

    @staticmethod
    def email_transfer():
        try:

            for prayer_time in [App.fajr,App.asr,App.isha,App.maghrib,App.dhuhr]:
                if str(App.current_time) == str(prayer_time):
                    hour = int(App.current_time[0:2])
                    if 6 > hour > 4:
                        App.image_files = ['.\\Images\\Fajr1.jpg', '.\\Images\\Fajr2.jpg', '.\\Images\\Fajr3.jpg']
                    elif 14 > hour > 11:
                        App.image_files = ['.\\Images\\Dhuhr1.jpg', '.\\Images\\Dhuhr2.jpg', '.\\Images\\Dhuhr3.jpg']
                    elif 17 > hour > 14:
                        App.image_files = ['.\\Images\\Asr1.jpg', '.\\Images\\Asr2.jpg', '.\\Images\\Asr3.jpg']
                    elif 19 >= hour > 17 and int(App.current_time[3:5]) < 10:
                        App.image_files = ['.\\Images\\Maghrib1.jpg', '.\\Images\\Maghrib2.jpg']
                    elif 20 >= hour >= 19:
                        App.image_files = ['.\\Images\\Isha1.jpg', '.\\Images\\Isha2.jpg']
                    else:
                        pass

                    file = random.choice(App.image_files)
                    with open(file,'rb') as _file:
                        file_data = _file.read()
                        file_type = imghdr.what(_file.name)
                        file_name = "Daily Quote..."
                    App.msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

                    list_of_email = ['wamawamazina@gmail.com', '19slsusman@gmail.com', ]
                    for email in list_of_email:
                        App.msg['To'] = email
                        Modul.conn.send_message(App.msg)
                        del App.msg['To']
                        Modul.conn.quit()
                    break
                else:
                    pass
        except UnboundLocalError:
            print('Error')


App().email_transfer()
