filenames = input("Enter filenames separated by space: ").split()

filenames.sort(key=len)

print("Sorted by length:", filenames)