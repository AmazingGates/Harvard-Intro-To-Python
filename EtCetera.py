# In this section we will be going over the "Et Cetera" of Python. We went over a lot during this course
#and these are just a few things that we didn't get to go over.
# "set()" is a data type that allows us to filter out duplicates. Example below.
# To add values in a "set()" we use the ".add()". We use the ".append()" when we are working with "list/[]"
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slyterin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)