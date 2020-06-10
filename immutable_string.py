#  Strings are immutable means we can't change the value of any char. of the string.
name = "Sushant"
print(name[1])

# name[1] = 'T' --> It gives the error since it tries to change the value of a string.
print(name.replace("u","T"))  # It replaces the value in original string.

# But if you define a new variable & store the result of replace method then
# it can't change original string but make a  new string & operate on it.

name.replace("u","T")   #This operation is not feasible.
print(name)

