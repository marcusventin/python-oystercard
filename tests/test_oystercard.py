from random import randint
import pytest
from unittest.mock import MagicMock

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
    
    def test_touch_in_raises_error_if_balance_is_below_minimum(self):
        card = Oystercard()
        card.balance = card.MINIMUM_BALANCE - 1

        entry_station = MagicMock()
        entry_station.name = 'entry_station'

        with pytest.raises(Exception,
            match="Insufficient balance to travel."):
            card.touch_in(entry_station)
