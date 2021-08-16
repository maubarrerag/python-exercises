# Here's the lambda function we will demonstrate:
f = lambda n: n**.5 == int(n**.5)

# Before we use that lambda functions,  let's see how filter() 
# works with a named function:
def is_perfect_square(n):
    return n**.5 == int(n**.5)

perfect_squares = list(filter(is_perfect_square, range(100)))
print('Using a named function:', perfect_squares,'-'*70,sep='\n')

# Now we use filter() with a lambda function to do the same thing:
perfect_squares = list(filter(lambda n: n**.5 == int(n**.5), 
	range(100)))
print('Using a lambda function:', perfect_squares,'-'*70,sep='\n')

# And here's how we can accomplish the same thing 
# using list comprehension:
perfect_squares = [n for n in range(100) if n**.5 == int(n**.5)]
print('Using list comprehension:', perfect_squares,'-'*70,sep='\n')