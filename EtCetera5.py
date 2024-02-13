# In this section we will be going over "unpacking". "unpacking" helps us unpack single values and split 
#them into two separate variables.
# To unpack a value we initialize it by putting a "*" before the variable. ("*coins")
# Using the "*coins" method us helps take a single sequence, "list/[]" or "dict/{}" and unpack all the 
#of the individual arguments inside it.
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "knuts")


# In the example below, we will be working the same code as above, but this time we will be
#passing in the names of the values instead of the numbers.
# Also, we will be using a coins dicitionary "{}" instead of a list "[]"
# When "unpacking" a dicitionary "{}" we have to use two "**"s before our variable ("**coins").
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "knuts")