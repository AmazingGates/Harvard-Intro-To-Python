# In this example, we will be going over "loops". "loops" have the ability to do something over and over again
#with-in a piece of code, creating a sort of cycle.



# In the example below, a sort of "loop" has been created by repeating the same piece of code multiple times. 
#Of course, there are much more efficient ways to achieve this goal.
print("meow")
print("meow")
print("meow")


# In the code below we will be going over the "while" syntax. The "while" syntax is the key to creating a "loop".
# First, we declared and assigned "i" to 3. 
# Next, we started a "while loop" where "i" does not equal 0.
# Next, we instructed the code to print out "Long Live Gates" as long as the condition of "i" does not equal 0 is True.
# Next, we instructed the code to subtract 1 from 3 everytime the print() is called, and then return to the top 
#of the code to start the process again until the conditions are no longer True and the "loop" is stopped.
i = 3
while i != 0:
    print("Long Live Gates")
    i = i - 1


# In the example below, we are going to create the same exact "while loop" as above, but this time we are 
#going to count up instead of down.
i = 0
while i != 3:
    print("Alia Marie Gates")
    i = i + 1