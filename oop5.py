# In this section we will be going over "operator overloading". This allows us to take common symbols and implement 
#our own definitions. Example of common symbols ("+", "=", "x", "/")
# We will also be using a "__str__" to tell vault to print our vaule as a"string"
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles= sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)


# In the example below we will be working the same code as above, but this time we will be using
#"operator overloading" to add our two "Vault"s ("potter + weasley") together.
# The process we will use to perform this action will involve using the "object.__add__(self,other)" method.
# In this "method", "self" is assigned to whatever object is on the left of the "+" sign, while "other"
#is assigned to whatever object is on the right side of the "+" sign.
# Basically, in this example, we "taught" our code how to add two Vaults together.
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles= sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)