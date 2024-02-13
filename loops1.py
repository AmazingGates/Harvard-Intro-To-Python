# In the example below we will be going over "for" loops and "list []". 
# "for" loops allow us to itterate over a "list []" of items.
# "list" are another type of data. It gives
#us the opportunity to contain multiple values all in the same place/variable.
for i in [0, 1, 2]:
    print("Brian and Alia Gates")


# In the example below, we will be simplifying the above code to be neater and more efficient. For this process, we 
#will be using a "range()". The "range()" returns to us a range of values. The "range()" expects at least 1 arguement. 
#That arguement will represent the number of values you want returned. Example (range(3)).
# Using the "range()", we can manually tell the code how many values we want returned without having to make a 
#"list []", which saves us from manually having to type out each value in a large "list []".
for i in range(3):
    print("Brian and Alia")  


# In the example below, we will be looking a further at the "list" syntax. 
# In the example below, we are able to access each person separately by referencing there location in the "list".
students = ["Harry", "Hermione", "Ron"]

print(students[0])
print(students[1])
print(students[2])

# In the example below we will be using a "loop" to simplify the code above.
students = ["Harry", "Hermione", "Ron"]

for student in students:
    print(student)


# In the example below we will using the same exact code as the code above. The only difference is instead indexing the 
#string name ("Harry"), we will be indexing string location ("0"). To do this we will be using a python function
#"len()". The "len()" helps get the length of the list (meaning it can count how many items are in "list/[]").
# To use the "leng()", it gets passed as an argument to the "range()". ("range(len())"). Lastly, the name of
#the "list/[]" ("family"), gets passed to the "len()" to tell the code iterate/count the length of the list.
#("range(len(family))")
# To have the code return to us the length of the "list/[]" (by way of location occupation counter "Brian" = "[0]")
#we must use the "print()" and pass to it the variable that is initialized ("i") as the counter ("print(i)") for 
#"range()" To see the entire thing action, see the code below.
family = ["Brian", "Alia", "Ranya"]

for i in range(len(family)):
    print(i)

