import datetime
from zoneinfo import ZoneInfo

import geocoder
import requests
from django.http import HttpResponse
from django.template import loader
from meteo.models import Worldcities


def temp_somewhere(request):
    """Return the temperature at the requested location."""
    random_item = Worldcities.objects.all().order_by("?").first()
    city = random_item.city
    location = [random_item.lat, random_item.lng]
    temp = get_temp(location)

    template = loader.get_template('index.html')
    context = {
        'city': city,
        'temp': temp,
    }
    return HttpResponse(template.render(context, request))


def temp_here(request):
    """Return the temperature at the current location."""
    location = geocoder.ip('me').latlng
    temp = get_temp(location)

    template = loader.get_template('index.html')
    context = {
        'city': 'Your location',
        'temp': temp,
    }
    return HttpResponse(template.render(context, request))


def get_temp(location):
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    api_request = (f'{endpoint}?latitude={location[0]}&longitude={location[1]}&'
                   f'hourly=temperature_2m&temperature_unit=fahrenheit')
    now = datetime.datetime.now(ZoneInfo('America/Chicago'))
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']['temperature_2m'][hour]
    return temp
