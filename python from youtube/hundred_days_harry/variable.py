
ticket_number = 5744564
message = f"My ticket /r number is \t{ticket_number} which is too \n large"

print("Daniel",45,"Willium",sep="~",end="***\n")

list1 = [1.5, "abc"]
tupple1 = (("parrot",'pecoke'),('bear','fox'))
dictionary1 = {
    "name":"Daniel",
    "age": 47,
    "canVote": True,
    "address":{
        "road": "5/a kiumxing",
        "post": 9874
    },
    "interests": ["cooking","reading","gamming"]
}
print(list1) 
print(tupple1)
print(dictionary1)

# for loop 
for index, element in enumerate(list1):
    print(index,element)
"""
num1 = int(input("Type your first number: "))
num2 = int(input("Type your second number: "))
total = num1 +  num2
substruct = num1 - num2
multiply = num1 *  num2
divide = num1 / num2

result = {
    "total": total,
    "substruct": substruct,
    "multiply": multiply,
    "divide": divide,
}
print(result)
"""
ss_name = """Adil
Tadil
Nadil"""

for index, character in enumerate(ss_name):
    print(index,character)

# print(ss_name)

import time 
print("Current time = ",time.strftime("%H:%M:%S"))
print(range(10))

def numPrinter(rangeNumber=10,*restArgsAsIterable):
    total = 0;
    for num in range(rangeNumber):
        print(num,restArgsAsIterable)
        total = total + num
    return total

print("END LOOP")

sumResult = numPrinter(11,43,'er')
print({'sumResult':sumResult})