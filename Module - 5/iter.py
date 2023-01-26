numbers = [5,1,4,9,36,78]

numbers_iter = iter(numbers)
try:
    print(next(numbers_iter))
    print(next(numbers_iter))
    print('I am adoing other tasks. but I will remember you iter position and will resume from there')
    print(next(numbers_iter))
    print(next(numbers_iter))
    print('Doing something else and calling again iter next')
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
except StopIteration:
    print("Iteration has stopped")