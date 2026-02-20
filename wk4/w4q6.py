def is_perfect(num):
    if num <= 1:
        return "Not a perfect number"
    
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    
    if total == num:
        return "Perfect number"
    else:
        return "Not a perfect number"

num = int(input("Enter a number: "))
print(is_perfect(num))
