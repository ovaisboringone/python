products = list(map(int, input("Enter product IDs: ").split()))
item = int(input("Enter product ID to search: "))

for p in products:
    if p == item:
        print("Found")
        break
else:
    print("Not Found")