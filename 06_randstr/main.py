from random import randint

mylist = ["blue", "sky", "washes", "over", "me"]

mylist_length = len(mylist)

upper_bound = mylist_length - 1

result = ""

for i in range(0, 9):
    myrandindex = randint(0, upper_bound)
    result = result + mylist[myrandindex]
    result = result + " "

print(result)
