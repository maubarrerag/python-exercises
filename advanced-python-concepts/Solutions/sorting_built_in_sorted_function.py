# Simple sort() method
# This one has been done for you
colors = ['red', 'blue', 'green', 'orange']
# colors.sort()
# print(colors)
new_colors = sorted(colors)
print('Simple sorted()',new_colors,'-'*70, sep='\n')

# The reverse argument:
#colors.sort(reverse=True)
#print(colors)
new_colors = sorted(colors, reverse=True)
print('Reverse order',new_colors,'-'*70, sep='\n')

# The key argument:
#colors.sort(key=len)
#print(colors)
new_colors = sorted(colors, key=len)
print('Ordered by length of key',new_colors,'-'*70, sep='\n')

# The key argument with named function:
def get_lastname(name):
    return name.split()[-1]

people = ['George Washington', 'John Adams', 
    'Thomas Jefferson', 'John Quincy Adams']
#people.sort(key=get_lastname)
#print(people)
new_people = sorted(people, key=get_lastname)
print('Ordered by lastname using named function',new_people,
    '-'*70, sep='\n')

# The key argument with lambda function:
people = ['George Washington', 'John Adams', 
    'Thomas Jefferson', 'John Quincy Adams']
#people.sort(key=lambda name: name.split()[-1])
#print(people)
new_people = sorted(people, key=lambda name: name.split()[-1])
print('Ordered by lastname using lambda function',new_people,
    '-'*70, sep='\n')

# Combining key and reverse
#colors.sort(key=len, reverse=True)
#print(colors)
new_colors = sorted(colors, key=len, reverse=True)
print('Ordered by reverse length of key',new_colors,
    '-'*70, sep='\n')