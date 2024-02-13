# Here, "x" and "y" have been declared and assigned to an int(). In return, The int() is given a parameter of input().
#Lastly, the input() is given the return value of "What is x"/"What is y".
x = int(input("What is x? "))
y = int(input("What is y? "))



# In addition to "if" and "elif", there is also the "else" statement. "Else" is used as a catch all in the final line of
#the code and it doesn't need any conditions. "else" doesn't need any conditions because it is the last line of code and 
#all the other possible conditions have been false, which leaves only one possible condition. In the example below
#"if" and "elif" were false, which means that "else" was the only option, so it didn't need any conditions to be true.

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y are equal")