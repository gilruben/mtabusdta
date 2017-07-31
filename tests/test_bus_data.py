from ..bus_data import get_bus_data, get_bus_stops

# Test get_bus_data function with a valid MTA bus as argument
def test_get_bus_data_valid_arg():
    bus_data = get_bus_data('q23')

    assert len(bus_data.keys()) == 4
    assert type(bus_data["directions"]) == list
    assert len(bus_data["directions"]) == 2
    assert type(bus_data["directions"][0]) == dict
    assert type(bus_data["directions"][0]["destination"]) == str
    assert type(bus_data["directions"][0]["directionId"]) == int
    assert type(bus_data["directions"][1]) == dict
    assert type(bus_data["directions"][0]["destination"]) == str
    assert type(bus_data["directions"][0]["directionId"]) == int
    assert type(bus_data["routeId"]) == str
    assert type(bus_data["bus"]) == str

# Test get_bus_data function with a invalid bus as argument.
# Returns a dictionary with a list of suggestions.
def test_get_bus_data_suggestions():
    bus_data = get_bus_data('q20')

    assert len(bus_data.keys()) == 2
    assert type(bus_data['suggestions']) == list
    assert len(bus_data['suggestions']) > 0

    # The first element in the suggested data list.
    suggested_data = bus_data['suggestions'][0]

    assert type(suggested_data["directions"]) == list
    assert len(suggested_data["directions"]) == 2
    assert type(suggested_data["directions"][0]) == dict
    assert type(suggested_data["directions"][0]["destination"]) == str
    assert type(suggested_data["directions"][0]["directionId"]) == int
    assert type(suggested_data["directions"][1]) == dict
    assert type(suggested_data["directions"][0]["destination"]) == str
    assert type(suggested_data["directions"][0]["directionId"]) == int
    assert type(suggested_data["routeId"]) == str
    assert type(suggested_data["bus"]) == str


# Test get_bus_data function with a invalid bus as argument.
# No matching bus data or suggestions will be found.
# Returns a dictionary with key 'empty' and value True.
def test_get_bus_data_no_mathches_no_suggestions():
    bus_data = get_bus_data('z30089')

    assert len(bus_data.keys()) == 1
    assert bus_data['empty'] == True
    assert type(bus_data['empty']) == bool


# Test get_bus_stops function with a valid routeId and directionId
# Returns a dictionary with a list of all the stops for the given routeId and
# directionId
def test_get_bus_stops():
    stops = get_bus_stops('MTA NYCT_Q16', 1)

    assert type(stops['stops']) == list
    assert len(stops['stops']) > 0
