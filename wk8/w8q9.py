arr = list(map(int, input("Enter sorted Book IDs: ").split()))
target = int(input("Enter Book ID to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    
    if arr[mid] == target:
        print("Book ID found at index", mid)
        found = True
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Book ID not found")