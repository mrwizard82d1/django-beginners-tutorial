import datetime
from zoneinfo import ZoneInfo

import geocoder
import requests


def temp_here():
    """Return the temperature at the current location."""
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    location = geocoder.ip('me').latlng
    api_request = f'{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m'
    now = datetime.datetime.now(ZoneInfo('America/Chicago'))
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    return meteo_data['hourly']['temperature_2m'][hour]
