# In this example, we are going to use the modulas symbol "%". The modulas symbol "%" is used to calculate the remainder
#of one number divided by another.
x = int(input("What is x? "))

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")


# In the example below, we are going to turn the code into a function(), which we can call on whenever we want.
def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()