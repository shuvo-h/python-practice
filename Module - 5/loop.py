numbersList = [5,1,4,9,36,78,20]
total = sum(numbersList)
print(total)

# loop on list or array 
totalSum = 0
for i in numbersList:
    totalSum += i

print(totalSum)
# loop on list with index number
for idx,item in enumerate(numbersList):
    print(item," enume ",idx)

# loop on set
numTotal = 0
numsSet = {14,65,35,78,14,65,85,35}
for i in numsSet:
    numTotal += i

print(numTotal)

# loop on tuple
tupleTotal = 0
tupleList = (14,65,35,78,14,65,85,35)
for i in tupleList:
    tupleTotal += i

print(tupleTotal)

# loop on dictionary or object
sumDictionary=0
marksDictionary = {'physics':12, 'chemistry':45,'math':56}
for item in marksDictionary:
    sumDictionary += marksDictionary[item]
print(sumDictionary)

# loop 1st element key of the object/dictionary, 2nd element is it's value
for itemKey,itemValue in marksDictionary.items():
    print(itemKey,itemValue)