# In this section we will be going over "classes". "classes" are kinds of blueprints for pieces of data, or
#a mold that we can define or create and give a name. This helps us get back data exactly how we want when we use 
#"classes".
# In essence, "classes let us invent our own data types and give them names."
#  When we use classes, we are creating "objects". "objects" is just a "class" in action.
# We will be using the keyword "class" that gives us access to "classes" functions and features.
# Also in the example below, the "if statement" that we are using is hard coding "Alias" house name to "Gates", 
#regardless of what the user inputs. Try it in the example below.
# Classes "class" come with "methods" that allow us to determine the "class" function and features.
# We will also be using the "__init__" to intialize the contents of "objects" from a "class".
# The "__init__" is an "instance method"
# The "self" parameter is used to give us access to the "object" currently created.
# We will also be using the keyword "raise" in the code below. We use the "raise"keyword when we want to
#raise our own exceptions and alert the programmer of an error.
class Students:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slyterin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house




def main():
    student = get_student()
    if student.name == "Alia":
        student.house = "Gates"
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Students(name, house)


if __name__=="__main__":
    main()


# In this example we will be going over the method "__str__". This method allows us to have our function 
#automatically called anytime another function wants to see our object as string.
class Students:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slyterin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Students(name, house)

if __name__=="__main__":
    main()


# In this example we will be cleaning up the code above. When "class" is passed as an argument, it gets
#written like this (get(cls)).
class Students:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
@classmethod
def get(cls):
    name = input("Name: ")
    house = input("Housee: ")
    return cls(name, house)



def main():
    student = Students.get()
    print(student)


if __name__=="__main__":
    main()