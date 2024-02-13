name = input("What's your name? ")

if name == "Harry":
    print("House Gryffindor")
elif name == "Hermione":
    print("House Gryffindor")
elif name == "Ron":
    print("House Gryffindor")
elif name == "Draco":
    print("House Slytherin")
else:
    print("Who are you?")


# Below is an example of the above code, but simplified by using the "or" syntax. 
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name =="Ron":
    print("House Gryffindor")
elif name == "Draco":
    print("House Slytherin")
else:
    print("Who are you?")

# In this example we will be going over a "match" syntax. The "match" syntax works almost identically to a "switch"
#statement in other programs.
# Lastly, we will be using the "match" syntax on the original code above to show the usefulness of the "match" syntax.
name = input("What's your name? ")

match name:
    case "Harry":
        print("House Gryffindor")
    case "Hermione":
        print("House Gryffundor")
    case "Ron":
        print("House Gryffindor")
    case "Draco":
        print("House Slytherin")
    case _:
        print("Who are you?")


# In the example below, we will be simplifying our "match" syntax code. In the "match" syntax, the vertical bars
#that separate "Harry", "Hermione", and "Ron" work just like the "or" syntax and thus allows us consolidate our
#code and make it tighter and neater.
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("House Gryffindor")
    case "Draco":
        print("House Slytherin")
    case _:
        print("Who are you?")