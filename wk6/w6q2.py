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

if a < 0 or b < 0 or c < 0:
    print("Invalid score entered")


print("Lowest score is: ", d)
