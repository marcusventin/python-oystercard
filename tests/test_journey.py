from unittest.mock import MagicMock
from random import randint

from lib.journey import Journey
from lib.oystercard import Oystercard

class TestJourney():
    def test_start_journey_sets_in_journey_to_True(self):
        card = MagicMock()
        journey = Journey(card)

        station = MagicMock()
        station.name = 'test_entry'

        journey.in_journey = False

        journey.start_journey(station)
        assert journey.in_journey == True
    
    def test_end_journey_sets_in_journey_to_False(self):
        card = MagicMock()
        journey = Journey(card)

        station = MagicMock()
        station.name = 'test_exit'

        journey.in_journey = True

        journey.end_journey(station)
        assert journey.in_journey == False
    
    # def test_journey_history_is_empty_by_default(self):
    #     card = MagicMock()
    #     journey = Journey(card)
    #     assert len(journey.journey_history) == 0

    def test_start_journey_adds_entry_station_to_current_journey(self):
        card = MagicMock()
        journey = Journey(card)
        assert journey.current_journey == {}

        station = MagicMock()
        station.name = 'test_station'

        journey.start_journey(station)
        
        assert journey.current_journey['entry_station'] == 'test_station'
    
    # def test_end_journey_adds_completed_journey_to_journey_history(self):
    #     card = MagicMock()
    #     journey = Journey(card)
    #     assert journey.journey_history == []

    #     entry_station = MagicMock()
    #     entry_station.name = 'test_entry'

    #     exit_station = MagicMock()
    #     exit_station.name = 'test_exit'

    #     journey.start_journey(entry_station)
    #     journey.end_journey(exit_station)

    #     assert len(journey.journey_history) == 1
    #     assert journey.journey_history[0]['entry_station'] == 'test_entry'
    #     assert journey.journey_history[0]['exit_station'] == 'test_exit'
    
    def test_start_journey_assigns_penalty_fare_if_uncompleted_previous_journey(self):
        card = MagicMock()
        random_number = randint(1, 100)
        card.PENALTY_FARE = random_number

        station = MagicMock()
        station.name = 'test_station'

        journey = Journey(card)
        journey.current_journey = {'entry_station': 'test_entry',}

        journey.start_journey(station)

        assert journey.fare == random_number
    
    def test_end_journey_assigns_penalty_fare_if_no_entry_station(self):
        card = MagicMock()
        random_number = randint(1, 100)
        card.PENALTY_FARE = random_number

        station = MagicMock()
        station.name = 'test_station'

        journey = Journey(card)
        assert journey.current_journey == {}

        journey.end_journey(station)

        assert journey.fare == random_number
    
    def test_end_journey_deducts_min_fare_if_completed_journey(self):
        card = MagicMock()
        random_number = randint(1, 100)
        card.MINIMUM_FARE = random_number

        station = MagicMock()
        station.name = 'test_station'

        journey = Journey(card)
        journey.current_journey = {'entry_station': 'test_entry',}

        journey.end_journey(station)

        assert journey.fare == random_number

