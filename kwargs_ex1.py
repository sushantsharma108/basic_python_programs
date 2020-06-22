# **kwargs is the optional arguments.

def func(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

names = ['sushant','sharma','vscode']
print(func(names,reverse_str = True))
# In the above line reverse_str is optional, if you will not write it then the function
#  will convert the case of elements in title().
