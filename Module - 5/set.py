import numbers


# list can contain duplicate elements 
numbers = [14,65,35,78,14,65,85,35]
print(numbers)

# set only can contain unique elements (No Duplicate Element)
nums = {14,65,35,78,14,65,85,35}
print(nums)

# convert a list or array to set 
convertListToSet = set(numbers)
print(convertListToSet)
convertListToSet.add(74)
convertListToSet.add(73)
convertListToSet.remove(78)
print(convertListToSet)
print(len(convertListToSet))