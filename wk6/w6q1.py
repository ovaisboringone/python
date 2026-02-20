a = float(input("Enter 1st score : "))
b = float(input("Enter 2nd score : "))
c = float(input("Enter 3rd score : "))
if a < 0 or b < 0 or c < 0:
    print("Invalid score entered")
d = a
if b > a and b > c:
    d = b
if c > b and c > a:
    d = c


print("Highest score is: ", d)
