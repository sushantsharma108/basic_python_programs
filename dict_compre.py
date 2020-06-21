# Dictionary Comprehension
# square = {1:1,2:4,3:9}
square = {num:num**2 for num in range(1,11)}
print(square)
# In this case, num:num**2 indicates the relationship b/w key and value pair of a dict.

# Now below is a modified code. 
square = {f"Square of {num} is":num**2 for num in range(1,11)}
for key,value in square.items():
    print(f"{key}:{value}")

 