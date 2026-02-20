n = int(input("Enter the number of list elements: "))

l = []
for i in range(n):
    m = input(f"Enter list element {i+1}: ")
    l.append(int(m))

print(l)
l.sort()
print(l)

consecutive = True
for i in range(len(l) - 1):
    if l[i+1] - l[i] != 1:
        consecutive = False
        break

print(consecutive)
