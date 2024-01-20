for index in range(5,9):
    if index == 7:
        break
    print(index)
else:
    print("no index value in loop")


i=0
while i<10:
    # if i == 7:
    #     break
    print(i)
    i += 1
else:
    print('while I exceed')

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
calculatMultiplY()
