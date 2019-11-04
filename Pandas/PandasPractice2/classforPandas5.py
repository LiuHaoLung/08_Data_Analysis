import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)

# 無論是在欄或列裡面，只要有丟失的資料，都會直接被丟掉
print(df.dropna())

# 如果有指定 axis = 1，也就代表說，只要欄位的地方，有丟失的資料，才會被丟掉
print(df.dropna(axis = 1))

# thresh 代表的是，可以指定在這個 dataframe 裡面，有幾個 non-NaN，所以如果當 thresh = 2 ，代表只要在列裡面，有兩個不是 non-NaN 就會被留下來。
print(df.dropna(thresh = 2))

# 用 fillna 可以將在 dataframe 裡面，全部 NaN 的資料填滿。
print(df.fillna(value = 'FILL VALUE'))

# 可以先選取一欄（df['A])
# 再用 fillna 來填滿 NaN 資料
# 最後指定值，也就是這個欄位的平均數，將NaN取代為平均數
print(df['A'].fillna(value = df['A'].mean()))