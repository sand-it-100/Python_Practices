'''
enumerate() ----> gives both index and value

words = ["hi", "python", "baby"]
for i in range(len(words)):
    print(i, words[i])            words[i] krna pdh rha!!!

words = ["hi", "python", "baby"]         
for i, word in enumerate(words):      
    print(i, word)

'''



def find_longest_word(words_list):
    max_len=0
    max_index=0
    for i ,word in enumerate(words_list):
        if len(word) > max_len:
            max_len = len(word)
            max_index=i
    return max_len , words_list[max_index]
list =["khushi","Priya","Sandhya","Anjali","neha","Sananda","sanna"]
result=find_longest_word(list)
print("longest length:",result[0])
print("longest word:",result[1])