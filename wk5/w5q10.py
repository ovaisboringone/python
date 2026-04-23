def count_vowels_consonants(text):
    vowels = "aeiou"
    v_count = 0
    c_count = 0

    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count

text = input("Enter text: ")
v, c = count_vowels_consonants(text.lower())
print("Vowels =", v)
print("Consonants =", c)
