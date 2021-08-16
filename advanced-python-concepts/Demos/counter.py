from collections import Counter
c = Counter(['green','blue','blue','red','yellow','green','blue'])
print('Example 1:', c, '-'*70, sep='\n')

dice_rolls = [(a,b)
              for a in range(1,7)
              for b in range(1,7)]

roll_sums = [sum(roll) for roll in dice_rolls]
c = Counter(roll_sums)
print('Example 2:', c, '-'*70, sep='\n')