n = int(input("Enter the range (e.g., 15): "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print("Squares Dictionary:")
print(squares)