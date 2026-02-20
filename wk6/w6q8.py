n = int(input("Enter the number of list elements: "))

l = []
for i in range(n):
    m = input(f"Enter list element {i+1}: ")

    if m.lstrip('-').isdigit():
        l.append(int(m))
    else:
        l.append(m)

print(l)

total = 0
for i in l:
    if isinstance(i, int):
        total += i

print(total)
