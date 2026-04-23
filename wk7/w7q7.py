x =int(input("Enter value of x: "))
rev = 0
temp = x
place = 1
while temp>0:
    d = temp % 10
    rev = rev +d*place
    temp //=10
    place *= 10

if x == rev:
    print(True)
else:
    print(False)

