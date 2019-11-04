import pandas as pd

sal = pd.read_csv('Salaries.csv')

# 1. 讀取檔案。
print(sal.head())

# 2. 檢查 DataFrame。
print(sal.head())

# 3. 檢查有多少項目。
print(sal.info())

# 4. 計算在 BasePay 的平均值。
print(sal['BasePay'].mean())

# 5. 找到在 OvertimePay 的最大值。
print(sal['OvertimePay'].max())

# 6. 找到 EmployeeName 是 JOSEPH DRISCOLL。
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL'])

# 7. 找到 EmployeeName 是 JOSEPH DRISCOLL 且只顯示 JobTitle。
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

# 8. 找到 EmployeeName 是 JOSEPH DRISCOLL 且只顯示 TotalPayBenefits。
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

# 9. 找到 TotalPayBenefits 的最大值，並顯示出完整的 DataFrame。
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])
print(sal.loc[sal['TotalPayBenefits'].idxmax()])

# 10. 找到 TotalPayBenefits 的最大值，並只顯示出 EmployeeName。
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])

# 11. 找到TotalPayBenefits 的最大值，並顯示出完整的 DataFrame。
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()])
print(sal.loc[sal['TotalPayBenefits'].idxmin()])

# 12. 找到在 2011 - 2014 年中，所有員工 BasePay 的平均值。
print(sal.groupby('Year').mean()['BasePay'])

# 13. 有多少個獨一無二的職位。
print(sal['JobTitle'].nunique())
print(len(sal['JobTitle'].unique()))

# 14. 前五名最多的職位是什麼。
print(sal['JobTitle'].value_counts().head(5))

# 15. 在 2013 年中，有多少人的職位是只有出現一次。
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))

# 16. 找到有多少人的職位中，有 Chief 這個字。
def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

# 17. 職位的長度和薪水的相關性。
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['TotalPayBenefits','title_len']].corr())