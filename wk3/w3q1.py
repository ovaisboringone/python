n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    nums.append(int(input(f"Enter number {i+1}: ")))

total = sum(nums)
product = 1
for num in nums:
    product *= num

average = total / n if n != 0 else 0
print("SUM:", total)
print("PRODUCT:", product)
print("AVERAGE:", average)