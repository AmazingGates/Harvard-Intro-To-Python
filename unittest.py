# In this section we will be talking about "Unit Test". A "unit test" gives us the ability to test our own code. 
# We do this by writing the "unit test" code that we will use to test our code. Example below
def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()