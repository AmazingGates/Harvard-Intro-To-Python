# Here, "x" and "y" have been declared and assigned to an int(). In return, The int() is given a parameter of input().
#Lastly, the input() is given the return value of "What is x"/"What is y".
x = int(input("What is x? "))
y = int(input("What is y? "))


# "or" can be used to simplify questions even further. For example, instead of asking two separate questions 
#(x < y:), and (x > y:), "or" can be used to fuse the two questions together. For example (x < y or x > y:).

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")