import pandas as pd

# 1. 讀取檔案。
ecom = pd.read_csv('Ecommerce Purchases')

# 2. 檢查 DataFrame。
print(ecom.head())

# 3. 檢查有多少項目及目前欄位名稱為何。
print(ecom.info())
print(ecom.columns)

# 4. 計算在 Purchase Price 的平均值。
print(ecom['Purchase Price'].mean())

# 5. 找到在 Purchase Price 的最大值及最小值。
print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())

# 6. 有多少人的語言選擇的是 en。
print(ecom[ecom['Language'] == 'en'].count())

# 7. 有多少人的職位是 Lawyer。
print(ecom[ecom['Job'] == 'Lawyer'].info())
print(ecom[ecom['Job'] == 'Lawyer'].count())

# 8. 有多少人購買時間是在 AM 及 PM。
print(ecom['AM or PM'].value_counts())

# 9. 前五名最多的職位是什麼。
print(ecom['Job'].value_counts().head(5))

# 10. 有人從 ''90 WT'' 進行了購買，此交易的購買價是多少？。
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

# 11. 擁有這個信用卡卡號 ''4926535242672853'' 的人，email 是多少。
print(ecom[ecom['Credit Card'] == 4926535242672853 ]['Email'])

# 12. 有多少人的信用卡公司為 ''American Express'' 且購買金額在 95 之上。
print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())

# 13. 有多少人的信用卡到期年為 2015。
print(sum(ecom['CC Exp Date'].apply(lambda x : x[3:])== '25'))

# 14. 前五名最多的郵件是什麼。
print(ecom['Email'].apply(lambda x : x.split('@')[1]).value_counts().head(5))