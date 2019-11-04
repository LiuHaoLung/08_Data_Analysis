import pandas

dtxt = pandas.read_csv('/Users/How.Short/Desktop/Employees.txt')
print(dtxt)

dtxt2 = pandas.read_csv('/Users/How.Short/Desktop/Employees2.txt',delimiter = '|')
print(dtxt2)

dcsv = pandas.read_csv('/Users/How.Short/Desktop/Employees.csv')
print(dcsv)

dcsv = pandas.read_csv('/Users/How.Short/Desktop/Employees.csv',header = None)
print(dcsv)

dcsv = pandas.read_csv('/Users/How.Short/Desktop/Employees.csv',header = None,names = ['A','B','C','D','E','F','G','H'])
print(dcsv)

dcsv = pandas.read_csv('/Users/How.Short/Desktop/Employees.csv',header = None,prefix = 'COL')
print(dcsv)

dcsv = pandas.read_csv('/Users/How.Short/Desktop/Employees.csv')
dcsv.set_index('ID')
print(dcsv)
dcsv.set_index('ID',inplace = True)
print(dcsv)
dcsv.set_index('Address',inplace = True)
print(dcsv)
dcsv = pandas.read_csv('/Users/How.Short/Desktop/Employees.csv')
print(dcsv.shape)

dcsv = pandas.read_csv('/Users/How.Short/Desktop/Employees.csv',skiprows = 4)
print(dcsv)

dcsv = pandas.read_csv('/Users/How.Short/Desktop/Employees.csv',nrows = 5)
print(dcsv)

djson = pandas.read_json('/Users/How.Short/Desktop/Employees.json')
print(djson)

dxlsx = pandas.read_excel('/Users/How.Short/Desktop/Employees.xlsx')
print(dxlsx)

dxlsx = pandas.read_excel('/Users/How.Short/Desktop/Employees.xlsx',sheet_name = 0)
print(dxlsx)