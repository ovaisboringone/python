list1 = set(input("Enter first list: ").split())
list2 = set(input("Enter second list: ").split())

common = list1.intersection(list2)

print("Common elements:", list(common))