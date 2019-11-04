import pandas

djson = pandas.read_json('/Users/How.Short/Desktop/Python內容/Python-class/classforpandas/Employees.json')
print(djson)

print(djson.loc[5])

print(djson.loc[[2,4,7]])

print(djson.loc[3:5])

print(djson.loc[0:2,'Phone':'Skills'])

djson.set_index('Address',inplace = True)
print(djson)

print(djson.loc["1st Address, Miami":"5th Address, Miami"])

print(djson.loc["1st Address, Miami":"5th Address, Miami",'Phone'])

print(djson.loc["1st Address, Miami":"5th Address, Miami",['LastName','Skills']])

print(djson.loc["1st Address, Miami":"5th Address, Miami","LastName":"Skills"])

print(djson.loc["1st Address, Miami","Phone"])

print(djson.loc[:,'Phone'])

print(djson[:])

print(djson.loc[:,:])

print(djson.loc[:,"Department"])

print(set(djson.loc[:,"Department"]))

djson = pandas.read_json('/Users/How.Short/Desktop/Python內容/Python-class/classforpandas/Employees.json')
print(djson)

print(djson.iloc[4])

print(djson.iloc[[4,6,8]])

print(djson.iloc[2,2:5])

print(djson.iloc[:,2:5])

print(djson.iloc[:])

print(djson.iloc[:,:])

print(djson.sample())

print(djson.sample())

print(djson.sample(4))

print(djson.sample(n = 4))

print(djson.sample(frac = 0.5))

print(djson.sample(frac = 0.2))

djson = pandas.read_json('/Users/How.Short/Desktop/Python內容/Python-class/classforpandas/Employees.json')
djson.set_index('ID',inplace = True)
print(djson)

print(djson[djson.loc[:,'Salary'] < 50000])

print(djson[(djson.loc[:,'Salary'] < 50000) | (djson.loc[:,'Salary'] > 56000)])
print(djson[(djson.loc[:,'Salary'] > 50000) & (djson.loc[:,'Department'] == 'Sales')])
print(djson[~(djson.loc[:,'Department'] == 'IT')])