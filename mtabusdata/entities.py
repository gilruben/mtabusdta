from _data_fetch import get_bus_data

class Bus():
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
            self.name = name.upper()
            self.directions = data['directions']
            self.routeId = data['routeId']
