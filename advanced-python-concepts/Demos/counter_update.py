grades = {'English':97, 'Math':93, 'Art':74, 'Music':86}
grades.update({'Math':97, 'Gym':93})
print('Updating with a dictionary', grades, '-'*70, sep='\n')

from collections import Counter
c = Counter(['green','blue','blue','red','yellow','green','blue'])
c.update(['red','yellow','yellow','purple'])
print('Updating with a list', c, '-'*70, sep='\n')

c = Counter(['green','blue','blue','red','yellow','green','blue'])
d = Counter(['green','violet'])
c.update(d)
print('Updating with a counter', c, '-'*70, sep='\n')