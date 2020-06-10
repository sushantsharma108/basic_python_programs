sen = "She is very beautiful and she is a great dancer."
print(sen.replace(" ","_"))         #It replaces the spaces within the string with the underscore or defined 
                                    #character or word.

print(sen.replace("is","was"))      #It replaces the word "is" with "was" but in whole string.

print(sen.replace("is","was",1))      #It replaces the word "is" with "was" but only one time not in whole string.

print(sen.replace("is","was",2))      #It replaces the word "is" with "was" but only two times not in whole string.

# The parameters 1,2,2,etc... are the no. of counts for which we want to replace the word in a string.

# find(): This method is used to find the position of a character or a word in a string.
print(sen.find("is"))    # It gives the starting position/ index of the word "is".

sen =  "is She is very beautiful and she is a great dancer."
print(sen.find("is"))     # It  also gives the starting position/ index of the word "is" but in a new defined string.
print(sen.find("is",1))   # It  also gives the starting position/ index of the word "is" but its search will not start
                            # from 0th position of "is" but where the next "is" is written i.e at  7th position.

sen = "She is very beautiful and she is a great dancer."
is_pos1 = sen.find("is")         # it gives the position of first "is".
is_pos2 = sen.find("is",is_pos1)     
print(sen.find("is",is_pos2 + 1))