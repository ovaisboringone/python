n = int(input("Enter a number: "))

if n < 0:
    print("Invalid input")
elif n <= 1:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime, first factor:", i)
            break
    else:
        print("Prime number")