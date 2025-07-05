#------------------My Achievement--------------------------#
def remove_chr(str,n):
    k=""
    for chr in str:
        if chr==str[n]:
            chr=k
        else:
            k+=chr
    return k
str="SANDit"
result=remove_chr(str,3)
print(result)

#  Using a loop
def remove_chr(str,n):
    k=""
    for chr in range(len(str)):
        if chr !=n:
            k+=str[chr]
    return k
str="SANDit"
result=remove_chr(str,3)
print(result)
