class Person:
    name = ''
    salary = 0
    age = 0
    isMarried = False

    # constructor  
    def __init__(self,initialName,initialSalary,initialAge,initialMarriag):
        self.name = initialName
        self.salary = initialSalary
        self.age = initialAge
        self.isMarried = initialMarriag
    
    # getters as property using @property decorator
    @property
    def salaryInYear(self):             # by adding @property, we are converting this method as a property so we can access the value without calling the salaryInYear method
        return self.salary * 12
    
    # setter as property using @methodName.setter decorator
    @salaryInYear.setter
    def salaryInYear(self,newYearlyValue):
        self.salary = int(newYearlyValue / 12)

    # static methods
    @staticmethod
    def addSalaryIncentive(selfObj,salaryIncentivePercent):
        selfObj.salary = selfObj.salary + (selfObj.salary * salaryIncentivePercent)/100

    # Magic/Dunder methods 
    def __len__(self):        # to make custom Dunder method, use first & last double underscore; It is over-write the len() method only for this class & instance
        i=0
        for character in self.name:
            i += 1
        return i

    # custom methods 
    def infoPrint(self):
        print(f"The salary of {self.name} is {self.salary}")


personObj = Person('Velko',7000,52,True)
# print(personObj.name)
# Person.addSalaryIncentive(personObj,5)
print(f"Yearly salary = {personObj.salaryInYear} | Monthly salary = {personObj.salary}")
# personObj.salaryInYear = 1200
# print(f"Yearly salary = {personObj.salaryInYear} | Monthly salary = {personObj.salary}")
# personObj.infoPrint()
print(len(personObj))


import logging
# decorator function 
def greetDecoratorFn(fn):
    def wrapperFn(*args,**kwargs):
        print('executing before function call')
        result = fn(*args,**kwargs)
        print('executing after function call')
        logging.error('test info msg')
        return result
    return wrapperFn

@greetDecoratorFn
def makeMultiply(x,y):
    print(f"The Multiple of {x} x {y} is {x*y}")
# makeMultiply(10,20)                      #using decorator way by @
# greetDecoratorFn(makeMultiply(30,40))
    



# OOP main class
class Employee:
    id = ''
    name = ''
    _balance = 0        #__doubleUnderscore means private property, can't access outside of the class but child inheritnce class can access
    __password = ''     #_singleUnderscore means private property, can't access outside of the class

    def __init__(self, name,id,password,balance) -> None:
        self.id = id
        self.name = name
        self.__password = password
        self._balance = balance
    
    def showDetails(self):
        print(f"name: {self.name}| Balance = {self._balance} | password = {self.__password}")

employee1 =  Employee('Daniel',789,'hArDpaSSwOrf',3000)
# print(employee1.__password)   # can not access the private property
# print(employee1._Employee__password)   # Name Mnagling: can access the private property forcefully
# employee1.showDetails()




# OOP inheritance of class Employee 
class Programmer(Employee):
    language = ""
    def __init__(self, name, id, password, balance,language):
        super().__init__(name, id, password, balance)               # call super().__init__ method to pass data to parent class
        self.language = language

    def showLanguage(self):
        print(f"{self.name} is expert in {self.language} with salary {self._balance}")

employee2 =  Programmer('Daniel',789,'sIMplEpaSSwOrf',2500,'Python & Javascript')
employee2.showLanguage()
# print(employee2.__dir__())


import requests
response = requests.get("https://jsonplaceholder.typicode.com/photos")
data = response.json()
print(data)

