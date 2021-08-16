# Simple sort() method:
colors = ['red', 'blue', 'green', 'orange']
colors.sort()
print('Colors sorted', colors, '-'*70, sep='\n')

# The reverse argument:
colors.sort(reverse=True)
print('Colors sorted in reverse order', colors, '-'*70, sep='\n')

# The key argument:
colors.sort(key=len)
print('Colors sorted by length', colors, '-'*70, sep='\n')

# The key argument with named function:
def get_lastname(name):
    return name.split()[-1]

people = ['George Washington', 'John Adams', 'Thomas Jefferson', 
	'John Quincy Adams']
people.sort(key=get_lastname)
print('People sorted by last name using named function', 
	people, '-'*70, sep='\n')

# The key argument with lambda function
people = ['George Washington', 'John Adams', 'Thomas Jefferson', 
	'John Quincy Adams']
people.sort(key=lambda name: name.split()[-1])
print('People sorted by last name using lambda function', 
	people, '-'*70, sep='\n')

# Combining key and reverse
colors.sort(key=len, reverse=True)
print('Colors sorted by length and reversed', 
	colors, '-'*70, sep='\n')