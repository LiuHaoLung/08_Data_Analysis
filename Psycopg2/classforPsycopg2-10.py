import psycopg2

# 打開要輸入到資料庫的文字檔
f = open('employees.txt')

# 建立一個空的 list，可以儲存這個文字檔的內容
records = []

# 一行一行讀取這個文字檔，並根據符號進行分行
for i in f.readlines():
    records.append(i.split('/ '))

# 開啟連結資料庫
try:
    connection = psycopg2.connect(database = 'staff',user = 'louis',password = 'louis830630',host = '127.0.0.1',port = '5432')

except psycopg2.Error as err:
    print('An error was generated!')

else:
    print('Connect to database was successful!')

# 建立 cursor
cursor = connection.cursor()

# 將分割後的文字檔內容，寫入在資料庫內
try:
    for i in records:
        cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) values (%s,%s,%s,%s,%s,%s,%s);",(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

except psycopg2.Error as err:
    print("An error was generated while inserting the records!")
    
else:
    print("Records inserted successfully!\n")

# 儲存以上的變動
connection.commit()
connection.close()