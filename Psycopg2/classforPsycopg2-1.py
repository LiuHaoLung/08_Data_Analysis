import psycopg2

try:
    connection = psycopg2.connect(database = 'staff',user = 'louis',password = 'louis830630',host = '127.0.0.1',port = '5432')

except psycopg2.Error as err:
    print('An error was generated!')

else:
    print('Connect to database was successful!')