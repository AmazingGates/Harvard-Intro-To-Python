# We will be learning about "exceptions". "exceptions" refer to problems in your code.
# The first keyword we will learn about is a "try". We can use try to check if anything erroneaus took place within
#your code.
# The second keyword is "exept". "except" allows you to do something else if there is a problem in the code.
try:
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError:
    print("Please Enter A Whole Number")
else:
    print(f"x is {x}")



# In the code below we are going to try a "while True" loop with an "exception" to see what happens.
# The first we did was run the "While True" loop with our code with an "else" and a "break". 
# That means that the "while True" loop will repeatedly run the error message if the user enters anything
#other than whole int/number. 
# In the event that the user does enter a correct int/number, we also installed an "else" statement with a "break"
#to break the loop and complete excecuting the code.
while True:
    try:
        x = int(input("What is x? "))
    except ValueError:
        print("Please Enter A Whole Number")
    else:
        break
        
print(f"x is {x}")


# In the example below, we are going to invent a "function()" that gets an "integer/int()" from a user.
# By creating this "function()" we can get an "integer/int()" from the user any time we like.
# Also, we used a "return" with this code. A "return" has to come written with the "get_int()" code
#when we expect a "value/input" back from the user.
# Also we  create a "def main()" to serve as the main part of our program, and it will be the "main()"
#that we use to call our "get_int()".
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()


# In the example below we will be talking about a "pass". A "pass" lets handle an "exception" but not do anything to it.
# So essentially, we catch but just choose to ignore it.
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            pass
        else:
            return x

main()