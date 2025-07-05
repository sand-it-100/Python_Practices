# Method 9: sorted(key=len)
def find_longest_word(words_list):
    word=sorted(words_list,key=len)[-1]       # something new here !!!
    return len(word), word
words=["Sandhya","Sakshi","Ankan","Riya","Pratiyusha","Manisha"]
result=find_longest_word(words)
print("longest word:",result[1])
print("longest length:",result[0])  