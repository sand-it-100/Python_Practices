'''   
1. Find longest word in a list.
Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9   
 '''
list=["ANKAN","JAYA","RIYA","SANANDA","SAHEEN","SANDit","juli"]
def find_longest_word(word_list):
    list1=[]
    for i in list:
        list1.append((len(i),i))
    list1.sort()
    if list1[-2][0] == list1[-1][0]:
        print("Longest word:",list1[-2][-1])
        print("/n Longest length:",list1[-2][0])

    return list1[-1][0], list1[-1][-1]

list=["ANKAN","JAYA","RIYA","SANANDA","SAHEEN","SANDHYA","JULI"]
result=find_longest_word(list)
print("Longest word:",result[-1])
print("/n Longest length:",result[0])

    
    