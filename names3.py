# In this section we will be going over the process of adding/writing to our "csv.file" directing from our program.
# We will  be using a ".writer()" to help us to write directly to our "family1.csv" file.
# We will also be using a ".writerow()" that will help us write directly to the row we want.
# We pick the rows we want to write to by passing them in as arguments in the ".writerow()"
#("writerow([member, status])").
import csv

member = input("What is your name? ")
status = input("Who are you? ")

with open("family1.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([member, status])


# In this example we will be perfoming the same code as above, but this time we will be using a "DictWriter()"
#to help us acheive this.
# We will also be passing our ".writerow()" a "dict/{}" (".writerow({"member": member, "status": status})")
# Also, we will  pass our ".DictWriter()" a second parameter of "fieldnames=" which will be assigned a "list/[]"
#(".DictWriter(file, firldnames=["member", "status"])")
import csv

member = input("What is your name? ")
status = input("Who are you? ")

with open("family1.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["member", "status"])
    writer.writerow({"member": member, "status": status})