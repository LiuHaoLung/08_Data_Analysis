import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})

# 要顯示幾筆資料
df.head()

# unique 可以找到獨一無二的值。
print(df['col2'].unique())

# 可以不用回傳出 array。
# 可以用 len 的 func 來看獨一無二值有幾個。
# 可以用 pandas 內建的 func nunique 來看獨一無二值有幾個。
print(len(df['col2'].unique()))
print(df['col2'].nunique())

# 可以計算出在這欄位裡頭，每一個值出現過幾次。
print(df['col2'].value_counts())

def times2(x):
    return x * 2

# 可以自訂一個 func ，並利用 pandas 內建的 apply func ，來執行自訂的 func。
print(df['col1'].apply(times2))

# 除了可以利用 apply 來執行自訂的 func 外，也可以執行 python 自訂的 func。
print(df['col3'].apply(len))

# 利用 lambda ，就可以不用自訂 func。
print(df['col2'].apply(lambda x : x * 2))

# 可以查看目前的 DataFrame 欄位是什麼。
print(df.columns)

# 可以查看目前的 DataFrame index 是什麼。
print(df.index)

# 用 sort_values 可以將指定的欄位值進行排序。
print(df.sort_values('col2'))

# 可以找到在這個 DataFrame 裡面的值，是不是有 NaN ，並回傳 bool。
print(df.isnull())

data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

# 樞紐分析表。
print(df.pivot_table(values = 'D', index = ['A','B'], columns = ['C']))

