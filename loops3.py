# In this example we will be using Dictionaries/"dict/{}"syntax.
# "dict" are a datastructure that allows you to associate one value with another. Meaning that in Dictionaries, their
#words and thier meanings. In "dict", their are Keys and Values.
# To complete the process we must use the "print()" and pass the name of the "dict/{}" ("print(family)").
# Lastly we index into which "Key and Value" pair we want by using only the pairs "key" name (print(family["Alia"]))
# For the results, see the example below.
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

print(family["Alia"])

# In the code below we will be coding the same code as above, only this time we will be usinh a "loop"
# Writing the code like this helps interate over the family "dict/{}" and only returns its keys, "Key" ("Alia",
# "Brian", "Ranya")
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

for i in family:
    print(i)

# In the code below we will be returning both the "Key" and its "Value" by indexing into the pair during the "print()".
#("print(i, family[i])")
#To see this action run the code below.
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

for i in family:
    print(i, family[i], sep=", ") # "sep=''" is used to add comas to the return value


#Using the ".update()", we can add items or change existing items in our dictionaries. Example below
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

family.update({"Bam Bam": "Brian and Alias Son"})
family.update({"Ranya": "Will have Brians Baby Also"})
print(family)


# In the example below, we will be using a ".pop()". Using this ".pop()" we can remove a "key" "value" pair from 
#our "dict{}" by passing in the "key" of the pair to the ".pop()". See example below.
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

family.pop("Alia")
print(family)


# In the example below we will be using a ".popitem()". The ".popitem()" works just like a ".pop()", but instead
#it removes the last "key" "value" pair in your "dict{}", and it doesn't need to be passed any parameters to work.
# Example below
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

family.popitem()
print(family)


# In the example below, we will be using a ".clear()". This ".clear()" lets us clear our entire "dict{}".
#Example below
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

family.clear()
print(family)


# In the example below we will be using a ".keys()". The ".keys()" allows us to return only the "key"
#of the "key "value pair. In the Example below we will use a variable to help us with this ".keys()".
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

family.update({"Bam Bam": "Brian and Alias Son"})
family.update({"Ranya": "Will have Brians Baby Also"})
keys = family.keys()
print(keys)

# In the example below we will be doing the same as the above code, but instead we will be returning only the
#"value", using the ".values()"
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

family.update({"Bam Bam": "Brian and Alias Son"})
family.update({"Ranya": "Will have Brians Baby Also"})
values = family.values()
print(values)


# In this example we will returning only the "key"s again, but this time we will be using a "for loop".
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

family.update({"Bam Bam": "Brian and Alias Son"})
family.update({"Ranya": "Will have Brians Baby Also"})
keys = family.keys()

for key in family.keys():
    print(key)


# In this example we will only be returning the "value"s again, but this time we will be using a "for loop".
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

family.update({"Bam Bam": "Brian and Alias Son"})
family.update({"Ranya": "Will have Brians Baby Also"})
values = family.values()

for value in family.values():
    print(value)


# Lastly, in the example below we will be using an ".items()". This will return both the "key" and "value" 
#of our "dict{}" in an easier to read format. Again, we will be using a "for loop" to help us with that.
family = {"Alia": "Wife", "Brian": "Husband", "Ranya": "Sister In-Law"}

family.update({"Bam Bam": "Brian and Alias Son"})
family.update({"Ranya": "Will have Brians Baby Also"})
items = family.items()
for key, value in family.items():
    print(f"{key}: {value}")