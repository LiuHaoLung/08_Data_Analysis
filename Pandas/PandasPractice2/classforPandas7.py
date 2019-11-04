import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

# Concatenating
# 基本上，只是將不同的 DataFrame 黏（glues）在一起。

# 要用 concatenation，呼叫在 pd 裡的 concat 方法，並用 list ，把將要黏再一起的 DataFrame 回傳為參數。
# 基本上，是從列的角度，將不同的 DataFrame 黏在一起。
print(pd.concat([df1,df2,df3]))

# 是從欄的角度，將不同的 DataFrame 黏在一起。
# 如果該 DataFrame 裡面，沒有相對應的資料，則會出現 NaN。
print(pd.concat([df1,df2,df3],axis = 1))

# Merging
# 根據既有的邏輯，將不同的 DataFrame 合併再一起。
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    

# 將要 merge 的 DataFrame 放在最前面，和 concat 不同，不需要將 DataFrame 變成 list。
# inner 代表的是內部連接。
# 相同的 key ，就會將資料連接再一起。
print(pd.merge(left,right,how = 'inner',on = 'key'))

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# 當 key1 和 key2 都相同時，資料才會被連接再一起。
# 在 left index = 0 的時候， key1 = key2 = K0，在 right index = 0 的時候，key1 = key2 = K0，所以資料會被連接再一起。
# 在 left index = 2 的時候， key1 = K1， key2 = K0，在 right index = 1 的時候，key1 = K1， key2 = K0，所以資料會被連接再一起。
# 在 left index = 2 的時候， key1 = K1， key2 = K0，在 right index = 2 的時候，key1 = K1， key2 = K0，所以資料會被連接再一起。
# 同等意思，也就是說，當 left 和 right 的資料裡面，有交集的話，才會顯示出來。
print(pd.merge(left,right,on = ['key1','key2']))

# 用 outer 的話，代表說，是兩個資料表進行聯集，如果一個資料表有，另外一個沒有則顯示 NaN。
print(pd.merge(left,right,how = 'outer', on = ['key1','key2']))

# 以 right 的 DataFrame 的資料表為準，如果 left 有的話，則顯示出來，如果沒有的話，則出現 NaN。
print(pd.merge(left,right,how = 'right', on = ['key1','key2']))

# Joining
# 將不同 index 的 DataFrame 進行合併，並產生一個結果出來。
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 


right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

# 以 left 這個 DataFrame 為基準，合併 right 這個 DataFrame，如果 right 沒有這個資料的話，則顯示 NaN。
print(left.join(right))

# 一樣是以 left 這個 DataFrame 為基準，但方法為 outer join，也就代表說，是進行兩個 DataFrame 的聯集。
print(left.join(right,how = 'outer'))












