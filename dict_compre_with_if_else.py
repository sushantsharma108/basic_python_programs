# dict comprehension with if else
# d = {1:'odd',2:'even'}
numbers = list(range(1,11))
# [1,2,3,4,5,6,7,8,9,10]
dictionary = {i:('Even' if i%2==0 else 'Odd') for i in numbers}
for key,value in dictionary.items():
    print(f"{key}:{value}")