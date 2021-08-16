from timeit import repeat

str_nums1 = """
numbers = str(random.randint(1,100))
for i in range(1000):
    num = random.randint(1,100)
    numbers += ', ' + str(num)"""
    
str_nums2 = """
numbers = [str(random.randint(1,100)) for i in range(1,1000)]
numbers = ', '.join(numbers)"""

tds1 = repeat(str_nums1, number=1000, repeat=4, setup='import random')
tds2 = repeat(str_nums2, number=1000, repeat=4, setup='import random')

print("Results from using repeat()")
print(tds1, tds2, sep="\n")
print('-' * 70)

print('str_nums2 compared to str_nums1:')
print('{:.2%}'.format( sum(tds2) / sum(tds1)) )
print('-' * 70)

print('str_nums1 compared to str_nums2:')
print('{:.2%}'.format( sum(tds1) / sum(tds2)) )