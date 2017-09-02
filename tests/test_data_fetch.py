from pytest import raises
from ..mtabusdata._data_fetch import get_bus_data, get_bus_stops, get_stop_data


class TestGetBusData():
    # Test get_bus_data function with a valid MTA bus as argument.
    def test_get_bus_data_valid_arg(self):
        bus_data = get_bus_data('q23')

        assert len(bus_data.keys()) == 4
        assert type(bus_data["directions"]) == list
        assert len(bus_data["directions"]) == 2
        assert type(bus_data["directions"][0]) == dict
        assert type(bus_data["directions"][0]["destination"]) == str
        assert type(bus_data["directions"][0]["direction_id"]) == int
        assert type(bus_data["directions"][1]) == dict
        assert type(bus_data["directions"][0]["destination"]) == str
        assert type(bus_data["directions"][0]["direction_id"]) == int
        assert type(bus_data["route_id"]) == str
        assert type(bus_data["bus"]) == str


    # Test get_bus_data function with a invalid bus as argument.
    # Returns a dictionary with a list of suggestions.
    def test_get_bus_data_suggestions(self):
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
        assert type(suggested_data["directions"][0]["direction_id"]) == int
        assert type(suggested_data["directions"][1]) == dict
        assert type(suggested_data["directions"][0]["destination"]) == str
        assert type(suggested_data["directions"][0]["direction_id"]) == int
        assert type(suggested_data["route_id"]) == str
        assert type(suggested_data["bus"]) == str


    # Test get_bus_data function with a invalid bus as argument.
    # No matching bus data or suggestions will be found.
    # Returns a dictionary with key 'empty' and value True.
    def test_get_bus_data_no_mathches_no_suggestions(self):
        bus_data = get_bus_data('z30089')

        assert len(bus_data.keys()) == 1
        assert bus_data['empty'] == True
        assert type(bus_data['empty']) == bool


class TestGetBusStops():
    # Test get_bus_stops function with a valid route_id and direction_id.
    # Returns a dictionary with a list of all the stops for the given route_id and
    # direction_id.
    def test_get_bus_stops(self):
        stops = get_bus_stops('MTA NYCT_Q16', 1)

        assert type(stops['stops']) == list
        assert len(stops['stops']) > 0


    # Test get_bus_stops function with a invalid route_id.
    # Returns a dictionary with an empty list and an error string.
    def test_get_bus_stops_bad_route_id(self):
        stops = get_bus_stops('MTA NYCT_Q', 1)

        assert len(stops.keys()) == 2
        assert type(stops['stops']) == list
        assert len(stops['stops']) == 0
        assert stops['error'] == 'route_id is not valid'


    # Test get_bus_stops function with a invalid direction_id.
    # Returns a dictionary with an empty list and an error string.
    def test_get_bus_stops_bad_direction_id(self):
        stops = get_bus_stops('MTA NYCT_Q16', 9)

        assert len(stops.keys()) == 2
        assert type(stops['stops']) == list
        assert len(stops['stops']) == 0
        assert stops['error'] == 'direction_id is not valid'


class TestGetStopData():
    # Test get_stop_data function with a valid stop id.
    # Returns a list with data about the stop given.
    def test_get_stop_data(self):
        stop_data = get_stop_data('MTA_550943')

        assert type(stop_data) == dict
        assert type(stop_data['timestamp']) == str

        stop = stop_data['stop']
        assert type(stop) == dict
        assert type(stop['id']) == str
        assert type(stop['latitude']) == float
        assert type(stop['longitude']) == float
        assert type(stop['name']) == str
        assert type(stop['direction']) == str

        assert type(stop_data['next_buses']) == list
        assert type(stop_data['situations']) == list


        # Test one element from next_buses field if it exists.
        try:
            onebus = stop_data['next_buses'][0]

            assert type(onebus) == dict
            assert type(onebus['bearing']) == float
            assert type(onebus['destination']) == str
            assert type(onebus['destination_id']) == str
            assert type(onebus['direction_id']) == int
            assert type(onebus['route_id']) == str
            assert type(onebus['operator_id']) == str
            assert type(onebus['origin_id']) == str
            assert type(onebus['progress_rate']) == str
            assert type(onebus['bus_name']) == str
            assert type(onebus['location']) == dict
            assert type(onebus['location']['latitude']) == float
            assert type(onebus['location']['longitude']) == float
        except IndexError:
            pass


        # Test one element from situations field if it exists.
        try:
            one_situation = stop_data['situations'][0]

            assert type(one_situation['consequences']) == list
            assert type(one_situation['start_time']) == str
            assert type(one_situation['description']) == str
            assert type(one_situation['severity']) == str
            assert type(one_situation['situation_number']) == str
        except IndexError:
            pass

    # Test get_stop_data with an invalid string argument.
    # Returns a dictionary with one key, 'error'.
    def test_get_stop_data_bad_stop_id(self):
        stop_data = get_stop_data('MTA')

        assert type(stop_data) == dict
        assert stop_data['error'] == 'Stop id is not valid'


    # Test get_stop_data with a non string argument.
    # Should raise a TypeError.
    def test_get_stop_data_nonstring_arg(self):
        with raises(TypeError):
            raise(get_stop_data(123))
