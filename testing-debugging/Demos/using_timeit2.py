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

td1 = timeit(str_nums1, number=1000, setup='import random')
td2 = timeit(str_nums2, number=1000, setup='import random')

print(td1, td2)