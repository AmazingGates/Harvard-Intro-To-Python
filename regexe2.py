# In this example we will be going over the process of extracting information in order to answer some question.
# We will be using a ".replace()". This function takes two parameters. The first is the value you want replaced
#and the second is the one you wabt to replace it with.
#(We are only using the "https://twitter.com/") as an example of a value being replaced out. 
#Any value can be replaced out
import re

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"USERNAME: {username}")


# In this example below We will be using a "re.sub()", which takes 3 arguments. 
#(We are only using the "https://twitter.com/") as an example of a value being subbed out. 
#Any value can be subbed out
import re

url = input("URL: ")

re.sub(r"^(https?://)?(www\.)twitter\.com/", "", url)
print(f"USERNAME: {username}")


# In the example below we will be doing the same thing as above, but instead of "re.sub()" 
#we will be using a ".search()"
# We also used the ":=" operator.
import re

url = input("URL: ").strip()

if matches := re.search(r"https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"USERNAME:", matches.group(1))