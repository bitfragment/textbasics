By combining list indexing with random number generation, we can *randomly select an item from a list.*

How is that possible? First, remember that items in a list are numbered in ordinary numerical order, beginning with zero:

    mylist = ["rock", "paper", "scissors"]
              0       1        2

Second, remember that we can use the **randint** command (once we have imported it from its module) to select a random integer in any range that we specify:

    from random import randint
    print(randint(0, 9))

This means that if we can generate a random number in the same range used to number the items in a particular list, then we can use that number as a list index number to retrieve a specific item — effectively randomly selecting an item in the list!


## Get the length of a list

There's one problem. Since we know that items in a list are numbered beginning with zero, zero will be the *lower bound*, or minimum value, of the range we pass to the **randint** command. But what do we use for the *upper* bound, or maximum value, of that range?

We want the upper bound of the range to be the index number of the *last item* in the list, don't we?

Here we can use another Python command: **len**. This command returns the *length* of any list, meaning the number of items it contains. Since there are three items in our list, the following command will return the value **3**:

    len(mylist)

To make things easier to read, let's assign the value returned by this command to another variable:

    mylist_length = len(mylist)

This new variable, **mylist_length**, now holds the length of **mylist** — that is, 3. We can now use **mylist_length** as the upper bound passed to the **randint** command.


## Setting the upper bound

There's just one problem. Remember that items in a list are numbered *beginning with zero*, not with 1. This means if the number of items in a list is 3, then the last item in that list will have the index number 2 (not 3); while the second-to-last item in the list will have the index number 1 (not 2); and the first item in the list will have the index number 0 (not 1).

For this reason, we'll need to subtract 1 from the value of **mylist_length** if we want to pass it to the **randint** command as an upper bound.

To keep things easy to read, let's create another new variable called **upper_bound** and assign it the value of the length of **mylist** minus one:

    upper_bound = mylist_length - 1


## Generating a random index number for our list

Now we're ready to select a random number that is guaranteed to be one of the list index numbers in our list. Let's assign that to another variable, **myrandindex**:

    myrandindex = randint(0, upper_bound)


## Randomly selecting an item from the list

Recall the syntax for selecting a single item from a list, which you learned in a previous exercise. Instead of specifying a particular index number, however, in this case you're using the randomly selected number:

    print(mylist[myrandindex])

Each time you run this program, it will print a randomly selected item from the list!


## Instructions for this exercise

1. Run the existing program and observe its output.
2. Extend the existing list by adding additional items to it.
3. Run the program again and observe its output.
4. Experiment further, if you like (there are no tests to pass in this exercise)
5. Click "submit" to submit your code.
