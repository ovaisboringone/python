def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split(" "))

sentence = input("Enter sentence: ")
print(reverse_words(sentence))
