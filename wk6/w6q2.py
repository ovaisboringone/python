a = float(input("Enter temperature 1: "))
b = float(input("Enter temperature 2: "))
c = float(input("Enter temperature 3: "))
if b < a:
    if b < c:
        d = b

else:
    if c < a:
        d = c
    else:
        d = a


print("Lowest score is: ", d)
