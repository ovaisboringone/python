Catalog = {}
Sale = {}

n = int(input("Enter number of catalog items: "))
for i in range(n):
    item = input("Enter item name: ")
    price = int(input("Enter price: "))
    Catalog[item] = price

m = int(input("Enter number of sale items: "))
for i in range(m):
    item = input("Enter sale item name: ")
    price = int(input("Enter sale price: "))
    Sale[item] = price

# Merge
Catalog.update(Sale)

print("Updated Catalog:", Catalog)
