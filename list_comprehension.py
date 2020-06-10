# List Comprehension:
# with the help of list comp. we can create a list in one line.
# Creating a list of Squares of no. from 1 to 10.
squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)
# The above method is used to create a list by simple method.

# Now we'll create a list using List Comprehension.
squares1 = [i*i for i in range(1,11)] # This is a list which you have to define using [].
print(squares1)
# This method reduces the four lines of code into a SINGLE LINE.

negative_list = []
for i in range(-1,-11,-1):
    negative_list.append(i+1)
print(negative_list)

negative_list2 = [i for i in range(-1,-11,-1)]
print(negative_list2)

name_list = ['Sushant','Tushar','Rajeev','Pradyumn']
new_list = []
# for name in name_list:
#     letters_list.append(name[0])
# print(letters_list)

new_list = [name[0] for name in name_list]  # "data_to_be_append for counter in list_name"
print(name_list)
