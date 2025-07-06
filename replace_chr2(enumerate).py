# Using enumerate()
def rep_first_chr_occ(str):
    first = str[0]
    return ''.join(chr if i==0 or chr != first else "$" for i,chr in enumerate(str))
print(rep_first_chr_occ("ANANDAM"))
