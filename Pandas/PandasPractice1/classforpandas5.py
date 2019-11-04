import pandas

djson = pandas.read_json('/Users/How.Short/Desktop/Python內容/Python-class/classforpandas/Employees.json')
print(djson)

djson['Badge ID'] = ["0010", "0011", "0012", "0013", "0014", "0015", "0016", "0017", "0018", "0019"]
print(djson)

djson = djson.append([{"Address": "11th Address, Miami", 
                    "Department": "IT", 
                    "FirstName": "John", 
                    "ID": 11, 
                    "LastName": "Doe", 
                    "Phone": "09090977", 
                    "Salary": "60000", 
                    "Skills": "Java", 
                    "Badge ID": "0020"}, 
                    {"Address": "12th Address, Miami", 
                    "Department": "IT", 
                    "FirstName": "Jake", 
                    "ID": 12, 
                    "LastName": "Winston", 
                    "Phone": "09090988", 
                    "Salary": "59000", 
                    "Skills": "Python", 
                    "Badge ID": "0021"},
                    {"Address": "13th Address, Miami", 
                    "Department": "IT", 
                    "FirstName": "Jacob",
                    "ID": 13, 
                    "LastName": "Mueller", 
                    "Phone": "09090999", 
                    "Salary": "59600", 
                    "Skills": "Routing", 
                    "Badge ID": "0022"}], ignore_index = True)

print(djson)

djson["Badge ID"] = djson["FirstName"] + '2019'
print(djson)

djson["FirstName"] = djson.shape[0] * ['Jack']
print(djson)

print(djson.shape)
print(djson.shape[0])

djson.loc[djson['Department'] == 'IT','Salary'] = '90000'
print(djson)

djson.loc[(djson['Department'] == 'IT') & (djson['Skills'] == "Networking"),'Salary'] = '100000'
print(djson)

djson.loc[djson["ID"] == 9,["Salary","Phone"]] = ["80000","77777777"]
print(djson)

djson.set_index("Badge ID",inplace = True)
print(djson)

print(djson.drop('Luke2019'))

print(djson.drop('Phone','columns'))

print(djson.drop(djson.index[4]))

print(djson.drop(djson.index[0:4]))

print(djson.drop(djson.columns[1],1))

print(djson.drop(djson.columns[5:],1))



