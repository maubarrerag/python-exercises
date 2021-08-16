import sqlite3
connection = sqlite3.connect('../lahman2016.sqlite')

query = '''SELECT nameFirst, nameLast, weight, 
strftime('%Y', debut / 1000, 'unixepoch')
FROM Master
ORDER BY weight DESC
LIMIT 5'''

cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()
cursor.close()
connection.close()

print (results)

# Challenge: Make output pretty

for record in results:
    print('''{} {} weighed {} pounds when he started 
        his MLB career in {}.'''
    .format(record[0],
        record[1],
        record[2],
        record[3]) )