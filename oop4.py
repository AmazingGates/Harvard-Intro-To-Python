# In this section we will be playing around with data types to get a better feel for them.
# When we print he the type of a value, we should be able to see its class. ("print(type())")
print(type({}))


# In this example we will be going over a "class method" and its functions. ("@classmethod")
# We must import random to use its functions in our code.
# Also, we will go over the steps to assign a name to a random house, using the "random.choice"
import random
class Hat:
    def __init__(self):
      self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slyterin"]

    
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")


# In the example below we will be cleaning up the code above.
# We must import random to use its functions in our code.
# We are also going to use a "@classmethod"
import random
class Hat:

        
    houses = houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slyterin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")


# In this section we will be going over an "inheritance". With an "inheritance" we are able to design our
#classes in heirarchy that allows one class to borrow attributes ("variables" "methods") from another class if 
#they all have those in common.
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against The Dark Arts")