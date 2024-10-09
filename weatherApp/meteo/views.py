import geocoder
import requests


def temp_here():
    """Return the temperature at the current location."""
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    location = geocoder.ip('me').latlng
    api_request = f'{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature'
    return requests.get(api_request).json()
