import sqlite3


connection = sqlite3.connect('../lahman2016.sqlite')

query = '''SELECT nameFirst, nameLast, weight, debut
FROM Master
ORDER BY weight DESC
LIMIT 20'''

connection.row_factory = sqlite3.Row
cursor = connection.cursor()
cursor.execute(query)

results = cursor.fetchall()

cursor.close()
connection.close()

for row in results:
    try:
        print(row[0]+" "+row[1]+' weighed '+str(row[2])+' when he debuted in '+[part for part in str(row[3]).split('-')][0])
    except:
        pass