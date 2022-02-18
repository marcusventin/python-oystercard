class Oystercard():
    MAXIMUM_BALANCE = 90
    MINIMUM_BALANCE = 1

    def __init__(self):
        self.balance = 0
        self.in_journey = False
    
    def top_up(self, top_up):
        if type(top_up) != int:
            raise Exception("Top up value must be a whole number.")
        if top_up <= 0:
            raise Exception("Top up value must be positive.")
        if self.balance + top_up > self.MAXIMUM_BALANCE:
            raise Exception("You can't exceed the maximum balance.")
        else:
            self.balance += top_up
    
    def deduct(self, fare):
        self.balance -= fare
    
    def touch_in(self):
        if self.balance < self.MINIMUM_BALANCE:
            raise Exception("Insufficient balance to travel.")
        else:
            self.in_journey = True

    def touch_out(self):
        self.in_journey = False
