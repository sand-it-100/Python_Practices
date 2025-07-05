# Method1 --> loop + concatenation & slicing -----------------------------
def swap(str):
    for chr in range(len(str)):
        if chr==0:
            first=str[len(str)-1]
        elif chr== len(str)-1 :
            last=str[0]
    return first + str[1:len(str)-1] + last
str="NumPy"
result=swap(str)
print(result)

# Method2 (Only Loop) ------------------------------
def swap(str):
    swap_ele=""
    for chr in range(len(str)):
        if chr==0:
            swap_ele+=str[len(str)-1]
        elif chr== len(str)-1 :
            swap_ele+=str[0]
        else:
            swap_ele+=str[chr]
    return swap_ele
str="NumPy"
result=swap(str)
print(result)