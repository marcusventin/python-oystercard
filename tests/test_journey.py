from unittest.mock import MagicMock

from lib.journey import Journey

class TestJourney():
    def test_start_journey_sets_in_journey_to_True(self):
        journey = Journey()

        station = MagicMock()
        station.name = 'test_entry'

        journey.in_journey = False

        journey.start_journey(station)
        assert journey.in_journey == True
    
    def test_end_journey_sets_in_journey_to_False(self):
        journey = Journey()

        station = MagicMock()
        station.name = 'test_exit'

        journey.in_journey = True

        journey.end_journey(station)
        assert journey.in_journey == False
    
    def test_journey_history_is_empty_by_default(self):
        journey = Journey()
        assert len(journey.journey_history) == 0

    def test_start_journey_adds_entry_station_to_current_journey(self):
        journey = Journey()
        assert journey.current_journey == {}

        station = MagicMock()
        station.name = 'test_station'
        journey.start_journey(station)

        assert "entry_station" in journey.current_journey.keys()
        assert journey.current_journey['entry_station'] == 'test_station'
    
    def test_end_journey_adds_completed_journey_to_journey_history(self):
        journey = Journey()
        assert journey.journey_history == []

        entry_station = MagicMock()
        entry_station.name = 'test_entry'

        exit_station = MagicMock()
        exit_station.name = 'test_exit'

        journey.start_journey(entry_station)
        journey.end_journey(exit_station)

        assert len(journey.journey_history) == 1
        assert journey.journey_history[0]['entry_station'] == 'test_entry'
        assert journey.journey_history[0]['exit_station'] == 'test_exit'