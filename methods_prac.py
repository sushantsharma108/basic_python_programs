name = input("Enter your name: ")
character = input("Enter the Char: ")

length =print(len(name))
name = name.lower()
                                #shortcut method is: print(f" Character count : {name.lower().count(character.lower())}")
print(name.count(character))
