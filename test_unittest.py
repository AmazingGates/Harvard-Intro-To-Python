# Here we will write the "unit test" code that we will use to test our "unit test" program.
# In the example below, we start the "unit test"code by importing "square" from the "unittest" program.
# In this example we will be using the "assert" keyword. This keyword will let us proclaim that something is true.
# We will also use a "try" and "except" for any errors that may arise. This is will make the errors easier to read 
#and troubleshoot.
# To see an example of the "test_unittest" in action, go to "unittest" and change "n * n", to "n + n", then come
#back and run the "python test_unittest.py"
from unittest import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
         print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
         print("3 squared was not 9")

    
if __name__ == "__main__":
        main()
