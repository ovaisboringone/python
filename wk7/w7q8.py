list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

merged = list1 + list2
merged.sort()

print("Sorted merged list:", merged)