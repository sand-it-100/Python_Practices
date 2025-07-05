'''
9. Remove nth character from a string.
Write a Python program to remove the nth index character from a nonempty string.

'''

def remove_chr(str,n):
    first_half=str[:n]
    second_half=str[n+1:]
    return first_half + second_half
str="NumPy"
result=remove_chr(str,3)
print(result)
