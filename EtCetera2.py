# In this section we will be going over "constants". "constants" are variables that are permanent.
# Altough Python doesn't really have "contants" like other languages, it still has ways of alerting
#users, other programmers, or even yourself to leave certain "variables" alone. 
# The method Python programmers use to indicate that a "variable" is "global" and shouldn't be changed
#is by writing the "variable" in all capital letters. ("VARIABLE")
class Cat:
    MEOWS = 3

    def meow(self):
        for i in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()