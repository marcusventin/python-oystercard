class Journey():
    def __init__(self, oystercard):
        self.oystercard = oystercard
        self.in_journey = False
        self.current_journey = {}
        self.fare = 0
    
    def start_journey(self, entry_station):
        if self.current_journey != {}:
            self.clear_journey()
            self.fare = self.oystercard.PENALTY_FARE
        self.in_journey = True
        self.current_journey['entry_station'] = entry_station.name
        
    def end_journey(self, exit_station):
        if 'entry_station' not in self.current_journey.keys():
            self.fare = self.oystercard.PENALTY_FARE
        else:
            self.fare = self.oystercard.MINIMUM_FARE
        self.in_journey = False
        self.current_journey['exit_station'] = exit_station.name
        self.clear_journey()
    
    def clear_journey(self):
        self.current_journey = {}
