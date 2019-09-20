import random
class Dice:
    def __init__(self):
        self.d1 = 0
        self.d2 = 0
        self.numOfDoubles = 0
    
    def roll(self):
        self.d1 = random.randint(1, 6)
        self.d2 = random.randint(1, 6)

        # Uh oh doubles?
        if self.d1 is self.d2:
            self.numOfDoubles += 1
        if self.numOfDoubles is 3:
            self.numOfDoubles = 0
            return 10
        else:
            self.numOfDoubles = 0
            return self.d1 + self.d2
