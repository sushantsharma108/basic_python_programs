# common methods to delete the data from the lists.
fruits = ['banana','apple','orange','grapes','kiwi','pineapple']
# pop() method to delete data fromm the list. By default it deletes the last element of the list.
fruits.pop() # By default, it will delete last element
print(fruits)

# fruits.pop(2)  #deletes element at the 2nd index.
# print(fruits)

# delete stmt or delete operator: both are same, it works as same as pop() method.
del fruits[2]
print(fruits)

# remove():if you don't know that on which position the element is placed, then you can delete it by passing an arg.
fruits.remove('kiwi')
print(fruits)

# if there are two same elements in the list,and you apply remove() method then it removes the first element of same name.
fruits = ['banana','apple','orange','grapes','kiwi','pineapple','orange']
fruits.remove('orange')
print(fruits)