import sqlite3
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

create = '''CREATE TABLE states (
'state' text,
'pop2014' integer,
'pop2000' integer
)'''

cursor.execute(create)

insert = 'INSERT INTO states VALUES (?,?,?)'

data = []
with open('states.txt') as f:
    for line in f.readlines():
        state_data = line.split('\t')
        tpl_state_data = ( state_data[0],
                          int(state_data[1].replace(',','')),
                          int(state_data[2].replace(',','')) )
                          
        data.append(tpl_state_data)
        
cursor.executemany(insert, data)
        
select = '''SELECT state,
CAST( (pop2014*1.0/pop2000) * pop2014 AS INTEGER) pop2028
FROM states ORDER BY pop2028 DESC'''
cursor.execute(select)

results = cursor.fetchall()
cursor.close()
connection.close()

for record in results:
    print('''The projected population of {} in 2028 is {:,}.'''
        .format(record[0], record[1]))