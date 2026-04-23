start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

result = []

for i in range(start, end+1):
    result.append((i, 5*(i**3)))

print(result)