'''
11. Remove odd index chars from a string.
Write a Python program to remove characters that have odd index values in a given string.

'''
def removal_of_odd_index(str):
    str_len=""
    for i in range(0,len(str)):
        if i%2 ==0:
            str_len+=str[i]
            print(i,end=" ")
    return str_len
str="NumPy"
result=removal_of_odd_index(str)
print(result)