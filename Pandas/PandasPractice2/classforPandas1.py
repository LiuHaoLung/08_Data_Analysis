import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

# 有索引值 0,1,2（index），每一個索引值對應到不同的資料。
print(pd.Series(data = my_data))

# 可以自行指定索引值，只要在 () 裡面加上 index 的參數。
print(pd.Series(data = my_data,index = labels))

# 可以不用打上 data 跟 index，也會有相同的答案。
print(pd.Series(my_data,labels))

# numpy array 也可以成為 pandas 的 series。
print(pd.Series(arr))
print(pd.Series(arr,labels))

# 除了以上之外，也可以將 dict 變成 pandas 的 series 資料，但會自動將 dict 的關鍵字變成 index。
print(pd.Series(d))

# 在 pandas 的 series 中，可以存任何型態的資料，除了數值之外，也可以存字串。
print(pd.Series(data = labels))

# 也可以在 series 中放入內建的 func。
print(pd.Series(data = [sum,print,len]))

ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
print(ser1)
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)

# 可以直接利用在 series 中的 index 抓取資料，在 [] 裡面打上字串，因為這些 series 中的 index 是字串。
print(ser1['USA'])

ser3 = pd.Series(data = labels)
print(ser3[2])

# 可以將兩個 series 相加。
# 如果有同樣的 index 會直接將值相加，但如果是一個 series 有另外一個 series 沒有，則會出現 NaN，因為在這兩個 series 並沒有 match。
# 在 pandas 裡面如果將兩個 series 相加，則會將值變成 float，盡可能的保持所有的資料。
print(ser1 + ser2)