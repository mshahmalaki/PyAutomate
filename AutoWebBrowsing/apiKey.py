import requests


base_url = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': 'OPENWEATHERMAP_API_KEY', 'q': 'Tehran,IR'}
response = requests.get(base_url, params=parameters)
print(response.content)
