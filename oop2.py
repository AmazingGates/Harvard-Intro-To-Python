# In this section we will be going over the process of creating our own "method"s.
# The "method" we created is the "def charm()" "method". This "method", like many others should always
#take at least one parameter. ("def charm(self)").
class Students:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slyterin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Stag"
            case "Otter":
                return "Otter"
            case "Jack Russell Terrier":
                return "Jack Russell Terrier"
            case _:
                return "Flaming Wand"



def main():
    student = get_student()
    if student.name == "Alia":
        student.house = "Gates"
    print("Expecto Patronum")
    print(student.charm())
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Students(name, house, patronus)


if __name__=="__main__":
    main()