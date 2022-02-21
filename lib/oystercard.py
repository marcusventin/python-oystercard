class Oystercard():
    MAXIMUM_BALANCE = 90
    MINIMUM_BALANCE = 1
    MINIMUM_FARE = 1

    def __init__(self):
        self.balance = 0
        self.in_journey = False
        self.entry_station = None
        self.journey_history = []
        self.current_journey = {}
    
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
            self.in_journey = True
            self.entry_station = entry_station
            self.current_journey['entry_station'] = entry_station.name

    def touch_out(self, exit_station):
        self.in_journey = False
        self.deduct()
        self.entry_station = None
        self.current_journey['exit_station'] = exit_station.name
        self.journey_history.append(self.current_journey)
        self.current_journey = {}
