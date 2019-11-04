'''
判斷陣列維度的方法：
1. 如果在回傳 array() 裡面，只有一對 [] 則代表是一維陣列。
2. 如果再回傳 array() 裡面，有兩對 [[]] 則代表是二維陣列。


arange 和 linspace 的差別在：
1. arange() 裡的參數為，起始值、終值和增值。
2. linspace() 裡的參數為，起始值、終值和出現多少個數。
'''

import numpy as np

# 將最原始的 list 轉變成 NumPy 中的 array。
my_list = [1,2,3]
print(np.array(my_list))

# 將原始的多個 list 轉變成 NumPy 中的 二維陣列。
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat))

# np.arange() 是直接將數值轉變成陣列。
# 在 () 內，第一個數字是起始值為 0 ，第二個數字是終值為 10，但跟 python 的 range 相同，都不包含終值。
print(np.arange(0,10))

# 第三個數字為增值， step 的意思。
print(np.arange(0,11,2))

# 建立特殊陣列，其在陣列裡面的值皆為 0。
print(np.zeros(3))
# 如果在原本的 () 裡面再加上 ()，則代表會變成二維陣列。
print(np.zeros((5,5)))
# 第一個數字代表的是行的數量為 2，第二個數字代表的是列的數量為 3。
print(np.zeros((2,3)))

print(np.ones(4))
print(np.ones((3,4)))

# linspace：可以建立等差數列，從 0 開始到 5，出現 10 個數字。因為預設 endpoint 為 True ，所以一定會出現終值，如果 endpoint 設定為 False，則不會出現終值。
print(np.linspace(0,5,10))
print(np.linspace(1,5,10))

# eye：建立對角矩陣，在 () 內的數字，代表會出現幾行幾列，且行跟列的數量皆會相同，同時在對角線的部分，皆為1。
print(np.eye(5))
print(np.eye(4))
print(np.eye(3))
print(np.eye(2))
print(np.eye(1))

# random.rand：建立亂數矩陣，如果在 () 內的數字只有一個，代表是一維陣列，在陣列裡就會出現幾個數，出現數字的值都會在 0-1 之間。
print(np.random.rand(5))
# 如果在 () 內的數字只有兩個，代表是二維陣列，在陣列裡會出現幾行幾列，出現數字的值都會在 0-1 之間。
print(np.random.rand(5,5))

# 建立常態分配的陣列，在 () 內的數字為一個，代表是一維陣列，在陣列裡就會出現多少個數字。
print(np.random.randn(2))
# 建立常態分配的陣列，在 () 內的數字為兩個，代表是二維陣列，在陣列裡會出現幾行幾列。
print(np.random.randn(4,4))

# random.randint：在 () 內，第一個數字為最小值，第二個數字為最大值，且隨機選取一個數字。
print(np.random.randint(1,100))
# 在 () 內，第一個數字為最小值，第二個數字為最大值，第三個數字為要選幾個，其中最小值是被包含在裡面的（inclusive），最大值是不被包含在裡面的（exclusive）。
print(np.random.randint(1,100,10))

arr = np.arange(25)
print(arr)

ranarr = np.random.randint(0,50,10)
print(ranarr)

# 重新改變陣列的形狀，原本是一維陣列，但用 reshape 可以將陣列改為二維陣列。
# 但在轉換形狀的過程中，陣列要能被滿足，也就是說在 arr 是只有 25 個數字，所以只能滿足 5x5 的二維陣列，但不能滿足 5x10 的二維陣列，所以就會出現錯誤。
print(arr.reshape(5,5))

arr1 = np.arange(24)
print(arr1)
# 在 arr1 裡面，只有 24 個數字，要將 arr1 的形狀轉變為 5x5 的二維陣列是可以的，但會自動填滿缺少的部分，所以會發現在二維陣列中，多出一個數字 24。
print(arr.reshape(5,5))

# 在建立出來的亂數陣列中，如果要找到最大值，可以用 max() 方法，如果要找到最小值，可以用 min() 方法。
print(ranarr.max())
print(ranarr.min())

#在建立出來的亂數陣列中，如果要找到最大值所在的 index，可以用 argmax() 方法，如果要找到最小值所在的 index，可以用 argmin() 方法。
print(ranarr.argmax())
print(ranarr.argmin())

# shape：可以得知目前這個陣列的形狀為何，arr 回傳的為 (25,)，因為是一維陣列，所以不會有第二個參數。
print(arr.shape)

# 因為已經將 reshape 後的結果，丟給變數 arr，所以在呼叫一次 arr.shape 就會是二維陣列的狀態。
arr = arr.reshape(5,5)
print(arr.shape)

# 可以了解陣列的資料型態是什麼。
print(arr.dtype)






















