# This is a program to print the list in which there is a reverse of each string in a list using list comprehension.
def reverse_string(list):
    return [i[::-1] for i in list]
    

list_of_strings = ['abc','def','tuv','wxyz']

print(reverse_string(list_of_strings))
