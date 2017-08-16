Python provides us with a way to randomly select numbers. (It's more correct to say *pseudo*-randomly select numbers, but we won't go into that here.)

Why would one want to do this? To start with, for the same reason you might flip a coin: to decide the question of which team starts with the ball, in a soccer match, or to decide a (hopefully relatively unimportant) question that you can't resolve any other way. (For example, shall I eat a sandwich or a salad for lunch today?)

To randomly select a number in Python, you must first *import* a special *module* (a separate package of code) containing the relevant commands.

That module is called **random**, and it provides a variety of commands for working with random numbers.

Since for this purpose of this exercise, we're only interested in randomly selecting integers, rather than any other kind of number, we'll import the command we need this way:

    from random import randint

Once you've done that, you can select a random number between 0 and 9 this way:

    print(randint(0, 9))

Each time you run this command, it will print a randomly selected integer between 0 and 9. (This doesn't mean it's impossible to get the same number twice or more in a row.)

For now, just print some random numbers. In our next exercise, you'll see how to put this to interesting use.

**Instructions for this exercise:**

1. Run the existing program and observe its output.
2. Modify the program to print randomly selected numbers in a different range.
3. Run the program again and observe its output.
4. Experiment further, if you like (there are no tests to pass in this exercise)
5. Click "submit" to submit your code.
