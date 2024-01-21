def printNumber():
    for index in range(5,9):
        if index == 7:
            break
        print(index)
    else:
        print("no index value in loop")
# printNumber()

def countNumber():
    i=0
    while i<10:
        if i == 7:
            break
        print(i)
        i += 1
    else:
        print('while I exceed')
# countNumber()

# use of function with try except 
def calculatMultiplY():
    try:
        multiplierNumer = int(input('Insert the number you want to multiply:'))
        if(multiplierNumer <= 1):
            raise ValueError("Value must be more than 1")
        print(f"Multiplication table of {multiplierNumer} is: ")
        for i in range(1,11):
            print(f"{int(multiplierNumer)} x {i} = {i*int(multiplierNumer)}")
    except ValueError as err:
        print(f"Input value must be number. => {err}")
    except IndexError:
        print("index doexn't exit on array list")
    except Exception as err:
        print(err)
    finally:
        print("try excemtion finally finished")
    return "calculation finished"
# calculatMultiplY()

def printEnumareateList():
    marks = [45,85,68,45]
    for (index,item) in enumerate(marks, start=50):  #start means replace the index number 0 as 50
        print(index,' => ', item)
# printEnumareateList()