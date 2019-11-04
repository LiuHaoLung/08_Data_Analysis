import numpy as np

arr = np.arange(0,11)

# 用原本數學的符號 + 就可以將兩個陣列裡的值做相加。
print(arr+arr)

# 用原本數學的符號 * 就可以將兩個陣列裡的值做相加。
print(arr * arr)

# 在陣列直接加上一個數字，就可以將陣列裡的值，加上這個數字。
print(arr + 100)
print(arr * 100)
print(arr ** 2)

# 將陣列取平方根。
print(np.sqrt(arr))

# 將陣列取指數值。
print(np.exp(arr))

# 無論何種方法都可以取出這個陣列裡面的最大值
print(np.max(arr))
print(arr.max())

# 將陣列取三角函數值。
print(np.sin(arr))

# 將陣列取對數值。
print(np.log(arr))

# 平常在 python 執行 1/0 會出現 ZeroDivisionError，但在 NumPy 裡面，會出現 RuntimeWarning，在不對那個值，會出現 nan ，其他的還是會有輸出。
print(arr / arr)
print(1 / arr)









