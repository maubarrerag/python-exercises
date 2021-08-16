# You may need to install via pip install mysql-connector-python
import mysql.connector

connection = mysql.connector.connect(
            host='MySQLC11.newtekwebhosting.com',
            user='student',
            password='webuc8',
            database='baseball')

query = '''SELECT nameFirst, nameLast, weight, year(debut)
FROM Master
ORDER BY weight DESC
LIMIT 5'''

cursor = connection.cursor() # pass dictionary=True to return 
                             # records as dicts
cursor.execute(query)
results = cursor.fetchall()
cursor.close()
connection.close()

print(results)