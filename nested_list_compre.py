# List comprehension in nested list
# In this program we want to generate a nested list using List comprehension
example = [[1,2,3],[1,2,3],[1,2,3]]
nested_comp = [[i for i in range(1,4)] for j in range(1,4)]
print(nested_comp)

# In the line no. 4 we have appended a list using list comprehension and that 
# list is also created with the help of list comprehension means the first written
# part in square brackets[]. 