a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while y != 0:
    carry = x & y
    x = x ^ y
    y = carry << 1

print("Sum:", x)