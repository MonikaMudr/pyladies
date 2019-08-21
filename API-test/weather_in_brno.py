import requests

token = '668b36b9b996979206e4ea4657a2dc81'
url = 'http://api.openweathermap.org/data/2.5/forecast'

parameters = {
    'APIKEY' : token,
    'q' : 'brno',
    'units' : 'metric'
}

response = requests.get(url, params=parameters)
forecast = response.json()

def get_picture_weather(weather):
    pictures_weather = {
        'Snow' : '\N{SNOWFLAKE}',
        'Rain' : '\N{UMBRELLA WITH RAIN DROPS}',
        'Clouds' : '\u2744',
        'Clear' : '\N{SUN WITH FACE}'
    }
    return pictures_weather.get(weather, '?')

for sample in forecast['list']:
    time = sample['dt_txt']
    temperature = sample['main']['temp']
    graph = '.' * int(temperature)
    weather_icon = get_picture_weather(sample['weather'][0]['main'])
    print(f'{time} {weather_icon} {graph} {temperature}')


