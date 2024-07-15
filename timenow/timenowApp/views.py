from django.shortcuts import render
from django.http import HttpResponse
import pytz
from datetime import datetime

# Time zones dictionary

time_zones = {
    'usa': 'America/New_York',
    'uk': 'Europe/London',
    'japan': 'Asia/Tokyo',
    'australia': 'Australia/Sydney',
    'uae': 'Asia/Dubai',
    'jordan': 'Asia/Amman'  # Added Jordan to the list
}

def get_current_time(country):
    if country.lower() in time_zones:
        tz = pytz.timezone(time_zones[country.lower()])
        current_time = datetime.now(tz)
        return current_time.strftime('%Y-%m-%d  %H:%M ')
    else:
        return None


def country_time(request, country):
  if get_current_time(country):
    time = get_current_time(country)
    return render(request, "timenowApp/country_time.html", context={
        "country": country.upper(),
        "time": time,
        })
  else:
    return HttpResponse("Invalid Country, please choose from: USA/Jordan/UAE/Australia/UK/Japan") 
    
    
def index(request):
  return render(request,"timenowApp/index.html")
