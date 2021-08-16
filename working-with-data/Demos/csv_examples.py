# Reading with reader()
import csv

print('Using reader(): ')
with open('../csvs/us-population-2010-2014.csv', newline='') as csvfile:
    pops = csv.reader(csvfile)        
    for i, row in enumerate(pops, 1):
        print(', '.join(row))
        if i >= 5:
            break
print('-'*70)

# Reading with DictReader()

sexes = {'A':'Both', 'M':'Male', 'F':'Female'}
print('Using DictReader(): ')
with open('../csvs/us-population-2010-2014.csv', newline='') as csvfile:
    pops = csv.DictReader(csvfile)
    
    header = ','.join(pops.fieldnames)
    print(header)

    print('-' * len(header))
        
    for row in pops:
        sex = sexes[row['SEX']]
        print(sex,
              row['AGE'],
              row['POPESTIMATE2010'],
              row['POPESTIMATE2011'],
              row['POPESTIMATE2012'],
              row['POPESTIMATE2013'],
              row['POPESTIMATE2014'])   
print('-'*70)   

# Finding data in a CSV file

print('Finding data in a CSV file: ')
with open('../csvs/us-population-2010-2014.csv', newline='') as csvfile:
    pops = csv.DictReader(csvfile)
    
    for row in pops:
        if (row['AGE'] == '30' and row['SEX'] == 'F'):
            population = row['POPESTIMATE2011']
            break
    else:
        population = None

print(population)
print('-'*70)  

# Call find_pop() multiple times

def find_pop(pops, age, sex, year):
    for row in pops:
        if (row['AGE'] == str(age) and row['SEX'] == sex):
            return row['POPESTIMATE' + str(year)]
    return None
print('Call find_pop() multiple times: ')
with open('../csvs/us-population-2010-2014.csv', newline='') as csvfile:
    pops = csv.DictReader(csvfile)
    pop1 = find_pop(pops, 30, 'F', 2011)
    pop2 = find_pop(pops, 30, 'F', 2011)

print(pop1, pop2)
print('-'*70)  

# Call find_pop() multiple times using csvfile.seek(0) 

print('''Call find_pop() multiple times with repositioning 
    of cursor using seek(0): ''')
with open('../csvs/us-population-2010-2014.csv', newline='') as csvfile:
    pops = csv.DictReader(csvfile)
    pop1 = find_pop(pops, 30, 'F', 2011)
    csvfile.seek(0)
    pop2 = find_pop(pops, 30, 'F', 2011)

print(pop1, pop2)
print('-'*70) 

# Create a list from csv.DictReader()

print('''Call find_pop() multiple times using a list 
    from csv.DictReader: ''')

with open('../csvs/us-population-2010-2014.csv', newline='') as csvfile:
    pops = list(csv.DictReader(csvfile))

pop1 = find_pop(pops, 30, 'F', 2011)
pop2 = find_pop(pops, 30, 'F', 2011)

print(pop1, pop2) 
print('-'*70)  

# Writing with writer()

import pymysql, csv
connection = pymysql.connect(host='MySQLC11.newtekwebhosting.com',
                             user='student',
                             password='webuc8',
                             database='baseball'
                            )
query = '''SELECT year(debut) year, avg(weight) weight
FROM Master
WHERE debut is NOT NULL
GROUP BY year(debut)
ORDER BY year(debut)'''
    
with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    
connection.close()

print('Writing with writer(): ')

with open('../csvs/mlb-weight-over-time.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Year', 'Weight'])
    writer.writerows(results)   

print('-'*70)