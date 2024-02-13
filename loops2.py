# In the example below, we will discuss how to get a user to give a number, instead of hard coding one with the range().
# Also, we will use for the first time a Python keyword ("Continue"), which simply tells the code to stay within the 
#loop while the conditions are True.
# Also we will be using another Python keyword, a ("break"). "break" is used to break you out of your most recently 
#begun loop.

while True:
    n = int(input("What is n? "))
    if n < 4:
       continue
    else:
       break


# In the code below, we will be simplifying the code above. Also, for the example below, we brought back the range()
while True:
    n = int(input("What is n? "))
    if n > 0:
        break

for i in range(n):
    print("Brian and Alia Gates")


# In the example below, we will be working on the same code, but this time we will be using a function() to
#complete it.
def main():
    number = get_number()
    Gates(3)


def get_number():
    while True:
        n = int(input("What Is n? "))
        if n > 0:
            return n


def Gates(n):
    for _ in range(n):
        print("Alia Gates ")


main()