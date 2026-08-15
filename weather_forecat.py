import requests

city_name = input("Enter a city name: ")
API_Key = '94a50946f8ba0ad3e1e9e8b1d39ccb90'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is ', data['weather'][0]['description'])
    print('Current Temperature is ', data['main']['temp'])
    print('Current Temperature Feels like  ', data['main']['feels_like'])
    print('Humidity is ', data['main']['humidity'])