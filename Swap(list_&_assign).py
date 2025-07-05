# String me assignment nehi to ---> List ke through assign kar do,simple!!!
def swap(str):
    list_str=list(str)
    list_str[0],list_str[-1]=list_str[-1],list_str[0]
    return ''.join(list_str) 
str="NumPy"
result=swap(str)
print(result)

# What about replace()........?