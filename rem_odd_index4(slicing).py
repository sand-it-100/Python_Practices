# Using Slicing--------------------------
def removal_of_odd_indices(str):
    string=str[0::2]
    return string
str="abcdef"
result=removal_of_odd_indices(str)
print(result)