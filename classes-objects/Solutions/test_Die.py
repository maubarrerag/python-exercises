# Test the Die class:

from Die import Die

die = Die()

print("Roll die once:")
print(die.roll())
print('-'*70)

# Challenge:

from collections import Counter

rolls = []
for i in range(100000):
    roll = die.roll()
    rolls.append(roll)
    
c = Counter(rolls)
c_sorted = sorted(c.items())

print('''Count the number of times each side 
    occurred with 100,000 rolls:''')
print(c_sorted)
print('-'*70)