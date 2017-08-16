In a previous exercise, you created and printed a *string*.

Python allows you to create *lists* of strings (and other types of data, as well).

A *list* is enclosed in square brackets, and items in the list are separated by commas. In a list of strings, the commas must be placed outside, not inside, each closing quotation mark:

    ["item1", "item2", "item3"]

You can print a list of strings just as easily as you can print a single string, by passing the list as data to the **print** command (remember to enclose it in parentheses):

    print(["item1", "item2", "item3"])

The combination of both parentheses and square brackets can make this program confusing. One way to improve this program is to assign the list to a *variable* and then print the variable instead of the list itself.

A variable is a name of your choosing (you can choose whatever you like, as long as it isn't also the name of a Python command). You assign a variable to represent another piece of data using the equals sign:

    mylist = ["item1", "item2", "item3"]

Think of the variable as a shortcut to your data. Once you have assigned your list of strings to the variable **mylist**, the variable **mylist** can be used whenever you want to access the data in your list. For example, you can pass the variable **mylist** to the **print** command, instead of passing the list itself:

    print(mylist)

**Instructions for this exercise:**

1. Run the existing program and observe its output.
2. Add the string "scissors" to the end of the list of strings.
3. Run the program again to print the newly extended list.
4. Click "submit" to submit your code.
5. If your code fails the tests, check it for errors, correct, and submit again until it passes the tests.
