# Method 7: zip() + map()

def find_longest_word(words_list):
    length=list(map(len, words_list))
    pairs=list(zip(length,words_list))
    return max(pairs)
words_list=["Sandhya","Sakshi","Ankan","Riya","Pratiyusha","Manisha"]  
# when it was.... list = ["Sandhya","Sakshi","Ankan","Riya","Pratiyusha","Manisha"]  python got confused becoz of.... result = find_longest_word(list) 
 # TypeError: 'list' object is not callable                                               # it was should be list()
result=find_longest_word(words_list)            # len() ---> len is callable
print("longest word:",result[1])                # len --> len is not callable
print("longest length:",result[0]) 