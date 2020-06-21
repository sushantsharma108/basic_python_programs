string = "Sushant Sharma"
word_counter = {char:string.count(char) for char in string}
print(word_counter)
for key,value in word_counter.items():
    print(f"{key}:{value}")
