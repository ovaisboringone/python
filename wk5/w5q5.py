import string

def word_count(sentence):
    words = sentence.lower().translate(str.maketrans("", "", string.punctuation)).split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

sentence = input("Enter sentence: ")
print(word_count(sentence))
