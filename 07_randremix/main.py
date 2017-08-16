from random import randint

mystring = "blue sky washes over me"

mylist = mystring.split()

mylist_length = len(mylist)

upper_bound = mylist_length - 1

result = ""

for i in range(0, 25):
    myrandindex = randint(0, upper_bound)
    result = result + mylist[myrandindex]
    result = result + " "

print(result)
