def armstrong(n):
    digits = len(str(n))
    temp = n
    total = 0
    while temp > 0:
        u = temp % 10
        total += (u**digits)
        temp //= 10
    
    return total == n

n = int(input("Enter numeric key value: "))
if armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")




