# In the example below we will be talking about "packages". "packages" are third party libraries we have
#access to.
# One of the locations you can find "packages" is pypi.org.
# "cowsay" is a third party library which gives us access to a function that makes cows speak on your
#screen. To intsall "cowsay" you can run this command in your terminal "pip install cowsay".
# Once you have installed the "cowsay" library, you still have to import its functions by way 
#the example below.
# In the example below we used a "cowsay.trex" version of the function. It does the same exact thing,
#byt instead of a cow greeting you, you get a Trex.
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])