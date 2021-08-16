from collections import Counter
with open('../Solutions/Declaration_of_Independence.txt') as f:
    doi = f.read()

word_list = [word for word in doi.upper().split() if len(word) > 5]
    
c = Counter(word_list)
print('10 most common word in the Declaration of Independence:', c.most_common(10),'-'*70,sep='\n')

print('All the words in the Declaration of Independence:', list(c.elements()),'-'*70,sep='\n')