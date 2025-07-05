# List Comprehension............ 
def remove_chr(str,n):
    return ''.join( [str[i] for i in range(len(str)) if i !=n ] )   # joining of elements of list.
str="SANDHYA"
result=remove_chr(str,3)
print(result)