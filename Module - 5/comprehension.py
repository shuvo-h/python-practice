numbers = [12,45,63,69,87,41,65,24]

odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

print(odd_numbers)

# comprehension: use a condition before the for loop and make the whole operation inside a list/array
odd_numbers_comp = [num % 2 == 1 for num in numbers]
print(odd_numbers_comp)

# before for loop, take each element, and end of the for loop, add a condition how the element will be returned
# select the number, from the for loop, match the conditio_1, match the conditio_2, 
#                           element  |  for_loop     |  condition
odd_numbers_comp_condition = [num for num in numbers if num % 2 == 1]
print(odd_numbers_comp_condition)
#                                  element  |  for_loop     |  condition_1     |  conditiona_2
odd_numbers_comp_double_condition = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odd_numbers_comp_double_condition)

# double loop and select the two elements from thro list/array 
names = ['sari','lari','lori','cori']
ages = [37,32,21]
name_age_pair = [(name, age) for name in names for age in ages if age < 25]
print(name_age_pair)

name_age_pair_oldMethod = []
for name in names:
    for age in ages:
        if(age < 25):
            name_age_pair_oldMethod.append((name,age))
print(name_age_pair_oldMethod," => same as shortcut comprehension method")
