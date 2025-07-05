'''
reduce(function,iterable) 
reduce(lambda a,b : a if......)

a is the accumulated result {a changes only if b is longer — otherwise it stays}
b is the next word {b changes every step — it's the next word in the list}

'''
from functools import reduce
def find_longest_word(words_list):
    word=reduce(lambda a, b : a if len(a) > len(b) else b , words_list)
    return len(word),word
list =["shristi","khushi","Priya","Sandhya","Anjali","neha","Sananda","sanna"]
result=find_longest_word(list)
print("longest length:",result[0])
print("longest word:",result[1])