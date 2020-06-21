# More about get() method, two same keys in a dictionary
user = {'name':'Sushant Sharma','age': 22}
# print(user.get('name'))
# print(user.get('names')) This line will print none since there is no key named as 'names' in our dictionary.

# If you don't wanna return 'None' as an output then....
print(user.get('names','Not Found!'))
# This will print "Not Found!" since there is no key named as 'names' in our dictionary.

# Now suppose if there are two same keys in a dictionary with same key name then...
user1 = {'name':'Sushant Sharma','age': 22,'age':28}
print(user1) # The O/P of above line will overwrite the age 22 with 28.
# If there are two same keys in a dictionary then the latest value(right most value) of those keys will overwrite
# the value of previous key.
