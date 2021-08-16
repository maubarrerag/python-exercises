from collections import Counter
c = Counter(['green','blue','blue','red','yellow','green','blue'])
c.subtract(['red','yellow','yellow','purple'])
print(c)