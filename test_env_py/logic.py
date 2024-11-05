# List Comprehensions
myNumbers = [0,1,2,3,4,5,6,7,8,9]
squire = [number**2 for number in myNumbers if number % 2 == 1]
print(squire)

# 2. Lambda Functions like anoymous function: generally use in map(),filter(),sorted
mapsquire = map(lambda el:el**2,myNumbers)
print(list(mapsquire))

filterNums = filter(lambda el:el%2 != 0,myNumbers)
print(list(filterNums))

people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

names = map(lambda el:el['name'],people)
print(list(names))
agePeple = filter(lambda el:el['age']>=30,people)
print(list(agePeple))
sortedPeple = sorted(people,key=lambda el:el['city'],reverse=True)
print(list(sortedPeple))