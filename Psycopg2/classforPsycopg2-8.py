import psycopg2

try:
    connection = psycopg2.connect(database = 'staff',user = 'louis',password = 'louis830630',host = '127.0.0.1',port = '5432')

except psycopg2.Error as err:
    print('An error was generated!')

else:
    print('Connect to database was successful!')

cursor = connection.cursor()
cursor.execute("select * from mystaff.employees where salary between 40000 and 55000;")
records = cursor.fetchone()
for i in records:
    print(i)

cursor.execute("select * from mystaff.employees where salary between 40000 and 55000;")
records = cursor.fetchmany(size = 2)
for i in records:
    print(i)