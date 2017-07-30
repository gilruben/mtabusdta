import requests, json

def get_bus_data(bus):
    url = 'http://bustime.mta.info/api/search?q=' + bus

    response = requests.get(url)

    data = json.loads(response.text)

    is_empty = data["searchResults"]["empty"]
    matches = data["searchResults"]["matches"]
    suggestions = data["searchResults"]["suggestions"]

    bus_data = {
        "empty": False
    }

    #
    if len(matches):
        directions = matches[0]["directions"]

        direction0 = {
            "destination": str(directions[0]["destination"]),
            "directionId": int(directions[0]["directionId"])
        }
        direction1 = {
            "destination": str(directions[1]["destination"]),
            "directionId": int(directions[1]["directionId"])
        }

        bus_data["directions"] = [direction0, direction1]
        bus_data["routeId"] = str(matches[0]["id"])
        bus_data["bus"] = str(matches[0]["shortName"])


    return bus_data
