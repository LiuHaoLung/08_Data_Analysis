import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

print(df > 0)

booldf = df > 0
print(booldf)
# 可以將這個判斷放入 DataFrame 的參數中，則回傳出來的表，如若是滿足這個判斷式的，則會直接給出值，如若是不滿足這個判斷式的，則會給出 NaN。
print(df[booldf])

# 可以將以上步驟合併為相同步驟，直接在 DataFrame 的參數裡，放上 df > 0 ，就可以達成。
print(df[df > 0])

# 可以選出特定欄位，並進行比較，也可以得到以上答案。
print(df['W'] > 0)

# 利用這個方式，只會回傳在 W 這個欄位為 True 的值，也就是說第 C 列這一列，並不會被回傳。
print(df[df['W'] > 0])
print(df[df['Z'] < 0])

result = df[df['W'] > 0]
print(result)
print(result['X'])
# 可以將以上步驟合併為相同步驟，先挑選 W 這個欄位 > 0 的，回傳正個 DataFrame，在從這個結果選出 X 這個欄位。
print(df[df['W'] > 0]['X'])

# 除了找到一個欄位，也可以找多個欄位。
print(df[df['W'] > 0][['Y','X']])


# 所以在 pandas 裡面，要用 and 只能用 % 這個符號。
# 如果要用 or，則需要用 | 這個符號。
# 如果要用 not ，則需要用 ~ 這個符號。
print(df[(df['W'] > 0) & (df['Y'] > 1)]) 

# 如果用了 reset_index 這個方法，則原本的 index 就會變成 DataFrame 裡的一欄，index 則變成是數字 0-4。
print(df.reset_index())

newind = 'CA NY WY OR CO'.split()
df['States'] = newind
#set_index 和 reset_index 不同的地方在於：
#用 set_index 的方式，會取代原本 index 的欄位，然後把這欄變成 index。
#但用 reset_index 的方式，則不會取代原本 index 的欄位，且原本 index 的欄位，會變成 DataFrame 的其中一欄。
print(df.set_index('States'))
print(df.reset_index())
# 但無論是 set_index 和 reset_index，都不會影響到原本的 DataFrame ，因為在 inplace 的地方，都沒有設為 True。
print(df)