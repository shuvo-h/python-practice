from math import sqrt,floor,ceil
import math
# print(math.sqrt(9))

import loop as allLoopMethods
# allLoopMethods.calculatMultiplY()

# os module 
import os 
if (not os.path.exists('tesstFolder')):
    os.mkdir('tesstFolder')
    

# global vs local variables 
num = 4  # global variable
def printNum():
    num = 65
    num2 = 85  # local variable
    print(f"hello number {num} & {num2}")
# printNum()
# print(num)

openedFile = open('tesstFolder/testFile.txt','r')
# allText = openedFile.read()
# openedFile.write('a new lorem is waiting. \n')
# allText = openedFile.read()
# print(allText)

# read as line 
while True:
    textLine = openedFile.readline();
    if not textLine:
        break
    print(textLine)
openedFile.close()

# lambda is a anoymous function wich must be completed in a single line
def makeMultiply(x,y):
    return x * y 
# print(makeMultiply(5,3))
lambdaAnoumousFn = lambda x,y: x*y
# print(lambdaAnoumousFn(6,3))