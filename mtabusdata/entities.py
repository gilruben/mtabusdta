import copy

from _data_fetch import get_bus_data, get_bus_stops, get_stop_data

class Bus(object):
    def __init__(self, name = '', directionId = 0):
        data = get_bus_data(name)
        is_empty = data.get('empty')
        suggestions = data.get('suggestions')


        if is_empty:
            raise ValueError('Not a valid MTA bus name.')
        elif suggestions:
            # Extracts the name of the buses and puts them in a list
            name_suggestions = map(lambda suggestion: suggestion['bus'], suggestions)
            raise ValueError('Not a valid MTA bus name. Suggestions: ' + ', '.join(name_suggestions))
        elif type(directionId) != int:
            # Checks that directionId is either 0 or 1, othewise an error is thrown
            raise TypeError('directionId must an int')
        elif directionId != 0 and directionId != 1:
            raise ValueError('directionId must be 0 or 1')
        else:
            self.directionId = directionId
            self._name = name.upper()
            self._directions = data['directions']
            self._routeId = data['routeId']


    # Getter and Setters for directionId property
    @property
    def directionId(self):
        return self._directionId

    @directionId.setter
    def directionId(self, directionId):
        if type(directionId) != int:
            # Checks that directionId is either 0 or 1, othewise an error is thrown
            raise TypeError('directionId must an int')
        elif directionId != 0 and directionId != 1:
            raise ValueError('directionId must be 0 or 1')
        else:
            self._directionId = directionId


    # Getter and Setter for name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        pass


    # Getter and Setter for directions property
    @property
    def directions(self):
        return self._directions

    @name.setter
    def name(self, directions):
        pass


    # Getter and Setter for routeId property
    @property
    def routeId(self):
        return self._routeId

    @routeId.setter
    def routeId(self, routeId):
        pass


    def get_stops(self):
        # Will catch the error thrown if stops is not an attribute of self.
        try:
            # If stops were previously saved, and those stops correspond to the
            # directionId saved, return the stops.
            if self.stops and (self.stops.directionId == self.directionId):
                return self.stops
        except AttributeError:
            pass

        # If no stops were previously saved or if the saved stops do not
        # correspond to the saved directionId, get and save stop data from
        # bustime api.
        stops = get_bus_stops(self.routeId, self.directionId)['stops']
        self.stops = {
          'directionId': self.directionId,
          'stops': stops
        }

        return self.stops


class Stop(object):
    def __init__(self, stop_id):
        data = get_stop_data(stop_id)

        self._stop_id = stop_id.upper()
        self._timestamp = data['timestamp']
        self._next_buses = data['next_buses']
        self._stop_info = data['stop']
        self._situations = data['situations']


    # Getter and Setters for stop_id property
    @property
    def stop_id(self):
        return self._stop_id

    @stop_id.setter
    def stop_id(self, stop_id):
        pass


    # Getter and Setter for timestamp property
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        pass


    # Getter and Setter for next_buses property
    @property
    def next_buses(self):
        return copy.deepcopy(self._next_buses)

    @next_buses.setter
    def next_buses(self, next_buses):
        pass


    # Getter and Setter for stop_info property
    @property
    def stop_info(self):
        return copy.deepcopy(self._stop_info)

    @stop_info.setter
    def stop_info(self, stop_info):
        pass


    # Getter and Setter for situations property
    @property
    def situations(self):
        return copy.deepcopy(self._situations)

    @situations.setter
    def situatuations(self, situations):
        pass
