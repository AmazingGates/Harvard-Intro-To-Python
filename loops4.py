# In this example we are going to learn how to link more than one piece of information to your key at a time.
# In the example below we are able to store a lot more infortion by storing multiple "dict/{}"s with multiple
# "Keys" and multiple "Values" inside of a list.
# When we run the "print()" and only pass in the argument of "student", "(print(student))" the code shoulde return a 
#list of your dictionaries written exactly as you typed the, brackets and all.
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slyterin", "patronus": None}
]

for student in students:
    print(student)



# In the example below we going to run the same excact code as above be we are going to index into our 
#variables ("student") location and return the "Key"s "Value", which would be the students name "(Hermione)"
# To do this we run the "print()" and pass into it with our Variable "student", ("print(student)").
# Then we must index into our Variables "student" location with a "Key" to bring back its "Value" 
#("print(student["name"])")
# This will bring the "Value"/"Hermione" for the "Key"/"name", and be returned like this (Hermione).
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slyterin", "patronus": None}
]

for student in students:
    print(student["name"])


# In the code below we are going to do the same exact thing as the code above but this time we are going to
#bring back multiple "Value"s from multiple "Key"s.
# we can do this be indexing into multiole "Key"s at one time. (print(student["name"], student["house"],
# student["patronus"])
#We run like this, the code should return (Hermione Gryffindor Otter)
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slyterin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"])