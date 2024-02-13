# Ask user for their name
name = input("What's your name? ").strip().title()

# .strip() removes whitespace from str
# .title() Capitalizes user's first and last name

# Split user's name into first name and last name. For example, if I typed out my Whole name when prompted,
# only my first name will get returned. But, if I added the {last} template to the print function, both names
# will still get returned regardless.
first, last = name.split(" ")

# Say hello to user
# The "f" must be added to the print function when template strings are used, as per the example below.
print(f"hello, {first}")