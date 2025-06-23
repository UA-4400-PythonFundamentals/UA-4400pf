from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()


city = "Lviv, UA"

obs = mgr.weather_at_place(city)
print(obs.weather)
w = obs.weather



weather_info = {
    "Status": w.detailed_status,
    "Wind": w.wind(),
    "Humidity": w.humidity,
    "Temperature": w.temperature('celsius'),
    "Rain": w.rain,
    "Heat Index": w.heat_index,
    "Clouds": w.clouds,
}

from pprint import pprint
pprint(weather_info)
