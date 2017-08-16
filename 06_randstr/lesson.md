Now that we know how to randomly select an item from a list of strings, let's generate a new string consisting of a sequence of items randomly chosen from our list.

To start, let's create a slightly longer and (possibly) more interesting list of strings than the lists we've been using so far.

    mylist = ["blue", "sky", "washes", "over", "me"]

Let's also assign an *empty string* to a new variable called **result**. This empty string — which we're going to fill up soon — is represented by quotation marks that aren't enclosing anything:

    result = ""

We're going to randomly select an item from our list of strings, a certain number of times, and add each item selected to this currently empty result.

We can use the plus symbol (**+**) to *concatenate*, or add together, two or more strings, producing a single new, longer string. The following expression, for example, will produce the single string "hi there":

    "hi" + " " + "there"

That's how we'll build up our result. We'll use another new construct here, called a *loop*, to randomly select an item from the list ten times, concatenating each randomly selected item with the existing result. Each time, we'll also add a blank space as a word separator.

    for i in range(0, 9):
        myrandindex = randint(0, upper_bound)
        result = result + mylist[myrandindex]
        result = result + " "

When this loop concludes, the value of **result** will be a string containing ten words, each randomly selected from the list.


**Instructions for this exercise**

1. Run the existing program and observe its output.
2. Modify the values passed to the **range** command, which determines how many times the commands in the loop are performed.
3. Run the program again and observe its output.
4. Extend the existing list by adding new items, then run the program again.
5. Experiment further, if you like (there are no tests to pass in this exercise)
6. Click "submit" to submit your code.
