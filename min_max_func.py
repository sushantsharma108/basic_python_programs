numbers =[60,5,9]
# print(min(numbers))
# print(max(numbers))

# Yahan hum ek func. define karenge jisme hume greatest difference find out karna h matlab ki, sabse
# bade no. me se sabse chhota no. ko ghatana(minus)

# def greatest_diff(l):
    # for i in l:
    #     minm = min(l)
    #     maxm = max(l)
    # return (maxm-minm) 
def greatest_diff(l):
    return max(l) - min(l)
    
print(greatest_diff(numbers))



