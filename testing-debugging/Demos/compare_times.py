import time

t1 = time.perf_counter()
t2 = time.perf_counter()
print("Time difference between t1 and t2")
print(t1, t2, t2-t1)
print('-'*70)

# Compare how fast two pieces of code run:

import random

start_time = time.perf_counter()
numbers = str(random.randint(1,100))
for i in range(1000):
    num = random.randint(1,100)
    numbers += ',' + str(num)
end_time = time.perf_counter()
td1 = end_time - start_time

start_time = time.perf_counter()
numbers = [str(random.randint(1,100)) for i in range(1,1000)]
numbers = ', '.join(numbers)
end_time = time.perf_counter()
td2 = end_time - start_time

print('''Time Delta 1: {}
Time Delta 2: {}'''.format(td1, td2))
print('-'*70)

# Run each snippet through a loop 1000
# to get a better idea of time difference

start_time = time.perf_counter()
for j in range(1000):
    numbers = str(random.randint(1,100))
    for i in range(1000):
        num = random.randint(1,100)
        numbers += ',' + str(num)
end_time = time.perf_counter()
td1 = end_time - start_time

start_time = time.perf_counter()
for j in range(1000):
    numbers = [str(random.randint(1,100)) for i in range(1,1000)]
    numbers = ', '.join(numbers)
end_time = time.perf_counter()
td2 = end_time - start_time

print('''Time Delta 1: {}
Time Delta 2: {}'''.format(td1, td2))
print('-'*70)

# Use timeit() to avoid manual calculation:

import random
from timeit import timeit

def string_nums1():
    numbers = str(random.randint(1,100))
    for i in range(1000):
        num = random.randint(1,100)
        numbers += ', ' + str(num)
    
def string_nums2():
    numbers = [str(random.randint(1,100)) for i in range(1,1000)]
    numbers = ', '.join(numbers)

td1 = timeit(string_nums1, number=1000)
td2 = timeit(string_nums2, number=1000)

print("Results from using timeit()")
print(td1, td2)
print('-'*70)

# Use timeit() with setup using code stored in strings

from timeit import timeit

str_nums1 = """
numbers = str(random.randint(1,100))
for i in range(1000):
    num = random.randint(1,100)
    numbers += ', ' + str(num)"""
    
str_nums2 = """
numbers = [str(random.randint(1,100)) for i in range(1,1000)]
numbers = ', '.join(numbers)"""

td1 = timeit(str_nums1, number=1000, setup='import random')
td2 = timeit(str_nums2, number=1000, setup='import random')

print("Results from using timeit() and setup with code stored in strings")
print(td1, td2)
print('-'*70)

# Use timeit() with globals() using code stored in strings:

import random
from timeit import timeit

str_nums1 = """
numbers = str(random.randint(1,100))
for i in range(1000):
    num = random.randint(1,100)
    numbers += ', ' + str(num)"""
    
str_nums2 = """
numbers = [str(random.randint(1,100)) for i in range(1,1000)]
numbers = ', '.join(numbers)"""

td1 = timeit(str_nums1, number=1000, globals=globals())
td2 = timeit(str_nums2, number=1000, globals=globals())

print("Results from using timeit() and globals() with code stored in strings")
print(td1, td2)
print('-'*70)

# Use repeat() instead of timeit():

from timeit import repeat

string_nums1 = """
numbers = str(random.randint(1,100))
for i in range(1000):
    num = random.randint(1,100)
    numbers += ', ' + str(num)"""
    
string_nums2 = """
numbers = [str(random.randint(1,100)) for i in range(1,1000)]
numbers = ', '.join(numbers)"""

tds1 = repeat(string_nums1, number=1000, repeat=4, setup='import random')
tds2 = repeat(string_nums2, number=1000, repeat=4, setup='import random')

print("Results from using repeat()")
print(tds1, tds2)
print('-'*70)