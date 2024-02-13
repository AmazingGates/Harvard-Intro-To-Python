# Here, "score" has been declared and assigned to an int(). In return, The int() is given a parameter of input().
#Lastly, the input() is given the return value of "Score: ".
score = int(input("Score: "))



# The "and" question is used like the "or" question. Meaning they can help simplify code by asking fewer questions 
#by joining questions together. The difference is that unlike the "or", where you choose one condition or 
#the other before it can be true or false, the "and" must have all conditions met before the statement can be
#true or false.
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Failed, Please Study.")



# In the example below, both the "or" and the "and" questions have been removed and the previous code is written in
#its most simpliest form. This is just an example of making code neater and more reable, but it does the same exact
#thing as the previuous code above.
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Failed, Please Study.")