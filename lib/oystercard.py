from lib.journey import Journey

class Oystercard():
    MAXIMUM_BALANCE = 90
    MINIMUM_BALANCE = 1
    MINIMUM_FARE = 1
    PENALTY_FARE = 6

    def __init__(self):
        self.balance = 0
        self.journey = Journey(self)
    
    def top_up(self, top_up):
        if type(top_up) != int:
            raise Exception("Top up value must be a whole number.")
        if top_up <= 0:
            raise Exception("Top up value must be positive.")
        if self.balance + top_up > self.MAXIMUM_BALANCE:
            raise Exception("You can't exceed the maximum balance.")
        else:
            self.balance += top_up
    
    def deduct(self, fare=MINIMUM_FARE):
        self.balance -= fare
    
    def touch_in(self, entry_station):
        if self.balance < self.MINIMUM_BALANCE:
            raise Exception("Insufficient balance to travel.")
        else:
            self.journey.start_journey(entry_station)
            self.deduct(self.journey.fare)
            
    def touch_out(self, exit_station):
        self.journey.end_journey(exit_station)
        self.deduct(self.journey.fare)
        
        
