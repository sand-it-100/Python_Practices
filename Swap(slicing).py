'''  
10. Swap first and last chars of a string.
Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
 
'''
# TypeError:'str' object does not support item assignment.
'''
  str[0]=str[-1]
  str[-1]=str[0]      So,
'''
def swap(str):
    str=str[-1] + str[1:-1] + str[0]
    return str
str="SANDHYA"
result=swap(str)
print(result)