# In this section we will be going over "type hints". We use "type hints" to tell Python what type of 
#classification we want a "variable" to have.
# In the example below we be using the "type hint", "mypy".
# The "mypy" program tells us if our code is adherring to our own "type hints"
def meow(n: int):
    for i in range(n):
        print("meow")


number: int  = int(input("Number: "))
meow(number)


# In this section we we will be going over "docstrings". "docstrings" standardize how we should document our functions.
# In the example below we will be going over the process.
# In the example below, everything in between the triple quotes (""") is our documentation about our code to ourselves
#and other programers. Although it has no real function, it can, and it is useful to document your code this way
#when working team projects and large scale projects.
def meow(n: int) -> str:
    """"
    Meow n times.

    :param n: Number of times meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n 


number: int  = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")