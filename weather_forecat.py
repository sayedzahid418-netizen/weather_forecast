import requests

city_name = input("Enter a city name: ")
API_Key = '############################'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is ', data['weather'][0]['description'])
    print('Current Temperature is ', data['main']['temp'])
    print('Current Temperature Feels like  ', data['main']['feels_like'])
    print('Humidity is ', data['main']['humidity'])
