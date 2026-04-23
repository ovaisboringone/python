list1 = set(input("Enter first email list: ").split())
list2 = set(input("Enter second email list: ").split())

master = list1.union(list2)

print("Master email list:", list(master))