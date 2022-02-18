from lib.oystercard import Oystercard

class TestOystercard():
    def test_has_balance_attribute(self):
        card = Oystercard()
        assert card.balance == 0