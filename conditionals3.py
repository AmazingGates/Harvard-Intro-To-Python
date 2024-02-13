# Here, "x" and "y" have been declared and assigned to an int(). In return, The int() is given a parameter of input().
#Lastly, the input() is given the return value of "What is x"/"What is y".
x = int(input("What is x? "))
y = int(input("What is y? "))


# "or" can be used to simplify questions even further. For example, instead of asking two separate questions 
#(if x < y:), and (if x > y:), "or" can be used to fuse the two questions together. For example (if x < y or x > y:).

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")



# In the example below, the "or" is removed completely to simplify the code even more. In it's place, the not equal to
#symbol is used ("!=") to acheive the same goal as the code with the "or" statement.
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")