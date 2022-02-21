from lib.station import Station

class TestStation():
    def test_has_name_attribute(self):
        station = Station("King's Cross")
        assert station.name == "King's Cross"

    def test_has_zone_attribute(self):
        station = Station(1)
        assert station.zone == 1