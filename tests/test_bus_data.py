from ..bus_data import get_bus_data

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
