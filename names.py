# In this section we will be using "File I/O". "File I/O" helps us read information from and write send information 
#to files themselves. This helps us to save data persistently.
# In the example below, we use an ".append()", which helps us append functions with values by passing in 
#the return value (".append(input("What is your name"))")
# We also use ".sorted()" to sort the returned values before printing them. (".sorted(names)")
names = []

for i in range(3):
    names.append(input("What is your name? "))

for name in sorted(names):
    print(f"hello, {name}")


# In the example below, we will be going over the methods to save the information we generate with our code
#by saving it to a "FileI/O".
# We can acheive this by using a "open()". The "open()" opens a file for us so that we can read information 
#from it, or write information to it.
# We also use a ".write()". This function helps write values to the persistent file we created.
# Lastly we use a ".close()". This function will close and save the file once we are done with it.
# To see the file that we created and saved the information to ("name.txt"), we run our program regularly
#enter a name. Once the program has run, in the terminal, write ("code name.txt"), then run that command.
# A new window should open in your tabs with the file ("name.txt") that has the stored names inside it.
# Here we passed in the "a" as the second argument we our ".open()". It stands for append.
# This will help us return ALL the names we enter as return values, instead of overwriting the old with the new.
# We also added a "\n" (new line) command in our ".write()" to make sure the values ("names") are returned
#stacked on top of eachother in a list fashion, instead of crammed side by side. (".write(f"{name}\n")").
# Also in the example below, we commented out the ".close()" to try a more "pythonic" approach at closing
#the file using the "with" keyword, which allows us to specify to the code that we want it to open AND 
#Automatically close a file.
name = input("What is your name? ")

with open("names.txt", "a") as file: 
    file.write(f"{name}\n")
#file.close()