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

