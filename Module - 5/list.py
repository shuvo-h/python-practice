numbers = [5,1,4,9,36,78]

print(numbers[-2])

# slice list from 1 idx to -2 idx
# list[start_idx:end_idx:step]
print(numbers[1:-2:1])
print(numbers[2:])  # from 2nd idx to last of the list
print(numbers[2::3])  # from 2nd idx to last of the list with step jump 3 elements
print(numbers[4:0:-1]) # step count to reverse directino from 4th idx to 0th idx
print(numbers[::]) # full array list
print(numbers[::-1]) # full array list with reverse element

myList= [5, 10, 15, 25]
print(myList[::-2])


lamb = lambda x: x ** 3
print(lamb(5))
