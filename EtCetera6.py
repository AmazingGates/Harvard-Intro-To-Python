# In this section we will be going over "*args", and the "**kwargs" again. Not only are these two symbols used for 
#unpacking, but they are also used as a visual indicator in Python when a function might take a variable 
#number of arguments. Meaning that a function doesn't have to take 3 arguments. It can take 0, or 1, 0r 2 etc etc...
# In the example below, we go over the process of using the "*args" and "**kwargs". ("args" and "kwags") are just
#place holders that the Python community accepts with the "*" and "**", even though other place holders will work.
# Also in Python, the "*args" is always on the left as the "Positional", and "**kwargs" are on the right as the
#"Named" ("f(*args, **kwargs)").
# In the example below, we used the "*args" and "**kwargs" to let the code know that we will be passing any of 
#arguments to the f()'s "Positional/*args" and "Named/**kwargs" place holders. ("f(*args, **kwargs)").
def f(*args, **kwargs):
    print("Named", kwargs)


f(galleon=100, sickles=50, knuts=25)


# In this section we will be talking about the "map()". "map()" is a function that allows us to apply some function to 
#every element of a sequence, like a "list/[]", or a "dict/{}"
# In the example below, we will be coding a program called yell. Where we want the computer to YELL back all 
#of its responses.
# The opposite is also possible by using the ".lower()".
def main():
    yell("Long Live Gates")


def yell(phrase):
    print(phrase.upper())


if __name__=="__main__":
    main()

# In this section we will be coding the same yell program as above, but this time we will be using the 
#"map()" function.
def main():
    yell("this", "is", "cs50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__=="__main__":
    main()
