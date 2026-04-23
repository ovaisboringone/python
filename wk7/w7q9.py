numbers = list(map(int, input("Enter numbers: ").split()))
n = len(numbers)

# Bubble Sort
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

largest = numbers[-1]

for i in range(n-2, -1, -1):
    if numbers[i] != largest:
        print("Second Largest:", numbers[i])
        break