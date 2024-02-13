# In this example we will build a three block column from mario bros, game.
for i in range(3):
    print("#")


# In the example below, we will be solving the same problem, but we will use a "function()" instead.
def main():
    print_column(3)


def print_column(height):
    for i in range(height):
        print("#")


#main()


# In the example below, we will be using a "function()" again to solve almost the same problem, except this time,
#we want the row blocks to be horizontal(laying down) and not vertical(standing up)
def main():
    print_row(6)


def print_row(width):
        print("#" * width)


main()


# In the example below we will be printing out square of "#". It should be 3 blocks high, and 3 blocks wide.
def main():
     print_square(3)


def print_square(size):
     for i in range(size):
          print("#" * size)


main()