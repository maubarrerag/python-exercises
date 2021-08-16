# Get unique permutations:
dice_rolls = [(a,b,c,d,e)
              for a in range(1,7)
              for b in range(1,7)
              for c in range(1,7)
              for d in range(1,7)
              for e in range(1,7)]

print('Solution 1', dice_rolls, '-'*70, sep='\n')

# Get unique combinations:
dice_rolls = [(a,b,c,d,e)
              for a in range(1,7)
              for b in range(a,7)
              for c in range(b,7)
              for d in range(c,7)
              for e in range(d,7)]

print('Solution 2', dice_rolls, '-'*70, sep='\n')