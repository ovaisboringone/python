s=input("Enter a sentence: ")
words=s.split()
freq={word:words.count(word)for word in words}
print(freq)