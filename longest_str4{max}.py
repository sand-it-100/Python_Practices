# Method 2: max(key=len)
def find_longest_word(words_list):
    word= max(words_list,key=len)
    return len(word) , word              # ............max(iterable , key)...................
list =["ss","kk","pp","9k","AK47","nine","thirty","five"]
result=find_longest_word(list)
print("longest length:",result[0])
print("longest word:",result[1])