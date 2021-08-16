import pymysql
connection = pymysql.connect(host='MySQLC11.newtekwebhosting.com',
                             user='student',
                             password='webuc8',
                             database='baseball'
                            )
                        
query = '''SELECT nameFirst, nameLast, weight, year(debut)
FROM Master
ORDER BY weight DESC
LIMIT 5'''
    
with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
connection.close()

print(results)