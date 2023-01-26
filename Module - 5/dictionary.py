# dictionary or object operations 
marks = {'physics':12, 'chemistry':45,'math':56}

# update 
marks['math'] = 56.32

# add
marks['english'] = 89

# delete 
del marks['chemistry']
print(marks)

# get keys, values, items
marks_keys = marks.keys()
marks_values = marks.values()
marks_items = marks.items()
print(marks_keys," <=> ",marks_values," <=> ",marks_items)