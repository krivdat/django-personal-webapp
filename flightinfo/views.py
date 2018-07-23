import json
import requests
from django.shortcuts import render

def index(request):
    locations = { # lamin,lomin,lamax,lomax
        "Switzerland": [45.8389,5.9962,47.8229,10.5226],
        "Prague": [49.8604,14.0617,50.2457,14.9653],
    }

    loc = "Prague"
    query = "https://opensky-network.org/api/states/all?" \
        + "lamin=" + str(locations[loc][0]) \
        + "&lomin=" + str(locations[loc][1]) \
        + "&lamax=" + str(locations[loc][2]) \
        + "&lomax=" + str(locations[loc][3])
    # print(query)

    response = requests.get(query)
    respjson = json.loads(response.text)
    flightinfo = []
    for record in respjson['states']:
        if record[8] is not True: # get only planes not on the ground
            flightinfo.append(record)
            
    return render(request, 'flightinfo/base.html', {'flightinfo': flightinfo, 'loc': loc})
