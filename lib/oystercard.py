class Oystercard():
    def __init__(self):
        self.balance = 0
    
    def top_up(self, top_up):
        if type(top_up) != int:
            raise Exception("Top up value must be a whole number.")
        else:
            self.balance += top_up
