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
