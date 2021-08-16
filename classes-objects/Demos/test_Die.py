# Test Die class:

from Die import Die
from collections import Counter

die = Die()
for i in range(100000):
    roll = die.roll()
    
c = Counter(die.rolls)
c_sorted = sorted(c.items())
print("Die class keeps track of roll history:")
print(c_sorted)
print('-'*70)