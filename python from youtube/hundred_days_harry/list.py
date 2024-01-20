listNum = [11,96,1,8]
listNum.append(100)             # [11, 96, 1, 8, 100]
listNum.sort(reverse=True)      # [100, 96, 11, 8, 1]
listNum.reverse()               # [1, 8, 11, 96, 100]
listNum.index(100)              # 4; the index number of the number
listNum.count(96)               # 1; here 96 is present once in the list
newList = listNum.copy()        # create a new copy of old list
newList.insert(2,55)            # [1, 8, 55, 11, 96, 100] insert 55 at index position 2
newList.extend([63,42])         # [1, 8, 55, 11, 96, 100, 63, 42] actually combine two array
newList[2:5]
# print(listNum,newList)

# tupple methods
tuppleData = (4,7,'red',True)       # a type of array/list which elements are constant. you can not change the tupple value. when you need to keep constant the elements, then use tupple
tuppleData[-2]
len(tuppleData)
if 'red' in tuppleData:
    result = "yes, 'RED' is present"
else:
    result = "no, 'RED' is not present"

tuppleData[2:4]
# print(type(tuppleData), tuppleData)

# add 'Daniel' at 2nd index of a tupple
def changeTuppleElement(tuppleData,newValue,indexNumber):
    tuppleDataList = list(tuppleData)
    tuppleDataList.pop(indexNumber-1)
    tuppleDataList.insert(indexNumber-1,newValue)
    newTupple = tuple(tuppleDataList)
    return newTupple

student = ('xyz collage','Willium',28,True,'eight')
result = changeTuppleElement(student,'Daniel',2)
# print(student,result)


# string methods in python 
roll = 10
subject = "Mathematics"
fees = 560.895264
formattedString = f"My subject is {subject} and my roll is = {roll}. My exam fees is = {fees:.3f}"
# print(formattedString)

# docstring in python only written immediately after function/method/class/module declaration
def makeSquire(n):
    '''Take a number n, and make squire of that number then return'''
    return n**2
# print(makeSquire(4),"DocString value = ",makeSquire.__doc__)

def makeFactorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * makeFactorial(n-1)
# print(makeFactorial(1))
    

def makeFibonacciSeries(n):
    count = 1
    num1=0
    num2=1
    next_number = num2
    if(n==0):
        print(num1)
    elif (n==1):
        print(num1)
        print(num2)
    else:
        while count <= n:
            print(num1)
            next_number = num1 + num2
            num1,num2 = num2, next_number
            count += 1


# makeFibonacciSeries(10)

# set : unordered collection list, no duplicate value, values are readonly
carSet_1 = {'BMW',36000,True,'green','available'}
carSet_2 = {'BMW',35000,True,'red','available'}
carUnion = carSet_1.union(carSet_2) # create new set with all items
carIntersection = carSet_1.intersection(carSet_2) # create new set with common items
# print(carUnion,carIntersection)
# carSet_1.update(carSet_2) # update the carSet_1 by adding values ofcarSet_2
# carSet_1.intersection_update(carSet_2) # update the carSet_1 by adding common values between the two set
carSymetric = carSet_1.symmetric_difference(carSet_2) # A-B: which are not common
# carSet_1.symmetric_difference_update(carSet_2) # A-B: which are not common

"""
    - union()
    - update()
    - intersection()
    - intersection_update()
    - symmetric_difference()
    - symmetric_difference_update()
    - isdisjoint()                     // check if an items of a set is same on another set
    - issuperset()                      // similar to isdisjoint. but it check if all element of a set is present in another set or not. 
    - issubset()                      // reverse of issuperset. 
    - add()
    - remove/discard()
    - del                               // delete the entire set
    - pop()
"""

dictionaryVar = {
    "name":"David",
    "roll": 45,
    "isPassed": False
}
dictionaryVar2 = {
    "name":"Willium",
    "roll": 18,
}

# print(dictionaryVar['name'],dictionaryVar.get('name'))
# print(dictionaryVar.values())
# print(dictionaryVar.keys())
# print(dictionaryVar.items())
# for key, value in dictionaryVar.items():
dictionaryVar.update(dictionaryVar2)
print(dictionaryVar)
"""
    - values()
    - keys()
    - items()
    - update()
    - clear()
    - del varName['keyName']// delete a property
    - pop('keyName')        // remove the specific key
    - popItem()             // remove the last property

"""
