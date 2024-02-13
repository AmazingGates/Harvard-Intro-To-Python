# Python Functions
# Functions must first be defined with a (def) before they can be called.
# In thhe example below, the hello() takes a parameter of to, which looks like this (def hello(to)).
# Also, the parameter of (to) can take an assignment, which looks like this (def hello(to="World")). With this,
# the default value will be "hello world", in the event that the user doesn't call "hello()" with an argument,
# which looks like this "hello(name)". (Example of calling "hello()" without an argument.) (Example of calling 
# "hello(name)" with an argument.)


def hello(to="World"):
    print("hello,", to)


name = input("What's your name? ")
hello(name)