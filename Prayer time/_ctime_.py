import requests

user_params = {
    "zone":'Africa/Lagos'
}

response = requests.get(url='https://api.aladhan.com/v1/currentTime', params=user_params)
response.raise_for_status()
