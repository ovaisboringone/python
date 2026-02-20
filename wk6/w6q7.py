r1 = int(input("Enter starting number r1:"))
r2 = int(input("Enter ending number r2:"))
if (r1 > r2):
    print("r1 must be smaller than r2")
else:
    for i in range(r1, r2+1):
        print(i)
