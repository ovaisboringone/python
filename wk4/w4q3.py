import math

def effective_area(R, r):
    if R <= r:
        return "Invalid input"
    return round(math.pi * (R**2 - r**2), 2)

R = float(input("Enter outer radius R: "))
r = float(input("Enter inner radius r: "))

print("Effective Area =", effective_area(R, r))
