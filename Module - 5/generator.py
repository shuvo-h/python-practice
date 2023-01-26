from unittest import result


numbers = [5,1,4,9,36,78]
# generator is just a simple function, which 'yield' result as a chunk rather than 'return', but conditionally 'return' can also be used to stop the generator to send 'yield' chunk
#  use 'yield' insted of 'return'. 'yield' doesn't break the function rather wait to complete the full process but in mean time, it send back the result chunk wht yield already got, 
#  similar to stream pip() to res in expressJS: readStream.pip(res)
def get_numbers(nums):
    for num in nums:
        yield num

result = get_numbers(numbers);
# print(list(result))
print(next(result))
print(next(result))
print("I am doing other task 1")
print("I am doing other task 2")
print(next(result))
print(next(result))