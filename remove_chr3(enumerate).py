'''     Enumerate ---> it returns tuple of (index,str) as well

(chr for i,chr in enumerate("NumPy") if i != 3)
enumerate("Numpy") ---> (0, 'N'), (1, 'u'), (2, 'm'), (3, 'P'), (4, 'y')
goes through each tuple — unpacks index i and character chr.
'N', 'u', 'm', 'y'
''.join(['N', 'u', 'm', 'y']) → "Numy"

'''
def remove_chr(str,n):
    return ''.join( chr for i ,chr in enumerate(str)  if i !=n  )  
str="SANDHYA"
result=remove_chr(str,3)
print(result)