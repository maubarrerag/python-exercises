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

print(td1, td2)