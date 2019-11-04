import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

# 在 DataFrame 中：
# 第一個參數為：資料。
# 第二個參數為：行索引。
# 第三個參數為：列索引。
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
# 直接用 .x 也可以找到相對應的欄，x 要替換成欄位的名稱。
print(df['W'])
print(df.W)
# 如果是要回傳多個欄，則需要在原本的 list 裡面，再加上一個 list。
print(df[['W','Z']])

# 如果要建立新的欄位時，先建造出新欄位的名稱，再將值放在右邊。
df['new'] = df['W'] + df['Y']
print(df)

print(df.drop('new',axis = 1))
# 就算用了 drop 的方法，表面看起來是有實際的將 new 這一欄刪除，但實質上並不會影響到最原本的 DataFrame。
print(df)

# 在 pandas 的預設上，不會希望意外地遺失或刪除資料，所以如果真的要刪除資料，則需要加上 inplace 這步驟，才會真正被刪除。
df.drop('new',axis = 1,inplace = True)
print(df)

# 因為在 drop 預設的地方，axis = 0 就代表是行，所以不需要在參數的地方，再打上 axis 這部分。
print(df.drop('E'))

# loc 代表的是 location，可以用 loc 的方式，直接找到列，除此之外，也可以發現，列也是 series 的一種。
print(df.loc['A'])

# iloc 是要回傳要找的列的 index。無論是用 loc 或 iloc 都可以找到想要找的列。
print(df.iloc[2])

# 找到相對應的值，就是在 B 這列且在 Y 這欄的值。
print(df.loc['B','Y'])

# 如果是要抓在這個 DataFrame 的子集資料的話，則會用到在最外圍的 [] 裡面再加上兩個 [[列],[欄]]。
print(df.loc[['A','B'],['W','Y']])