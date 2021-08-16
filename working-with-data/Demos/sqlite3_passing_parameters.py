import sqlite3
connection = sqlite3.connect('../lahman2014.sqlite')

query = '''SELECT yearID, HR
FROM batting
WHERE playerID IN (SELECT playerID
                    FROM master
                    WHERE nameFirst = ? AND nameLast = ?)
ORDER BY yearID'''

cursor = connection.cursor()
player = ( 'Babe', 'Ruth' )
cursor.execute(query, player)
results = cursor.fetchall()
cursor.close()
connection.close()

print(results)