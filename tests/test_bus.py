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
    # Test the directionId variable of the Bus class when the class was
    # initialized without a directionId
    def test_directionId_not_given(self):
        new_bus = Bus('Q23')
        assert new_bus.directionId == 0

    # Test the directionId variable of the Bus class when the class was
    # initialized with a valid int as directionId
    def test_directionId_given(self):
        new_bus = Bus('Q23', 1)
        assert new_bus.directionId == 1

    # Test the directionId variable of the Bus class when the class was
    # initialized with an invalid int as directionId
    def test_directionId_incorrect_int(self):
        with raises(ValueError):
            raise Bus('Q23', 9)

    # Test the directionId variable of the Bus class when the class was
    # initialized with an non int variable as directionId
    def test_directionId_incorrect_type(self):
        with raises(TypeError):
            raise Bus('Q23', '9')


class TestBusInitialization():
    def test_bus(self):
        new_bus = Bus('Q23', 1)

        assert new_bus.directionId == 1
        assert type(new_bus.name) == str
        assert type(new_bus.directions) == list
        assert len(new_bus.directions) == 2
        assert type(new_bus.directions[0]) == dict
        assert type(new_bus.directions[0]["destination"]) == str
        assert type(new_bus.directions[0]["directionId"]) == int
        assert type(new_bus.directions[1]) == dict
        assert type(new_bus.directions[0]["destination"]) == str
        assert type(new_bus.directions[0]["directionId"]) == int
        assert type(new_bus.routeId) == str


class TestBusGetStops():
    def test_get_stops(self):
        new_bus = Bus('Q23')
        stops = new_bus.get_stops()

        assert type(stops) == dict
        assert len(stops.keys()) == 2
        assert type(stops['directionId']) == int
        assert stops['directionId'] == 0
        assert type(stops['stops']) == list
        assert len(stops['stops']) > 0
