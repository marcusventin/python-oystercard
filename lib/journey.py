class Journey():
    def __init__(self):
        self.in_journey = False
        self.journey_history = []
        self.current_journey = {}
    
    def start_journey(self, entry_station):
        self.in_journey = True
        self.current_journey['entry_station'] = entry_station.name
    
    def end_journey(self, exit_station):
        self.in_journey = False
        self.current_journey['exit_station'] = exit_station.name
        self.clear_journey()
    
    def clear_journey(self):
        self.journey_history.append(self.current_journey)
        self.current_journey = {}
