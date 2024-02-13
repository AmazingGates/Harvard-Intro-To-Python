def main():
    x = int(input("What is x? "))
    print("x squared is", square (x))


def square(n):
    return n * n


main()

# In the example above, main() is defined. Next, x is declared and assigned an input with a value of ("What's x? ").
# Next, print() is given two parameters ("x squared is", square (x)). In this example, the second parameter of print(),
# is calling the value of "x" to be squared.
# Next, the squared() is defined and given an argument of (n).
# Next, a "return" is initiated to return the value of the "squared (x)" by multiplying "n * n". The returned value of n * n 
# will be the answer to the question "What is x? ".
# Finally, to run the program (starting from the top), the main() is called.
