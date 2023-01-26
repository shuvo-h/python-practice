numbers = [14,65,35,78,14,65,85,35]
# tupple is immetuable, not editable. permanent memory story until application alive
numbers_tupple = 14,65,35,78,14,65,85,35
print(" List/Array => ",numbers," Tupple => ",numbers_tupple)
nums_tupple = (45,36,98,74,34) 
print(nums_tupple)
print(nums_tupple[2]) # element access through index

# here [12,45,12] is one single element of tupple, you can't edit it. But you can edit the list element of the list inside tupple element
tupple2D = ([12,45,12],[45,11,36])
print(tupple2D)
tupple2D[0][1] = 48     # editing  element of tupple list 45 -> 48
print(tupple2D)

sort_number = 2 # it is a number
sort_tupple = 2, # it is a tupple just for a Koma","
print(sort_number,sort_tupple)

tupple_from_list = tuple(numbers)
print(tupple_from_list)





