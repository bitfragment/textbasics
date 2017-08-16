from random import randint

mylist = ["rock", "paper", "scissors"]

mylist_length = len(mylist)

upper_bound = mylist_length - 1

myrandindex = randint(0, upper_bound)

print(mylist[myrandindex])