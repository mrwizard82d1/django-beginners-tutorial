import datetime
from zoneinfo import ZoneInfo

import geocoder
import requests
from django.http import HttpResponse


def temp_here(request):
    """Return the temperature at the current location."""
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    location = geocoder.ip('me').latlng
    api_request = f'{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m'
    now = datetime.datetime.now(ZoneInfo('America/Chicago'))
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']['temperature_2m'][hour]
    return HttpResponse(f"Here it's {temp} degrees C")
