# In this section we will be modifing a code to take command line arguments to get input from the user.
# Using this method, after we type in the python file.py name "python EtCetera4.py" we will enter a "-n",
#which represents the number of times we the value run, then we input a number after the "-n" as the
#indicator of number of times to run. ("python EtCetera4.py -n 6"). That command line input is just an example 
#we are using here. In practice, it will take the name of the file you are using at the time.
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for i in range(n):
        print("meow")
else:
    print("usage: meows.py")


# In this section we will be going over the "argparse" library. This library allows us to pass in 
#configuration options at the command line.
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for i in range(int(args.n)):
    print("meow")