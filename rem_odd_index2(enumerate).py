# Using enumerate--------------------
def removal_of_odd_indices(str):
    string= (''.join( chr for index,chr in enumerate(str) if index % 2 ==0) )
    return string 
str="abcdef"
result=removal_of_odd_indices(str)
print(result)