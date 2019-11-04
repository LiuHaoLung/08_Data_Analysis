import numpy as np
import pandas as pd
from numpy.random import randn

# 設定 index。
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
# 將不同的資料 zip 再一起，並回傳 tuples。
hier_index = list(zip(outside,inside))
# MultiIndex 可以讓 DataFrame 有兩個 index。
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

# 首先，用 loc['G1'] 則會回傳在這個 G1 index 裡的資料。
print(df.loc['G1'])
# 再者，如果在第一個 loc 後，再加上一個 loc ，則可以取得相對應的資料。
# 也就是說，先取得 G1 裡面的資料，再來就是取得 index 1 的資料。
# 故就是先取得最外圍的 index，再取得裡面的 index。
print(df.loc['G1'].loc[1])

# 用 index.names 可以得知在這兩個 index 是不是有名字。
# 如果在 index.names 後面放上 = ，則可以幫 index 設定名字，在 [] 裡，第一個名字為 G1 的名字，第二個名字為 1,2,3 的名字。
df.index.names = ['Groups','Num']
print(df)

# 先取得最外圍的 index，在取得內部的 index，最後選取欄。
print(df.loc['G2'].loc[2].loc['B'])
# 再選取欄的地方，無論有沒有加上 .loc 都可以選取到這個值。
print(df.loc['G2'].loc[2]['B'])

# 用 xs 的方式，可以橫跨 index ，並取得資料。
# df.xs(1,level = 'Num')，代表取得欄位名稱為 Num，且 index 為 1 的資料。
print(df.xs(1,level = 'Num'))