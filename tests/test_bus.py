from pytest import raises
from ..mtabusdata.entities import Bus

class TestBusName():
    # Test a valid bus name
    def test_name(self):
        new_bus = Bus('Q23')
        assert new_bus.name == 'Q23'

    # Test an invalid bus name
    def test_invalid_name(self):
        with raises(ValueError):
            raise Bus('Z300')

    # Test an invalid bus name, but suggestions are given
    def test_invalid_name_with_sugg(self):
        with raises(ValueError):
            raise Bus('Q20')


class TestBusDirectionId():
    # Test the direction_id variable of the Bus class when the class was
    # initialized without a direction_id
    def test_direction_id_not_given(self):
        new_bus = Bus('Q23')
        assert new_bus.direction_id == 0

    # Test the direction_id variable of the Bus class when the class was
    # initialized with a valid int as direction_id
    def test_direction_id_given(self):
        new_bus = Bus('Q23', 1)
        assert new_bus.direction_id == 1

    # Test the direction_id variable of the Bus class when the class was
    # initialized with an invalid int as direction_id
    def test_direction_id_incorrect_int(self):
        with raises(ValueError):
            raise Bus('Q23', 9)

    # Test the direction_id variable of the Bus class when the class was
    # initialized with an non int variable as direction_id
    def test_direction_id_incorrect_type(self):
        with raises(TypeError):
            raise Bus('Q23', '9')


# Test that certain properties of Bus class cannot change
class TestPropsCanNotChange():
    # Test editing name property of a bus instance
    def test_edit_bus_name(self):
        new_bus = Bus('Q23')
        new_bus.name = 'Q34'
        # User should not be able to edit the name property
        assert new_bus.name == 'Q23'

    def test_edit_bus_routeId(self):
        new_bus = Bus('Q23')
        new_bus.routeId = 'MTABC_Q66'
        # User should not be able to edit the routeId property
        assert new_bus.routeId == 'MTABC_Q23'



class TestBusInitialization():
    def test_bus(self):
        new_bus = Bus('Q23', 1)

        assert new_bus.direction_id == 1
        assert type(new_bus.name) == str
        assert type(new_bus.directions) == list
        assert len(new_bus.directions) == 2
        assert type(new_bus.directions[0]) == dict
        assert type(new_bus.directions[0]["destination"]) == str
        assert type(new_bus.directions[0]["direction_id"]) == int
        assert type(new_bus.directions[1]) == dict
        assert type(new_bus.directions[0]["destination"]) == str
        assert type(new_bus.directions[0]["direction_id"]) == int
        assert type(new_bus.routeId) == str


class TestBusGetStops():
    def test_get_stops(self):
        new_bus = Bus('Q23')
        stops = new_bus.get_stops()

        assert type(stops) == dict
        assert len(stops.keys()) == 2
        assert type(stops['direction_id']) == int
        assert stops['direction_id'] == 0
        assert type(stops['stops']) == list
        assert len(stops['stops']) > 0
