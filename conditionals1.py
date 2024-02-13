# Here, "x" and "y" have been declared and assigned to an int(). In return, The int() is given a parameter of input().
#Lastly, the input() is given the return value of "What is x"/"What is y".
x = int(input("What is x? "))
y = int(input("What is y? "))


# "elif" is a concatanated form of "else if". "elif" can be used to consalidate repititive code, which in
#return enables the programmer to ask fewer questions.

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")