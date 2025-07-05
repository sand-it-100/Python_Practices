"""
sort(key,reverse) ----> 1. List method
                        2. Change occurs in Original list
                        3. apply only for list
                        4. eg. my_list.sort()
                        5.Alphabetical is default

 &  
sorted(key,reverse) ----> 1.Built-in-method
                          2.change occurs in New copy list
                          3.apply for all (list,tuple,set etc)
                          4.eg. sorted(my_list, key=len)
                          5.Alphabetical is default
                        
key= How to compare (eg. by length .....key=len)

reverse = False (Ascending (default))
          True (Descending (reverse order))

"""

# Method 1: sort() + tuple list
def find_longest_word(words_list):
    list=[(len(word),word) for word in words_list]      # tuple list
    print(type(list))
    list.sort()
    return list[-1][0], list[-1][-1]             # for having tuple
words=["Sandhya","Sakshi","Ankan","Riya","Pratiyusha","Manisha"]
result=find_longest_word(words)
print("longest word:",result[1])
print("longest length:",result[0])  

# comparision ----> 1. Comparision
             #      2. sorting
             #      3. methods