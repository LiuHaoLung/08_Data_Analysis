import pandas

d = pandas.DataFrame([['Andy', 46, 'Engineer'], ['Jane', 33, 'Nurse'], ['Robert', 21, 'Student'], ['Maria', 30, 'Student']])

print(type(d))
print(d)

d = pandas.DataFrame([['Andy', 46, 'Engineer'], ['Jane', 33, 'Nurse'], ['Robert', 21, 'Student'], ['Maria', 30, 'Student']],columns = ['Name','Age','Occupation'])
print(d)

d = pandas.DataFrame([['Andy', 46, 'Engineer'], ['Jane', 33, 'Nurse'], ['Robert', 21, 'Student'], ['Maria', 30, 'Student']],columns = ['Name','Age','Occupation'],index = ['ID1','ID2','ID3','ID4'])
print(d)

print(d.Name)
print(d.Age)
print(d.Occupation)
print(d.Age.min())
print(d.Name.max())
print(d.min())