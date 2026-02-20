def remove_noise(s):
    temp = ""
    for i in range(len(s)):
            if i % 2 != 0 and not s[i].isalnum():          
                continue
            temp += s[i]

    final = ""

    for i in range(len(temp)):
        if i % 2 != 0:
            final = final + temp[i]

    print(final)


s = input("Enter a string: ")
remove_noise(s)
