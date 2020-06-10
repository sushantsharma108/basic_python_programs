# ELSE stmt : Syntax:- 
# else:
#   stmt1
#   stmt2....

age = int(input("Enter Your Age: "))
if age >= 18:                       # Indentation is must after condition & colon is also must.
    print("You Can Play This Game. ")

else:                                # else is optional to write but else always comes after if not alone.
    print("You Can't Play This Game. ")         # if stmt. can be alone but else doesn't.
    