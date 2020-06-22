# kwargs(keyword arguments)
# **kwargs(double star operator)

# kwargs as a parameter
def func(name,**kwargs):  #You can pass multiple parameters in function call & it will convert them into a dictionary.
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    # print(kwargs)
    # print(type(kwargs))

func('Vaibhav',first_name = 'Sushant', last_name = 'Sharma')
# In the above code, the first parameter is not compusory to enter as an argument.You can skip that.
# and if you pass the args in func. call then kwargs take them as input in a dictionary.

# DICTIONARY UNPACKING.

# as we are providing the data in a dictionary by ourselves but if you have a dictionary which is readymade then
# you can also pass it in **kwargs.
dictionary = {'Name':'Sushant Sharma','Age':24,'Address':'New Delhi'}
func('vaibhav',**dictionary)  # you can pass a whole dictionary in **kwargs.