# we use enumerate function with for loop to track position of  our item in iterable.

# How can we do this without enumerate function.
names = ['sushant','sharma','shubham']
# pos = 0
# for i in names:
#     print(f"{pos}: {i}")
#     pos += 1

# with enumerate function.
for pos,name in enumerate(names):
    print(f"{pos}-->{name}")  
# Now we can use the above code for tracking the position of our item in iterable using enum. func.

# Func. which will take 2 arguments, one a list of strings and a string whose position you have to 
# find in the list using enum. func.

def find(list1,string):
    for pos1,str2 in enumerate(list1):
        if str2 == string:
            return pos1
    return -1
str2 = input()
print(find(names,str2))
