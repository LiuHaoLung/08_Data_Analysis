import pandas
from sqlalchemy import create_engine

# 利用 pandas module 輸入四個所需要的檔案，如：txt、csv、json、xlsx。

dtxt = pandas.read_csv('/Users/How.Short/Desktop/Python內容/Python-class/classforpandas/my-employees.txt')
dcsv = pandas.read_csv('/Users/How.Short/Desktop/Python內容/Python-class/classforpandas/my-employees.csv')
djson = pandas.read_json('/Users/How.Short/Desktop/Python內容/Python-class/classforpandas/my-employees.json')
dxlsx = pandas.read_excel('/Users/How.Short/Desktop/Python內容/Python-class/classforpandas/my-employees.xlsx')

# 載入已經存在的 SQL 資料表，當作 pandas 的 DataFrame，並寫入一個新的資料表在資料庫裡。
engine = create_engine('postgresql+psycopg2://louis:louis830630@127.0.0.1:5432/staff')
dsql = pandas.read_sql_table('employees', engine, schema = 'mystaff')

# 將原本已存在的資料表欄位名稱，重新命名。
dsql.rename({"id": "ID", "first_name": "FirstName", "last_name": "LastName", "department": "Department", "phone": "Phone", "address": "Address", "salary": "Salary"}, axis = 'columns', inplace = True)

# 將輸入的四個檔案，寫入在資料庫裡，並將這個資料表命名為 allstaff，且不使用預設的 index。
dtxt.to_sql('newstaff', engine, schema = 'mystaff', index = False)

# 因為已經將資料寫到資料表內，且已經建立一個新的資料表 allstaff，所以在 if_exists 就會是 append，因為要將資料擴增到這個資料表內。
dcsv.to_sql('newstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')
djson.to_sql('newstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')
dxlsx.to_sql('newstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')
dsql.to_sql('newstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')

# 印出 employees 所有的資料表。
query_all = pandas.read_sql_query('SELECT * FROM mystaff.newstaff', engine)

# 計算在這個資料表內，有多少名 employees，且印出數量。
query_count = pandas.read_sql_query('SELECT COUNT (*) FROM mystaff.newstaff', engine)
total_employees = query_count.iloc[0][0]

# 計算在這個資料表內，Department 有幾個。
query_dept = pandas.read_sql_query('SELECT COUNT(DISTINCT "Department") FROM mystaff.newstaff', engine)
total_depts = query_dept.iloc[0][0]

# 計算每一個部門裡，有多少名 employees。
query_epd = pandas.read_sql_query('SELECT "Department", COUNT("LastName") FROM mystaff.newstaff GROUP BY "Department"', engine)

# 將 index 設為 Department。
query_epd.set_index("Department", inplace = True)

# 計算在 Logistics 這個部門裡，有幾位 employees。
log_emp = query_epd.loc["Logistics", "count"]

# 計算在 marketing 這個部門裡，有幾位 employees。
mk_emp = query_epd.loc["Marketing", "count"]

# 計算在 sales 這個部門裡，有幾位 employees。
sls_emp = query_epd.loc["Sales", "count"]

# 計算在 IT 這個部門裡，有幾位 employees。
it_emp = query_epd.loc["IT", "count"]

# 計算在 HR 這個部門裡，有幾位 employees。
hr_emp = query_epd.loc["HR", "count"]

# 計算在 Salary 這個欄位，最大值為多少。
sal_high = query_all['Salary'].max()

# 計算在 Salary 這個欄位，最小值為多少。
sal_low = query_all['Salary'].min()

# 計算在 Salary 這個欄位，平均數為多少。
sal_avg = query_all['Salary'].mean()

# 在 HTML 裡要呈現的內容。
summary = [["Total number of employees", int(total_employees)],
           ["Employees in Logistics", int(log_emp)],
           ["Employees in Marketing", int(mk_emp)],
           ["Employees in Sales", int(sls_emp)],
           ["Employees in IT", int(it_emp)],
           ["Employees in HR", int(hr_emp)],
           ["Highest salary", int(sal_high)],
           ["Lowest salary", int(sal_low)],
           ["Salary average", int(sal_avg)]]

summary_html = pandas.DataFrame(summary, columns = ["Stats", "Value"])
with open("summary.html", "w") as f:
    summary_html.to_html(f, index = False, justify = 'center')

