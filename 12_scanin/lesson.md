When used in an expression, the **in** command returns a *boolean* value: that is, either **True** or **False**. It returns **True**, for example, if one string is found *in* another string, and **False** otherwise. This expression:

    "blue" in "blue sky"

returns **True**. So does this expression:

    "blue" in "bluefish"

These expressions, on the other hand, will return **False**:

    "blue" in "red dawn"
    "blue" in "yellowfin"

We can use the **in** command to detect keywords in text input by the user.


**Instructions for this exercise**

1. Run the existing program, interact with it by typing a string that *does not* contain the string "blue", and observe its output.
2. Run the existing program, interact with it by typing a string that *does* contain the string "blue", and observe its output.
3. Change the string "blue" to something else, and edit the second message accordingly (note that inside the string representing the second message, the keyword is enclosed in single quotation marks). Repeat steps 1 and 2.
4. Click "submit" to submit your code.
