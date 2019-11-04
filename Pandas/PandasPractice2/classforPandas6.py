import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

df.groupby('Company')
byComp = df.groupby('Company')
print(byComp)

# 使用 groupby 的方法後，只會顯示物件。
# 在呼叫要合併的方法，像是 mean，就會出現資料。
# 沒有辦法合併 person 這欄，因為都是字串，是沒有辦法被合併的。
# 並會將 DataFrame 的 index 設為 company。
print(byComp.mean())
print(byComp.std())
print(byComp.sum())

# 先將相同的 company 的資料總合合併之後。
# 在呼叫 FB 這個欄位的資料。
print(byComp.sum().loc['FB'])

# 通常來說，是不會將 groupby 指定給變數，而是將不同步驟，合併為一條。
print(df.groupby('Company').sum().loc['FB'])

# 將 company 設定為 index。
# 並會計算在相同 company 中，不同欄位共有幾筆資料。
print(df.groupby('Company').count())

# max 方法，可以呼叫欄位中，最大的值，像是 Person 就會呼叫字母最大的人，Sales 就會呼叫數字最大的值。
# 但 Person 跟 Sales 的數值，並不會相對應起來。
# min 也是相同。
print(df.groupby('Company').max())
print(df.groupby('Company').min())

# 描述性統計。
print(df.groupby('Company').describe())

# 可以利用 transpose 的方法，來進行表格的變化。
print(df.groupby('Company').describe().transpose())

# 可以抓出個別公司的資料。
print(df.groupby('Company').describe().transpose()['FB'])