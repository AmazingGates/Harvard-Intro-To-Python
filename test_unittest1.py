# In this section we will be going over the "pytest" tool. "pytest" is a third party program that we can download 
#and install. "pytest" will automatically test our code for us, as long as we write the "unit test" ourself.
# "pytest" helps us cut back on the length of our "unit test".
from unittest import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# Did not get "pytest" to work. Use the orginal test_unittest.py because it worked. Try "pytest" at a later date.