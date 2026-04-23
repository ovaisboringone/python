def word_count(sentence):
    sentence = sentence.lower()

    # remove punctuation
    for ch in ",.!?":
        sentence = sentence.replace(ch, "")

    words = sentence.split()
    count = {}

    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1

    return count


sentence = input("Enter sentence: ")
print(word_count(sentence))
