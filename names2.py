# In this section, we will be going over the steps to use a "csv" (comma separated value).
# "csv"s help us store multiple pieces of information that are related in the same file.
# To get return our values separated, we will be using a ".split()". Example (".split(",")")
with open("family.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is {row[1]}")  # {row[0]} = "key", {row[1]} = "value".


# In this example, we will be writing the same code as above but in a "for loop" and ".sorted()" version.
family = []

with open("family.csv") as file:
    for line in file:
        member, status = line.strip().split(",")
        family.append(f"{member} is {status}")

for name in sorted(family):
    print(name)


# In this example we will be working with the same code but we will be using "dict/{}" to perform a different version.
# We will also be sorting the return values using a ".sorted()"
# We also used a "list/[]" to wrap our code so we could iterrate over it with a "for loop".
# In order to sort a "dict/{}" we have to ccreate a "function()". This way we can pass our created "function()"
#as a parameter to the ".sorted()" to successfully sort our "dict/{}". Examples below
# Also, when we pass our created "function()" into the ".sorted()", we don't have to manually call our 
#created function. Once the ".sorted()" is run, it will automatically run our created function also. 
family = []

with open("family.csv") as file:
    for line in file:
        member, status = line.strip().split(",")
        name = {"member": member, "status": status}
        family.append(name)


def get_name(name):
    return name["member"]

for name in sorted(family, key=get_name):
    print(f"{name['member']} is {name['status']}")


# In this section we will be going over the "csv" "module". Yes, there is a "module" named "csv" that is 
#separate from the "csv.file" we created.
# The "csv" "module" gives us access to a function called "reader()". This functions main purpose is to
#read the "csv.file" we created, then we no longer have to write the details of "csv.file" into the code.
# In the example below, we will be writing the same code as above, but this time we will be using the
#"reader()" in our code.
# First me must start our code by importing the "csv" "module".
import csv 

family = []

with open("family.csv") as file:
    reader = csv.reader(file)
    for member, status in reader:
        family.append({"member": member, "status": status})

for name in sorted(family, key=lambda name: name["member"]):
    print(f"{name['member']} is from {name['status']}")

    
# In this example we will be using a "DictReader()". A "DictReader()" allows us to iterate over the whole file,
#top to bottom and load in each line of text, not as a list of columns, but as a dictionary of columns. 
import csv 

family = []

with open("family.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        family.append({"member": row["member"], "status": row["status"]})

for name in sorted(family, key=lambda name: name["member"]):
    print(f"{name['member']} is from {name['status']}")