# REplace first char occurences with $-----------------------------
def rep_first_chr_occ(string):
    str=string[0]
    for i in range(1,len(string)):
        if string[i]==string[0]:
            str+='$'
        else:
            str+=string[i]
    return str
print(rep_first_chr_occ("ANANDAM"))