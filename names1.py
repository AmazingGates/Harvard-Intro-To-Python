# In this example we will go over the steps to actually access the values(names) in the file we created.
# This time, we will be passing in an "r" as our second argument in the ".open()". (".open("names.txt", "r")").
# This will enable us to read existing/created files.
# We will also be using a "readlines()". This function reads all the lines and returns them to me as a list.
# Lastly we use an ".rstrip()" with line as the second argument in our "print()". ("line.rstrip()").
# This ensures that any extra spacing or gapping gets stripped away and leaves us with a nice neat list.
# Also, we will use a ".sorted()" to return the values(names) in a sorted order. 
# We used a "list/[]" to contain our values. This helped us to iterrate over the list and return the sorted
#values(names)
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")


# In the example below, we will be running the same exact code from above, but this time we will return the "reveresed"
#sorted value(name) list.
# We will do this by passing a second argument to the ".sorted()". We will be passing in a "reverse=True" argument. 
# It should look like this ".sorted(names, reverse=True)"
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")