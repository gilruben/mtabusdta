from pytest import raises
from ..mtabusdata.entities import Stop

class TestStopId():
    # Test a valid stop id.
    def test_stop_id(self):
        new_stop = Stop('MTA_501248')
        assert new_stop.stop_id == 'MTA_501248'


class TestReassigningProperties():
    # Test reassigning stop_id
    # Should not able to reassign the original stop id.
    def test_reassign_stop_id(self):
        new_stop = Stop('MTA_501248')
        new_stop.stop_id = 'MTA_550943'

        assert new_stop.stop_id == 'MTA_501248'


    # Test reassigning timestamp.
    # Should not able to reassign the original timestamp.
    def test_reassign_timestamp(self):
        new_stop = Stop('MTA_501248')
        savedTimestamp = new_stop.timestamp
        new_stop.timestamp = '131312344'

        assert new_stop.timestamp == savedTimestamp


    # Test reassigning next_buses.
    # Should not able to reassign the original next_buses.
    def test_reassign_next_buses(self):
        new_stop = Stop('MTA_501248')
        next_buses = new_stop.next_buses

        assert next_buses is not new_stop.next_buses
        assert next_buses[0] is not new_stop.next_buses[0]


    # Test reassigning stop_info.
    # Should not able to reassign the original stop_info.
    def test_reassign_stop_info(self):
        new_stop = Stop('MTA_501248')
        stop_info = new_stop.stop_info

        assert stop_info is not new_stop.stop_info


    # Test reassigning situations.
    # Should not able to reassign the original situations.
    def test_reassign_situations(self):
        new_stop = Stop('MTA_501248')
        situations = new_stop.situations

        assert situations is not new_stop.situations
