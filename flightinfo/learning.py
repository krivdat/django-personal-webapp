import json
import requests

locations = { # lamin,lomin,lamax,lomax
    "Switzerland": [45.8389,5.9962,47.8229,10.5226],
    "Prague": [49.8604,14.0617,50.2457,14.9653],
    "Kosice": [48.6136,21.1367,48.7790,21.3547],
}

loc = "Kosice"
query = "https://opensky-network.org/api/states/all?" \
    + "lamin=" + str(locations[loc][0]) \
    + "&lomin=" + str(locations[loc][1]) \
    + "&lamax=" + str(locations[loc][2]) \
    + "&lomax=" + str(locations[loc][3])
# print(query)

response = requests.get(query)
respjson = json.loads(response.text)

print("Found {} results for location {}.".format(len(respjson['states']),loc))
print("List of aircrafts not on ground:\n")

for record in respjson['states']:
    if record[8] is not True:
        print("Callsign: {}".format(record[1]))
        print("Country: {}".format(record[2]))
        print("Speed (km/h): {:.0f}".format(record[9]*3.6))
        print("Altitude (m): {:.0f}\n".format(record[7]))
        # print("On ground: {}\n".format(record[8]))

# print(respjson['states'][0])
