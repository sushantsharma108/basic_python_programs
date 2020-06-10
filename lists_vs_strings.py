# lists vs strings
# lists are mutable: we can change any data in a list.
# strings are immuatable: we can't change(assign any new char) the string

s = "string"
print(s.title())  # You can't change original string but makes a new temp. string and prints it.

list = ['word1','word2','word3']
list.pop()  # It will amke changes in the original list.
print(list)

list = ['word1','word2','word3']
list.append('word4')
print(list)