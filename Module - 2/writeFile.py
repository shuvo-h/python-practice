# with open('messageFile.txt','a') as fileWriter:
#     fileWriter.write(f'I am a new line writing through python\n')
# with open('messageFile.txt','r') as fileReader:
#     text = fileReader.read()
#     print(text)



# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)


def display(**kwargs):
    for i in kwargs:
        print(i, end=" ")

display(em="kel",sala=900)