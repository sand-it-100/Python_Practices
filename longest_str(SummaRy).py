def find_longest_word(words_list):
    longest = max(words_list, key=len)
    return len(longest), longest

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])

def find_longest_word(words_list):
    longest = ''
    for word in words_list:
        if len(word) > len(longest):
            longest = word
    return len(longest), longest

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])


def find_longest_word(words_list):
    word_len = [(len(w), w) for w in words_list]
    return max(word_len)  # returns tuple (length, word)

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])


def find_longest_word(words_list):
    word_len = [(len(w), w) for w in words_list]
    sorted_words = sorted(word_len)  # returns new sorted list
    return sorted_words[-1][0], sorted_words[-1][1]

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])


from functools import reduce

def find_longest_word(words_list):
    longest = reduce(lambda a, b: a if len(a) > len(b) else b, words_list)
    return len(longest), longest

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])



def find_longest_word(words_list):
    max_len = 0
    max_index = 0
    for i, word in enumerate(words_list):
        if len(word) > max_len:
            max_len = len(word)
            max_index = i
    return max_len, words_list[max_index]

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])


def find_longest_word(words_list):
    longest = sorted(words_list, key=len)[-1]
    return len(longest), longest

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])


def find_longest_word(words_list):
    if len(words_list) == 1:
        return len(words_list[0]), words_list[0]
    
    rest_len, rest_word = find_longest_word(words_list[1:])
    
    if len(words_list[0]) > rest_len:
        return len(words_list[0]), words_list[0]
    else:
        return rest_len, rest_word

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])


def find_longest_word(words_list):
    lengths = list(map(len, words_list))           # Get lengths of all words
    pairs = list(zip(lengths, words_list))         # Pair length with each word
    longest = max(pairs)                           # max() on (length, word) tuple
    return longest[0], longest[1]

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])


def find_longest_word(words_list):
    max_len = 0
    max_index = 0
    for i, word in enumerate(words_list):
        if len(word) > max_len:
            max_len = len(word)
            max_index = i
    return max_len, words_list[max_index]

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word:", result[1])
print("Length of the longest word:", result[0])
