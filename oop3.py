# In this section we will be going over the "properties()", which are attributes that have defense mechanisms put 
#into place by the programmer to safeguard against other programmers from messing things up. 
#"properties()" are implemented by writting them into code.
# We will also be going over the "decorators" keyword, which are functions that  modify the behavior of other functions.
class Students:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    # This is considered a "Getter". A "Getter" is a function for a class that gets some attribute. The "Getter"
    #always gets one parameter.
    @property
    def house(self):
        return self._house
    

    # This is considered a "Setter". A "Setter" is a function of a class that sets some value. The "Setter"
    #gets two parameters.
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slyterin"]:
            raise ValueError("Invalid House")
        self._house = house



def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Students(name, house)


if __name__=="__main__":
    main()