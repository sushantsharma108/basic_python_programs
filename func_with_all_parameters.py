# function with all parameters -- very important

# PADK- parameters(Normal), *args, default parameters, **kwargs.
# If you have to use the above 4 parameters then use them in the above defined order. If you will not, then it
# will give error.
def func(name,*args,last_name = 'unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('Sushant',1,2,3,Address = 'New Delhi',Phone = 9885971212)
