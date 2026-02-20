n = int(input("Enter a number: "))

if n < 0:
    print("Invalid input")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial:", fact)