largest = max(45,36,78,41,205,69)
print(largest)

nums = {14,65,35,78,14,65,85,35}
big_max = min(nums)
print(big_max)

numbers = [5,1,4,9,36,78]
reverse_nums = reversed(numbers)
print(list(reverse_nums))

sorted_nums = sorted(numbers,reverse=True)
print(list(sorted_nums))

actors = [
    {'name':'rohit', 'age':34},
    {'name':'kohli', 'age':36},
    {'name':'rishab', 'age':28},
    {'name':'kl rahul', 'age':32},
    {'name':'surjo', 'age':24},
    {'name':'Iare', 'age':28},
]
# sorted_actors = sorted(actors,key=lambda actor: actor['age'],reverse=True)
sorted_actors = sorted(actors,key=lambda actor: actor['name'],reverse=True)
print(sorted_actors)