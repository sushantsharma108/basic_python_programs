# WORD COUNTER:
def word_counter(string):
    count = {} # This dict. will store the count of characters in a string.
    for i in string:
        count[i] = string.count(i)
    return count

print(word_counter("sushant"))


