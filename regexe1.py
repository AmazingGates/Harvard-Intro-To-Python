# In this section we will be going over the process of reformatting the users input.
name = input("What is your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}")


# In the example below we will be reformatting the code using the "re.search()"
import re
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"Hello, {name}")


# In the example below we will be using a "walrus/:=" operator to code the same program as above. The ":=" 
#allows us to assign a value right to left and ask a boolean question about it at the same time.
import re
if matches := re.search(r"^(.+), ?(.+)$", name):
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"Hello, {name}")