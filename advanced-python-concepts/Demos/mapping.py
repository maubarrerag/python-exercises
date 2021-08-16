# Here's the lambda function we will demonstrate:
f = lambda n: n**2

# Before we use that lambda function,  let's see how map() works 
# with a named function:
def square(n):
    return n**2

squares = list(map(square, range(10)))
print('Squares with a named function:', squares,'-'*70,sep='\n')

# Now we use map() with a lambda function to do the same thing:
squares = list(map(lambda n: n**2, range(10)))
print('Squares with a lambda function:', squares,'-'*70,sep='\n')

# And here's how we can accomplish the same thing 
# using list comprehension:
squares = [n**2 for n in range(10)]
print('Squares using list comprehension:', squares,'-'*70,sep='\n')