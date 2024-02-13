def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="World"):
    print("hello,", to)


main()

# In the example above, main() is first defined (def main()).
# Inside the def main() function, "name" is assigned to an input().
# The input() takes a parameter, (input("What's your name? ").)
# Also inside the def main() function, the hello() function is given an argument of "name", (hello(name).)
# Next, the hello() is defined and also given an argument of "to", and "to" is then given an assignment of "world"
# Which looks like this (def hello(to="World"):)
# Inside the defined hello() function, (def hello(to="World"):), the print() function is called with two arguements,
# Which looks like this ( print("hello,", to).)
# Lastly, the main() function is called, which  prompts the computer to run the program starting from the top.