# Conditionals, are conditional statements in Python, and are used to ask questions and answer those question
#pertaining to which line of code you want to run at that moment.
# To ask a question (or use a Conditional), an "if" statement must be used.


# Here, "x" and "y" have been declared and assigned to an int(). In return, The int() is given a parameter of input().
#Lastly, the input() is given the return value of "What is x"/"What is y".
x = int(input("What is x? "))
y = int(input("What is y? "))



# Here, in these examples, an "if" statement is used to determine which line of code will be printed out based on 
#the conditions set by the programmer.
if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x and y are equal")
