def is_prime(num):
    if num <= 1:
        return "Not prime"
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not prime"
    
    return "Prime"

num = int(input("Enter a number: "))
print(is_prime(num))
