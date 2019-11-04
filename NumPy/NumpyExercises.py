import numpy as np

#1. 建立有10個0的陣列。
print(np.zeros(10))

#2. 建立有10個1的陣列。
print(np.ones(10))

#3. 建立有10個5的陣列。
print(np.ones(10) * 5)

#4. 建立一個陣列裡面包含10到50。
print(np.arange(10,51))

#5. 建立一個陣列範圍從10到50，但只包含偶數。
print(np.arange(10,51,2))

#6. 建立一個3x3的二維陣列，裡頭包含0到8。
print(np.arange(0,9).reshape(3,3))

#7. 建立一個3x3的對角二維陣列。
print(np.eye(3))

#8. 從0到1中，隨機挑選一個值。
print(np.random.rand(1))

#9. 建立一個二維常態分配陣列，裡頭包含25個值。
print(np.random.randn(25))

#10. 建立一個二維陣列，包含的值從 0.01到1。
print(np.arange(1,101).reshape(10,10) / 100)

#11. 建立一個線性陣列，裡頭的值從0到1，且有25個。
print(np.linspace(0,1,25))

#12. 從以下的陣列找到相對應的值：
mat = np.arange(1,26).reshape(5,5)
print(mat)

#13. 找到一個陣列裡頭的值包含12到25。
print(mat[2:,1:])

#14. 找到在陣列裡的20。
print(mat[3,4])

#15. 找到一個陣列裡頭的值包含2,7,12。
print(mat[:3,1:2])

#16. 找到一個陣列裡頭的值包含21到25。
print(mat[4,:])

#17. 找到一個陣列裡頭的值包含16到25。
print(mat[3:,:])

#18. 將陣列裡面的值全部相加。
print(mat.sum())

#19. 計算這個陣列的標準差。
print(mat.std())

#20. 找到這個陣列每一欄的總和。
print(mat.sum(axis = 0))
