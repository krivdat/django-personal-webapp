import json
import requests

locations = { # lamin,lomin,lamax,lomax
    "Switzerland": [45.8389,5.9962,47.8229,10.5226],
    "Prague": [49.8604,14.0617,50.2457,14.9653],
}

# all records for Switzerland
loc = "Prague"
query = "https://opensky-network.org/api/states/all?" \
    + "lamin=" + str(locations[loc][0]) \
    + "&lomin=" + str(locations[loc][1]) \
    + "&lamax=" + str(locations[loc][2]) \
    + "&lomax=" + str(locations[loc][3])
print(query)

response = requests.get(query)
respjson = json.loads(response.text)

print("Found {} results for location {}.\n".format(len(respjson['states']),loc))

for record in respjson['states']:
    print("Callsign: {}".format(record[1]))
    print("Country: {}".format(record[2]))
    print("Speed (km/h): {}".format(record[9]*3.6))
    print("Altitude (m): {}".format(record[7]))
    print("On ground: {}\n".format(record[8]))

# print(respjson['states'][0])
