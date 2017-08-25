import requests, json

# Receives a string representing an MTA bus name. ex: q23, q44, m60 (is not
# case sensitive).
# Returns a dictionary with data pertaining to that bus.
#
# If the bus given as argument matches an existing bus, the function will return
# the bus name, routeId, and a list of directions in which the bus can go. Each
# direction is a dictionary containing the destination(final stop) and
# directionId.
#
# If the bus given as argument does not match an existing bus, the bustime
# api will attempt to give suggestions. If suggestions are available, the
# function will return a dictionary with a list of the suggested bus data. Each
# bus data in the list will be formatted the same way as when a matching bus is
# found by the function.
#
# If the bus has no matching data or suggestions, a dictionary with key 'empty'
# and value True is returned.
#
# ALL RETURNS HAVE AN 'empty' KEY THAT SIGNALS WHETHER DATA WAS FOUND OR NOT.
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


# Receives string representing the routeId and an integer representing the
# directionId.
# Returns a dictionary containing a list of all the stops for the given routeId
#
# If an incorrect routeId or directionId is supplied, the dictionary returned
# will contain an empty list of stops and a string representing an error message
def get_bus_stops(routeId, directionId):
    stops = { 'stops': [] }

    if  directionId != 0 and directionId != 1:
        stops['error'] = 'directionId is not valid'
        return stops


    routeId = routeId.replace(' ', '+')
    url = 'http://bustime.mta.info/api/stops-on-route-for-direction?routeId=' + routeId + '&directionId=' + str(directionId)
    response = requests.get(url)


    try:
        stops = response.json()
    except ValueError:
        stops['error'] = 'routeId is not valid'

    return stops


# Receives a string representing the stop id
# Returns a dictionary with data about the stop
def get_stop_data(stop_id):
    if type(stop_id) != str:
        raise TypeError('Stop id must be a string')

    stop_data = {}
    url = 'http://bustime.mta.info/api/stop-for-id?stopId=' + stop_id
    response = requests.get(url)

    try:
        data = response.json()

        # Extracts specific fields from a dictionary containing bus data
        # Returns a new dictionary with data about the bus
        def extract_bus_data(bus_data):
            data = bus_data['MonitoredVehicleJourney']
            location = data['VehicleLocation']

            return {
              'bearing': data['Bearing'],
              'destination': str(data['DestinationName']),
              'destination_id': str(data['DestinationRef']),
              'direction_id': int(data['DirectionRef']),
              'route_id': str(data['LineRef']),
              'operator_id': str(data['OperatorRef']),
              'origin_id': str(data['OriginRef']),
              'progress_rate': str(data['ProgressRate']),
              'bus_name': str(data['PublishedLineName']),
              'location': {
                'latitude': location['Latitude'],
                'longitude': location['Longitude']
              }
            }


        # Extracts specific fields from a dictionary containing situation data.
        # Returns a new dictionary with data about the situation
        def extract_situation_data(situation_data):
            return {
              'consequences': situation_data['Consequences']['Consequence'],
              'start_time': str(situation_data['PublicationWindow']['StartTime']),
              'description': str(situation_data['Description']),
              'severity': str(situation_data['Severity']),
              'situation_number': str(situation_data['SituationNumber'])
            }


        service_data = data['siri']['Siri']['ServiceDelivery']
        timestamp = str(service_data['ResponseTimestamp'])
        buses = service_data['StopMonitoringDelivery'][0]['MonitoredStopVisit']
        stop_info = data['stop']

        situations = service_data['SituationExchangeDelivery']

        try:
            situations = situations[0]['Situations']['PtSituationElement']
        except IndexError:
            pass


        stop_data['timestamp'] = timestamp
        stop_data['next_buses'] = map(extract_bus_data, buses)
        stop_data['situations'] = map(extract_situation_data, situations)
        stop_data['stop'] = {
          'id': str(stop_info['id']),
          'latitude': stop_info['latitude'],
          'longitude': stop_info['longitude'],
          'name': str(stop_info['name']),
          'direction': str(stop_info['stopDirection'])
        }

    except ValueError:
        return { 'error': 'Stop id is not valid' }

    return stop_data
