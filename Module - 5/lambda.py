# it return value automatically without return statement, just like arrow function in javascript
numbersList = [5,1,4,9,36,78]


squire = lambda x: x*x
print(squire(6))

add = lambda x,y: x+y;
print(add(4,7))

double_it_fn = lambda x: x*2
doubled_number = map(double_it_fn,numbersList) # map is smilar to reduce function in javascript
print(list(doubled_number)) # map return a map object, so convert it to list to make it readable
tripled_number = map(lambda x: 3*x,numbersList)
print(list(tripled_number))

bigger_numbers = filter(lambda num: num > 10,numbersList)
print(list(bigger_numbers))

users = [{'name':'sakib', 'age':36},{'name':'rakib', 'age':32},{'name':'nazil', 'age':30},]
senior_user = filter(lambda user: user['age']>30,users)
print(list(senior_user))
