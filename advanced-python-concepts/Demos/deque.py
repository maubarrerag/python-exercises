from collections import deque

names=deque(['Stephen','Nat'])
print('The deque items:')
for name in names:
    print(name)

names.append('Roger') 
print('The deque items with new name appended to the right end:')
for name in names:
    print(name) 
print('-'*70) 

names.popleft()
print('The deque items with name on left end removed:')
for name in names:
    print(name) 
print('-'*70)

names.appendleft('Donna')  
print('The deque items with new name appended to the left end:')
for name in names:
    print(name) 
print('-'*70) 

names.insert(1, 'Connie')
print('The deque items with name inserted at position 1:')
for name in names:
    print(name)

names.pop()
print('The deque items with name removed from the right end:')
for name in names:
    print(name)  

names.clear()
print('The deque cleared, item count is: ' + str(len(names)))
print('-'*70)