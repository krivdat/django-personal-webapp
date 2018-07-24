import json
import requests
from django.shortcuts import render

def index(request, loc='Prague'):
    locations = { # lamin,lomin,lamax,lomax
        "Switzerland": [45.8389,5.9962,47.8229,10.5226],
        "Prague": [49.8604,14.0617,50.2457,14.9653],
        "Kosice": [48.6136,21.1367,48.7790,21.3547],
        "Bratislava": [48.0941,16.9595,48.2256,17.2781],
    }

    query = "https://opensky-network.org/api/states/all?" \
        + "lamin=" + str(locations[loc][0]) \
        + "&lomin=" + str(locations[loc][1]) \
        + "&lamax=" + str(locations[loc][2]) \
        + "&lomax=" + str(locations[loc][3])
    # print(query)
    response = requests.get(query)
    respjson = json.loads(response.text)
    flights = []
    try:
        for record in respjson['states']:
            if record[8] is not True: # get only planes not on the ground
                if record[13] is not None:
                    altitude = int(record[13])
                else:
                    altitude = "---"
                if record[9] is not None:
                    speed = int(record[9]*3.6)
                else:
                    speed = "---"
                if record[11] is not None:
                    verticalrate = record[11]
                    if verticalrate > 0:
                        status = "rise"
                    elif verticalrate < 0:
                        status = "descent"
                    else:
                        status = ""
                else:
                    verticalrate = "---"
                    status = ""
                flights.append({
                    'Callsign': record[1],
                    'Country': record[2],
                    'Speed': speed,
                    'Altitude': altitude,
                    'VerticalRate': verticalrate,
                    'Status': status })
    except:
        return render(request, 'flightinfo/error.html', {
            'errormsg':'Oops, something went wrong...',
            'response':respjson })

    return render(request, 'flightinfo/base.html', {'flights':flights, 'loc':loc})
