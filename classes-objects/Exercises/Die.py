import random

class Die:

    def __init__(self, sides=6):
        self._sides = sides

    def getSlides(self):
        return self._slides
    
    def roll(self):
        if self._sides > 0:
            return random.randint(1,self._sides)
        
    #add a roll() method