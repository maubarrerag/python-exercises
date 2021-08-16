# Strings are immutable, so when variable, v1, holds a string and 
# is assigned to another variable, v2, v2 is really just getting the string v1 holds, not the variable itself
v1 = 'A'
v2 = v1
print(v1, v2)
v1 += 'B'
print(v1, v2)
print ('-'*70)

# Another way to look at it. Notice that vs[0] remains 'A' even after v1 has 'C' appended to it:
v1 = 'A'
vs = [v1, 'B']
v1 += 'C'
print(vs)
print ('-'*70)

# But lists, which are mutable, can be modified in place:
v1 = [1, 2]
v2 = v1
print(v1, v2)
v1 += [3]
print(v1, v2)

v1 = [1, 2]
v2 = v1
vs = [v1, v2]
v1.append(3) 
v1 += [4]
print(vs)
print ('-'*70)

# Careful though. If you use the assignment operator, you will overwrite the old list and create a new list object:
v1 = [1, 2]
v2 = v1
print(v1, v2)
v1 = v1 + [3]
print(v1, v2)
print ('-'*70)