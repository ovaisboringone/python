votes = {}

n = int(input("Enter number of candidates: "))

for i in range(n):
    name = input("Enter candidate name: ")
    count = int(input("Enter vote count: "))
    votes[name] = count

# Convert dictionary to list of tuples
items = list(votes.items())

# Sort descending for winner
items.sort(key=lambda x: x[1], reverse=True)
print("Winner:", items[0])

# Sort ascending for lowest votes
items.sort(key=lambda x: x[1])
print("Fewest votes:", items[0])