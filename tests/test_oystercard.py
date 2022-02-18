from random import randint

from lib.oystercard import Oystercard

class TestOystercard():
    def test_has_balance_attribute(self):
        card = Oystercard()
        assert card.balance == 0
    
    def test_top_up_adds_to_balance(self):
        card = Oystercard()
        assert card.balance == 0
        number = randint(1, 100)
        card.top_up(number)
        assert card.balance == number