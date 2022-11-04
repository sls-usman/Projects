import time
import imghdr
import random
import smtplib
import requests
import concurrent.futures
from bs4 import BeautifulSoup
from email.message import EmailMessage

html_data = requests.get(
    'https://www.google.com/search?q=daily'
    '+motivational+qutes&tbm=isch&ved=2ahUK'
    'Ewieu8-m5JT7AhUugM4BHbpPBj4Q2-cCegQIABA'
    'A&oq=daily+motivational+qutes&gs_lcp=Cg'
    'NpbWcQAzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6'
    'gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQ'
    'JzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzI'
    'HCCMQ6gIQJ1DgBljAYGDGYWgCcAB4A4ABAIgBAJ'
    'IBAJgBAKABAaoBC2d3cy13aXotaW1nsAEKwAEB&'
    'sclient=img&ei=8ydlY951roC6vg-6n5nwAw').text

# Google url that carries all url for images

soup = BeautifulSoup(html_data, 'html.parser')
# Parse the response object into a html file which can easily be exploited by BS4.
list_of_img = [image['src'] for image in soup.find_all('img')]
list_of_img.pop(0)
# used the pop method to the remove the first element of the list which is not an img url
today_image = random.choice(list_of_img)
# Chosen image from the images list at random

# initialising smtp for email
conn = smtplib.SMTP_SSL('smtp.gmail.com', 465)
conn.login('19slsusman@gmail.com', 'vpjoiwuhhxdtxxre')


def img_down(url):
    # url here is a string of image_url from list_of_img

    image_ = requests.get(url).content
    # image downloaded from the above image list
    image_name_ = url.split('/')[3][16:26]
    image_name = f'{image_name_}.jpg'

    with open(image_name, 'wb') as _image:
        _image.write(image_)
    # Writing the byte data into a jpg extension to convert to an actual img

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    time_obj = time.localtime().tm_wday
    # time_obj here is a number return between 0-6 as a weekday
    for day in days:
        if time_obj == days.index(day):
            today = day
            break
    # Looping through days to get day which corresponds to the time_obj number.

    msg = EmailMessage()
    msg['From'] = '19slsusman@gmail.com'
    msg['Subject'] = f"{today} Motivational quote..."
    msg.set_content('Click to view...')

    with open(image_name, 'rb') as _file:
        file_data = _file.read()
        file_type = imghdr.what(_file.name)
    # opens the image in byte mode and gets its type which is passed below

    msg['To'] = '19slsusman@gmail.com, usmandankama1@gmail.com'
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=image_name)
    # Line above adds the image to the message body
    conn.send_message(msg)


with concurrent.futures.ThreadPoolExecutor() as executor:
    result = executor.submit(img_down,today_image)

# Increases the pace at which the images are downloaded.

