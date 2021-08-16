import sqlite3
import csv
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

create = '''CREATE TABLE states (
'state' text,
'pop2014' integer,
'pop2000' integer
)'''

cursor.execute(create)
insert = 'INSERT INTO states (state, pop2014,pop2000) VALUES (?,?,?)'

with open('states.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        cursor.execute(insert, [row[0].strip(), int(row[1].strip().replace(',','')), int(row[2].strip().replace(',',''))])


        
select = '''SELECT state,CAST( (pop2014*1.0/pop2000) * pop2014 AS INTEGER) pop2028 FROM states ORDER BY pop2028 DESC'''

cursor.execute(select)
results = cursor.fetchall()
for row in results:
    print("The projected 2040 population of "+row[0]+" is "+str(row[1])+".")
cursor.close()
connection.close()
