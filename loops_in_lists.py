# # looping in lists.
# # for loop in list:
# fruits = ['grapes','kiwi','orange','papaya']
# for fruit in fruits:    #fruit is a counter variable.
#     print(fruit)

# # While loop in list:
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# # looping in lists using enumerate:
# supplies = ['pens','staplers','carbons','high']
# for i, supply in enumerate(supplies):
#     print(f"Index {i} in supplies is: {supply}")

# Looping through mulltiple lists using "zip()":
name = ['yash','sushant','somdutt']
age = [17,22,45]
for n,a in zip(name,age):  # This line can bind up two lists so that we can do looping through 2 lists.
    print(f"{n} is {a} years old.")