def find_longest_word(words_list):
    longest=""
    for word in range(len(words_list)):
        if len(words_list[word]) > len(longest):
            longest = words_list[word]
    return len(longest) ,longest
list =["khushi","Priya","Sandhya","Anjali","neha","Sananda","sanna"]
result=find_longest_word(list)
print("longest length:",result[0])
print("longest word:",result[1])