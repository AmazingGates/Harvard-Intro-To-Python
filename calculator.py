x = float(input("What is X? "))
y = float(input("What is Y? "))

# int() convert strings into whole numbers
# float() handles decimals numbers
# round() rounds to the nearest int

# By adding a comma and passing a second parameter of (2) we can limit how many digits we return after the (.)
z = round(x / y, 2)

# Arrow up / These two can work perfectly fine together or apart to gain the same outcome / Arrow down.

# Using the (.2f) lets us limit the digits returned after the (.) to 2.
print(f"{z:.2f}")