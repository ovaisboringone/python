def reverse_words(sentence):
    words = sentence.split(" ")
    result = []

    for word in words:
        reversed_word = word[::-1]
        result.append(reversed_word)

    return " ".join(result)


sentence = input("Enter sentence: ")
print(reverse_words(sentence))