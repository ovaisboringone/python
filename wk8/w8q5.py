data = "Different string Methods!"

# tokenize
words = data.split()

# uppercase
upper_text = data.upper()

# find substring
index = data.find("rules")

# search character
exists = 'o' in data

# replace symbol
sanitized = data.replace("!", "?")

print("Tokens:", words)
print("Uppercase:", upper_text)
print("Index of 'rules':", index)
print("Contains 'o':", exists)
print("Sanitized:", sanitized)