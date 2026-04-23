l=eval(input("Enter the data packet IDs: "))

even = []
odd = []

for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)