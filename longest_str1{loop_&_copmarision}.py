# Method 3: Manual loop & Comparision

def find_longest_word(words_list):
    largest=" "
    print(type(largest))
    for list in words_list:
        if len(list) > len(largest):
            largest=list
    return len(largest),largest
list=["Sandhya","Sakshi","Ankan","Riya","Pratiyusha","Manisha"]
result=find_longest_word(list)
print("longest word:",result[1])
print("longest length:",result[0])     #Something New!!