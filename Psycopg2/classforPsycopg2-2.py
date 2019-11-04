import psycopg2

try:
    connection = psycopg2.connect(database = 'staff',user = 'louis',password = 'louis830630',host = '127.0.0.1',port = '5432')

except psycopg2.Error as err:
    print('An error was generated!')

else:
    print('Connect to database was successful!')

cursor = connection.cursor()
cursor.execute('''create table mystaff.employees
(id int primary key not null,
first_name varchar(25) not null,
last_name varchar(25) not null,
department varchar(25) not null,
phone varchar(25),
address varchar(25),
salary int);''')

connection.commit()
connection.close()