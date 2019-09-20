class Player:
    def __init__(self):
        self.space = 0

    def setSpace(self, rollAmount):
        if self.space + rollAmount > 39:
            self.space = rollAmount - 40
        else:
            self.space += rollAmount
        
        