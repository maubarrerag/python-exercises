# Test the Triangle class:

from Triangle import Triangle

good = [3,3,5]
bad = [3,3,9]
print( Triangle.is_triangle(good) )
print( Triangle.is_triangle(bad) )
t1 = Triangle(good)
print(t1.area)
t2 = Triangle(bad)