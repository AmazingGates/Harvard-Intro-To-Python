# In this section we will be going over "Object-Oriented Programming", which is helpful to us when our 
#codes become larger.
# In the example below we will be going over the process of returning multiple values at once. This process
#is called a "tuple". ("return name, house")
# "tuple"s are inmutable, meaning we can still index into it, but we can't change what's inside them. 
#("print(f"{student[0]} from {stundent[1]})")
# On a side note "tuple"s use parentheses(name, house), or no wraping "name, house", and list use [name, house].
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__=="__main__":
    main()


# In the example below, we will be running the same code as above, but this time we will be using a "dict/{}"
# Also in the example below we will be going over the process of correcting a users input using an 
#"if statement".
# "list/[]" like "dict/{}"s are mutable, meaning you can change what's inside them.
def main():
    student = get_student()
    if student["name"] == "Alia":
        student["house"] = "Gates"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__=="__main__":
    main()