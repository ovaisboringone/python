data = {}

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    badge_id = int(input("Enter badge ID: "))
    data[name] = badge_id

search_id = int(input("Enter Badge ID to search: "))

found = False

for name, id in data.items():
    if id == search_id:
        print("Owner:", name)
        found = True
        break

if not found:
    print("ID not found")
