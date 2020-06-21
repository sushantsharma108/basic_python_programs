# List comprehension with if-else stmts.
nums = list(range(1,11))
new_list = []
# Now we want that if odd no. comes in our list then it should become negative number & if even no. comes then it should 
# become number * 2.
# [-1,4,-3,8...] 
for i in nums:
    if i%2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)
# THE ABOVE DESCRIBED METHOD IS COVENTIONAL METHOD TO THIS PROGRAM.

# THE BELOW METHOD IS USED WITH LIST COMPREHENSION FOR THE PROGRAM.
new_list2 = [i*2 if(i%2==0) else -i for i in nums]
print(new_list2)