# Using List Comprehension & join----------------------------
def removal_of_odd_indices(str):
    string= ''.join([str[i] for i in range(len(str)) if i%2==0] )
    return string 
str="abcdef"
result=removal_of_odd_indices(str)
print(result)