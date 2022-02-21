class Journey():
    def __init__(self, oystercard):
        self.oystercard = oystercard
        self.in_journey = False
        self.journey_history = []
        self.current_journey = {}
    
    def start_journey(self, entry_station):
        self.in_journey = True
        if self.current_journey != {}:
            self.oystercard.deduct(self.oystercard.PENALTY_FARE)
            self.clear_journey()
        self.current_journey['entry_station'] = entry_station.name
    
    def end_journey(self, exit_station):
        if 'entry_station' not in self.current_journey.keys():
            self.oystercard.deduct(self.oystercard.PENALTY_FARE)
        else:
            self.oystercard.deduct()
        self.in_journey = False
        self.current_journey['exit_station'] = exit_station.name
        self.clear_journey()
    
    def clear_journey(self):
        self.journey_history.append(self.current_journey)
        self.current_journey = {}
