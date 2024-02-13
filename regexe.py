# In this section we will be learning abour  the "regexe". The "regexe" is mostly just a tool that we can use to 
#define patterns in our code to help us compare to data we receive from someone else.
# In the example below we are going over the process of using the "regexe".
# To access the "regexe" tools we will be using the "re" "module".
# In the "re" "module" ("." = any character except a newline) ("*" = 0 or more repititions) ("+" = 1 or more repititions)
#("?" = 0 or 1 repititions) ("{m}" = m repititions (This expression lets us specify excalty how many repititions 
#we want by manually typing in a number) ("{m,n}" = m-n repititions (This expression lets us specify the range we want
#our repitition to be. "{1-100}") ("^" = matches the start of the string) ("$" = matches the end of the string 
#or just before the newline at the end of the string) ("[]" = set of characters (lets us look for certain 
#characters specifically) ("[^]" complementing set (means you CANNOT match any of these characters)) 
#("\w" = any alphanumeric symbol or underscore) ("\W" = not an alphanumerical symbol or underscore)
#("\d" = decimal digit) ("\D" = not a decimal) ("\s" = whitespacecharacters) ("\S" = not whitespace characters)
#("A|B" = either A or B (Means A has to match or B has to match)) ("..." = a group (means we can group things together)
#("?:..." = non-capturing version))
#See an example of these expressions being used below in the "re.serach()"
# Also, we used an "r" string (raw string) in the "re.serach()". The "r" string tells the code to disregard the
#backslash "\" and not read it in the normal way. Now we can use the backslash "\" safely for negating the 
#"." in ".com", treating it as a regular dot/period.
# "re.IGNORECASE", "re.MULTILINE", "re.DOTALL" are "flags" of "re.search()". They get passed like variables
#into the function as arguments.
# "re.IGNORECASE" ignores the case of the input and reads everything as lowercase.
# "re.MULTILINE" is used when we want read multi lines of input.
# "re.DOTALL" lets us configure the "." expression how we want.
# "re.match()" = will automatically start matching at the beginninf of the string
# "re.fullmatch()" = will automatically start matchubg at the beginning and the end.
import re

email = input("What is your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")