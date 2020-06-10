# This code will define a func. in which it takes a list of words as arguments and return the reversed words in that list.
 
def reversed_words(l):
    rev_list = []   # This is an empty list to store the reversed words after appending multiple items.
    for i in l:
        rev_list.append(i[::-1])  # i[::-1] reverses each & every string in the list.
    return rev_list
string_list = ['abc','vut','xyz']
print(reversed_words(string_list))   # Func. call in print func.
         
