print("Hello \nWorld....")   #\n escape sequence
print("Hello \tWorld....")    #\t escape sequence
print("Hello \'World\' ...")       #\'<format string>\' escape sequence = 'string'
print("Hello, \"World\"....")     #\"<format string>\" escape sequence = "string"
print("Hello, \n\t\"World\".....")     #\n\t escape sequence
print("This is \ backslash.")       #normal backslash
print("This is backslash. \\")       #\\ means single backslash
print("This is double backslash \\\\")     #\\\\ escape sequence
print("This is triple backslash \\\\\\")      #\\\\\\ escape sequence
print("This is triple backslash \\\\\\\\")       #\\\\\\\\ escape sequence

# If we want that the escape sequences b/w the strings work as a normal text then shortcut method 
#  is  to write "r" just before the inverted commas in the format string.

print(r"This is line A \n and line B")
print(r"Hi, i'm \n Sushant Sharma.")
print("Line A \\n Line B")
print(r"\" \' ")