from random import randint
import pytest

from lib.oystercard import Oystercard

class TestOystercard():
    def test_has_balance_attribute(self):
        card = Oystercard()
        assert card.balance == 0
    
    def test_top_up_adds_to_balance(self):
        card = Oystercard()
        assert card.balance == 0
        number = randint(1, card.MAXIMUM_BALANCE)
        card.top_up(number)
        assert card.balance == number
    
    def test_top_up_raises_error_if_exceeds_maximum_balance(self):
        card = Oystercard()
        card.top_up(card.MAXIMUM_BALANCE)
        with pytest.raises(Exception,
            match = "You can't exceed the maximum balance."):
            card.top_up(1)
    
    def test_deduct_subtracts_fare_from_balance(self):
        card = Oystercard()
        card.top_up(card.MAXIMUM_BALANCE)
        number = randint(1, card.MAXIMUM_BALANCE)
        card.deduct(number)

        assert card.MAXIMUM_BALANCE - number == card.balance
    
    def test_touch_in_sets_in_journey_to_true(self):
        card = Oystercard()
        card.balance = card.MAXIMUM_BALANCE
        assert card.in_journey == False
        card.touch_in("entry_station")
        assert card.in_journey == True
    
    def test_touch_out_sets_in_journey_to_false(self):
        card = Oystercard()
        card.in_journey = True
        card.touch_out()
        assert card.in_journey == False
    
    def test_touch_in_raises_error_if_balance_is_below_minimum(self):
        card = Oystercard()
        card.balance = card.MINIMUM_BALANCE - 1
        with pytest.raises(Exception,
            match="Insufficient balance to travel."):
            card.touch_in("entry_station")
    
    def test_touch_out_deducts_fare_from_balance(self):
        card = Oystercard()
        card.balance = card.MAXIMUM_BALANCE
        card.in_journey = True
        card.touch_out()
        assert card.balance == card.MAXIMUM_BALANCE - card.MINIMUM_FARE

    def test_touch_in_saves_entry_station(self):
        card = Oystercard()
        card.balance = card.MAXIMUM_BALANCE
        card.touch_in("entry_station")
        assert card.entry_station == "entry_station"

    def test_touch_out_sets_entry_station_to_None(self):
        card = Oystercard()
        card.balance = card.MAXIMUM_BALANCE
        card.touch_in("entry_station")
        card.touch_out()
        assert card.entry_station == None

