# Create a dictionary that shows the number of different ways each 
# number (2 through 12) can be rolled.
dice_rolls = [(a,b)
              for a in range(1,7)
              for b in range(1,7)]

# Solution 1 if else
# Loop through list checking for existence of each key. 
# If it exists, increment it by 1. If it doesn't, add it 
# and set it to 1.
roll_counts = {}
for roll in dice_rolls:
    if sum(roll) in roll_counts:
        roll_counts[sum(roll)] += 1
    else:
        roll_counts[sum(roll)] = 1
        
print('Solution 1:', roll_counts,'-'*70,sep='\n')

# Solution 2 try except
# Loop through trying to increment each key. If it fails, this means 
# the key doesn't exist, so add it and set it to 1.roll_counts = {}
roll_counts = {}
for roll in dice_rolls:
    try:
        roll_counts[sum(roll)] += 1
    except KeyError:
        roll_counts[sum(roll)] = 1
        
print('Solution 2:', roll_counts,'-'*70,sep='\n')

# Solution 3 defaultdict
from collections import defaultdict

roll_counts = defaultdict(int)
for roll in dice_rolls:
    roll_counts[sum(roll)] += 1

print('Solution 3:', roll_counts,'-'*70,sep='\n')