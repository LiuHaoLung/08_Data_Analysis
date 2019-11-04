import numpy as np
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('example')
print(df)

# 用 to_csv 的方法，可以將檔案輸出為 CSV，且 index = False ，代表在存檔時，不會將原本 index 這欄存入檔案中。
df.to_csv('My_output',index = False)

# 如果在一個 excel 裡面，有很多個 sheet，則可以用 sheet_name 來決定要輸出的 sheet。
print(pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1'))

# 在存檔時，也可以自己更改 sheet 的名稱。
df.to_excel('Excel_Sample2.xlsx',sheet_name = 'NewSheet')

data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(data[0])

# 建立一個短暫存在在記憶體中的 SQL。
engine = create_engine('sqlite:///:memory:')

# 將原本的 df 寫入在這個 engine 的 SQL中，並將資料表名稱設定為 my_table。
df.to_sql('my_table',engine)

sqldf = pd.read_sql('my_table',con = engine)
print(sqldf)