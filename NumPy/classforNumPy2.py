import numpy as np

arr = np.arange(0,11)
print(arr)
print(arr[8])
print(arr[1:5])
# 和 python list 的 slicing 一樣，但不包含終值，也就是不包含 index 5。
print(arr[0:5])
# 從 index 0 開始選，選到 index 5，不包含 index 6。
print(arr[:6])
print(arr[0:6])
# 從 index 5 開始選到最後。
print(arr[5:])

arr[0:5] = 100
# 將選起來的值都變成 100。
print(arr)

arr = np.arange(0,11)
print(arr)
slice_of_arr = arr[0:6]
print(slice_of_arr)
# 代表抓取全部的值。
print(slice_of_arr[:])

# 如果將值取代了，不管是原本（arr）還是（slice_of_arr）都會變成新的值。在 NumPy 裡面，不是 copy array，而是取代掉，因為可以節省記憶體空間。
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)

# 和上面的不同，如果不想取代掉原本陣列裡的值，而是想要複製後再取代，則要用 copy() 方法來達成。
arr_copy = arr.copy()
print(arr)
print(arr_copy)
arr_copy[:] = 100
print(arr_copy)
print(arr)

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
# 如果是要抓取二維陣列裡的值，則需要輸入行列的 index，第一個 [] 是行，第二個 [] 是列。
print(arr_2d[0][0])
print(arr_2d[1][1])
# 不用兩個 [][]也可以，在單一個 [] 裡面輸入 x,x即可，第一個 x 代表行的 index，第二個 x 代表列的 index。
print(arr_2d[1,1])
# 第一個是行，所以是從頭抓取到 index 1，就會抓 5,10,15,20,25,30。
# 第二個是列，所以是從 index 1 抓取全部，最後就會抓到 10,15,25,30。
print(arr_2d[:2,1:])
print(arr_2d[1:,:])

arr = np.arange(1,11)
print(arr)
print(arr > 5)
bool_arr = arr > 5
# 將陣列裡的每個值和 5 比較，如果有 > 5 就會回傳 True，如果 < 5 就會回傳 False，也可以將結果陣列指定給其他變數。
print(bool_arr)
# 可以用這樣的方式，來做陣列的選取，用 arr[bool_arr] 就只會回傳是 True 的結果。
print(arr[bool_arr])
print(arr[arr > 5])
print(arr [arr < 3])







