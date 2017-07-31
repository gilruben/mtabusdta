import requests, json

def get_bus_data(bus):
    # Takes a dictionary containing bus data from the matches list or the
    # the suggestions list. Both the matches and suggestions lists can be found
    # in the searchResults in the response from the api request below.
    # Returns a compacted version of the bus data. Compacted version contains
    # destinations, directionIds, Id, and shortName. This data is necessary.
    def compact_bus_data(data):
        bus_data = {}
        directions = data['directions']

        direction0 = {
            'destination': str(directions[0]['destination']),
            'directionId': int(directions[0]['directionId'])
        }
        direction1 = {
            'destination': str(directions[1]['destination']),
            'directionId': int(directions[1]['directionId'])
        }

        bus_data['directions'] = [direction0, direction1]
        bus_data['routeId'] = str(data['id'])
        bus_data['bus'] = str(data['shortName'])

        return bus_data




    url = 'http://bustime.mta.info/api/search?q=' + bus
    response = requests.get(url)
    data = json.loads(response.text)

    search_results = data['searchResults']
    is_empty = search_results['empty']
    matches = search_results['matches']
    suggestions = search_results['suggestions']


    # If there is data for the bus passed as argument, take what is necessary
    # from the data and return it.
    # Else if there are suggestions, take what is necessary from each suggested
    # data.
    if len(matches):
        target_data = matches[0]

        bus_data = compact_bus_data(target_data)
        bus_data['empty'] = False

        return bus_data
    elif len(suggestions):
        bus_data = {}
        bus_data['empty'] = False
        bus_data['suggestions'] = map(compact_bus_data, suggestions)

        return bus_data
    else:
        return { 'empty': True }
