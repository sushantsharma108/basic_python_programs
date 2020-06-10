# Lists is the inbuilt data structure. It is an ordered collection of items.
# Lists can store any type of data whether it is integer, floating point, strings, etc....
#  lists are denoted by square brackets.[]
numbers = [1,2,3,4,5,6]
print(numbers)

words = ["Sushant","Sharma",'Yash','Kumar','Vats']
print(words)

mixed_list = [1,2,7,8,'Sushant','Yash',2.345, None]     #None means nothing in Python Not zero.
print(mixed_list)

# If we want to acces any element of a list then I can apply the indexing.
print(words[2])
print(numbers[2])
print(words[0:3])       # We can use slicing in lists as we used in strings.

#  Most Important thing in the lists is, you must knnow to store,access & retrieve the data in a list.

# To change any data in a list.
mixed_list[1] = "Nandini"
print(mixed_list)
mixed_list[2:] = ["Seven"]  # If you will assign the string then string will spread apart
print(mixed_list)            #but if you will assign the list then list will spread apart.