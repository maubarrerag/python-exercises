import random
from collections import Counter

from WeightedDie import WeightedDie

# Weighting Die class:

class WeightingDie(WeightedDie):
    "A weighted die"
    def __init__(self, sides=6):
        """Creates a die that favors sides it has previously rolled
        
        Keyword arguments:
        sides (int) -- number of die sides.
        """
        self._weights = [1] * sides
        super().__init__(self._weights, sides)
    
    def roll(self):
        """Returns a value between 1 and the number of die sides."""
       # COMPLETE THE CODE