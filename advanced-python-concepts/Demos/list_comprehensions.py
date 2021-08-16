# Roll two dice to create a list of 2-item tuples:
dice_rolls = [(a,b)
              for a in range(1,7)
              for b in range(1,7)]
print ('Example 1:', dice_rolls,'-'*70,sep='\n')

# Roll two dice without duplicates:
dice_rolls = [(a,b)
              for a in range(1,7)
              for b in range(a,7)]
print ('Example 2:', dice_rolls,'-'*70,sep='\n')

# Accomplish same thing without list comprehension
dice_rolls = []
for a in range(1,7):
    for b in range(a,7):
        dice_rolls.append( (a,b) )
print (dice_rolls)
print ('Example 3:', dice_rolls,'-'*70,sep='\n')