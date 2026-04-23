def calculate_routes(n):
    if n<=1:
        return 1
    else:
        return n * calculate_routes(n-1)
    
n= int(input("Enter the number n: "))
print(f"Factorial of {n} = {calculate_routes(n)}")