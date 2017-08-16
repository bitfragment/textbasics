In a previous exercise, you created a list of strings.

Python automatically numbers all of the items in a list. You can use this automatic numbering to extract one or more items from a list and do something else with it (print it, for example).

There is one tricky thing to remember here. Items in a list are numbered in ordinary numerical order, but *beginning with zero* rather than beginning with **1**, as you might expect:

    mylist = ["item1", "item2", "item3"]
              0        1        2

You can refer the first item in this list by enclosing the *index number* **0** in square brackets following the variable name that represents that list. This is called list *indexing*, or "indexing into" the list:

    mylist[0]

You can refer to the second item by enclosing the *index number* **1** in square brackets following the variable name that represents that list:

    mylist[1]

And so on. The command

    print(mylist[0])

will print *only* the string "item1", and nothing else from the list, while

    print(mylist[1])

will print *only* the string "item2", and nothing else from the list.

**Instructions for this exercise:**

1. Run the existing program and observe its output.
2. Modify the program so that it prints *only* the string "paper".
3. Run the program again and observe its output.
4. Click "submit" to submit your code.
5. If your code fails the tests, check it for errors, correct, and submit again until it passes the tests.
