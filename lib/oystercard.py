class Oystercard():
    MAXIMUM_BALANCE = 90

    def __init__(self):
        self.balance = 0
    
    def top_up(self, top_up):
        if type(top_up) != int:
            raise Exception("Top up value must be a whole number.")
        if top_up <= 0:
            raise Exception("Top up value must be positive.")
        if self.balance + top_up > self.MAXIMUM_BALANCE:
            raise Exception("You can't exceed the maximum balance.")
        else:
            self.balance += top_up
