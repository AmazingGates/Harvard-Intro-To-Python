# In this section we will be learning about "libraries" and their subsections. "libraries" are of codes that 
#other people have written that you can use in your own code, or they can be "libraries" that you have
#written in the past.
# "libraries" are usually run through "modules". A module is just a library with added functions and other
#features bulit into it. The purpose of "libraries" and "modules" is to encourage the reuseability of
#code.
# "random" is another module that comes with "libraries". "random" helps implement randomness in our code.
# "import" is another key word we will learn about. the "import" helps import the content and functions 
#of a "module" so that we may have access to and use them.
# In the example below, we will be using an "import" to import a "random" "module" by creating a "heads 
#or tails program".
import random

coin = random.choice(["heads", "tails"])
print(coin)

# Here we will be learing about a "from". We use the "from" when we are getting functions from a module.
# A "from" helps pick and choose which functions we want from the modules. It can be written like in the 
#example below.
from random import choice

coin = choice(["heads", "tails"])


# Here we are going to be learning about the "random.randint(a, b)", which gives us the ability to get back
#a random integer/number.
import random

number = random.randint(1, 10)
print(number)


# Here we going to go over a "random.shuffle(x)". A "random.shuffle(x)" takes in a list of values and
#shuffles them up.
import random

cards = ["Ranya", "Alia", "Brian"]
random.shuffle(cards)
for card in cards:
    print(card)


# Here, we will be learning about the "statistics" library. This "statistics" library gives us access to functions 
#like "calculations" and "means" and "probabilities" and "medians" and "modes"
# In the example below we first use the "mean" function. A "mean" gives us the average between a list of numbers.
import statistics

print(statistics.mean([100, 90, 100]))


# Here we will be going over "command-line arguments". "command-line arguments" allows to provide input values 
#at the command-line.
# In the example below is what the code would look like and we will be using a "sys" "module".
# "sys" is a "module" that gives us access to commands typed at the command-line.
# "sys.argv" is a list of all the words the user typed in after the prompt, before they hit enter.
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Please enter your name after you type .py")


# In the example below, we are going to use a "sys.exit". When a "sys.exit" is run, it exits the code
#then and there. We will be using the "sys.exit" in a "for loop"
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])


# In the example below, we are going to going generate names for more than one person like above.
# We will also be using a "slice". A "slice" helps us take a "slice" or subset of a list.
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, Welcome", arg)