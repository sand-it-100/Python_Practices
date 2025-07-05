'''
string.replace(old, new, count)

text = "apple apple apple"
print(text.replace("apple", "banana", 2))
-----> banana banana apple

'''
# Using Replace method--------------------------
def remove_chr(str,n):
    return str.replace(str[n],'')  
str="SANDHYA"
result=remove_chr(str,3)
print(result)