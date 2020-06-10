# Function to print a reversed list.
# def rev_list(l):
#     return l.reverse()  #this line will not return anything.
# numbers = [1,2,3,4]
# print(rev_list(numbers))

# Reversing List using reverse() method. 
# def rev_list(l):
#     l.reverse()  # This line will reverse the original list.
#     return l       #This line will return the reversed list.
# numbers = [1,2,3,4]
# print(rev_list(numbers))

# # Reversing list with list slicing.

# def rev_list(l):  # This line will reverse the original list.
#     return l[::-1]       #This line will return the reversed list.
# numbers = [1,2,3,4]      # STRING AND LIST SLICING ARE SAME OR EQUAL.
# print(rev_list(numbers))

# Reversing List using POP() and APPEND() method: frequently used in back and forth of pages on a website.
def rev_list(l):
    r_list = []
    for i in range(len(l)):
        popped_item = l.pop()  # This block of code will give the reversed list, since pop() method first removes the items from last to 
        r_list.append(popped_item)  # to first and stores them in a varible in each iteration.
    return r_list

numbers = [1,2,3,4,5]
print(rev_list(numbers))

