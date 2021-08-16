# Test WeightingDie class:

from WeightingDie import WeightingDie
from collections import Counter

die = WeightingDie()

for i in range(1000):
    die.roll()
    
c = Counter(die.rolls)
c_sorted = sorted(c.items())
print(c_sorted, die._weights)