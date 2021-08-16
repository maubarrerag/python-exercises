import requests
weather = {'city': {'coord': {'lat': 41.85, 'lon': -87.6501},
          'country': 'US',
          'id': 4887398,
          'name': 'Chicago'},
 'cnt': 2,
 'cod': '200',
 'list': [{'clouds': {'all': 0},
           'dt': 1524236400,
           'dt_txt': '2018-04-20 15:00:00',
           'main': {'grnd_level': 1024.6,
                    'humidity': 82,
                    'pressure': 1024.6,
                    'sea_level': 1047.8,
                    'temp': 47.39,
                    'temp_kf': 3.52,
                    'temp_max': 47.39,
                    'temp_min': 41.04},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'clear sky',
                        'icon': '01d',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 338.001, 'speed': 2.55}},
          {'clouds': {'all': 8},
           'dt': 1524247200,
           'dt_txt': '2018-04-20 18:00:00',
           'main': {'grnd_level': 1024.41,
                    'humidity': 75,
                    'pressure': 1024.41,
                    'sea_level': 1047.37,
                    'temp': 48.83,
                    'temp_kf': 2.64,
                    'temp_max': 48.83,
                    'temp_min': 44.08},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'clear sky',
                        'icon': '02d',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 59.5004, 'speed': 2.3}}],
 'message': 0.006}

city_name = weather['city']['name']
max_temp_tomorrow = weather['list'][0]['main']['temp_max']

print('The high tomorrow in {} will be {}.'.format(city_name,
                                                  max_temp_tomorrow))
# Getting JSON from a feed
# You will need an API key from http://home.openweathermap.org/

#import requests
from pprint import pprint #"pretty prints" the data in a human-readable way

api_key = 'abca198b092b0295697beb48914a442c'
feed = "http://api.openweathermap.org/data/2.5/forecast/?APPID=" + api_key
params = {'id': 4887398, 'mode': 'json', 
          'units': 'imperial', 'cnt': 2}
r = requests.get(feed, params)
weather = r.json()

city_name = weather['city']['name']
max_temp_tomorrow = weather['list'][0]['main']['temp_max']

print(r.url) #prints the URL created using the params
print('-' * 50)
print('The high tomorrow in {} will be {}.'.format(city_name,
                                                  max_temp_tomorrow))
print('-' * 50)
pprint(weather)