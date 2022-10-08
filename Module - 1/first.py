# print("My First Py Code")
# a=int(input("Number 1\n"))

# b=int(input("Number 2\n"))

"""
a="ABC DEF"

x=f"SKv TuR = {a}"
print(x)

"""


price = -10
if price :
    print("Yes")
else :
    print("No")


a=0
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else :
    print("Non negative")

i=1
while(i<3):
    # print(i,end=" ")
    i+=1

i=1
while(i<10):
    print(i,end=" ")
    i+=1
    if i==5:
        break

i=1
while(i<10):
    print(i,end=" ")
    if i==5:
        break
    i+=1

print("\n")

for i in range(10): 
    if i==5:
        continue
    print(i,end=" ")

print("\n")
a="Bd"
for i in range(len(a)):
    print(a[i],end="")
print("\n")
a="Bd"
for i in range(len(a)):
    print(i,end="")
print("\n")
i=1
while(i<3):
    print(i)
    i+=1