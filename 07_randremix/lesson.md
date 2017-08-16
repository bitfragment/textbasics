When randomly generating a string from a list of other strings, the extent to which the result is an *interesting* result often depends on the length of the list of possible choices: more words to choose from means more possible combinations of words.

It's certainly possible to manually type out a very long list of words, in the hope of making the result more interesting — but it would almost certainly be very tedious, wouldn't it?

Fortunately, a shortcut is available, in the command **split**. This command transforms a string into a list of smaller strings, and it does this by "breaking" the string anywhere it finds a blank space. The command

    "blue sky washes over me".split()

will produce the list:

    ["blue", "sky", "washes", "over", "me"]
    
What this means is that you can copy a chunk of text from some other source and paste it into your program (between quotation marks!) as a string, assigning it to the variable **mystring** in this program. That string will be automatically split into a list of words that will form the list of items randomly selected. Go ahead and try it.


**Instructions for this exercise**

1. Run the existing program and observe its output.
2. Copy a sentence, a paragraph, or a sequence of paragraphs from any web page. *Important: choose text that does not contain any double quotation marks — because we are using double quote marks to demarcate a string, here, any double quotation marks in your copied text may cause the program to fail.* Replace the string "blue sky washes over me" with your copied text.
3. Run the program again and observe its output.
4. Experiment further, if you like (there are no tests to pass in this exercise)
5. Click "submit" to submit your code.
